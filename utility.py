from maindb import re_mogo
from bson import ObjectId
import time
from datetime import datetime


def get_time_number():
    return int(time.time())


import random

def get_random_index():
    return random.randint(0, 19)


def date_to_timestamp(date_string):
    dt = datetime.strptime(date_string, "%Y-%m-%d")
    return int(time.mktime(dt.timetuple()))

# Example
timestamp = date_to_timestamp("2026-05-13")
print(timestamp)

def get_dateformat(ts=None):
    if ts is None:
        ts = time.time()
    return datetime.fromtimestamp(ts).strftime("%Y-%m-%d")

def get_totale_amount(id):
    #returen the totale amount of drug 
    
   
    mon=re_mogo("drug")
    mv=mon.find({"drug_id":str(id)}, {"amount":1})
    amount=0
    for fx in mv:
        print("like _______ not ",fx)
        amount=amount+float(fx["amount"])
    return amount

def priorty_ex_reduction(id,amount):
    mon=re_mogo("drug")
    mv=mon.find({"drug_id":str(id)}, {"amount":1,"expiry_date":1,"_id":1})
    nv={}
    nv_={}
    amount=float(amount)
    for fx in mv:
        co_=date_to_timestamp(fx["expiry_date"])-get_time_number()
        if co_ > 0:
            nv[fx["_id"]]=date_to_timestamp(fx["expiry_date"])
            nv_[fx["_id"]]=float(fx["amount"])
            print(nv)
        else:
          print("ex_______")
    nv= dict(sorted(nv.items(), key=lambda item: item[1]))
    print("sort nv-------",nv)
    total=0
    for fx_ in nv_:
        total+=total+nv_[fx_]
    if total < amount:
        print("it is back")
        return False
    print("it not back")
    for fx1 in nv:
        x=nv_[fx1]-amount
        if(x>=0):
           mon.update_one(
                    {"_id":fx1},
                    {
                        "$set": {
                            "amount":x,
                        }
                    }
                )  
           break
        else:
            amount=-1*x
            mon.update_one(
                    {"_id":fx1},
                    {
                        "$set": {
                            "amount":0,
                        }
                    }
                ) 


def crilance_priorty_ex_reduction(id,amount):
    mon=re_mogo("drug")
    mv=mon.find({"drug_id":str(id)}, {"amount":1,"expiry_date":1,"_id":1})
    nv={}
    nv_={}
    amount=float(amount)
    for fx in mv:
        co_=date_to_timestamp(fx["expiry_date"])-get_time_number()
        if co_ > 0:
            nv[fx["_id"]]=date_to_timestamp(fx["expiry_date"])
            nv_[fx["_id"]]=float(fx["amount"])
            print(nv)
        else:
          print("ex_______")
    nv= dict(sorted(nv.items(), key=lambda item: item[1]))
    print("sort nv-------",nv)
    total=0
    for fx_ in nv_:
        total+=total+nv_[fx_]
    if total < amount:
        print("it is back")
        return True
    return False 



def get_invoces():
    mon=re_mogo("invo_no")
    mv=mon.find_one({"_id":ObjectId('6a153994e482896a223dfc84')},{"no":1})
    return mv["no"]
def get_su_invoces():
    last = get_invoces()
    if last:
        new_no = last+ 1
    else:
        new_no = 1
    mon=re_mogo("invo_no")
    mon.update_one(
        {"_id":ObjectId('6a153994e482896a223dfc84')},
        {"$set": {"no":new_no}}
    )
    return f"INV-{new_no:07d}"


#-------------------------chking____site__________________
# priorty_ex_reduction("6a0f04e038f9fa8478e3a038",2000)


  
  
  


  

