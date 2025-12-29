marks = int(input("Enter your marks (0-100): "))

if marks >= 90:
    print("This student's score of " + str(marks) + " earns an A grade")
elif marks >= 80:
    print("This student's score of " + str(marks) + " earns a B grade")
elif marks >= 70:
    print("This student's score of " + str(marks) + " earns a C grade")
elif marks >= 60:
    print("This student's score of " + str(marks) + " earns a D grade")
else:
    print("This student's score of " + str(marks) + " earns an F grade")