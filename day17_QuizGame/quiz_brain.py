class QuizBrain:

    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0

    def next_question(self):
        current_q = self.q_list[self.q_number] 
        self.q_number += 1
        user_ans = input(f"Q.{self.q_number}: {current_q.text}. (True/False)?: ")
        self.check_answer(user_ans, current_q.answer)

    def still_has_questions(self):
        return self.q_number < len(self.q_list)
    
    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer is {correct_ans}")
        print(f"Your correct score is {self.score}/{self.q_number} \n")
        
