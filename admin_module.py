#!/usr/bin/env python
# coding: utf-8

# In[4]:


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
        
        def register(self,privilege):
            name=input("Enter the user Name: ")
            dob=input("Enter the Date of Birth in this format (DD-MM-YYYY) : ")
            age=int(input("Enter the Age: "))
            gender=input("Enter the Gender: ")
            father_name=input("Enter the Father's Name: ")
            address=input("Enter the Address: ")
            ph_no=input("Enter the Phone Number: ")
            email_id=input("Enter the Email id: ")
            dept=input("Enter the Dept: ")
            if privilege==1:
                registered_as='A'
            elif privilege==2:
                registered_as='T'
            elif privilege==3:
                registered_as='S'
                
            set_pwd=input("Enter your Password: ")

            dob=datetime.strptime(dob, '%d-%m-%Y').date()

            try:
                insert_stmt = (
                   "INSERT INTO USERS_TABLE(NAME,DOB,AGE,GENDER,FATHERS_NAME,ADDRESS,PHONE_NUMBER,EMAIL_ID,DEPT,REGISTERED_AS,SET_PWD)"
                   "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                )

                data = (name,dob,age,gender,father_name,address,ph_no,email_id,dept,registered_as,set_pwd)
                commit_handler.execute(insert_stmt, data)
                mydb.commit()
                print("New User Registered successfully")
            except:
                print("There is some Error while adding the new user, Please give the proper details or Please Contact IT Support Team")
                mydb.rollback()
                
                
        def delete(self,privilege):
            if privilege==4:
                registered='A'
            elif privilege==5:
                registered='T'
            elif privilege==6:
                registered='S'
            
            del_user=input("Enter a username to delete: ")
            
            commit_handler.execute("SELECT COUNT(*) CNT FROM USERS_TABLE WHERE NAME='%s' AND REGISTERED_AS='%s' " %(del_user,registered))
            rows=commit_handler.fetchall()
            
            if rows[0][0] > 1: 
                print("More than one user found, please check the below details:")
                commit_handler.execute("SELECT USER_ID,NAME,DOB,AGE,FATHERS_NAME,DEPT FROM USERS_TABLE WHERE NAME='%s' AND REGISTERED_AS='%s' " %(del_user,registered))
                rows=commit_handler.fetchall()
                i=0
                for row in rows:
                    print("************************************************************")
                    print("User Id: {}".format(rows[i][0]))
                    print("Name: {}".format(rows[i][1]))
                    print("DOB: {}".format(rows[i][2]))
                    print("Age: {}".format(rows[i][3]))
                    print("Father's Name: {} ".format(rows[i][4]))
                    print("Department: {} ".format(rows[i][5]))
                    print("************************************************************")
                    i=i+1
                delete_user_id=input("Enter the id of the user you want to delete: ") 
                delete_user_name=input("Enter the name of the user you want to delete: ") 
               
                try:
                    delete_stmt = ("DELETE FROM USERS_TABLE WHERE USER_ID='%s' AND NAME='%s' AND REGISTERED_AS='%s'"
                                    %(delete_user_id,delete_user_name,registered))

                    commit_handler.execute(delete_stmt)
                    mydb.commit()
                    print("User Deleted")
                except:
                    print("There is some Error while deleting the user, Please Contact IT Support Team")
                    mydb.rollback()
                
            elif rows[0][0] == 1:
                try:
                    delete_stmt = ("DELETE FROM USERS_TABLE WHERE NAME='%s' AND REGISTERED_AS='%s'"
                                    %(del_user,registered))

                    commit_handler.execute(delete_stmt)
                    mydb.commit()
                    print("User Deleted")
                except:
                    print("There is some Error while deleting the user, Please Contact IT Support Team")
                    mydb.rollback()
            else:
                print("Username not found, Please check the username")
          
        def access(self,privilege):
            if privilege==1:
                registered='A'
            elif privilege==2:
                registered='T'
            elif privilege==3:
                registered='S'
            
            acc_user=input("Enter a username to access the data: ")
            
            commit_handler.execute("SELECT COUNT(*) CNT FROM USERS_TABLE WHERE NAME='%s' AND REGISTERED_AS='%s' " %(acc_user,registered))
            rows=commit_handler.fetchall()
            
            if rows[0][0] > 1: 
                print("More than one user found, please check the below user details:")
                commit_handler.execute("SELECT USER_ID,NAME,DOB,AGE,FATHERS_NAME,DEPT FROM USERS_TABLE WHERE NAME='%s' AND REGISTERED_AS='%s' " %(acc_user,registered))
                rows=commit_handler.fetchall()
                i=0
                for row in rows:
                    print("************************************************************")
                    print("User Id: {}".format(rows[i][0]))
                    print("Name: {}".format(rows[i][1]))
                    print("DOB: {}".format(rows[i][2]))
                    print("Age: {}".format(rows[i][3]))
                    print("Father's Name: {} ".format(rows[i][4]))
                    print("Department: {} ".format(rows[i][5]))
                    print("************************************************************")
                    i=i+1
                
            elif rows[0][0] == 1:
                commit_handler.execute("SELECT USER_ID,NAME,DOB,AGE,FATHERS_NAME,DEPT FROM USERS_TABLE WHERE NAME='%s' AND REGISTERED_AS='%s' " %(acc_user,registered))
                rows=commit_handler.fetchall()
                print("Please check the below user details:")
                i=0
                for row in rows:
                    print("************************************************************")
                    print("User Id: {}".format(rows[i][0]))
                    print("Name: {}".format(rows[i][1]))
                    print("DOB: {}".format(rows[i][2]))
                    print("Age: {}".format(rows[i][3]))
                    print("Father's Name: {} ".format(rows[i][4]))
                    print("Department: {} ".format(rows[i][5]))
                    print("************************************************************")
                    i=i+1
            else:
                print("Username not found, Please check the username")
          
        
        def modify(self,privilege):
            if privilege==1:
                registered='A'
            elif privilege==2:
                registered='T'
            elif privilege==3:
                registered='S'
            
            print("what do you want to modify, please select the option from the below menu,")
            print("1. Address")
            print("2. Phone Number")
            print("3. Email Id")

            mod_option=int(input())
            
            mod_user=input("Enter a username to modify the data: ")
            
            commit_handler.execute("SELECT COUNT(*) CNT FROM USERS_TABLE WHERE NAME='%s' AND REGISTERED_AS='%s' " %(mod_user,registered))
            rows=commit_handler.fetchall()
            
            if rows[0][0] > 1: 
                print("More than one user found, please check the below details:")
                commit_handler.execute("SELECT USER_ID,NAME,DOB,AGE,FATHERS_NAME,DEPT FROM USERS_TABLE WHERE NAME='%s' AND REGISTERED_AS='%s' " %(mod_user,registered))
                rows=commit_handler.fetchall()
                i=0
                for row in rows:
                    print("************************************************************")
                    print("User Id: {}".format(rows[i][0]))
                    print("Name: {}".format(rows[i][1]))
                    print("DOB: {}".format(rows[i][2]))
                    print("Age: {}".format(rows[i][3]))
                    print("Father's Name: {} ".format(rows[i][4]))
                    print("Department: {} ".format(rows[i][5]))
                    print("************************************************************")
                    i=i+1
                
                mod_user_id=input("Enter the id of the user you want to modify: ") 
                mod_user_name=input("Enter the name of the user you want to modify: ") 
                
                if mod_option==1:
                    mod_address=input("Enter the Address of the user you want to modify: ")
                elif mod_option==2:
                    mod_ph=input("Enter the Phone Number of the user you want to modify: ")
                elif mod_option==3:
                    mod_email=input("Enter the Email Id of the user you want to modify: ")
                    
                try:
                    if mod_option==1:
                        update_stmt = ("UPDATE USERS_TABLE SET ADDRESS='%s' WHERE USER_ID='%s' AND NAME='%s' AND REGISTERED_AS='%s'"
                                        %(mod_address,mod_user_id,mod_user_name,registered))

                        commit_handler.execute(update_stmt)
                        mydb.commit()
                        print("User Details Updated Successfully")
                    elif mod_option==2:
                        update_stmt = ("UPDATE USERS_TABLE SET PHONE_NUMBER='%s' WHERE USER_ID='%s' AND NAME='%s' AND REGISTERED_AS='%s'"
                                        %(mod_ph,mod_user_id,mod_user_name,registered))

                        commit_handler.execute(update_stmt)
                        mydb.commit()
                        print("User Details Updated Successfully")
                    elif mod_option==3:
                        update_stmt = ("UPDATE USERS_TABLE SET EMAIL_ID='%s' WHERE USER_ID='%s' AND NAME='%s' AND REGISTERED_AS='%s'"
                                        %(mod_email,mod_user_id,mod_user_name,registered))

                        commit_handler.execute(update_stmt)
                        mydb.commit()
                        print("User Details Updated Successfully")
                except:
                    print("There is some Error while updating the user, Please Contact IT Support Team")
                    mydb.rollback()
                
            elif rows[0][0] == 1:
                
                if mod_option==1:
                    mod_address=input("Enter the Address of the user you want to modify: ")
                elif mod_option==2:
                    mod_ph=input("Enter the Phone Number of the user you want to modify: ")
                elif mod_option==3:
                    mod_email=input("Enter the Email Id of the user you want to modify: ")
                    
                try:
                    if mod_option==1:
                        update_stmt = ("UPDATE USERS_TABLE SET ADDRESS='%s' WHERE NAME='%s' AND REGISTERED_AS='%s'"
                                        %(mod_address,mod_user,registered))

                        commit_handler.execute(update_stmt)
                        mydb.commit()
                        print("User Details Updated Successfully")
                    elif mod_option==2:
                        update_stmt = ("UPDATE USERS_TABLE SET PHONE_NUMBER='%s' WHERE NAME='%s' AND REGISTERED_AS='%s'"
                                        %(mod_ph,mod_user,registered))

                        commit_handler.execute(update_stmt)
                        mydb.commit()
                        print("User Details Updated Successfully")
                    elif mod_option==3:
                        update_stmt = ("UPDATE USERS_TABLE SET EMAIL_ID='%s' WHERE NAME='%s' AND REGISTERED_AS='%s'"
                                        %(mod_email,mod_user,registered))

                        commit_handler.execute(update_stmt)
                        mydb.commit()
                        print("User Details Updated Successfully")
                except:
                    print("There is some Error while updating the user, Please Contact IT Support Team")
                    mydb.rollback()
            else:
                print("Username not found, Please check the username")
          
        def student_details(self,dept):
            if dept==1:
                dept_name='CSE'
            elif dept==2:
                dept_name='ECE'
            elif dept==3:
                dept_name='EEE'
                
            registered='S'
            
            stud_user_opt=input("Do you want to access all the student details? Y/N : ")
            if dept==1:
                if stud_user_opt=='Y':
                    commit_handler.execute("SELECT CSE_STUD_ID, CSE_STUD_NAME, YEAR, Professional_English1, Matrices_and_Calculus, Engineering_Physics, Engineering_Chemistry, Python_Programming_Lab, Physics_Lab, Chemistry_Lab FROM cse_students WHERE REGISTERED_AS='%s' " %(registered))
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

                else:

                    acc_user=input("Enter the student name to access the details: ")

                    commit_handler.execute("SELECT COUNT(*) CNT FROM cse_students WHERE CSE_STUD_NAME='%s' AND REGISTERED_AS='%s' " %(acc_user,registered))
                    rows=commit_handler.fetchall()

                    if rows[0][0] > 1: 
                        print("More than one user found, please check the below user details:")
                        commit_handler.execute("SELECT CSE_STUD_ID, CSE_STUD_NAME, YEAR, Professional_English1, Matrices_and_Calculus, Engineering_Physics, Engineering_Chemistry, Python_Programming_Lab, Physics_Lab, Chemistry_Lab FROM cse_students WHERE CSE_STUD_NAME='%s' AND REGISTERED_AS='%s' " %(acc_user,registered))
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

                    elif rows[0][0] == 1:
                        commit_handler.execute("SELECT CSE_STUD_ID, CSE_STUD_NAME, YEAR, Professional_English1, Matrices_and_Calculus, Engineering_Physics, Engineering_Chemistry, Python_Programming_Lab, Physics_Lab, Chemistry_Lab FROM cse_students WHERE CSE_STUD_NAME='%s' AND REGISTERED_AS='%s' " %(acc_user,registered))
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
                    else:
                        print("Username not found, Please check the username")
            elif dept==2:
                if stud_user_opt=='Y':
                    commit_handler.execute("SELECT ECE_STUD_ID, ECE_STUD_NAME, YEAR, Professional_English1, Matrices_and_Calculus, Engineering_Physics, Engineering_Chemistry, Python_Programming_Lab, Physics_Lab, Chemistry_Lab FROM ece_students WHERE REGISTERED_AS='%s' " %(registered))
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

                else:

                    acc_user=input("Enter the student name to access the details: ")

                    commit_handler.execute("SELECT COUNT(*) CNT FROM ece_students WHERE ECE_STUD_NAME='%s' AND REGISTERED_AS='%s' " %(acc_user,registered))
                    rows=commit_handler.fetchall()

                    if rows[0][0] > 1: 
                        print("More than one user found, please check the below user details:")
                        commit_handler.execute("SELECT ECE_STUD_ID, ECE_STUD_NAME, YEAR, Professional_English1, Matrices_and_Calculus, Engineering_Physics, Engineering_Chemistry, Python_Programming_Lab, Physics_Lab, Chemistry_Lab FROM ece_students WHERE ECE_STUD_NAME='%s' AND REGISTERED_AS='%s' " %(acc_user,registered))
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

                    elif rows[0][0] == 1:
                        commit_handler.execute("SELECT ECE_STUD_ID, ECE_STUD_NAME, YEAR, Professional_English1, Matrices_and_Calculus, Engineering_Physics, Engineering_Chemistry, Python_Programming_Lab, Physics_Lab, Chemistry_Lab FROM ece_students WHERE ECE_STUD_NAME='%s' AND REGISTERED_AS='%s' " %(acc_user,registered))
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
                    else:
                        print("Username not found, Please check the username")
            elif dept==3:
                if stud_user_opt=='Y':
                    commit_handler.execute("SELECT EEE_STUD_ID, EEE_STUD_NAME, YEAR, Professional_English1, Matrices_and_Calculus, Engineering_Physics, Engineering_Chemistry, Python_Programming_Lab, Physics_Lab, Chemistry_Lab FROM eee_students WHERE REGISTERED_AS='%s' " %(registered))
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

                else:

                    acc_user=input("Enter the student name to access the details: ")

                    commit_handler.execute("SELECT COUNT(*) CNT FROM eee_students WHERE EEE_STUD_NAME='%s' AND REGISTERED_AS='%s' " %(acc_user,registered))
                    rows=commit_handler.fetchall()

                    if rows[0][0] > 1: 
                        print("More than one user found, please check the below user details:")
                        commit_handler.execute("SELECT EEE_STUD_ID, EEE_STUD_NAME, YEAR, Professional_English1, Matrices_and_Calculus, Engineering_Physics, Engineering_Chemistry, Python_Programming_Lab, Physics_Lab, Chemistry_Lab FROM eee_students WHERE EEE_STUD_NAME='%s' AND REGISTERED_AS='%s' " %(acc_user,registered))
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

                    elif rows[0][0] == 1:
                        commit_handler.execute("SELECT EEE_STUD_ID, EEE_STUD_NAME, YEAR, Professional_English1, Matrices_and_Calculus, Engineering_Physics, Engineering_Chemistry, Python_Programming_Lab, Physics_Lab, Chemistry_Lab FROM eee_students WHERE EEE_STUD_NAME='%s' AND REGISTERED_AS='%s' " %(acc_user,registered))
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
                    else:
                        print("Username not found, Please check the username")
                        
                        
class administration(operations):
    
    def admin(self):
        print("Hi")
        print("Do you want add or remove any admin,teacher or student, then give Add or Remove")
        print("")
        print("Do you want access the details of the admin,teacher or student, then give Access")
        print("")
        print("Do you want modify the details of the admin,teacher or student, then give Modify")
        print("")
        print("Do you want see the details of the students department wise, then give Department")
        print("")
        print("Do you want to Access our college website, then give Webportal: ")
        print("")

        option=input()

        if option.lower()=='add' or  option.lower()=='remove':
            print("Please select the option from the given menu below: ")
            print("")
            print("1.Register New Admin")
            print("2.Register New Teacher")
            print("3.Register New Student")
            print("4.Delete Existing Admin")
            print("5.Delete Existing Teacher")
            print("6.Delete Existing Student")
            
            user_input=int(input())
            
            if user_input==1 or user_input==2 or user_input==3:
                super().register(user_input)
            elif user_input==4 or user_input==5 or user_input==6:
                super().delete(user_input)
            
        elif option.lower()=='access':
            print("Please select the option from the given menu below: ")
            print("")
            print("1.Access Admin Details")
            print("2.Access Teacher Details")
            print("3.Access Student Details")
            
            user_input=int(input())
            
            if user_input==1 or user_input==2 or user_input==3:
                super().access(user_input)
            
        elif option.lower()=='modify':
            print("Please select the option from the given menu below: ")
            print("")
            print("1.Modify Admin Details")
            print("2.Modify Teacher Details")
            print("3.Modify Student Details")
            
            user_input=int(input())
            
            if user_input==1 or user_input==2 or user_input==3:
                super().modify(user_input)
                
        elif option.lower()=='department':
            print("Please select the option from the given menu below: ")
            print("")
            print("1.CSE")
            print("2.ECE")
            print("3.EEE")
            
            user_input=int(input())
            
            if user_input==1 or user_input==2 or user_input==3:
                super().student_details(user_input)
                
        elif option.lower()=='webportal':
            webbrowser.open('https://home.iitd.ac.in/')


# In[ ]:





# In[5]:


#obj3=administration()
#obj3.admin()


# In[ ]:




