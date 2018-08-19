import requests
from datetime import datetime
from collections import Counter

ACCESS_TOKEN = '5d9a6deb5d9a6deb5d9a6deb0d5dffd5e155d9a5d9a6deb06e32138fbd76b7872e91771'
API_URL = 'https://api.vk.com/method'
API_VERSION = '5.71'

def get_user_id(user_ids):
    url = '{url}/users.get'.format(url=API_URL)
    payload = {'v':API_VERSION, 'access_token':ACCESS_TOKEN, 'user_ids':user_ids, 'fields':'id'}
    res = requests.get(url, params=payload)
    return res.json()

def get_friends_list(user_id):
    url = '{url}/friends.get'.format(url=API_URL)
    payload = {'v':API_VERSION, 'access_token':ACCESS_TOKEN, 'user_id':user_id, 'fields':'bdate'}
    res = requests.get(url, params=payload)
    return res.json()

def calc_age(uid):
    res = get_user_id(uid)
    for user in res['response']:
        friend_list = get_friends_list(user['id'])
        age_counter = get_ages(friend_list)
    return sorted(age_counter.items(), key=lambda age: (-age[1], age[0]))

def calc_person_age(birth_date):
    dtob = parse_date(birth_date)
    if dtob:
        today = datetime.today()
        return today.year - dtob.year
    else:
        return

def parse_date(date_string):
    try:
        date = datetime.strptime(date_string, '%d.%m.%Y')
    except Exception:
        return None
    else:
        return date

def get_ages(friends):
    ages = Counter()
    for friend in friends['response']['items']:
        if 'bdate' in friend:
            age = calc_person_age(friend['bdate'])
            if age:
                ages[age] +=1
    return ages

if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)
