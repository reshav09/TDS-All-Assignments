from datetime import date, timedelta

# Define the date range
start_date = date(1985, 11, 8)   #write your date here
end_date = date(2012, 11, 27)    #write your date here

# Initialize counters
saturdays = 0
sundays = 0

# Loop through each date in the range
current_date = start_date
while current_date <= end_date:
    if current_date.weekday() == 5:  # Saturday
        saturdays += 1
    elif current_date.weekday() == 6:  # Sunday
        sundays += 1
    current_date += timedelta(days=1)

# Output results
print(f"Number of Saturdays: {saturdays}")
print(f"Number of Sundays: {sundays}")
print(f"Your Answer is: {sundays+saturdays} ")

