import requests

response = requests.get('http://127.0.0.1:5000/api/news')

if response.status_code == 200:
    print('Success!')
    print(response.json())
else:
    print(f'Failed with status code: {response.status_code}')
