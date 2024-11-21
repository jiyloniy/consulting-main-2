import requests

# http://127.0.0.1:8000/universities/
# login 
username = 'admin'
password = 'admin'
response = requests.post('http://127.0.0.1:8000/login/', json={'username': username, 'password': password})
print(response.status_code)
print(response.json())
# {'refresh': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczODIxNjU2NSwiaWF0IjoxNzMyMTY4NTY1LCJqdGkiOiIzYzkzZWY3YjBkNGU0ZTY1OGY0NmRhNzdhOGVmNDY5MSIsInVzZXJfaWQiOjF9.y4Fc7DCVNmrlEXRZvj4vfqqK7mlKcEe9oTiM67Marz4', 'access': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQwODA4NTY1LCJpYXQiOjE3MzIxNjg1NjUsImp0aSI6ImVkYjk3OTZmNDJiOTRjYzY5OTEzZWY5YWY4OTFkZmE4IiwidXNlcl9pZCI6MX0.Z6GCxBLDh4iVPEvUcbLd0mHrj4tSqXs_CGvzvKzdW6o'}
refresh = response.json()['refresh']

post_data = {
    "name": "KIUF",
    "type": 3,
    "city": "Farg'ona",
    "rank": {
        "jahon": "1000",
        "uzb": "10"
    },
    "requirements": {
        "TOPIK": "2",
        "GPA": "4"
    },
    "dastur": [
        "bakalavr"
    ],
    "scholarships": [
        "TOPIK 4 uchun 100% grant"
    ],
    "departments": [
        "it",
        " ingliz tili",
        " koreys tili",
        " turizm"
    ],
    "img": "https://consulting-buix.onrender.com/media/universities/kiuf.jpg",
    "url_link": "https://youtu.be/_ApRc02PRoU",
    "is_active": True,
    "comments": "No comment"
}

response = requests.post(' http://127.0.0.1:8000/universities/', json=post_data, headers={'Authorization': 'Bearer ' + refresh})
print(response.status_code)
print(response.json())