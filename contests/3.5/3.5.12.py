with open(input()) as fin, \
     open(input(), 'w') as fe, \
     open(input(), 'w') as fo, \
     open(input(), 'w') as fq:

    for raw in fin:
        nums = raw.split()
        for writer, condition in (
            (fe, lambda ev, od: ev > od),
            (fo, lambda ev, od: od > ev),
            (fq, lambda ev, od: ev == od),
        ):
            group = [s for s in nums
                     if condition(
                         sum(1 for d in s if d in '02468'),
                         len(s) - sum(1 for d in s if d in '02468')
                     )]
            writer.write(' '.join(group) + '\n')
