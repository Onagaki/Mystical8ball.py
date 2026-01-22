import random

answer = " "
rand = random.randint(0, 8)

Question = input("What is your question :")

if rand == 0:
    answer = "Yes - definitely."
elif rand == 1:
    answer = "It is decidely so."
elif rand == 2:
    answer = "Without a doubt."
elif rand == 3:
    answer = "Reply hazy, try again."
elif rand == 4:
    answer = "Ask again later."
elif rand == 5:
    answer = "Better not tell you now."
elif rand == 6:
    answer = "My sources say no."
elif rand == 7:
    answer = "Outlook not so good."
elif rand == 8:
    answer = "Very doubtful."

print(Question)
print(answer)