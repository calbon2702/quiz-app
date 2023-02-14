from question_model import Question
from data import DataCollection
from quiz_brain import QuizBrain
import requests

start_url = "https://opentdb.com/api.php?"

while True:
    print("Start of Quiz\n")
    num_questions = input("How many questions would you like? (Max 50)\n")
    difficulty = input("Select difficulty of questions (easy/medium/hard or skip for any):\n")

    data = DataCollection(num_questions, difficulty)
    data.set_category_json(int(input(f"{data.get_category_list()}\n")))

    # quiz = QuizBrain(question_bank)

    # while quiz.still_has_questions():
    #     quiz.next_question()

    # print("You've completed the quiz!")
    # print(f"Your final score is: {quiz.score}/{quiz.question_num}")