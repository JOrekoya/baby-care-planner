from datetime import datetime

class Utils:
    @staticmethod
    def parse_time(time_str):
        try:
            return datetime.strptime(time_str.strip(), "%I:%M %p")
        except ValueError:
            return datetime.strptime(time_str.strip(), "%I %p")

    @staticmethod
    def format_time(dt):
        return dt.strftime("%I:%M %p")

    @staticmethod
    def current_datetime():
        return datetime.now()
