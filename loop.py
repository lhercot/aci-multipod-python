'''
Loop script to poll the change page and keep it fresh
Should be replace by a WebSocket
'''
import requests
import time

while True:
    time.sleep(5)
    try:
        print("Poll")
        requests.get('http://localhost:5000/api/v0.1/modified')
    except Exception:
        print("Failed, retry")
