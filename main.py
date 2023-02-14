from question_model import Question
from data import DataCollection
from quiz_brain import QuizBrain
import requests

start_url = "https://opentdb.com/api.php?"

while True:
    print("Start of Quiz\n")
    data = DataCollection()
    data.set_num()
    data.set_diff()
    data.set_category_json()
    data.set_url()

    # quiz = QuizBrain(question_bank)

    # while quiz.still_has_questions():
    #     quiz.next_question()

    # print("You've completed the quiz!")
    # print(f"Your final score is: {quiz.score}/{quiz.question_num}")