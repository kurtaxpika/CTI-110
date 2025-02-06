# Dylan Makombe
# 02/01/2025
# M4 Pro
# More details on tuition

courses = {
    "MAT-035": {"desc": "Concepts of Algebra", "tuition": 460},
    "CTI-115": {"desc": "Computer System Foundations", "tuition": 520.98},
    "BAS-120": {"desc": "Intro to Analytics", "tuition": 500},
    "CSC-121": {"desc": "Python Programming", "tuition": 783.88}
}
stu_names = ["Zakari Watson", "Jerom Williams", "Dominique Ross", "Diana Shepard", "Yoko Mayo", "Rashad Ahmed", "Susan Jones"]
students = {
    "Zakari Watson": ["CTI-115", "CSC-121"],
    "Jerom Williams": ["CTI-115", "CSC-121", "MAT-035", "BAS-120"],
    "Dominique Ross": ["CTI-115", "CSC-121", "MAT-035"],
    "Diana Shepard": ["MAT-035", "CTI-115", "BAS-120", "CSC-121"],
    "Yoko Mayo": ["MAT-035"],
    "Rashad Ahmed": ["MAT-035", "BAS-120"],
    "Susan Jones": ["BAS-120", "CSC-121"]
}


def display_menu(): 
    # Display options that user can select from
    print("\n\n")
    print("---------------Menu---------------")
    print("1) Display Course Information")
    print("2) Lookup Course")
    print("3) Display Courses and Tuition for Specific Student")
    print("4) Display tuition for All Students")
    print("5) Display # of Students and Tuition for All Courses")
    print("6) Exit")
    print("-" * 30)
    

def display_courses():
    print(f"{'Code':<10} {'Description':<40} {'Tuition'}")
    print("-" * 60)
    for code, details in courses.items():
        print(f"{code:<10} {details['desc']:<40} ${details['tuition']:.2f}")
    print("-" * 60)

def lookup_course():
    course_code = input("Enter course code (case sensitive): ").strip()
    if course_code in courses:
        print("-" * 50)
        print(f"Code: {course_code}")
        print(f"Description: {courses[course_code]['desc']}")
        print(f"Tuition: ${courses[course_code]['tuition']}")
        print("-" * 50)
    else:
        print("Course not found. Please check the code and try again.")

# Function that lets you select a Student
def choose_student():
    for s in range(len(stu_names)):
        print(f"{s+1} {stu_names[s]}")
    student_choice = int(input("Choose a Student: "))
    return stu_names[student_choice-1]

# Function displays student's total tuition
def cal_total_tuition():
    print(f"{'Stu Name':<15} {'#Of Courses':<12}{'Tuition':<10}")
    print(f"-" * 45)
    mega_tuition = 0
    for stu in students:
        total_tuition = 0
        for course in students[stu]:
            if course in courses:
                total_tuition += courses[course]["tuition"]
        mega_tuition += total_tuition

        print(f"{stu:<15} {len(students[stu]):<12} ${total_tuition:,.2f}")
    print(f"-" * 45)
    print(f"Overall Tuition: ${mega_tuition:,.2f}")

# Choice 6
def course_earnings():
    mat_course = 0
    cti_course = 0
    bas_course = 0
    csc_course = 0

    print(f"{'Course Code':<15} {'# of Stu':<15} Tuition Generated")
    for stu in students:
        for course in students[stu]:
            if course == "MAT-035": 
                mat_course += 1
            if course == "CTI-115": 
                cti_course += 1
            if course == "BAS-120": 
                    bas_course += 1
            if course == "CSC-121": 
                csc_course += 1
    
    for each in courses:
        if each == "MAT-035":
            print(f"{each:<15}{mat_course:<15}${(courses[each]['tuition']) * mat_course:,.2f}")
        elif each == "CTI-115":
            print(f"{each:<15}{cti_course:<15}${(courses[each]['tuition']) * cti_course:,.2f}")
        elif each == "BAS-120":
            print(f"{each:<15}{bas_course:<15}${(courses[each]['tuition']) * bas_course:,.2f}")
        elif each == "CSC-121":
            print(f"{each:<15}{csc_course:<15}${(courses[each]['tuition']) * csc_course:,.2f}")

def main():
    display_menu()
    menu = True

    while menu == True:
        display_menu()
        choice = int(input("Enter choice: "))
        if choice == 1:
            display_courses()      
            
        elif choice == 2:
            lookup_course()

        elif choice == 3:
            # Ask the user to choose a student
            student_name = choose_student()
            print(f"\n{student_name}'s Courses and Tuition:")
            

            # Retrieve the courses for the selected student
            total_tuition = 0
            for course_code in students[student_name]:
                course_details = courses[course_code]
                print(f"{course_code:<10} {course_details['desc']:<40} ${course_details['tuition']}")
                total_tuition += course_details['tuition']

            # Display total tuition
            print("-" * 60)
            print(f"Overall Tuition: ${total_tuition:.2f}")

        elif choice == 4: 
            cal_total_tuition()

            

        elif choice == 5:
            course_earnings()

        elif choice == 6:
            menu = False

        else:
            print("That choice does not exist! Try Again!!!")







# Call the main
if __name__ == "__main__":
    main()