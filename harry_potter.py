import time
import sys
from datetime import datetime

def slow_print(text, delay=0.05):
    """Prints text one character at a time with a delay."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line

def calculate_countdown(event_date):
    """Calculates the time remaining until the event."""
    current_time = datetime.now()
    time_remaining = event_date - current_time
    days = time_remaining.days
    seconds = time_remaining.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return days, hours, minutes, seconds

def main():
    slow_print("Welcome to a magical journey...")
    time.sleep(1)
    slow_print("🌟✨ A world of wonder awaits! ✨🌟", 0.1)
    time.sleep(2)
    
    event_date = datetime(2025, 2, 12, 15, 30)  
    
    slow_print("\nUnwrapping your surprise... 🧙‍♀️🪄", 0.1)
    time.sleep(1)
    slow_print("\nHere is your countdown to the magic! 🕰️✨\n", 0.05)
    
    while True:
        days, hours, minutes, seconds = calculate_countdown(event_date)
        
        sys.stdout.write("\033[F\033[K")
        countdown_message = (
            f"Only {days} days, {hours} hours, {minutes} minutes, "
            f"and {seconds} seconds until we step into the Wizarding World!"
        )
        sys.stdout.write(countdown_message + "\n")
        sys.stdout.flush()
        
        time.sleep(1)

if __name__ == "__main__":
    main()
