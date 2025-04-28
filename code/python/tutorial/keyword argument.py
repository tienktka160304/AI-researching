def cheeseshop(kind, *args,**kwargs):
    print("-- Do u have any", kind, "?")
    print("-- Im sorry, we are all out of", kind)
    for arg in args:
        print(arg)
    print("-" * 40)
    for kw in kwargs:
        print(kw, ":", kwargs[kw])

cheeseshop('Hamurger', "oh i see","any other shop near here?", shopkeeper='Micheal', client='joohn', sketch='cheese shop')
# -- Do u have any Hamurger ?
# -- Im sorry, we are all out of Hamurger
# oh i see
# any other shop near here?
# ----------------------------------------
# shopkeeper : Micheal
# client : joohn
# sketch :  cheese shop


# def parrot(voltage, state = 'a stiff', action = 'voom', type = 'Norwegian Blue'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.")
#     print("-- Lovely plumage, the", type)
#     print("-- It's", state, "!")
    
# parrot('a million', 'bereft of life', 'jump')
# # -- This parrot wouldn't jump if you put a million volts through it.
# # -- Lovely plumage, the Norwegian Blue
# # -- It's bereft of life !