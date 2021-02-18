# Jun - 19/02/21
# V2 Fixed the issue with enumerate deleting half my list✓
# Added a function that checks for users int input(numcheck) ✓
# Fixed the issue with program not looping again when confirmation was declined✓
# Added a feature that prevents the text from moving when outputting the student name, la name and code etc etc {:>}


#List of all courses by year level
year_11 = ["Accounting","Business Studies","Digital Media","Programming","Drama C","Drama P","Economics","English","English ESOL","Health","Geography","History","Mathematics","Media Studies","Music","Physical Eduction","Chemistry","Physics","Biology","Design","Painting","Photography","Design and Visual Communication","Food technology","Industrial design"]
year_12 = ["Accounting","Business","Computer Science","English","Economics", "ESOL","Languages","Financial Literacy","Geography","Health","History","Hospitality & Culinary","Mathematics","Statistics","Media Studies","Oceania Studies","Drama","Music","Physical Education","Biology","Chemistry","Physics","Design and Visual Communication","Industrial Design","Food Technology","Visual Arts Design","Painting","Photography"]
year_13 = ["Accounting","Business","Computer Science","English","ESOL","Geography","Financial Literacy","History","Hospitality and Culinary","Police Studies","Health","Physical Education","Media Studies","Mathematics","Statistics","Calculus","Biology","Chemistry","Physics","General Science","Industrial Design","Design and Visual Communication","Food technology","Visual Arts Design","Painting","Photography"]

#Functions
def user_input(question,var=str):
    if True:
        try:
            x = var(input(question))
            return(x)
        except ValueError:
            print(f"Please use a {var} ")

def numcheck(question,low,high):
    while True:
        try:
            q = int(input(question))
            if low <= q <= high:
                return(q)
            else:
                print(f"Please enter a value between {low} and {high}")
        except ValueError:
            print("Please enter an int")
            
def course_select(question_amount):
    print("Now select your courses")
    for i in range(question_amount):
        course_num = numcheck(f"Course number {i+1}: ",1,len(student_courses))
        course_selected.append(student_courses[course_num-1])
    return(course_selected)

# Main 
code_teacher = user_input("LA teacher code: ")
name_teacher = user_input("Teacher name: ")
name_student = user_input("Student name: ")
year_level = numcheck("Enter year level: ",11,13)
#This allows the courses to be defined by one variable 
if year_level == 11:
    student_courses = year_11
    for x, course in enumerate(student_courses,1):
        print(x, course)
elif year_level == 12:
    student_courses = year_12
    for x, course in enumerate(student_courses,1):
        print(x, course)
else:
    student_courses = year_13
    for x, courses in enumerate(student_courses,1):
        print(x, course)

while True:    
    course_selected = []
    if year_level == 11:
        course_selected = course_select(3)
        course_selected.append("English")
        course_selected.append("Mathematics")
    elif year_level == 12:
        course_selected = course_select(6)
    else:
        course_selected = course_select(5)
    print("Teacher Name: {:>15}        Teacher Code: {:>15}\nStudent Name: {}       Student Year Level: {}\nSelected courses:".format(name_teacher,code_teacher,name_student,year_level))
    for x in course_selected:
        print(x)
    stop = str(input("Confirm selected courses? Y/N: "))
    if stop == "y":
        break
    elif stop == "Y":
        break