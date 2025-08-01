#explore_datetime.py
def display_current_datetime():
    from datetime import datetime
    
    # Get the current date and time
    current_date = datetime.now()
    
    # Format the date and time in a readable format
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"Current Date and Time: {formatted_date}")   
    

def calculate_future_date():
    from datetime import datetime, timedelta
    
    # Prompt the user for the number of days
    days = int(input("Enter the number of days to add to the current date: "))
    
    # Get the current date
    current_date = datetime.now()
    
    # Calculate the future date
    future_date = current_date + timedelta(days=days)
    
    # Format and print the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future Date after {days} days: {formatted_future_date}")

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date() 
