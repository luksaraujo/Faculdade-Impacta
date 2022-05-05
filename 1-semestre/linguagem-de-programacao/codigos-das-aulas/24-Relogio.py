from time import sleep

def relogio():
    h = 00
    while h < 24:
        m = 0
        while m < 60:
            s = 0
            while s < 60:
                print(f'{h:02}:{m:02}:{s:02}')
                sleep(1)
                s += 1
            m += 1
        h += 1
        if h == 24:
            h = 0
            m = 0
            s = 0
relogio()
