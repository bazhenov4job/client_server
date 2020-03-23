import subprocess

PROCESS = []

while True:
    ANSWER = input("Выберите действие:\n s - запуск, x - закрыть все окна, q - выйти\n")

    if ANSWER == 's':
        PROCESS.append(subprocess.Popen('python server.py',
                                        creationflags=subprocess.CREATE_NEW_CONSOLE))

        PROCESS.append(subprocess.Popen('python client.py -m w',
                                        creationflags=subprocess.CREATE_NEW_CONSOLE))

        for x in range(1):
            PROCESS.append(subprocess.Popen('python client.py -m r',
                                            creationflags=subprocess.CREATE_NEW_CONSOLE))

    elif ANSWER == 'x':
        while PROCESS:
            TO_KILL = PROCESS.pop()
            TO_KILL.kill()

    elif ANSWER == 'q':
        break
