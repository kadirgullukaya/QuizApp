questions = ["10+2 = ?", "5+9 = ?", "2+2 = ?", "3+2 = ?", "4+2 = ?"]
answers = [12, 14, 4, 5, 6]

score = 0
for question, answer in zip(questions, answers):
    print(question)
    ans = int(input("Answer: "))

    if ans == answer:
        print("Your answer is correct!")
        score += 100 / len(questions)
    else:
        print("Your answer is wrong!")


print("Your Score:", score)
