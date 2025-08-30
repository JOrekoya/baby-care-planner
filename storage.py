import json
import os

class Storage:
    FILE = "events.json"

    @staticmethod
    def save_event(event):
        events = Storage.load_events()
        events.append(event)
        with open(Storage.FILE, "w") as f:
            json.dump(events, f, indent=2)

    @staticmethod
    def load_events():
        if not os.path.exists(Storage.FILE):
            return []  # no file yet → return empty list
        try:
            with open(Storage.FILE, "r") as f:
                content = f.read().strip()
                if not content:  # file exists but empty
                    return []
                return json.loads(content)
        except (json.JSONDecodeError, IOError):
            # corrupted JSON or other read error
            return []
