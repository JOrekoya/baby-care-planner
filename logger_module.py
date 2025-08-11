import re
from utils import Utils

class Logger:
    @staticmethod
    def parse_event(user_input):
        user_input = user_input.lower()
        if "fed" in user_input:
            match = re.search(r'at (\d{1,2}(:\d{2})?\s*(am|pm))', user_input)
            if match:
                time_str = match.group(1)
                event_time = Utils.parse_time(time_str)
                return {"type": "feeding", "start_time": event_time.isoformat(), "end_time": None, "note": user_input}
        elif "slept" in user_input or "sleep" in user_input:
            match = re.search(r'from (\d{1,2}(:\d{2})?\s*(am|pm)) to (\d{1,2}(:\d{2})?\s*(am|pm))', user_input)
            if match:
                start_str = match.group(1)
                end_str = match.group(4)
                start_time = Utils.parse_time(start_str)
                end_time = Utils.parse_time(end_str)
                return {"type": "sleep", "start_time": start_time.isoformat(), "end_time": end_time.isoformat(), "note": user_input}
        return {"type": "unknown", "start_time": None, "end_time": None, "note": user_input}
