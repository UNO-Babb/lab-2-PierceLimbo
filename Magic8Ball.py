#Magic8Ball.py
#Name:Pierce Limbo
#Date:9/4/2025
#Assignment: Lab2

import random

def main():
  responses = [
        "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
  ]

  print("Magic 8 Ball")

  question = input("Ask a question and Magic 8 Ball will provide the answer: ")

  answer = random.choice(responses)
  print("Mystical 8 Ball says: ", answer)

if __name__ == '__main__':
  main()
