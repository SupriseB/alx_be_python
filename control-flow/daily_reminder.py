
# Prompting for a single task
task = input("Enter your task for today: ")
task_priority = input("Enter the task’s priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

# Use match case to handle priority
match priority:
    case "high":
        message = f"Reminder: '{task}' is a HIGH priority task."
    case "medium":
        message = f"Reminder: '{task}' is a MEDIUM priority task."
    case "low":
        message = f"Reminder: '{task}' is a LOW priority task."
    case _:
        message = f"Reminder: '{task}' has an UNKNOWN priority level."

# Adjusting message if task is time-bound
if time_bound == "yes":
    message += " This task requires immediate attention today!"

# Use a loop to display the reminder 3 times
for _ in range(3):
    print(message)
