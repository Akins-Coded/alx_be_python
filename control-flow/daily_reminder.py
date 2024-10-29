task = input("Enter your Task: ")
time_bound = input("Is it time-bound?(yes/no): ").lower()
priority = input("Priority(high/medium/low): ").lower()



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

