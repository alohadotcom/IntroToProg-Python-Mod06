# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Rich Sialana,04 Mar 2025,Program Completed
# ------------------------------------------------------------------------------------------ #

#import
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Constants Data
FILE_NAME: str = "Enrollments.json"

# My variables
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user

# Procesing-------------------------------#
class FileProcessor:
    '''
    A collection of processing layer functions that work with Json file
    ChangeLog:
    Rich Sialana, 04 Mar 2025, Created class
    '''

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        try:
            with open(file_name, "r") as file:
                student_data = json.load(file)
                file.close()

        except FileNotFoundError as e:
            IO.output_error_messages('Text file must exist before running this script!', e)
        except Exception as e:
            IO.output_error_messages('There was a non-specific error', e)
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        try:
            with open(file_name, "w") as file:
                json.dump(student_data, file)
        except TypeError as e:
            IO.output_error_messages('Please check that the data is valid Json format', e)
        except Exception as e:
            IO.output_error_messages('There was a non-specific error!', e)

# Presentation-------------------------------#
class IO:
    '''
    A collection of presentation layer that manage users input and output
    ChangeLog:
    Rich Sialana, 04 Mar 2025
    Added menu output and input functions
    Added a function to display the data
    Added a function to display custom error message
    '''

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        '''
        This function displays a custom error messages to the user
        Changelog:
        Rich Sialana, 04 Mar 2025, Create function
        '''
        print(message, end='\n\n')
        if error is not None:
            print('--Technical Error Message --')
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        '''This function displays the menu of choices to the user
        ChangeLog:
        Rich Sialana, 04 Mar 2025, Created function
        '''
        print()
        print(menu)
        print()  # adding extra space to make it look nicer

    @staticmethod
    def input_menu_choice():
        '''This function gets a menu choice from the user
        ChangeLog:
        Rich Sialana, 04 Mar 2025, Created function
        '''
        choice = '0'
        try:
            choice = input('Enter your menu choice number: ')
            if choice not in ('1', '2', '3', '4'):
                raise Exception('Please, choose only 1, 2, 3, or 4')
        except Exception as e:
            IO.output_error_messages(e.__str__())
        return choice

    @staticmethod
    def input_student_data(student_data: list):
        '''This function gets the user's input
        ChangeLog:
        Rich Sialana. 04 March 2025, Created functipn'''
        try:
            student_first_name = input("What is the student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError()

            student_last_name = input("What is the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError()
            course_name = input('Please enter the course name: ')
            student_data={'FirstName': student_first_name,
                         'LastName': student_last_name,
                         'CourseName': course_name}


            student_dict = {"FirstName": student_first_name,
                            "LastName": student_last_name, 'CourseName': course_name}
            students.append(student_dict)
        except ValueError as e:
            IO.output_error_messages('That value is not the correct type of data!', e)
        except Exception as e:
            IO.output_error_messages('There was a non-specific error!', e)
        return student_data

    @staticmethod
    def output_student_courses(student_data: list):
        '''This function displays the student data
        ChangeLog:
        Rich Sialana, 04 Mar 2025, Created function
        '''
        if not student_data:
            print("No student data available.")
            return

        print("-" * 50)
        for student in student_data:
            print(f"{student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}")

        print("-" * 50)

# beginning of the main body of this script
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Repeat the follow tasks
while True:
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":
        IO.input_student_data(student_data=students)
        continue

    elif menu_choice == "2":
        IO.output_student_courses(student_data=students)
        continue

    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    elif menu_choice == "4":
        break  # out of the while loop