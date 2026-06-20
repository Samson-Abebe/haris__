from flask import Flask, request, render_template,send_file,session ,jsonify,Response,redirect,url_for,send_from_directory, abort
from acc import Super_Admin,Store_Manager,cashier,sales_
from maindb import re_mogo
from bson import ObjectId
import time
from datetime import datetime, timedelta
def get_time_number():
    return int(time.time())
#---------------------the notification part------------------

nota={

}
mon=re_mogo("invoices")
mon_=re_mogo("drug")
def part_1(m):

     
    #collect____________________________
     m["Withholding"]["noofn"]=mon.count_documents({"withcon": {"$exists": False}})
    #expired______________________________
     today = datetime.now()
     future_date = today + timedelta(days=90)
     m["Expired"]["noofn"]=mon_.count_documents({"expiry_date": {"$lt": future_date.strftime("%Y-%m-%d") }, "disposal_date": {"$exists": False}, "amount": { "$gt": 0 }})
     #credit________________________________
     m["Credit"]["noofn"]=mon.count_documents({"stage":1,"credit_type": 'credit'})
     return m
def part_2(m):
    m["Product"]["noofn"]=mon.count_documents({"stage":2})
    #-------------------------------------
    today = datetime.now()
    future_date = today + timedelta(days=90)
    m["Expired"]["noofn"]=mon_.count_documents({"expiry_date": {"$lt": future_date.strftime("%Y-%m-%d") }, "disposal_date": {"$exists": False}, "amount": { "$gt": 0 }})
    #-------------------------------------
    
    return m
def part_3(m):
    mv=mon.count_documents({"stage":3,"credit_type": 'credit'})
    mv2=mon.count_documents({"stage":1,"credit_type": 'cash'})
    m["Sales"]["noofn"]=mv+mv2
    return m
def part_4(m):
    return m
def part_5(m):
    return m

def valid_departmnet(id):
    pinfo=session["pinfo"]
    department=pinfo["department"]
    if(str(id)==department):
        return False
    return True



def get_menu():
    #ceo first work is worked in this 
    if "pinfo" in session:
            pinfo=session["pinfo"]
            department=pinfo["department"]
            menu=False
            if department=="1":
                menu=part_1(Super_Admin)
                print("heloo form Super_Admin")
            if department=="2":
                menu=part_2(Store_Manager)
                print("heloo form store")
            if department=="3":
                menu=part_3(cashier)
                print("heloo form cashier")
            if department=="4":
                if pinfo["employment_type"]=='Staff':
                    menu=part_4(sales_)
                    print("heloo form sales")
                else:
                    menu=part_5(sales_)
                    print("heloo form agent")
            return menu 
    else:
      pinfo = None


def ceo(x):
    print("like it is the session ",session)
    menu=get_menu()
    mon=re_mogo("job")
    mv=mon.find_one({"_id":ObjectId(session["pinfo"]["_id"])},{"Session":1})
    if(not bool(mv["Session"])):
        return False 
    x=x[1:]
    if(menu):
        
        pinfo=session["pinfo"]
        time=pinfo["time"]
        ti=int(time)-get_time_number()
        if(ti<0):
            print("safftwo!!!!!")
            return False
      
        for x1 in menu:
            if x in menu[x1]["submenu"]:
                print("safffromfour!!!!!!!")
                return menu
               
        print("saffone")
    else:
        return False           

        



