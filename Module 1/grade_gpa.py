# Get input from user regarding 
letter_grade = input("Enter your letter grade: A, B, C, D, or F): ")

#Convert letter_garde to uppercase for ease of mstching
letter_grade = letter_grade.upper()


# We'll use a match case to determine the GPA from the letter_grade
match letter_grade:
    case "A":
        gpa = 4.0
    case "B":
        gpa = 3.3
    case "C":
        gpa = 2.5
    case "D":
        gpa = 2.0
    case "F":
        gpa = 1.0
    case _:
        print("Could not determine grade")
        gpa = 0.0
        

print (f"your GPA is {gpa}")