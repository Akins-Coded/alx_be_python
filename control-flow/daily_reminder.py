task = input("Describe your task: ")
priority = input("What is the Priority Level for this Task (high, medium, low) ? ").lower()
time_bound = input("IS The Task Time Sensitive  (yes or no) : ").lower()


match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = f"Invalid priority: '{task}'"

if time_bound == "yes":
    reminder = f"{message} that requires immediate attention today!"
elif time_bound == "no":
    reminder = f"{message}. Consider completing it when you have free time.!"

print("Reminder:", reminder)

