import requests

# https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=multiple

class DataCollection:
    def __init__(self, q_diff=""):
        self.q_num = "10"
        self.q_diff = ""
        self.q_category_json = {}
        self.q_category_name = ""
        self.q_category_id = ""
        self.q_url = ""

    def set_num(self):
        num = input("How many questions would you like? (Max 50)\n")

        if num == "":
            self.q_num = "10"

        else:
            self.q_num = num
    
    def set_diff(self):
        self.q_diff = input("Select difficulty of questions (easy/medium/hard or skip for any):\n")

    def get_full_category_json(self):
        category_json = requests.get("https://opentdb.com/api_category.php").json()
        return category_json

    def get_category_list(self):
        category_json_list = self.get_full_category_json()['trivia_categories']
        
        print("Pick a category (enter ID or skip to pick any category):\n")

        for cat in category_json_list:
            print(f"{cat['id']}: {cat['name']}")

    def set_category_json(self):
        cat_id = int(input(f"{self.get_category_list()}\n"))
        category_json = self.get_full_category_json()['trivia_categories']

        for cat in category_json:
            if cat['id'] == cat_id:
                self.q_category_json = cat
                break
        
        self.set_category_name(self.q_category_json['name'])
        self.set_category_id(self.q_category_json['id'])

    def set_category_name(self, name):
        self.q_category_name = name

    def set_category_id(self, id):
        self.q_category_id = id

    def set_url(self):
        url = "https://opentdb.com/api.php?"
        url += f"amount={self.q_num}"
        print(f"SELFNUM: {self.q_num}")

        if self.q_diff:
            url += f"&difficulty={self.q_diff}"

        if self.q_category_id:
            url += f"&category={self.q_category_id}"
