try:
    from colorama import *
except ModuleNotFoundError:
    print('Resources Are Missing. Please Install colorama.')
    fin = open("error_history.txt", "a")

    fin.write('\nModuleNotFoundError [Update Python And Install Colorama.]');

    fin.close()
    exit()

except MemoryError:
    print('Something Is Wrong With System Memory.')
    fin = open("error_history.txt", "at")

    fin.write('\nMemoryError [Run Memtest86+]');

    fin.close()
    exit()

except SystemError:
    print('A Unknown System Error Has Occurred.')
    fin = open("error_history.txt", "at")

    fin.write('\nSystemError [UNKNOWN]');

    fin.close()
    exit()


def pydos():
    print('Gordae PyDOS [Version 0.1]')
    while True:
        command = input('>>>')
        if command == "settings":
            print(NotImplemented)

        if command == "help":
            print('======[HELP]======')
            print('     settings     ')
            print('      color       ')
            print('More Coming On V0.2!')

        if command == "color":
            print(Fore.RED + "RED")
            print(Fore.BLUE + "BLUE")
            print(Fore.MAGENTA + "MEGENTA" )


pydos()