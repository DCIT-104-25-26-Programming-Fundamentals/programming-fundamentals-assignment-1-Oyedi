# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================

def display_menu():
    """Prints the main interactive menu."""
    print("\n================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def add_student(students):
    """
    Prompts the user for student name, ID, and assessment scores,
    and appends a new student dictionary to the students list.
    """
    name = input("Student name: ").strip()
    if not name:
        print("Error: Student name cannot be empty.")
        return

    try:
        student_id = int(input("Student ID: "))
    except ValueError:
        print("Error: Invalid ID. Student ID must be an integer.")
        return

    # Check for duplicate student ID
    for student in students:
        if student["id"] == student_id:
            print(f"Error: A student with ID {student_id} already exists.")
            return

    try:
        num_scores = int(input("How many scores? "))
        if num_scores <= 0:
            print("Error: Number of scores must be greater than 0.")
            return
    except ValueError:
        print("Error: Please enter a valid number.")
        return

    scores = []
    for i in range(1, num_scores + 1):
        while True:
            try:
                score = float(input(f"Enter score {i}: "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("Error: Score must be between 0 and 100.")
            except ValueError:
                print("Error: Please enter a valid numerical score.")

    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }
    
    students.append(student)
    print(f'Student "{name}" added successfully.')


def display_all_students(students):
    """Displays all student records formatted nicely in a table."""
    if not students:
        print("\nNo student records available.")
        return

    print("\n" + "-" * 55)
    print(f"{'Name':<15} {'ID':<12} {'Scores':<15} {'Average':<8}")
    print("-" * 55)

    for student in students:
        scores_str = ", ".join(str(int(s) if s.is_integer() else s) for s in student["scores"])
        avg_score = sum(student["scores"]) / len(student["scores"])
        print(f"{student['name']:<15} {student['id']:<12} {scores_str:<15} {avg_score:.2f}")

    print("-" * 55)


def calculate_student_average(students):
    """Finds a student by ID and displays their calculated average score."""
    if not students:
        print("\nNo student records available.")
        return

    try:
        search_id = int(input("Enter student ID: "))
    except ValueError:
        print("Error: Invalid ID format. Please enter an integer.")
        return

    for student in students:
        if student["id"] == search_id:
            avg_score = sum(student["scores"]) / len(student["scores"])
            print(f"{student['name']}'s average score: {avg_score:.2f}")
            return

    print(f"Error: Student with ID {search_id} was not found.")


def main():
    """Main function controlling the application execution loop."""
    students = []  # List of student dictionaries

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_all_students(students)
        elif choice == "3":
            calculate_student_average(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 4.")


# =============================================================================
# MAIN EXECUTION
# =============================================================================
if __name__ == "__main__":
    main()
# =============================================================================

