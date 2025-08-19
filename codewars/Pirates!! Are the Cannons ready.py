def cannons_ready(gunners):
    for value in gunners.values():
        if value == 'aye':
            continue
        elif value == 'nay':
            return 'Shiver me timbers!'
    return 'Fire!'

b = {'Mike':'aye','Joe':'nay','Johnson':'aye','Peter':'aye'}
print(cannons_ready(b))
