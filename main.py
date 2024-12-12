questions = ["10+2 = ?", "5+9 = ?", "2+2 = ?", "3+2 = ?"]
answers = [12, 14, 4, 5]

score = 0
for question, answer in zip(questions, answers):
    print(question)
    ans = int(input("Answer: "))

    if ans == answer:
        print("Your answer is correct!")
        score += 25
    else:
        print("Your answer is wrong!")


print("Your Score:", score)
