import subprocess

PROCESS = []

while True:
    ANSWER = input("Выберите действие:\n s - запуск, x - закрыть все окна, q - выйти\n")

    if ANSWER == 's':
        PROCESS.append(subprocess.Popen('python Server.py',
                                        creationflags=subprocess.CREATE_NEW_CONSOLE))

        PROCESS.append(subprocess.Popen('python Client.py',
                                        creationflags=subprocess.CREATE_NEW_CONSOLE))

    elif ANSWER == 'x':
        while PROCESS:
            TO_KILL = PROCESS.pop()
            TO_KILL.kill()

    elif ANSWER == 'q':
        break
