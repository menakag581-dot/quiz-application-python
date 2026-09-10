#Quiz Application
score = 0
questions = [
  {
      "question": "What is the capital of India?".
      "options": ["A. Chennai", "B.Mumbai","C.New Delhi","D.Kolkata"],
      "answer":"C"
},
{
      "question":"Which language is commonly used for Data Science?",
      "options":["A.Python","B.HTML","C.CSS","D.XML"],
      "answer":"A"
},
  {
      "question":"What does AI stand for?"
      "Options"[
          "A.Automatic Internet",
          "B.Artificial Intelligence",
          "C.Advanced Information",
          "D.Applied Internet"'
    ],
    "answer":"B"
  },
  {

      "question":"Which library is commonly used for data analysis in Python?",
      "options":["A.Pandas","B.Turtle","C.Tkinter","D.Pygame"],
      "answer":"A"
  },
  {
    "question":"Which symbol is used for comments in python?",
    "options":["A.//","B.<!--- --->","C.#","D.**"],
    "answer":"C"
  }
  }
  print("============PYTHON QUIZ=============")

for question in questions:
  print("\n"+question["question"])

for option in question ["options"]:
  print(option)

user_answer = input("Enter your answer (A/B/C/D):").upper()

if user_answer == question["answer"]:
  print("Correct")
  score +=1
else:
  print("Wrong!")
  print("Correct answer:",question["answer"])

print("\n==========QUIZ RESULT=============")
print("Your Score:",score,"/"len(questions))

if score == len(questions):
  print("Excellent!")
elif score>=3:
  print("Good job!")
else:
  print("Keep practicing")
