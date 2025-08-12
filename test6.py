import requests

def fetch_random_user():
    r = requests.get('https://randomuser.me/api/')
    

    if r.status_code == 200:
        data = r.json()

        # функция извлечения данных
        user_info = {
            "first_name": data['results'][0]['name']['first'],
            "last_name": data['results'][0]['name']['last'],
            "email": data['results'][0]['email'],
            "city": data['results'][0]['location']['city']
            }
        
        return user_info
    else:
        return {"error": f"Ошибка: {r.status_code} - {r.reason}"}
    
user_info = fetch_random_user()
print(user_info)