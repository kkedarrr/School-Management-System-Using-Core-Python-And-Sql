#!/usr/bin/env python
# coding: utf-8

# In[2]:


import mysql.connector as sql
import webbrowser
from datetime import datetime
mydb=sql.connect(
    host="localhost",
    user="root",
    passwd="Root",
    database="college_mgmt"
    )

commit_handler=mydb.cursor(buffered=True)

class operations:
        
        def student_details(self,dept,acc_id):
            if dept==1:
                dept_name='CSE'
            elif dept==2:
                dept_name='ECE'
            elif dept==3:
                dept_name='EEE'
                
            registered='S'
            
            if dept==1:
                
                commit_handler.execute("SELECT CSE_STUD_ID, CSE_STUD_NAME, YEAR, Professional_English1, Matrices_and_Calculus, Engineering_Physics, Engineering_Chemistry, Python_Programming_Lab, Physics_Lab, Chemistry_Lab FROM cse_students WHERE CSE_STUD_ID='%s' AND REGISTERED_AS='%s' " %(acc_id,registered))
                rows=commit_handler.fetchall()
                i=0
                for row in rows:
                    print("************************************************************")
                    print("Registered Id: {}".format(rows[i][0]))
                    print("Name: {}".format(rows[i][1]))
                    print("Year: {}".format(rows[i][2]))
                    print("")
                    print("****************************Marks***************************")
                    print("Professional_English – I: {}".format(rows[i][3]))
                    print("Matrices_and_Calculus: {}".format(rows[i][4]))
                    print("Engineering_Physics: {} ".format(rows[i][5]))
                    print("Engineering_Chemistry: {} ".format(rows[i][6]))
                    print("Python_Programming_Lab: {} ".format(rows[i][7]))
                    print("Physics_Lab: {} ".format(rows[i][8]))
                    print("Chemistry_Lab: {} ".format(rows[i][9]))
                    print("")
                    print("************************************************************")
                    i=i+1
                    
            elif dept==2:
            
                commit_handler.execute("SELECT ECE_STUD_ID, ECE_STUD_NAME, YEAR, Professional_English1, Matrices_and_Calculus, Engineering_Physics, Engineering_Chemistry, Python_Programming_Lab, Physics_Lab, Chemistry_Lab FROM ece_students WHERE ECE_STUD_ID='%s' AND REGISTERED_AS='%s' " %(acc_id,registered))
                rows=commit_handler.fetchall()
                i=0
                for row in rows:
                    print("************************************************************")
                    print("Registered Id: {}".format(rows[i][0]))
                    print("Name: {}".format(rows[i][1]))
                    print("Year: {}".format(rows[i][2]))
                    print("")
                    print("****************************Marks***************************")
                    print("Professional_English – I: {}".format(rows[i][3]))
                    print("Matrices_and_Calculus: {}".format(rows[i][4]))
                    print("Engineering_Physics: {} ".format(rows[i][5]))
                    print("Engineering_Chemistry: {} ".format(rows[i][6]))
                    print("Python_Programming_Lab: {} ".format(rows[i][7]))
                    print("Physics_Lab: {} ".format(rows[i][8]))
                    print("Chemistry_Lab: {} ".format(rows[i][9]))
                    print("")
                    print("************************************************************")
                    i=i+1
                    
            elif dept==3:
                
                commit_handler.execute("SELECT EEE_STUD_ID, EEE_STUD_NAME, YEAR, Professional_English1, Matrices_and_Calculus, Engineering_Physics, Engineering_Chemistry, Python_Programming_Lab, Physics_Lab, Chemistry_Lab FROM eee_students WHERE EEE_STUD_ID='%s' AND REGISTERED_AS='%s' " %(acc_id,registered))
                rows=commit_handler.fetchall()
                i=0
                for row in rows:
                    print("************************************************************")
                    print("Registered Id: {}".format(rows[i][0]))
                    print("Name: {}".format(rows[i][1]))
                    print("Year: {}".format(rows[i][2]))
                    print("")
                    print("****************************Marks***************************")
                    print("Professional_English – I: {}".format(rows[i][3]))
                    print("Matrices_and_Calculus: {}".format(rows[i][4]))
                    print("Engineering_Physics: {} ".format(rows[i][5]))
                    print("Engineering_Chemistry: {} ".format(rows[i][6]))
                    print("Python_Programming_Lab: {} ".format(rows[i][7]))
                    print("Physics_Lab: {} ".format(rows[i][8]))
                    print("Chemistry_Lab: {} ".format(rows[i][9]))
                    print("")
                    print("************************************************************")
                    i=i+1
                   
                
class studentMode(operations):
    
    def student(self):
        print("Hi")
        print("Please select the option from the given menu below: ")
        print("")
        print("1.Do you want to see your latest semester marks, then give 1: ")
        print("2.Do you want to Access our college website, then give 2: ")
        
        option=int(input())

        if option==1:
            
            user_input=int(input("Enter your register id to access your semester marks: "))
            user_pwd=input("Enter your password to access your semester marks: ")
        
            query = ("select count(*) CNT from (select CSE_STUD_ID from cse_students cse inner join users_table users_table on cse.CSE_USER_ID = users_table.USER_ID where (cse.CSE_STUD_ID = '%s' or cse.CSE_STUD_ID is null) union select EEE_STUD_ID from eee_students eee inner join users_table users_table on eee.EEE_USER_ID = users_table.USER_ID and (eee.EEE_STUD_ID = '%s' or eee.EEE_STUD_ID is null) union select ECE_STUD_ID from ece_students ece inner join users_table users_table  on ece.ECE_USER_ID = users_table.USER_ID and (ece.ECE_STUD_ID = '%s' or ece.ECE_STUD_ID is null)) AS T" %(user_input,user_input,user_input))
            commit_handler.execute(query)
            rows=commit_handler.fetchall()
            if rows[0][0] == 1:
            
                query = ("select DEPT,CSE_STUD_ID,SET_PWD from cse_students cse inner join users_table users_table on cse.CSE_USER_ID = users_table.USER_ID where (cse.CSE_STUD_ID = '%s' or cse.CSE_STUD_ID is null) union select DEPT,EEE_STUD_ID,SET_PWD from eee_students eee inner join users_table users_table on eee.EEE_USER_ID = users_table.USER_ID and (eee.EEE_STUD_ID = '%s' or eee.EEE_STUD_ID is null) union select DEPT,ECE_STUD_ID,SET_PWD from ece_students ece inner join users_table users_table  on ece.ECE_USER_ID = users_table.USER_ID and (ece.ECE_STUD_ID = '%s' or ece.ECE_STUD_ID is null)" %(user_input,user_input,user_input))
                commit_handler.execute(query)
                rows=commit_handler.fetchall()
                
                if rows[0][2]==user_pwd:

                    if rows[0][0] == 'CSE':
                        user_input=1
                        if user_input==1:
                            super().student_details(user_input,rows[0][1])
                    elif rows[0][0] == 'ECE':
                        user_input=2
                        if user_input==2:
                            super().student_details(user_input,rows[0][1])
                    elif rows[0][0] == 'EEE':
                        user_input=3
                        if user_input==3:
                            super().student_details(user_input,rows[0][1])
                            
                else:
                    
                    print("Please give the correct registered id and password to access your marks")
                                        
            else:
                print("Username not found, Please check the username")
                
        elif option==2:
            webbrowser.open('https://home.iitd.ac.in/')


# In[ ]:





# In[3]:


#obj3=studentMode()
#obj3.student()


# In[ ]:




