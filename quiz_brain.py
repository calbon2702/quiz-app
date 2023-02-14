class QuizBrain:
    def __init__(self, lst):
        self.question_num = 0
        self.question_lst = lst
        self.score = 0

    def still_has_questions(self):
        return self.question_num < len(self.question_lst)

    def next_question(self):
        current_question = self.question_lst[self.question_num]
        self.question_num += 1
        choice = input(f"Q.{self.question_num}: {current_question.text}\n")
        self.check_answer(choice, current_question.correct_answer)

    def check_answer(self, choice, answer):
        if choice.lower() == answer.lower():
            self.score += 1
            print("Correct answer!")
        else:
            print("Incorrect answer!")
        
        print(f"The correct answer is {answer}")
        print(f"Score: {self.score}/{self.question_num}\n")
