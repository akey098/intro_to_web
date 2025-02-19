from datetime import datetime, timedelta
import calendar
import time

# 1. Getting the Current Date and Time
current_time = datetime.now()
print("Current date and time:", current_time)

# 2. Extracting Specific Parts of a Date
year = current_time.year
month = current_time.month
day = current_time.day
hour = current_time.hour
minute = current_time.minute
second = current_time.second
print(f"Year: {year}, Month: {month}, Day: {day}, Hour: {hour}, Minute: {minute}, Second: {second}")

# 3. Creating a Specific Date and Time
specific_date = datetime(2023, 12, 25, 10, 30, 0)
print("Specific Date:", specific_date)

# 4. Formatting Dates and Times (strftime)
formatted_date = current_time.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date:", formatted_date)

# 5. Parsing Strings into Date Objects (strptime)
date_string = "2025-02-01 14:30:45"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Parsed Date Object:", parsed_date)

# 6. Performing Date Calculations (timedelta)
future_date = current_time + timedelta(days=7)
past_date = current_time - timedelta(days=3)
print("Future Date:", future_date)
print("Past Date:", past_date)

# 7. Finding the Difference Between Two Dates
event_date = datetime(2025, 12, 31)
days_until_event = (event_date - current_time).days
print("Days until event:", days_until_event)

# 8. Creating a Calendar
year = 2025
month = 2
print(calendar.month(year, month))

# 9. Implementing a Timer (Countdown)
countdown_seconds = 5
for i in range(countdown_seconds, 0, -1):
    print(f"Time remaining: {i} seconds")
    time.sleep(1)
print("Time's up!")

# 10. Measuring Execution Time
start_time = time.time()
time.sleep(0.5)  # Simulate processing time
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution Time: {execution_time:.4f} seconds")
