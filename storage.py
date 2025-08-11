import json
import os

class Storage:
    FILE_NAME = 'baby_log.json'

    @staticmethod
    def save_event(event):
        data = []
        if os.path.exists(Storage.FILE_NAME):
            with open(Storage.FILE_NAME, 'r') as f:
                data = json.load(f)
        data.append(event)
        with open(Storage.FILE_NAME, 'w') as f:
            json.dump(data, f, indent=2)

    @staticmethod
    def load_events():
        if os.path.exists(Storage.FILE_NAME):
            with open(Storage.FILE_NAME, 'r') as f:
                return json.load(f)
        return []
