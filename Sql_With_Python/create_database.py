''' 
  @Author: Uthsavi KP
  @Date: 2021-01-19 03:39:12
  @Last Modified by: Uthsavi KP
  @Last Modified time: 2021-01-23 09:57:25
  @Title: To create a database called clinic.

'''
import mysql.connector
from mysql.connector import errorcode
from mysql.connector.errors import Error
import os
import datetime
class ClinicManagement:
    def create_database(self):
        """
        creating a database called 'clinic'
        """
        try:
            self.mydb = mysql.connector.connect(
                host = os.environ.get("host"),
                user = os.environ.get("user"),
                password = os.environ.get("password")
                #database="clinic"
            )
            mycursor = self.mydb.cursor()
            mycursor.execute("DROP DATABASE IF EXISTS clinic")
            mycursor.execute("CREATE DATABASE clinic")    
            mycursor.execute("SHOW DATABASES")
            for db in mycursor:
                print(db)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)        
        else:
            mycursor.close()

    def create_table_doctors(self):
        """
        creating a table called doctors in
        clinic database which will  contain
        doctors record
        """
        mycursor = self.mydb.cursor()
        doctors_record = """CREATE TABLE doctors(
                        doctor_id INT NOT NULL,
                        date VARCHAR(50) NOT NULL,
                        name VARCHAR(50) NOT NULL,
                        specialization VARCHAR(50) NOT NULL,
                        availiability VARCHAR(50) NOT NULL,
                        PRIMARY KEY(doctor_id))"""
        mycursor.execute("USE clinic")  
        mycursor.execute("DROP TABLE IF EXISTS doctors")              
        mycursor.execute(doctors_record)
        mycursor.execute("SHOW TABLES")
        #result = self.mydb.fetchall()
        for tb in mycursor:
           print(tb) 
        #print(result)  
    def inserting_rows_into_doctors_table(self):
        """
        inserting rows/records into doctors table
        """
        try:
            sql_insert_formula = "INSERT INTO doctors (doctor_id, date, name, specialization, availiability) VALUES (%s, %s, %s, %s, %s)"
            mycursor = self.mydb.cursor()
            current_date = datetime.date.today()
            doctors_data = [(111, current_date, "John Smith", "Pediatrician", "12PM - 8PM"),
                (222, current_date, "Bella Edward", "Cardiologist", "10AM - 5PM"),
                (333, current_date, "Susan Yara", "Dermatologist", "10AM - 8PM"),
                (444, current_date, "Jackson Wang", "Neurologist", "10AM - 8PM"),
                (555, current_date, "Edward Jenner", "Orthodontist", "12AM - 8PM"),
                (666, current_date, "Joseph Lister", "Dentist", "12PM - 8PM"),
                (777, current_date, "Antony Young", "Plastic Surgeon", "8AM - 2PM"),
                (888, current_date, "John Smith", "Gynecologist", "2PM - 10PM"),]
            mycursor.executemany(sql_insert_formula, doctors_data)
            self.mydb.commit() 
            str(Error(errno=1146, sqlstate='42S02', msg="Table 'clinic.doctors' doesn't exist"))
        except mysql.connector.Error as e:
            print("Error code:", e.errno )       # error number
            print("SQLSTATE value:", e.sqlstate) # SQLSTATE value
            print("Error message:", e.msg)           

    def creating_patients_table(self):
        """
        creating a table called patients in
        clinic database which will contain
        patients details
        """
        try:
            mycursor = self.mydb.cursor()
            patients_record = """CREATE TABLE patients(
                        patient_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        name VARCHAR(50) NOT NULL,
                        mobile_number VARCHAR(50) NOT NULL,
                        age INT(50) NOT NULL
                        )"""
            mycursor.execute("DROP TABLE IF EXISTS patients")
            mycursor.execute(patients_record)   
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")           

    def inserting_rows_into_patients_table(self):
        """
        inserting records into patients table
        """
        try:
            mycursor = self.mydb.cursor()
            sql_patients_formula = "INSERT INTO patients (name, mobile_number, age) VALUES (%s, %s, %s)"
            patients_data = [("Olivia Young", "+1 310 5673457", 34),
                        ("Harry Clark", "+1 310 8588347", 47),
                        ("Noah Johnson", "+1 323 6838462", 17),
                        ("Jack Sebastian", "+1 626 9757499", 19),
                        ("Charlie Wilson", "+1 818 8738421", 15),
                        ("Ace Park", "+1 323 2345558", 65),
                        ("John Carter", "+1 323 4827824", 32),
                        ("Sabrina Spellman", "+1 626 6426433", 18),
                        ("Jackson Mark", "+1 626 1073979", 26),
                        ("Emily Davis", "+1 626 9347928", 29),
                        ("Blake Yaman", "+1 310 2979929", 67),
                        ("Robert Jones", "+1 310 5497920", 46),
                        ("James Charles", "+1 323 9127932", 22),
                        ("Shawn Gray", "+1 323 2972082", 69),
                        ("Jennifer Ellison", "+1 323 7393879", 52),
                        ("Sohphia Smith", "+1 626 3733838", 43),
                        ("Mia Mark", "+1 626 3868484", 12),
                        ("Amelia Foster", "+1 818 3880201", 89),
                        ("Harris Turner", "+1 818 8383438", 71),
                        ("Anastasia Rogers", "+1 818 3111347", 35),
                        ("Walter Lee", "+1 626 7733788", 44),
                        ("David Cook", "+1 310 1793252", 27),
                        ("Veronica Park", "+1 323 2034791", 39),
                        ("Rosa Brown", "+1 310 9643821", 20),
                        ("Camila Mendes", "+1 323 1125678", 34),
                        ("Mariana Cox", "+1 626 3242841", 64),]
            mycursor.executemany(sql_patients_formula, patients_data)
            self.mydb.commit()
            str(Error(errno=1146, sqlstate='42S02', msg="Table ' ' doesn't exist"))
        except mysql.connector.Error as e:
            print("Error code:", e.errno )       # error number
            print("SQLSTATE value:", e.sqlstate) # SQLSTATE value
            print("Error message:", e.msg)    

    def create_workers_table(self):
        """
        creating a table called workers in
        clinic database which will  contain
        all the details of workers working in clinic 
        """
        mycursor = self.mydb.cursor()
        try:
            workers_record = """CREATE TABLE workers(
                  worker_id INT NOT NULL ,
                  name VARCHAR(20) NOT NULL,
                  age INT(3) NOT NULL,
                  mobile_number VARCHAR(20) NOT NULL,
                  worker_position VARCHAR(20) NOT NULL,
                  PRIMARY KEY (worker_id))"""
            mycursor.execute(workers_record)   
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")          

    def inserting_rows_into_workers_table(self):
        """
        insering records into workers table
        """
        try:
            mycursor = self.mydb.cursor()
            sql_workers_formula = "INSERT INTO workers (worker_id, name, age, mobile_number, worker_position) VALUES (%s, %s, %s, %s, %s)"
            workers_data = [(100, "Terry Miller", 36, "+1 818 5356761", "Ward Boy"),
                        (200, "Harrison Baldwin" ,28, "+1 326 8974233", "Clearner"),
                        (300, "Lilly Watson", 46, "+1 626 5667843", "Nurse"),]
            mycursor.executemany(sql_workers_formula, workers_data)
            self.mydb.commit()
            str(Error(errno=1146, sqlstate='42S02', msg="Table ' ' doesn't exist"))
        except mysql.connector.Error as e:
            print("Error code:", e.errno )       # error number
            print("SQLSTATE value:", e.sqlstate) # SQLSTATE value
            print("Error message:", e.msg)

    def creat_bill_table(self):
        """
        creating a table called bill in
        clinic database which will  contain
        patients bill details
        """
        try:
            mycursor = self.mydb.cursor()
            bill_record = """CREATE TABLE bill(
                  patient_id INT NOT NULL AUTO_INCREMENT,
                  name VARCHAR(15) NOT NULL,
                  age INT(3) NOT NULL,
                  doctor_charges INT(10) NOT NULL,
                  room_charges INT(10) NOT NULL,
                  medicines INT(10) NOT NULL,
                  total_bill INT(10) NOT NULL,
                  PRIMARY KEY (patient_id),
                  KEY FK_patient_id (patient_id),
                  CONSTRAINT FK_patient_id FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE RESTRICT ON UPDATE CASCADE
                  )ENGINE=InnoDB DEFAULT CHARSET=utf8"""
            mycursor.execute("DROP TABLE IF EXISTS bill")
            mycursor.execute(bill_record)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")      

    def inserting_rows_into_bill_table(self):
        """
        inserting rows into bill table which
        contains patients bill details
        """
        try:
            mycursor = self.mydb.cursor()
            sql_bill_formula = "INSERT INTO bill (patient_id, name, age, doctor_charges, room_charges, medicines, total_bill) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            bill_data = [("1", "Olivia Young", 34, 1000, 1500, 1100, 3600),
                    ("2", "Harry Clark" , 47, 500, 0, 300, 800 ),
                    ("3", "Noah Johnson", 17, 700, 300, 550, 1550),]
            mycursor.executemany(sql_bill_formula, bill_data)
            self.mydb.commit() 
            str(Error(errno=1146, sqlstate='42S02', msg="Table ' ' doesn't exist"))
        except mysql.connector.Error as e:
            print("Error code:", e.errno )       # error number
            print("SQLSTATE value:", e.sqlstate) # SQLSTATE value
            print("Error message:", e.msg)         

    def view_patients_table(self):
        """
        creating a virtual table which contains
        only patients name
        """
        mycursor = self.mydb.cursor()
        mycursor.execute("DROP VIEW IF EXISTS view_patients")
        mycursor.execute("CREATE VIEW view_patients AS SELECT name FROM patients")


    def index_on_patient_id(self):
        mycursor = self.mydb.cursor()
        mycursor.execute("CREATE INDEX patient_index ON patients(patient_id)")        
if __name__ == "__main__":
    clinic_management = ClinicManagement()
    clinic_management.create_database()  
    clinic_management.create_table_doctors()
    clinic_management.inserting_rows_into_doctors_table() 
    clinic_management.creating_patients_table()
    clinic_management.inserting_rows_into_patients_table()
    clinic_management.create_workers_table()
    clinic_management.inserting_rows_into_workers_table()
    clinic_management.creat_bill_table()
    clinic_management.view_patients_table()
    clinic_management.inserting_rows_into_bill_table()