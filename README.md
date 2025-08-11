# Baby Care Planner 🍼🗓️

An AI-powered baby care assistant that helps new parents track and manage their baby's feeding and sleep routines. Baby Care Planner combines a conversational chatbot interface with smart care planning features to reduce parental stress and promote healthy routines.

---

## Project Goals
- Provide a simple interface for parents to log feedings and naps.
- Track care goals such as daily sleep totals and feeding schedules.
- Offer proactive suggestions/reminders (agentic AI concept).
- Future: Expand to wearable integrations and health alerts.

---

## Current Features (MVP)
- Conversational logging of feedings and sleep events.
- Tracks routines using simple text input (e.g., "Fed baby at 8 AM").
- Returns structured feedback to the user.
- Local JSON storage (coming soon).
- Modular codebase designed for scalability.

---

## Project Structure
baby-care-planner/
├── main.py # Main script to run the chatbot
├── logger.py # Parses user input into structured events
├── storage.py # (Planned) Save and retrieve logs
├── recommender.py # (Planned) Suggest next actions
├── utils.py # (Planned) Time formatting and helpers
├── README.md
└── .gitignore