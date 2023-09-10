# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 13:58:50 2023

@author: Shivani_SB
"""
def showall():
    sql= "SELECT * from REGISTER "
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        print("The LName is : ",  dictionary["LNAME"])
        print("The E-mail is : ", dictionary["EMAIL"])
        print("The Password is : ",  dictionary["PASSWORD"])
        print("The Role is : ",  dictionary["ROLE"])
        print("The Fname is ",  dictionary["FNAME"])
        
        dictionary = ibm_db.fetch_both(stmt)
        
def getdetails(email,password):
    sql= "select * from  REGISTER where email='{}' and password='{}'".format(email,password)
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        print("The LName is : ",  dictionary["LNAME"])
        print("The E-mail is : ", dictionary["EMAIL"])
        print("The Password is : ", dictionary["PASSWORD"])
        print("The Role is : ", dictionary["ROLE"])
        print("The Fname is ",  dictionary["FNAME"])
        
        dictionary = ibm_db.fetch_both(stmt)
        
def insertdb(conn,name,email,contact,address,role,branch,password):
    sql= "INSERT into REGISTER VALUES('{}','{}','{}','{}','{}')".format(Lname,email,password,role,Fname,)
    stmt = ibm_db.exec_immediate(conn, sql)
    print ("Number of affected rows: ", ibm_db.num_rows(stmt))

try:
    import ibm_db
    conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=6667d8e9-9d4d-4ccb-ba32-21da3bb5aafc.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=30376;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=zqs81892;PWD=U0PDL38UGcSYEbKk",'','')
    print(conn)
    print("connection successful...")
    insertdb(conn,"kulkarni","Hari@gmail.com",'1234567890','Faculty',"abcdef")
    getdetails("Hari@gmail.com",'1234567')
    #showall()

except:
    print(" RAK Error connecting to the database")



