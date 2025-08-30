from datetime import datetime

class Utils:
    @staticmethod
    def parse_time(time_str):
        """
        Parse a time like '2 PM' or '2:30 PM' and return a datetime set to today's date.
        """
        now = datetime.now()
        try:
            parsed = datetime.strptime(time_str.strip(), "%I:%M %p")
        except ValueError:
            parsed = datetime.strptime(time_str.strip(), "%I %p")
        # attach today's date
        parsed = parsed.replace(year=now.year, month=now.month, day=now.day)
        return parsed

    @staticmethod
    def format_time(dt):
        return dt.strftime("%I:%M %p")

    @staticmethod
    def current_datetime():
        return datetime.now()
