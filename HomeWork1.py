
# coding: utf-8

# In[8]:


def change_marks(a):
    if(a>=90):
        return 5
    elif(a>=80):
        return 4
    elif(a>=70):
        return 3
    elif(a>=60):
        return 2
    elif(a<60):
        return 0

        
        
change_marks(80)


courses={}
while(True):
    courseName=input("Enter course name Or -1 to Stop\n")
    if(courseName=="-1"):
        break;
    courseCredit=int(input("Enter course Credit\n"))
    courseMark=int(input("Enter course Mark\n"))
    courses[courseName]=(courseCredit,courseMark)
    
total_Credits=0;
total_Grades=0;
print(courses)

for i in courses:
    total_Credits=total_Credits+courses[i][0]
    total_Grades=total_Grades+(courses[i][0]*change_marks(courses[i][1]))

    
if(total_Credits!=0):
    print("GPA =", total_Grades/total_Credits)
else:
    print("No GPA has been calculated")

