fastest_sprint = 100
slowest_sprint = 0
summer = 0
average = 0

for i in range(5):
    sprints = float(input("Enter sprint time: "))
    if slowest_sprint < sprints:
        slowest_sprint = sprints
    if fastest_sprint > sprints:
        fastest_sprint = sprints
    summer += sprints

average = summer/5

print(f"Best time: {fastest_sprint}, Worst time: {slowest_sprint}, Average time: {round(average)}")


temp = 0
increasing = 0
decreasing = 0  
stagnant = 0
summer = 0
for i in range(6):
    user_ratings = int(input("Enter your weekly ratings: "))
    if i  == 0:
        temp = user_ratings
    summer += user_ratings
    if temp < user_ratings:
        increasing += 1
    elif temp > user_ratings:
        decreasing += 1
    elif temp == user_ratings:
        stagnant += 1
    if i != 0:
        temp = user_ratings
average = round(summer/6)
if abs(increasing - decreasing) < 3:
    print(f"The trend is varying, and the average rating is {average}")   
elif decreasing < increasing and stagnant < increasing:
    print(f"The trend is increasing, and the average rating is {average}")
elif decreasing > increasing and stagnant < decreasing:
    print(f"The trend is decreasing, and the average rating is {average}")
elif stagnant > increasing and stagnant > decreasing:
    print(f"The trend is stagnant, and the average rating is {average}")


NORMAL_TEMP = 98.6
increasing = 0
decreasing = 0
stagnant = 0
prev_temp = 0
summer = 0
for i in range(7):
    patient_temp = float(input("Enter patient temp: "))
    if patient_temp > NORMAL_TEMP:
        increasing += 1
    elif patient_temp < NORMAL_TEMP:
        decreasing += 1
    elif patient_temp == NORMAL_TEMP:
        stagnant += 1
    summer += patient_temp
print(f"Above normal: {increasing} days, Below normal: {decreasing} days, Equal to normal: {stagnant} days. Average temp: {round(summer/7)}")



total_accuracy = 0.0
previous_accuracy = None
improving = True
deteriorating = True
iterations = 10

for i in range(iterations):
    accuracy = float(input(f"Enter accuracy for iteration {i + 1}: "))
    total_accuracy += accuracy

    if previous_accuracy is not None:
        if accuracy > previous_accuracy:
            deteriorating = False
        elif accuracy < previous_accuracy:
            improving = False
        else:
            improving = deteriorating = False

    previous_accuracy = accuracy

if improving:
    trend = "Improving"
elif deteriorating:
    trend = "Deteriorating"
else:
    trend = "Fluctuating"

average_accuracy = total_accuracy / iterations

print(f"Trend: {trend}")
print(f"Average accuracy: {average_accuracy:.1f}%")


# 5. Autonomous Vehicles: Speed Control System
total_speed = 0.0
previous_speed = None
constant = True
increasing = True
decreasing = True
seconds = 10

for i in range(seconds):
    speed = float(input(f"Enter speed for second {i + 1}: "))
    total_speed += speed

    if previous_speed is not None:
        if speed > previous_speed:
            constant = False
            decreasing = False
        elif speed < previous_speed:
            constant = False
            increasing = False
        else:
            increasing = decreasing = False

    previous_speed = speed

if constant:
    trend = "Constant"
elif increasing:
    trend = "Increasing"
elif decreasing:
    trend = "Decreasing"
else:
    trend = "Fluctuating"

average_speed = total_speed / seconds

print(f"Speed trend: {trend}")
print(f"Average speed: {average_speed:.1f} mph")

# 6. Healthcare: Medication Adherence Tracking
pills_taken = 0
pills_missed = 0
days = 14
missed_limit = 3

for i in range(days):
    adherence = int(input(f"Did you take the pill on day {i + 1}? (1 for Yes, 0 for No): "))

    if adherence == 1:
        pills_taken += 1
    elif adherence == 0:
        pills_missed += 1
    else:
        print("Invalid input! Please enter 1 for Yes or 0 for No.")

if pills_missed > missed_limit:
    warning = "Warning: You have missed more than 3 days of medication!"
else:
    warning = "No warning needed."

print(f"Pills taken: {pills_taken}")
print(f"Pills missed: {pills_missed}")
print(f"Warning: {warning}")
