# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using constants, variables, and data classes
# with structured error handling for a course registration program.
# Change Log: (Who, When, What)
# KBoreta,8/13/2024,Created Script
# ------------------------------------------------------------------------------------------ #

import json

# Define the Data Constants
MENU: str = """
---- Course Registration Program ----
  Select from the following menu:
    1. Register a Student for a Course
    2. Show current data
    3. Save data to a file
    4. Exit the program
-----------------------------------------
"""

FILE_NAME: str = "Enrollments.json"

# Define the Data Classes and Functions

class FileProcessor:
    """Processes data to and from a file."""

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """Reads data from a file into a list of student data."""
        try:
            with open(file_name, 'r') as file:
                data = json.load(file)
                for item in data:
                    student_data.append(Student(item['first_name'], item['last_name'], item['course_name']))
        except FileNotFoundError as e:
            IO.output_error_messages("File not found.", e)
        except json.JSONDecodeError as e:
            IO.output_error_messages("Error decoding JSON from file.", e)
        except Exception as e:
            IO.output_error_messages("An unexpected error occurred while reading the file.", e)

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """Writes data from a list of student data to a file."""
        try:
            with open(file_name, 'w') as file:
                json.dump([s.to_dict() for s in student_data], file)
            print("Data saved successfully.")
        except Exception as e:
            IO.output_error_messages("An error occurred while writing to the file.", e)

class IO:
    """Handles Input and Output operations."""

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """Outputs error messages to the user."""
        print(f"Error: {message}")
        if error:
            print(f"Exception: {error}")

    @staticmethod
    def output_menu(menu: str):
        """Displays the menu to the user."""
        print(menu)

    @staticmethod
    def input_menu_choice():
        """Gets the menu choice from the user."""
        return input("Please select a menu option: ").strip()

    @staticmethod
    def output_student_courses(student_data: list):
        """Displays student courses to the user."""
        print("Current Student Registrations:")
        for student in student_data:
            print(f"{student.student_first_name} {student.student_last_name} is registered for {student.course_name}.")

    @staticmethod
    def input_student_data(student_data: list):
        """Gets student data from the user."""
        try:
            first_name = input("Enter the student's first name: ").strip()
            last_name = input("Enter the student's last name: ").strip()
            course_name = input("Enter the course name: ").strip()
            student_data.append(Student(first_name, last_name, course_name))
        except Exception as e:
            IO.output_error_messages("An error occurred while entering student data.", e)

class Person:
    """Represents a generic person."""
    def __init__(self, first_name: str = "", last_name: str = ""):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, value: str):
        if not value.isalpha():
            raise ValueError("First name should only contain letters.")
        self._first_name = value

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, value: str):
        if not value.isalpha():
            raise ValueError("Last name should only contain letters.")
        self._last_name = value

class Student(Person):
    """Represents a student enrolled in a course."""
    def __init__(self, first_name: str = "", last_name: str = "", course_name: str = ""):
        super().__init__(first_name, last_name)
        self._course_name = course_name

    @property
    def student_first_name(self) -> str:
        return self.first_name

    @property
    def student_last_name(self) -> str:
        return self.last_name

    @property
    def course_name(self) -> str:
        return self._course_name

    @course_name.setter
    def course_name(self, value: str):
        if not value.isalnum():
            raise ValueError("Course name should only contain letters and numbers.")
        self._course_name = value

    def to_dict(self) -> dict:
        """Returns the student data as a dictionary."""
        return {"first_name": self.first_name, "last_name": self.last_name, "course_name": self.course_name}

# Main Body of Script
if __name__ == "__main__":
    students = []
    FileProcessor.read_data_from_file(FILE_NAME, students)
    menu_choice = ""

    while menu_choice != "4":
        IO.output_menu(MENU)
        menu_choice = IO.input_menu_choice()

        if menu_choice == "1":
            IO.input_student_data(students)
        elif menu_choice == "2":
            IO.output_student_courses(students)
        elif menu_choice == "3":
            FileProcessor.write_data_to_file(FILE_NAME, students)
        elif menu_choice == "4":
            print("Exiting program.")
        else:
            print("Invalid option. Please select again.")


