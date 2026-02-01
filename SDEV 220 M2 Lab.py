# Claire Weaver
# GPACounter
# Determines wether a student has made the Dean's List or Honor Roll.

running = 1

while running < 2:
    last_name = str(input("Enter last name (or enter 'ZZZ' to quit): "))
    if last_name == "ZZZ":
        running += 1
    else:
        first_name = str(input("Enter first name: "))
        gpa = float(input("Enter GPA (X.XX): "))
        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List!")
        elif gpa >= 3.25 and gpa < 3.5:
            print(f"{first_name} {last_name} has made the Honor Roll!")
        else:
            print(f"{first_name} {last_name} is not in the Honors society!")
        running = 1
