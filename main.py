from logger_module import Logger
from storage import Storage
from recommender import Recommender
from goals import Goals
from utils import Utils

def main():
    print("Welcome to Baby Care Planner")
    while True:
        user_input = input("Log an event or type 'status' to check progress, 'exit' to quit: ")

        if user_input.lower() == 'exit':
            break

        elif user_input.lower() == 'status':
            events = Storage.load_events()
            feedings, sleep_hours = Goals.summarize_today(events)
            print(f"Today's Summary: {feedings} feedings, {round(sleep_hours, 1)} hrs of sleep.")
            print(Recommender.next_feeding_suggestion(events))
            print(Recommender.sleep_goal_status(events))
        else:
            parsed_event = Logger.parse_event(user_input)
            if parsed_event['type'] != 'unknown':
                Storage.save_event(parsed_event)
                print("Event logged successfully.")
            else:
                print("Could not understand the input. Try again.")

if __name__ == "__main__":
    main()
