SYMBOLS = {
            "&quot;": "\"",
            "&#039;": "\'",
            "&ldquo;": "\"",
            "&rdquo;": "\"",
            "&rsquo;": "\'",
            "&lsquo;": "\'"
        }

BAD_CHARACTERS = {
            "&aring;": "a",
            "&eacute;": "e"
        }

class Question:
    def __init__(self, text, answer, incorrect_answers, type):
        self.text = text
        self.correct_answer = answer
        self.incorrect_answers = incorrect_answers
        self.type = type

    def text_cleaner(self):
        for symbol, replacement in SYMBOLS.items():
            if symbol in self.text:
                self.text = self.text.replace(symbol, replacement)

            if symbol in self.correct_answer:
                self.correct_answer = self.correct_answer.replace(symbol, replacement)
            
            if symbol in self.incorrect_answers:
                self.incorrect_answers = self.incorrect_answers.replace(symbol, replacement)

        for character, replacement in BAD_CHARACTERS.items():
            if character in self.text:
                self.text = self.text.replace(character, replacement)

            if character in self.correct_answer:
                self.correct_answer = self.correct_answer.replace(character, replacement)
            
            if character in self.incorrect_answers:
                self.incorrect_answers = self.incorrect_answers.replace(character, replacement)