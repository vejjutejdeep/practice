import requests,json
# app = Flask(__name__)
# @app.route("")
# def get_user():
def create_user():
    users = input()
    url = "https://randomuser.me/api/?results=" + users

    response = requests.get(url)

    response_json = response.json()
    # print(response.json())
    person = []
    count = 1
    for i in response_json['results']:

        s_person = {}
        s_person['person' + str(count)]  = {
                'firstname' : i['name']['first'],
                'last_name'  :i['name']['last'],
                'email' :i['email'],
                'location' : i['location']['coordinates'],
                'datetime' : i['registered']['date'],
            }
        person.append(s_person)
        count += 1
    json_file = json.dumps(person)
    with open("data_file.json", "w") as write_file:
        json.dump(person, write_file)

def fetch_ramdom_user():

    with open('data_file.json', 'r') as read_file:

        user = []
        for each in read_file:
            print(each)

            user.append(each[1])
fetch_ramdom_user()