from utils import Utils
from datetime import datetime, timedelta

class Goals:
    DAILY_SLEEP_GOAL_HRS = 12
    FEEDING_INTERVAL_HRS = 4
    FEEDING_TARGET_PER_DAY = 8   # example target (can change)

    @staticmethod
    def summarize_today(events):
        """
        Return (feedings_count, total_sleep_hours) for events whose start_time is today.
        """
        today = Utils.current_datetime().date()
        feedings = 0
        total_sleep = timedelta()
        for e in events:
            start_iso = e.get("start_time")
            if not start_iso:
                continue
            try:
                start_dt = datetime.fromisoformat(start_iso)
            except Exception:
                continue
            if start_dt.date() != today:
                continue
            if e.get("type") == "feeding":
                feedings += 1
            elif e.get("type") == "sleep" and e.get("end_time"):
                try:
                    end_dt = datetime.fromisoformat(e.get("end_time"))
                    total_sleep += (end_dt - start_dt)
                except Exception:
                    continue
        return feedings, total_sleep.total_seconds() / 3600

    @staticmethod
    def get_summary(events):
        """
        Return a dict summarizing progress & targets for feeding and sleep.
        """
        feedings, sleep_hours = Goals.summarize_today(events)
        return {
            "feeding": {"current": feedings, "target": Goals.FEEDING_TARGET_PER_DAY},
            "sleep": {"current": round(sleep_hours, 2), "target": Goals.DAILY_SLEEP_GOAL_HRS}
        }
