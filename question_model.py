class Question:
    def __init__(self, text, answer, incorrect_answers, type):
        self.text = text
        self.correct_answer = answer
        self.incorrect_answers = incorrect_answers
        self.type = type

    def text_cleaner(self):
        exclusions = ["&quot;", "&#039;", "&ldquo;"]
        for i in exclusions:
            if i in self.text:
                self.text = self.text.replace(i, "")

            if i in self.correct_answer:
                self.correct_answer = self.correct_answer.replace(i, "")
            
            if i in self.incorrect_answers:
                self.incorrect_answers = self.incorrect_answers.replace(i, "")
