import logger

def main():
    print("Welcome to Baby Care Planner")
    user_input = input("Log an event: ")
    parsed_event = logger.parse_event(user_input)
    print(f"Parsed Event: {parsed_event}")

if __name__ == "__main__":
    main()

