import requests
url = "https://api.foldingathome.org/user/wcbutler@gmail.com" #change email with your email
user_data = requests.get(url).json()
print ('Folding@Home Score: ', user_data['score'])
