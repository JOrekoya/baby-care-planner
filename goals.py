from utils import Utils
from datetime import datetime, timedelta

class Goals:
    DAILY_SLEEP_GOAL_HRS = 12
    FEEDING_INTERVAL_HRS = 4

    @staticmethod
    def summarize_today(events):
        today = Utils.current_datetime().date()
        feedings = 0
        total_sleep = timedelta()
        for e in events:
            start = datetime.fromisoformat(e["start_time"]).date() if e["start_time"] else None
            if start != today:
                continue
            if e["type"] == "feeding":
                feedings += 1
            elif e["type"] == "sleep" and e["end_time"]:
                start_dt = datetime.fromisoformat(e["start_time"])
                end_dt = datetime.fromisoformat(e["end_time"])
                total_sleep += (end_dt - start_dt)
        return feedings, total_sleep.total_seconds() / 3600
