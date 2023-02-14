class Question:
    def __init__(self, text, answer, incorrect_answers, type):
        self.text = text
        self.correct_answer = answer
        self.incorrect_answers = incorrect_answers
        self.type = type

    def text_cleaner(self):
        exclusions = ["&quot;", "&#039;"]
        for i in exclusions:
            if i in self.text:
                self.text = self.text.replace(i, "")
