def concat(*args, sep='/'):
    return sep.join(args)

print(concat('earth', 'mars','venus'))
#earth/mars/venus
print(concat('earth', 'mars','venus', sep ='.'))
#earth.mars.venus