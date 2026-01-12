#Michael Audi
""" The Main function loop/menu for running operations on a database of course information """

import db_functions as dbf

course_db = {}
##course[""] = {"name":"", "cred":#, "dept":"", "desc":""}
course_db["CIS 161"] = {"name":"Computer Science 1", "cred":4, "dept":"CIS", "desc":"Algorithms, Algorithms, Algorithms!"}
course_db["CIS 120"] = {"name":"Computer Concepts", "cred":4, "dept":"CIS", "desc":"Computer Fundamentals, Key Applications, and Living Online"}
course_db["MUS 118"] = {"name":"Music Technology MIDI/Audio", "cred":3, "dept":"MUS", "desc":"Use various music production tools in live sound engineering and mixing"}
course_db["MUS 194"] = {"name":"Big Band Jazz", "cred":1, "dept":"MUS", "desc":"Study and performance of music for large jazz band. One major concert presented each term"}
course_db["CUL 101"] = {"name":"Introduction to Culinary Arts", "cred":4, "dept":"CUL", "desc":"Experience the basic theory and skill sets used throughout the field of culinary arts"}
course_db["CUL 242"] = {"name":"Charcuterie", "cred":4, "dept":"CUL", "desc":"Learn professional skills in variations of hors d'oeuvres and savories"}
course_db["ANTH 103"] = {"name":"Cultural Anthropology", "cred":4, "dept":"ANT", "desc":"Provides an introduction to the diversity of human beliefs and behaviors around the world"}
course_db["ANTH 254"] = {"name":"Magic, Witchcraft, Religion", "cred":4, "dept":"ANT", "desc":"Introduces students to the subject of religion in the broad anthropological context"}
course_db["AUT 101"] = {"name":"Basic Electricity-Automotive", "cred":2, "dept":"AUT", "desc":"A self paced course that provides understanding of fundamental principles of electricity"}
course_db["AUT 281"] = {"name":"Hybrid Electric Vehicles II", "cred":4, "dept":"AUT", "desc":"A study of HEV (hybrid electric vehicles) and EV (electric vehicles) part 2"}

def print_all():
    """prints all information in course_db using dbf.print_course_info"""
    return dbf.print_course_info(course_db)

def print_individual():
    """Queries the user for a course number, then prints it from course_db using dbf.print_single_course"""
    coursenum = input("Input Course Number to print (Ex: CIS 161 or ANTH 254):")
    return dbf.print_single_course(course_db, coursenum)

def add_entry():
    """Queries the user for Course Number, name, credits, department, and description, then adds it to course_db using dbf.add_course"""
    coursenum = input("Input Course Number to add (Ex: CIS 161 or ANTH 254) - ")
    coursename = input("Input Course Name to add (Ex: Computer Science 1) - ")
    coursecred = input("Input Course Credits to add (Ex: 4) - ")
    try:
        coursecred = int(coursecred)
    except ValueError:
        print("Type a number next time.")
        return False    
    coursedept = input("Input Course Department to add (Ex: CIS or ANT) (3 char exactly ALLCAPS) - ")
    coursedesc = input("Input Course Description to add (Ex: Algorithms, Algorithms, Algorithms!) - ")
    return dbf.add_course(course_db, coursenum, coursename, coursecred, coursedept, coursedesc)

def del_entry():
    """Queries the user for a Course number then deletes it from course_db."""
    coursenum = input("Input Course Number to delete (Ex: CIS 161 or ANTH 254) - ")
    return dbf.delete_course(course_db, coursenum)

def print_dept():
    """Queries the user for a course department, then prints out that department's courses using dbf.print_department_courses"""
    coursedept = input("Input Course Department to print (Ex: CIS or ANT) (3 char exactly ALLCAPS) - ")
    return dbf.print_department_courses(course_db, coursedept)

def main():
    """Course Database Utility - This Main function loop creates a menu for accessing the various database functions in order to manipulate the course_db dictionary"""

    print("Welcome to the Course Database Utility!")
    while True:
        print("\nPlease choose an option by typing the corresponding number:")
        print("1: Print the existing database.")
        print("2: Print individual entry based on Course Number")
        print("3: Add a course to the database.")
        print("4: Delete a course from the database.")
        print("5: Print all courses based on a Department")
        print("6: Exit Program")

        choice = input("Option: ").strip()
        if not choice.isdigit():
            print("Incorrect input, please type a number from 1 to 6.")
        else:
            if choice == "1":
                print_all()
            elif choice == "2":
                print_individual()
            elif choice == "3":
                add_entry()
            elif choice == "4":
                del_entry()
            elif choice == "5":
                print_dept()
            elif choice == "6":
                break
            else:
                print("Incorrect input, please type a number from 1 to 6.")

if __name__ == "__main__":
    main()