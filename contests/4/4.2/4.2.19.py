from itertools import cycle

def secret_replace(text, **rules):
    pools = {ch: cycle(vals) for ch, vals in rules.items()}
    out = []
    for ch in text:
        if ch in pools:
            out.append(next(pools[ch]))
        else:
            out.append(ch)
    return ''.join(out)


result = secret_replace("Hello, world!", l=("hi", "y"), o=("123", "z"))
print(result)