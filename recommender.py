from datetime import datetime, timedelta
from utils import Utils
from goals import Goals

class Recommender:
    @staticmethod
    def next_feeding_suggestion(events):
        latest_feeding = None
        for e in reversed(events):
            if e["type"] == "feeding" and e["start_time"]:
                latest_feeding = datetime.fromisoformat(e["start_time"])
                break
        if not latest_feeding:
            return "No feedings logged yet."
        time_since = Utils.current_datetime() - latest_feeding
        if time_since >= timedelta(hours=Goals.FEEDING_INTERVAL_HRS):
            return f"It's been {int(time_since.total_seconds()//3600)} hours since the last feeding. Time to feed."
        else:
            next_in = Goals.FEEDING_INTERVAL_HRS - (time_since.total_seconds() / 3600)
            return f"Next feeding in approximately {int(next_in * 60)} minutes."

    @staticmethod
    def sleep_goal_status(events):
        _, total_sleep_hours = Goals.summarize_today(events)
        remaining = Goals.DAILY_SLEEP_GOAL_HRS - total_sleep_hours
        if remaining <= 0:
            return "Sleep goal met for today."
        else:
            return f"Baby needs approximately {round(remaining, 1)} more hours of sleep today."
