import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}

request = requests.get(url="https://opentdb.com/api.php", params=parameters)

question_data = request.json()["results"]
