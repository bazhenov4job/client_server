import subprocess

answer = input("s - начать работу, x - завершить процессы, q - выйти:\n")
pros = []

while True:

    if answer == 's':
        pros.append(subprocess.Popen("python server.py", creationflags=subprocess.CREATE_NEW_CONSOLE))

        for _ in range(3):
            pros.append(subprocess.Popen("python client.py", creationflags=subprocess.CREATE_NEW_CONSOLE))

    elif answer == 'x':
        while pros:
            process = pros.pop()
            process.kill()

    elif answer == 'q':
        while pros:
            process = pros.pop()
            process.kill()

        break

    answer = input("s - начать работу, x - завершить процессы, q - выйти:\n")
