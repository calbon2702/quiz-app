import random

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
        if current_question.type == "boolean":
            choice = input(f"Q.{self.question_num}: {current_question.text} (true/false)\n")

        if current_question.type == "multiple":
            choice = self.multiple_choice(current_question)

        self.check_answer(choice, current_question.correct_answer)

    def check_answer(self, choice, answer):
        if choice.lower() == answer.lower():
            self.score += 1
            print("Correct answer!")
        else:
            print("Incorrect answer!")
        
        print(f"The correct answer is {answer}")
        print(f"Score: {self.score}/{self.question_num}\n")

    def multiple_choice(self, question):
        print(f"Q.{self.question_num}: {question.text}\n")
        answer_lst = question.incorrect_answers + [question.correct_answer]
        pick_dict = {}

        for i in range(len(answer_lst)):
            pick = random.choice(answer_lst)
            print(f"{i + 1}. {pick}")
            pick_dict[str(i + 1)] = pick
            answer_lst.remove(pick)

        choice = input()

        if choice in pick_dict.keys():
            choice = pick_dict[choice]

        return choice
