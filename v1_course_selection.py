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

#Don't need this function anymore because of a better method to display courses 
#def courses_display(year_level):
   # if year_level == 11:
        #for x, year_11 in enumerate(year_11,1):
            #print(x, year_11)
    #elif year_level == 12:
        #for x, year_12 in enumerate(year_12,1):
            #print(x, year_12)
    #else:
        #for x, year_13 in enumerate(year_13,1):
            #print(x, year_13)

def course_select(question_amount):
    print("Now select your courses")
    for i in range(question_amount):
        course_num = int(input(f"Course number {i+1}: "))
        course_selected.append(student_courses[course_num-1])
    return(course_selected)

# Main 

code_teacher = user_input("LA teacher code: ")
name_teacher = user_input("Teacher name: ")
#Add a low high for year level 
name_student = user_input("Student name: ")
year_level = user_input("Enter year level: ", int)
#This allows the courses to be defined by one variable 
if year_level == 11:
    student_courses = year_11
    # Research on enumerate more because it somehow deletes half of list
    for x, student_courses in enumerate(student_courses,1):
        print(x, student_courses)
    student_courses = year_11
elif year_level == 12:
    student_courses = year_12
    for x, student_courses in enumerate(student_courses,1):
        print(x, student_courses)
    student_courses = year_12
else:
    student_courses = year_13
    for x, student_courses in enumerate(student_courses,1):
        print(x, student_courses)
    student_courses = year_13
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
    print(f"Teacher Name: {name_teacher}        Teacher Code: {code_teacher}\nStudent Name: {name_student}       Student Year Level: {year_level}\nSelected courses:")
    for x in course_selected:
        print(x)
    stop = input("Confirm selected courses? Y/N: ")
    if stop == "Y" or "y":
        break
    else:
        continue