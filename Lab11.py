import os
import matplotlib.pyplot as plt


# Define a function to load the student data from the file
def load_student_data(file_path):
    students = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                student_name = parts[0]
                scores = list(map(int, parts[1:]))  # Convert scores to integers
                students[student_name] = scores
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    return students


# Function to calculate student grade
def calculate_student_grade(students, student_name):
    if student_name not in students:
        return "Student not found"

    scores = students[student_name]
    total_score = sum(scores)
    num_assignments = len(scores)
    grade_percentage = round((total_score / (num_assignments * 100)) * 100)
    return f"{grade_percentage}%"


# Function to get assignment statistics
def get_assignment_statistics(students, assignment_index):
    all_scores = []
    for student_scores in students.values():
        if assignment_index < len(student_scores):
            all_scores.append(student_scores[assignment_index])

    if not all_scores:
        return "Assignment not found"

    min_score = min(all_scores)
    max_score = max(all_scores)
    avg_score = sum(all_scores) / len(all_scores)

    return f"Min: {min_score}%\nAvg: {round(avg_score)}%\nMax: {max_score}%"


# Function to create histogram of assignment scores
def plot_assignment_graph(students, assignment_index):
    all_scores = []
    for student_scores in students.values():
        if assignment_index < len(student_scores):
            all_scores.append(student_scores[assignment_index])

    if not all_scores:
        return "Assignment not found"

    plt.hist(all_scores, bins=[0, 25, 50, 75, 100])
    plt.title(f"Distribution of scores for Assignment {assignment_index + 1}")
    plt.xlabel('Score Range')
    plt.ylabel('Number of Students')
    plt.show()


# Main program
def main():
    # Define the path to the students data file
    file_path = 'data/students.txt'  # Path to the students.txt file
    students = load_student_data(file_path)

    # Menu loop
    while True:
        print("1. Student grade")
        print("2. Assignment statistics")
        print("3. Assignment graph")
        user_choice = int(input("Enter your selection: "))

        if user_choice == 1:
            student_name = input("What is the student's name: ")
            result = calculate_student_grade(students, student_name)
            print(result)
            break

        elif user_choice == 2:
            assignment_name = input("What is the assignment name: ")
            assignment_index = None

            # Map assignment name to index (if you have a way to map, like 'Assignment 1', 'Assignment 2', etc.)
            if assignment_name == "Assignment 1":
                assignment_index = 0
            elif assignment_name == "Assignment 2":
                assignment_index = 1
            elif assignment_name == "Assignment 3":
                assignment_index = 2
            else:
                print("Assignment not found")
                continue

            result = get_assignment_statistics(students, assignment_index)
            print(result)
            break

        elif user_choice == 3:
            assignment_name = input("What is the assignment name: ")
            assignment_index = None

            # Map assignment name to index
            if assignment_name == "Assignment 1":
                assignment_index = 0
            elif assignment_name == "Assignment 2":
                assignment_index = 1
            elif assignment_name == "Assignment 3":
                assignment_index = 2
            else:
                print("Assignment not found")
                continue

            result = plot_assignment_graph(students, assignment_index)
            if result != "Assignment not found":
                break
            else:
                print(result)
                break


if __name__ == "__main__":
    main()
