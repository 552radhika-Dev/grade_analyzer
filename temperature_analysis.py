#Name: Radhika Sekar
#Roll No: iitp_aimltn_2602483
#Python: Loops & Automation - Subjective
#Question: Weekly Temperature Analysis

print("===== Task 1: Find Maximum and Minimum =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
max_temp=max(temperatures)
min_temp=min(temperatures)
for temp in temperatures:
    if temp == max_temp:
        print(f"Highest Temperature: {temp}°C")
    elif temp == min_temp:
        print(f"Lowest Temperature: {temp}°C")

print("\n===== Task 2: Count Hot Days =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
count_hot_days = 0
for temp in temperatures:
    if temp > 30:
        count_hot_days += 1
print(f"Hot days (> 30°C): {count_hot_days}")

print("\n===== Task 3: Alert System =====")
temperatures = [28, 32, 35, 40, 31, 33, 30]
hot_days_before_alert = 0
extreme_temp_day = None

for i, temp in enumerate(temperatures):
    if temp == 40:
        extreme_temp_day= i + 1 
        break
    elif temp > 30:
        hot_days_before_alert += 1

print(f"Hot days before alert: {hot_days_before_alert}")
print(f"Alert! Extreme temperature 40°C detected on day {extreme_temp_day }")

           





