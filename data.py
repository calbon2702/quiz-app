import requests

class DataCollection:
    def __init__(self, q_num, q_diff):
        self.q_num = q_num
        self.q_diff = q_diff
        self.q_category_json = {}
        self.q_category_name = ""
        self.q_category_id = ""

    def get_full_category_json(self):
        category_json = requests.get("https://opentdb.com/api_category.php").json()
        return category_json

    def get_category_list(self):
        category_json_list = self.get_full_category_json()['trivia_categories']
        
        print("Pick a category (enter ID or skip to pick any category):\n")

        for cat in category_json_list:
            print(f"{cat['id']}: {cat['name']}")

    def set_category_json(self, cat_id):
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
