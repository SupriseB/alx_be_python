
# Prompting for a single task
task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ").lower()
priority = input("Priority (high/medium/low): ").lower()


# Use match case to handle priority
match priority:
    case "high":
        Reminder = f"Reminder: '{task}' is a HIGH priority task."
    case "medium":
        Reminder = f"Reminder: '{task}' is a MEDIUM priority task."
    case "low":
        Reminder = f"Reminder: '{task}' is a LOW priority task."
    case _:
        Reminder = f"Reminder: '{task}' has an UNKNOWN priority level."

# Adjusting message if task is time-bound
if time_bound == "yes":
    message += " This task requires immediate attention today!"

# Use a loop to display the reminder 3 times
for _ in range(3):
    print(Reminder)
