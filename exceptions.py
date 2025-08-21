try:
    x = int(input("Enter an integer: "))
    print("You entered:", x)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
else:
    print("No exceptions occurred. The input was valid.")
finally:
    print("Execution completed.")  # This will always execute regardless of exceptions