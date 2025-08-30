import re
from utils import Utils
from storage import Storage

class Logger:
    @staticmethod
    def parse_event(user_input):
        """
        Parse natural text like:
          - "Fed baby at 2 PM"
          - "Baby slept from 1 PM to 3 PM"
        Returns a dict with consistent fields.
        """
        user_input_raw = user_input
        user_input = user_input.lower()
        timestamp = Utils.current_datetime().isoformat()

        # Feeding
        if "fed" in user_input or "feeding" in user_input:
            match = re.search(r'at (\d{1,2}(:\d{2})?\s*(am|pm))', user_input)
            if match:
                time_str = match.group(1)
                event_time = Utils.parse_time(time_str)
            else:
                event_time = Utils.current_datetime()
            return {
                "type": "feeding",
                "start_time": event_time.isoformat(),
                "end_time": None,
                "note": user_input_raw,
                "timestamp": timestamp
            }

        # Sleep (from ... to ...)
        if "slept" in user_input or "sleep" in user_input or "nap" in user_input:
            match = re.search(r'from (\d{1,2}(:\d{2})?\s*(am|pm)) to (\d{1,2}(:\d{2})?\s*(am|pm))', user_input)
            if match:
                start_str = match.group(1)
                end_str = match.group(4)
                start_time = Utils.parse_time(start_str)
                end_time = Utils.parse_time(end_str)
                # if end_time earlier than start_time, assume next day
                if end_time <= start_time:
                    from datetime import timedelta
                    end_time = end_time + timedelta(days=1)
                return {
                    "type": "sleep",
                    "start_time": start_time.isoformat(),
                    "end_time": end_time.isoformat(),
                    "note": user_input_raw,
                    "timestamp": timestamp
                }
            # fallback: "slept 2 hours" or "nap 30 minutes"
            match2 = re.search(r'(\d+(\.\d+)?)\s*(hours|hour|hrs|hr|minutes|minute|min)', user_input)
            if match2:
                qty = float(match2.group(1))
                unit = match2.group(3)
                # convert to duration and set start_time to now - duration
                from datetime import timedelta
                if unit.startswith('min'):
                    duration = timedelta(minutes=qty)
                else:
                    duration = timedelta(hours=qty)
                end_time = Utils.current_datetime()
                start_time = end_time - duration
                return {
                    "type": "sleep",
                    "start_time": start_time.isoformat(),
                    "end_time": end_time.isoformat(),
                    "note": user_input_raw,
                    "timestamp": timestamp
                }

        # Unknown
        return {
            "type": "unknown",
            "start_time": None,
            "end_time": None,
            "note": user_input_raw,
            "timestamp": timestamp
        }

    @staticmethod
    def get_event_summary(event_type):
        events = Storage.load_events()
        return sum(1 for e in events if e.get('type') == event_type)

    @staticmethod
    def get_all_events():
        return Storage.load_events()
