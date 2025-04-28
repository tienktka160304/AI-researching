def ask_ok(prompt, retries = 4, reminder ='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries -= 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


ask_ok('OK to overwrite the file? \n', 2, 'Come on, onlly yes or no')
# OK to overwrite the file? 
# o
# Come on, onlly yes or no
# OK to overwrite the file?
# ko
# Come on, onlly yes or no
# OK to overwrite the file?
# no