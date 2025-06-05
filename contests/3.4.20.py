from itertools import product
import sys


def tokenize(expr):

    tokens = []
    i = 0
    n = len(expr)
    while i < n:
        ch = expr[i]
        if ch.isspace():
            i += 1
            continue

        if ch == '(' or ch == ')':
            tokens.append(ch)
            i += 1
            continue

        if ch == '-' and i + 1 < n and expr[i + 1] == '>':
            tokens.append('->')
            i += 2
            continue

        if ch == '^':
            tokens.append('^')
            i += 1
            continue

        if ch == '~':
            tokens.append('~')
            i += 1
            continue

        if ch.isupper():
            tokens.append(ch)
            i += 1
            continue

        if ch.islower():
            if expr.startswith('not', i):
                tokens.append('not')
                i += 3
                continue
            if expr.startswith('and', i):
                tokens.append('and')
                i += 3
                continue
            if expr.startswith('or', i):
                tokens.append('or')
                i += 2
                continue

        print(f"Unexpected character sequence at position {i}: '{expr[i:]}'", file=sys.stderr)
        sys.exit(1)

    return tokens


def to_postfix(tokens):

    prec = {
        'not': 6,
        'and': 5,
        'or': 4,
        '^': 3,
        '->': 2,
        '~': 1,
    }
    assoc = {
        'not': 'right',
        'and': 'left',
        'or': 'left',
        '^': 'left',
        '->': 'right',
        '~': 'left',
    }

    output = []
    op_stack = []

    for tok in tokens:
        if len(tok) == 1 and tok.isupper():
            output.append(tok)
        elif tok == '(':
            op_stack.append(tok)
        elif tok == ')':
            while op_stack and op_stack[-1] != '(':
                output.append(op_stack.pop())
            if not op_stack:
                print("Mismatched parentheses", file=sys.stderr)
                sys.exit(1)
            op_stack.pop()
        else:
            while op_stack and op_stack[-1] != '(' and op_stack[-1] in prec:
                top = op_stack[-1]
                if (
                    (assoc[tok] == 'left' and prec[tok] <= prec[top])
                    or (assoc[tok] == 'right' and prec[tok] < prec[top])
                ):
                    output.append(op_stack.pop())
                else:
                    break
            op_stack.append(tok)

    while op_stack:
        if op_stack[-1] in ('(', ')'):
            print("Mismatched parentheses", file=sys.stderr)
            sys.exit(1)
        output.append(op_stack.pop())

    return output


def eval_postfix(postfix_tokens, locals_dict):
    
    stack = []
    for tok in postfix_tokens:
        if len(tok) == 1 and tok.isupper():
            stack.append(locals_dict[tok])
        elif tok == 'not':
            x = stack.pop()
            stack.append(not x)
        elif tok == 'and':
            right = stack.pop()
            left = stack.pop()
            stack.append(left and right)
        elif tok == 'or':
            right = stack.pop()
            left = stack.pop()
            stack.append(left or right)
        elif tok == '^':
            right = stack.pop()
            left = stack.pop()
            stack.append(left ^ right)
        elif tok == '->':
            right = stack.pop()
            left = stack.pop()
            stack.append((not left) or right)
        elif tok == '~':
            right = stack.pop()
            left = stack.pop()
            stack.append(left == right)
        else:
            print(f"Unknown token in RPN: {tok}", file=sys.stderr)
            sys.exit(1)

    if len(stack) != 1:
        print("Error evaluating postfix expression", file=sys.stderr)
        sys.exit(1)

    return stack[0]


def main():
    expr = input().strip()
    tokens = tokenize(expr)
    postfix = to_postfix(tokens)
    vars_ = sorted({ch for ch in expr if ch.isupper()})

    print(*vars_, 'F')

    for bits in product([0, 1], repeat=len(vars_)):
        locals_dict = {
            name: bool(bit)
            for name, bit in zip(vars_, bits)
        }
        result_bool = eval_postfix(postfix, locals_dict)
        result_int = int(result_bool)
        print(*bits, result_int)


if __name__ == "__main__":
    main()
