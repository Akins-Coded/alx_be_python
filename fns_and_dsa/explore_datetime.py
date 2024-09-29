from datetime import datetime, timedelta
def main():
    # Get the current date and time
    current_date_time = datetime.now()

    print(f"Current date and time: {current_date_time}")

    # Prompt user for the number of days to add
    number_of_days = int(input("Enter the number of days to add to the current date: "))

    # Calculate the future date
    future_date = current_date_time + timedelta(days=number_of_days)

    print(f"Future date: {future_date.date()}")

if __name__ == "__main__":
    main()
