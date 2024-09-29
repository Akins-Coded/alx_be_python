from datetime import datetime, timedelta


def display_future_date():
    # Get the current date and time
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

    # Prompt the user for the number of days to add
    number_of_days = int(input("Enter the number of days to add to the current date: "))

    # Calculate the future date
    future_date = current_date + timedelta(days=number_of_days)

    # Print the future date
    print("Future date:", future_date.strftime("%Y-%m-%d"))


# Call the function to display the future date
display_future_date()
