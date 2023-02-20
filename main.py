from question_model import Question
from data import DataCollector
from quiz_brain import QuizBrain

while True:
    print("Start of Quiz\n")

    data = DataCollector()
    data.set_num()
    data.set_diff()
    data.set_category_json()
    data.set_url()
    trivia_json = data.get_full_trivia_json()['results']

    question_bank = []

    for i in trivia_json:
        question_bank.append(Question(
            i['question'],
            i['correct_answer'],
            i['incorrect_answers'],
            i['type']
        ))

    for i in question_bank:
        i.text_cleaner()

    quiz = QuizBrain(question_bank)

    print("Lets begin the quiz.")
    print("For the True/False questions, type true or false.")
    print("For the multiple choice questions, type the option number or the option string.\n")

    while quiz.still_has_questions():
        quiz.next_question()

    print("You've completed the quiz!")
    print(f"Your final score is: {quiz.score}/{quiz.question_num}\n")