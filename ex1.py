is_sunny = eval(input("Is this a sunny day? (True/False): "))
has_umbrella = eval(input("Do you have an umbrella? (True/False): "))
# print(type(is_sunny), type(has_umbrella))
go_outside = False
stay_inside = False
perfect_day = False
if is_sunny == False and has_umbrella == False:
    print("I guess it's better to stay inside!")
    stay_inside = True
elif is_sunny == True and has_umbrella == False:
    perfect_day = True
    print("It's a perfect day to be outside!")
elif is_sunny == True or has_umbrella == True:
    go_outside = True
    print("Yup! You can go out now! Be safe!")