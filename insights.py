class Insights:
    def __init__(self, logger_class, goals_class):
        """
        logger_class: class with get_all_events() static method (Logger)
        goals_class: class with get_summary(events) static method (Goals)
        """
        self.logger_class = logger_class
        self.goals_class = goals_class

    def generate_summary(self):
        events = self.logger_class.get_all_events()
        goals = self.goals_class.get_summary(events)

        print("\n📊 Baby Care Summary 📊")
        print("------------------------")
        for goal, data in goals.items():
            print(f"{goal.title()} — {data['current']} / {data['target']}")

        print("\nRecent Events:")
        # show last 5 events (if any) with a readable time
        for event in events[-5:]:
            note = event.get("note", "")
            ts = event.get("timestamp") or event.get("start_time") or "unknown time"
            print(f" - {event.get('type','?').title()} at {ts} — {note}")
