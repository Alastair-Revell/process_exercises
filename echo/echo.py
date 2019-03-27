from datetime import datetime

def say_until_exit():
    txt = ''
    while txt != 'exit':
        txt = input("Say Something: ")
        time = (datetime.now().time()).isoformat()
        date = (datetime.now().date()).isoformat()
        print(date + ' | ' + time + ' | ' + 'You said: ' + txt)

say_until_exit()
