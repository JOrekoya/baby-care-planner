from logger import Logger
from storage import Storage
from recommender import Recommender
from goals import Goals
from utils import Utils
from insights import Insights

def main():
    print("Welcome to Baby Care Planner")
    insights = Insights(Logger, Goals)  # pass the classes (Logger has static helpers)

    while True:
        user_input = input("Log an event, type 'status', 'summary', or 'exit': ").strip()
        if not user_input:
            continue

        cmd = user_input.lower().strip()

        if cmd == 'exit':
            break

        elif cmd == 'status':
            events = Storage.load_events()
            feedings, sleep_hours = Goals.summarize_today(events)
            print(f"Today's Summary: {feedings} feedings, {round(sleep_hours, 1)} hrs of sleep.")
            print(Recommender.next_feeding_suggestion(events))
            print(Recommender.sleep_goal_status(events))

        elif cmd == 'summary':
            insights.generate_summary()

        else:
            parsed_event = Logger.parse_event(user_input)
            if parsed_event.get('type') and parsed_event['type'] != 'unknown':
                Storage.save_event(parsed_event)
                print("Event logged successfully.")
            else:
                print("Could not understand the input. Try again. Examples:\n"
                      "  - Fed baby at 2 PM\n  - Baby slept from 1 PM to 3 PM\n  - Nap 30 minutes")

if __name__ == "__main__":
    main()
