score = 0

# Question 1

answer1 = input("Q1. What is the capital of France?\nANSWER:- ")
if answer1.strip().lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Paris.")

# Question 2 

answer2 = input("Q2. which language is spoken in france?\nANSWER:- ")
if answer2.strip().lower() == "french":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is French.")

# Question 3 

answer3 = input("Q3. Who is the current President of France?\nANSWER:- ")
if answer3.strip().lower() == "emmanuel macron":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Emmanuel Macron.")

print(f"\nYour final score is: {score:>2}/3")

if score == 3:
    print("Congratulations! 🎉 You answered all three questions correctly!")
elif score == 2:
    print("Great job! You answered 2 out of 3 questions correctly. Keep it up!")
elif score == 1:
    print("Good effort! You answered 1 question correctly. Keep learning and try again!")
else:
    print("Don't give up! Keep learning and try again.You can do better next time!")