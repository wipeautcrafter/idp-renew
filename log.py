import requests


class Logger:
    def __init__(self, token:str, chat_id:str):
        self.token = token
        self.chat_id = chat_id

        self.endpoint = f"https://api.telegram.org/{self.token}/sendMessage"
    
    def log(self, message):
        data = {
            "chat_id": self.chat_id,
            "text": message
        }

        req = requests.post(self.endpoint, data)

        print(message)

        if(req.status_code != 200):
            raise Exception("Failed to send message.")