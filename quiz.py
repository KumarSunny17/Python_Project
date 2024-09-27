quiz_questions=[
    {
        "question":"who is the father or python?",
        "options":["A.james gosleng","B.guido von rossum","C.Dennis ritchie","D.bjourne strourtup"],
        "answer":"B"
    },
    {
        "question":"is python object oriented languege",
        "options":["A.no","B.yes","C.both","D.none of the avobe"],
        "answer":"C"
    },
    {
        "question":"what is pip",
        "options":["A.Python Installer Package","B.Python Package Installer","C.Python Packaging Index","D.none of the avobe"],
        "answer":"C"
    }

]

def display_question(question):
    print(question["question"])
    for option in question["options"]:
        print(option)
    user_answer=input("Enter you answer (A,B,C,D): ").upper()
    return user_answer

def check_answers(questions,user_answers):
    score=0
    for i, question in enumerate(questions):
        if user_answers[i]==question["answer"]:
            score+=1
    return score

def main():
    user_answers=[]
    correct_answers=[]
    for question in quiz_questions:
        user_answer=display_question(question)
        user_answers.append(user_answer)
    score = check_answers(quiz_questions,user_answers)
    print(f"Your score: {score}/{len(quiz_questions)}")

      


main()














