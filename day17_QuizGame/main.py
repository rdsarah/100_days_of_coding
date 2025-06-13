from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    q = item["question"]
    a = item["correct_answer"]
    question_bank.append(Question(q, a))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz. \nYour final score was {quiz.score}/{len(question_bank)}")
