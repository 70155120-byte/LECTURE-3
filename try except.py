try:
    age = int(input("Enter your age: "))

    if age >= 18:
        print("You are an adult.")
    else:
        print("You are under 18.")

except ValueError:
    print("Invalid input. Please enter your age as a number.")