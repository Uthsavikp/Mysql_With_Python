''' 
  @Author: Uthsavi KP
  @Date: 2021-01-19 18:22:54
  @Last Modified by: Uthsavi KP
  @Last Modified time: 2021-01-22 18:14:43
  @Title: To connect to the database and perform some operations on it.
'''
import mysql.connector
import os
import pandas as pd
import datetime

class ClinicPlaylist:
    def connecting_to_database(self):
        self.mydb = mysql.connector.connect(
        host = os.environ.get("host"),
        user = os.environ.get("user"),
        password = os.environ.get("password"),
        database="clinic"
        )
        if self.mydb.is_connected():
            print("Successfully connected")

    
    def display_doctors_table(self):
        """
        displaying doctors table using read_sql which 
        reads SQL query or database table into a DataFrame
        """
        mycursor = self.mydb.cursor()
        print(pd.read_sql("SELECT * FROM doctors",self.mydb))

    def display_patients_table(self):
        """
        displaying patients table using read_sql which 
        reads SQL query or database table into a DataFrame
        """
        mycursor = self.mydb.cursor()
        print(pd.read_sql("SELECT * FROM patients",self.mydb))
    

    def display_workers_table(self):
        """
        displaying works table using read_sql which 
        reads SQL query or database table into a DataFrame
        """
        print(pd.read_sql("SELECT * FROM workers",self.mydb))

    def search_doctor_details(self):
        try:
            id_input = int(input("Enter doctors id : "))
            id_details = "SELECT * FROM doctors WHERE doctor_id = %%s"%(id_input)
            print(pd.read_sql(id_details,self.mydb))
        except TypeError as e:
            print(e)    

    def search_patient_details(self):
        try:
            id_input = int(input("Enter patient id : "))
            id_details = "SELECT * FROM patients WHERE patient_id = %s"%(id_input)
            print(pd.read_sql(id_details,self.mydb))
        except Exception as err:
            print(err)

    def search_worker_details(self): 
        try:
            id_input = int(input("Enter worker id : "))
            id_details = "SELECT * FROM workers WHERE worker_id = %s"%(id_input)
            print(pd.read_sql(id_details,self.mydb))
        except Exception as err:
            print(err)    

    def insert_new_patient_details(self):
        try:
            patient_id = int(input("Enter Id of patient : "))
            name = input("Enter patients name : ")
            mobile_number = input("Enter patients mobile number in the format +1 XXX XXXXXXX : ")
            age = int(input("Enter patients age : ")) 
            sql_new_patients_formula = "INSERT INTO patients VALUES (%s, %s, %s, %s)"
            new_patient_data = (patient_id, name, mobile_number, age)
            mycursor = self.mydb.cursor()
            mycursor.execute(sql_new_patients_formula, new_patient_data)
            self.mydb.commit()
            print(pd.read_sql("SELECT * FROM patients", self.mydb))
        except Exception as err:
            print(err)

    def insert_new_doctor_details(self):
        try:
            doctor_id = int(input("Enter Id of doctor : "))
            name = input("Enter doctor name : ")
            specialization = input("Enter doctors specialization : ")
            availability = input("Enter doctors availability : ")
            current_date = datetime.date.today()
            sql_new_patients_formula = "INSERT INTO doctors VALUES (%s, %s, %s, %s, %s)"
            new_patient_data = (doctor_id,current_date, name, specialization, availability)
            mycursor = self.mydb.cursor()
            mycursor.execute(sql_new_patients_formula, new_patient_data)
            self.mydb.commit()
            print(pd.read_sql("SELECT * FROM doctors", self.mydb))
        except Exception as err:
            print(err)   

    def insert_new_worker_details(self):
        try:
            worker_id = int(input("Enter Id of worker : "))
            name = input("Enter worker name : ")
            age = int(input("Enter workers age : ")) 
            mobile_number = input("Enter wokers mobile number in the format +1 XXX XXXXXXX : ")
            worker_position = input("Enter workers designation : ")
            sql_new_patients_formula = "INSERT INTO workers VALUES (%s, %s, %s, %s, %s)"
            new_patient_data = (worker_id, name, age, mobile_number, worker_position)
            mycursor = self.mydb.cursor()
            mycursor.execute(sql_new_patients_formula, new_patient_data)
            self.mydb.commit()
            print(pd.read_sql("SELECT * FROM workers", self.mydb))
        except Exception as err:
            print(err)   

    def update_patient_details(self):
        try:
            Id = input("Enter patients Id who's mobile number you want to update : ")
            mobile_number = input("Enter patients new mobile number in the format +1 XXX XXXXXXX : ")
            mycursor = self.mydb.cursor()
            mycursor.execute("UPDATE patients SET mobile_number = %s WHERE Id = %s",(mobile_number, Id))   
            self.mydb.commit()
            print(pd.read_sql("SELECT * FROM patients",self.mydb))
        except Exception as err:
            print(err)

    def update_doctor_details(self):
        try:
            doctor_id = input("Enter doctors Id who's availability has to be updated : ")
            availability = input("Enter doctors new available timings : ")
            mycursor = self.mydb.cursor()
            mycursor.execute("UPDATE doctors SET availability = %s WHERE doctor_id = %s",(availability, doctor_id))   
            self.mydb.commit()
            print(pd.read_sql("SELECT * FROM doctors",self.mydb))
        except Exception as err:
            print(err)   

    def delete_patient_record(self):
        """
        deleting a patients record if the input
        matches with the patient id
        """
        try:
            patient_id = input("Enter patient id who's record you want to delete : ")
            mycursor = self.mydb.cursor()
            mycursor.execute("SET FOREIGN_KEY_CHECKS=0")
            mycursor.execute("DELETE FROM patients WHERE patient_id = %s",(patient_id,))
            self.mydb.commit()
            print(mycursor.rowcount, "record(s) deleted")
        except Exception as err:
            print(err) 

    def view_patients_table(self):
        print(pd.read_sql("SELECT * FROM view_patients",self.mydb))      

    def user_options(self):
        option = ""
        #mycursor = self.mydb.cursor()
        while option != "q":

            print("1.Display doctors table\n2.Display patients table\n3.Display workers table\n6.Search doctors\n5.Search patients\n6.Search workers\n7.Insert patient record\n8.Insert doctor record\n9.Insert worker record\n10.Update patient record\n11.update doctor record\n12.Delete patient record\n13.View patient names\nq.Quit the program")
            option = int(input("Enter your option : "))
            if option == 1:
                self.display_doctors_table()
            elif option == 2:
                self.display_patients_table()  
            elif option == 3:
                self.display_workers_table() 
            elif option == 4:
                self.search_doctor_details()
            elif option == 5:
                self.search_patient_details() 
            elif option == 6:
                self.search_worker_details() 
            elif option == 7:
                self.insert_new_patient_details()
            elif option == 8:
                self.insert_new_doctor_details()
            elif option == 9:
                self.insert_new_worker_details()  
            elif option == 10:
                self.update_patient_details()
            elif option == 11:
                self.update_doctor_details()   
            elif option == 12:
                self.delete_patient_record()  
            elif option == 13:
                self.view_patients_table()
            elif option == "q":
                break                              
            else:
                print("invalid option")
if __name__ == "__main__":
    clinic_playlist = ClinicPlaylist()
    clinic_playlist.connecting_to_database()
    clinic_playlist.user_options()        