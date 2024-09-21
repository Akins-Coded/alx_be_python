task = input("Describe your task: " )
priority = input("What is the Priority Level for this Task (high, medium, low) ? ").lower()
time_bound = input("IS The Task Time Sensitive  (yes or no) : " ).lower()


match priority:
    case "high":
       if time_bound == "yes":
           print(f"Reminder: '{task}' is a high priority task that requires immediate attention As Soon As Possible!")
       elif time_bound == "no":
           print(f"Reminder: '{task}' is a high priority task that requires attention today!")

    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires attention Kindly attend to it today!")
        elif time_bound == "no":
            print(f"Reminder: '{task}' is a medium priority task, attend to it when you can")

    case "low":
        if time_bound == "yes":
            print(f"Note: '{task}' is a low priority task. Consider completing it when you can!")
        elif time_bound == "no":
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time!")

