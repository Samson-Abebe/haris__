from flask import Flask, request, render_template,send_file,session ,jsonify,Response,redirect,url_for,send_from_directory, abort
import os
from datetime import datetime, timedelta

from maindb import re_mogo
import re
from support import get_menu,ceo,valid_departmnet
from utility import get_totale_amount,get_su_invoces,get_dateformat,priorty_ex_reduction,get_random_index,date_to_timestamp,crilance_priorty_ex_reduction
from acc import colors,job_,tamps,drug_categories
from flask_cors import CORS
from bson import ObjectId
app = Flask(__name__)
app.secret_key='mysecret$#^%^&%^&*withmoreopss'

"""
return render_template("sam.html",menu=menu,s=s,f=f,mid=mid)
"""
import cloudinary
import cloudinary.uploader
cloudinary.config(
    # cloud_name="djmdhqokw",
    # api_key="811589763914498",
    # api_secret="fn3f6SJpn_z9KBs_8vglZhrNzb0",
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    secure=True
)

import time

def get_time_number():
    return int(time.time())

def post_get():
 p=9   # Your code that may raise a "Method Not Allowed" error
 if request.method == 'POST':
            # Process GET request
            p=0
            print("SAMSON")
 elif request.method == 'GET':
            p=1  
 return p
@app.route('/',methods=['GET',"POST"])
def login():
    session.pop("pinfo", None)
    con=False
    return render_template("login.html",con=con)

@app.route('/log',methods=['GET',"POST"])
def log():
    phone = request.form.get("phone")
    password = request.form.get("password")

    print(f"Phone: {phone}, Password: {password}")
    session.pop("pinfo", None)
    mon=re_mogo("job")
    phone = request.form.get("phone")
    password = request.form.get("password")
    user = mon.find_one({
    "phone": phone,"password":password,"Session":1},
    {"_id":1,"fname":1,"department":1,"employment_type":1})
    
    if user:
        s={}
        s["cons"]="Wellcome"
        f="/log"
        x={}
        x["_id"]=str(user["_id"])
        x["fname"]=user["fname"]
        x["department"]=user["department"]
        x["dep_"]=job_[int(user["department"])]
        x["time"]=get_time_number()+259200
        x["employment_type"]=user["employment_type"]
        session["pinfo"]=x
        menu=get_menu() 
        mid="wellcome.html"
        #u have to redirect to some new wellcome function that all thing go ok 
        return render_template("sam.html",menu=menu,s=s,f=f,mid=mid)
    else:
        con=True
        print(con)
        return render_template("login.html",con=con)



        
       

    


@app.route('/Add Staf',methods=['GET',"POST"])
def root___1():
    #reggterd the staff 
    f="/Add Staf"
    menu=ceo(f)
    mid="addstaff.html"
    s={}
    s["cons"]="Dashboard/Add staf"
    
    if(menu):
                jp=post_get()
                if (jp==0):
                        name = request.form["name"]
                        email = request.form["email"]
                        department = request.form["department"]
                        phone = request.form["phone"]
                        employment_type = request.form["employment_type"]
                    
                        mon=re_mogo("job")
                        _data={
                            "fname":name,
                            "email":email,
                            "department":department,
                            "phone":phone,
                            "employment_type":employment_type,
                            "password":request.form["password"],
                            "Session":1
                        }
                        _data["rate"]=10
                        user = mon.find_one({"phone":phone})

                        if user:
                            print("er=Email already existsEmail not found")
                        else:
                            print("phone not found")
                            mon.insert_one(_data)
                            su="Email not found"

                        
                        return redirect(url_for("root___1"))
            
                
                
                return render_template("sam.html",f=f,menu=menu,s=s,mid=mid)
    else:
      return redirect(url_for("login"))


@app.route('/Add Product',methods=['GET',"POST"])
def root___2():
    #__regsterdstock

    jp=post_get()
    f="/Add Product"
    menu=ceo(f)
    mid="regsterstock.html"
    s={}
    s["cons"]="Product/Add Product"
    
    if(menu):
            if (jp==0):
                
                    drug_name = request.form.get('drug_name')
                    generic_name = request.form.get('generic_name')
                    group_id = int(request.form.get('pharmacy_group_id'))  # Receives integer 1 through 12
                    quantity = request.form.get('quantity')
                    date = get_time_number()
                
                    mon=re_mogo("_drug")
                    _data={
                        "drug_name":drug_name,
                        "generic_name":generic_name,
                        "group_id":group_id,
                        "price":quantity,
                        "date":date
                    }

                    mon.insert_one(_data)
                    return redirect(url_for("root___2"))
            return render_template("sam.html",f=f,menu=menu,s=s,mid=mid)
    else:
        return redirect(url_for("login"))


@app.route('/Rececivng Product',methods=['GET',"POST"])
def root___3():
    #instock
    f="/Rececivng Product"
    menu=ceo(f)
    mid="instock.html"
    s={}
    s["cons"]="Product/Rececivng Product"
    
    if(menu):
        _s={}
        mon=re_mogo("_drug")
        x=mon.find({},{"drug_name":1})
        for x1 in x:
            _s[str(x1["_id"])]=x1["drug_name"]
        s["1"]=_s
        jp=post_get()
        if (jp==0):
                drug_id = request.form["drug_name"]
                provider_name = request.form["provider_name"]
                expiry_date = request.form["expiry_date"]
                amount = request.form["amount"]
                cost_price = request.form["cost_price"]
                mon=re_mogo("drug")
                _data={
                    "drug_id":drug_id,
                    "provider_name":provider_name,
                    "expiry_date":expiry_date,
                    "amount":amount,
                    "cost_price":cost_price,
                    "date":get_time_number()
                }
                print(_data)
                mon.insert_one(_data)

            
                return redirect(url_for("root___3"))
        return render_template("sam.html",f=f,s=s,menu=menu,mid=mid)
    else:
        return redirect(url_for("login"))




@app.route('/Add Bank',methods=['GET',"POST"])
def root___4():    
   #banc
    f="/Add Bank"
    menu=ceo(f)
    mid="banc.html"
    s={}
    s["cons"]="Bank/Add Bank"
    jp=post_get()
    
    if(menu):
            if (jp==0): 
                    _data = {
                            "bank_name": request.form["bank_name"],
                            "account_name": request.form["account_name"],
                            "account_number": request.form["account_number"],
                            "account_type": request.form["account_type"],
                            "swift_code": request.form["swift_code"],
                            "balance": float(request.form["initial_balance"])
                        }
                    mon=re_mogo("banc")
                    mon.insert_one(_data)
                    return redirect(url_for("root___4"))
            return render_template("sam.html",f=f,menu=menu,s=s,mid=mid)
    else:
      return redirect(url_for("login"))
@app.route('/Add Customer',methods=['GET',"POST"])
def root___5():    
   #customer
    jp=post_get()
    f="/Add Customer"
    menu=ceo(f)
    mid="customer.html"
    s={}
    s["cons"]="Customer/Add Customer"
    if(menu):
        if (jp==0): 
                pinfo=session["pinfo"]
                doid=pinfo["_id"]
                _data = {
                            "customer_name": request.form["customer_name"],
                            "phone_number": request.form["phone_number"],
                            "email": request.form["email"],
                            "address": request.form["address"],
                            "notes": request.form["notes"],
                            "doid":doid
                        }
                mon=re_mogo("customer")
                mon.insert_one(_data)
                return redirect(url_for("root___5"))
        return render_template("sam.html",f=f,s=s,menu=menu,mid=mid)
    else:
        return redirect(url_for("login"))


@app.route('/Sales',methods=['GET',"POST"])
def root___6(): 
    jp=post_get()
    f="/Sales"
    menu=ceo(f)
    mid="invoices.html"
    s={}
    s["cons"]="Sales/Sales"
    if(menu):
        mon=re_mogo("customer")
        mv=mon.find({}, {"customer_name":1,"_id":1})
        _s={}
        for fx in mv:
            _s[str(fx["_id"])]=fx["customer_name"]
        s["s1"]=_s
        _s={}
        mon=re_mogo("banc")
        mv=mon.find({},{"_id":1,"bank_name":1})
        for fx in mv:
            _s[str(fx["_id"])]=fx["bank_name"]
        s["s3"]=_s
     
        
        # { id: "101", name: "Amoxicillin 500mg", unitPrice: 12.50, stock: 45 },
        _s=[]
        mon=re_mogo("_drug")
        mv=mon.find()
        for fx in mv:
            nv={}
            nv["id"]=str(fx["_id"])
            nv["name"]=fx["drug_name"]
            nv["unitPrice"]=float(fx["price"])
            nv["stock"]=5000#get_totale_amount(fx["_id"])
            _s.append(nv)
        s["s2"]=_s

      
        if(jp==0):
            pinfo=session["pinfo"]
            doid=pinfo["_id"]
            data = {
                "customer_id": request.form["customer_id"],
                "credit_type": request.form["credit_type"],
                "subtotal_price": request.form["subtotal_price"],
                "withholding_tax": request.form["withholding_tax"],
                "total_net": request.form["total_net"]
            }

            if request.form.get("bank_account"):
                data["bank_account"] = request.form["bank_account"]

            if request.form.get("payment_due_date"):
                data["payment_due_date"] = request.form["payment_due_date"]
            drugs = []

            for key in request.form:
                if key.startswith("drugs["):
                    drugs.append({
                        "drug_id": request.form.get(key.replace("[quantity]", "[drug_id]").replace("[unit_price]", "[drug_id]")),
                        "unit_price": request.form.get(key.replace("[quantity]", "[unit_price]").replace("[drug_id]", "[unit_price]")),
                        "quantity": request.form.get(key.replace("[unit_price]", "[quantity]").replace("[drug_id]", "[quantity]"))
                    })

            # Remove duplicate entries
            unique_drugs = []
            seen = set()

            for item in drugs:
                check = (item["drug_id"], item["unit_price"], item["quantity"])
                
                if check not in seen:
                    seen.add(check)
                    unique_drugs.append(item)
            if "image" not in request.files:
                return jsonify({"error": "No image uploaded"}), 400

            image = request.files["image"]

            # Upload to Cloudinary
            upload_result = cloudinary.uploader.upload(
                image,
                folder="staff"
             )

            image_url = upload_result["secure_url"]
            image_id = upload_result["public_id"]

            data["drugs"] = unique_drugs
            print(data)
            data["date1"]=get_time_number()
            data["doid"]=doid
            data["stage"]=1
            data["urls"]= image_url 
            data["public_id"]= image_id 
            data["invoices"]=get_su_invoces()
            mon_=re_mogo("job")
            mv=mon_.find_one({"_id":ObjectId(doid)},{"rate":1})
            data["comution"]=float(data["subtotal_price"])*(float(mv["rate"])*0.01)
            mon=re_mogo("invoices")
            mon.insert_one(data)
            return redirect(url_for("root___6"))
            
        return render_template("sam.html",f=f,s=s,menu=menu,mid=mid)
    else:
        return redirect(url_for("login"))


@app.route('/Stocks',methods=['GET',"POST"])
def root___7():
    #__regsterdstock
    jp=post_get()
    f="/Stocks"
    menu=ceo(f)
    mid="dis_stock.html"
    s={}
    s["cons"]="Product/Stocks" 
    if(menu):
        mon=re_mogo("drug")
        mon_=re_mogo("_drug")
        mv=mon.find({"disposal_date": {"$exists": False}},{"_id":0})
        colre_int=0
        coler={}
        s_=[]
        for fx in mv:
            nv={}
            mv_=mon_.find_one({"_id":ObjectId(fx["drug_id"])},{"drug_name":1,"generic_name":1,"price":1})
            nv["Name"]=mv_["drug_name"]
            nv["genericname"]=mv_["generic_name"]
            nv["providername"]=fx["provider_name"]
            nv["expiry"]=fx["expiry_date"]
            nv["Registereddate"]=get_dateformat(fx["date"])
            nv["price"]=mv_["price"]
            nv["costprice"]=fx["cost_price"]
            nv["Amount"]=int(fx["amount"])
            s_.append(nv)
            if mv_["drug_name"] in coler:
                pass
            else:
                coler[mv_["drug_name"]]=colors[colre_int]
                colre_int+=1
        s["s1"]=s_
        s["s2"]=coler
        print(s["s2"])


        return render_template("sam.html",f=f,s=s,menu=menu,mid=mid)
    else:
        return redirect(url_for("login"))


@app.route('/Staff',methods=['GET',"POST"])
def root___8():
    jp=post_get()
    f="/Staff"
    menu=ceo(f)
    mid="dis_Staff.html"
    s={}
    s["cons"]="Product/Staff" 
    if(menu):
        mon=re_mogo("job")
        mv=mon.find({},{"_id":0,"password":0})
        s_=[]
        for fx in mv:
            nv={}
            nv["FullName"]=fx["fname"]
            nv["Email"]=fx["email"]
            nv["Session"]=fx["Session"]
            nv["Department"]=job_[int(fx["department"])]
            nv["Phone"]=fx["phone"]
            nv["Type"]=fx["employment_type"]
            s_.append(nv)

            pass 
        s["s1"]=s_
        coler={
            "Staff":colors[3],
            "Agent":colors[7]
        }
        s["s2"]=coler
        return render_template("sam.html",f=f,s=s,menu=menu,mid=mid)
    else:
        return redirect(url_for("login"))

@app.route('/Customer',methods=['GET',"POST"])
def root___9():
   
    jp=post_get()
    f="/Customer"
    menu=ceo(f)
    mid="dis_Customer.html"
    s={}
    s["cons"]="Product/Customer" 
    if(menu):
        mon=re_mogo("customer")
        mon_=re_mogo("job")
        mv=mon.find({},{"_id":0})
        s_=[]
        coler={}
        colre_int=0
        for fx in mv:
            nv={}
            mv_=mon_.find_one({"_id":ObjectId(fx["doid"])},{"fname":1,"phone":1})
            nv["CustomerName"]=fx["customer_name"]
            nv["Phone"]=mv_["phone"]
            nv["Email"]=fx["email"]
            nv["address"]=fx["address"]
            nv["Description"]=fx["notes"]
            rb=mv_["fname"]+mv_["phone"]
            nv["RegistereBy"]=rb
            s_.append(nv)
            if rb in coler:
                pass
            else:
                coler[rb]=colors[colre_int]
                colre_int+=1
        s["s1"]=s_
        s["s2"]=coler
             
        return render_template("sam.html",f=f,s=s,menu=menu,mid=mid)
    else:
        return redirect(url_for("login"))







@app.route('/Rececivng Cash',methods=['GET',"POST"])
def root___10():
    jp=post_get()
    f="/Rececivng Cash"
    menu=ceo(f)
    mid="receciving.html"
    s={}
    s["cons"]="Product/Customer" 
    if(menu):
         
              s_=[]
              mon=re_mogo("invoices")
              mon_=re_mogo("customer")
              mon__=re_mogo("job")
              mv=mon.find({"stage":1,"credit_type": 'cash'},{"total_net":1,"invoices":1,
              "customer_id":1,"doid":1,"total_net":1,"_id":1})
              for fx in mv:
                nv={}
                mv_=mon_.find_one({"_id":ObjectId(fx["customer_id"])},{"customer_name":1,"phone_number":1})
                mv__=mon__.find_one({"_id":ObjectId(fx["doid"])},{"phone":1,"fname":1})
                nv["id"]=fx["invoices"]
                nv["customerName"]=mv_["customer_name"]
                nv["cp"]=mv_["phone_number"]
                nv["salespersonName"]=mv__["fname"]
                nv["sp"]=mv__["phone"]
                nv["slipUrl"]=str(fx["_id"])
                nv["netTotal"]=float(fx["total_net"])
                s_.append(nv)
              s["s1"]=s_
              print(".............",s)
            
              return render_template("sam.html",f=f,s=s,menu=menu,mid=mid)
    else:
        return redirect(url_for("login"))
    

@app.route('/Approve Credit',methods=['GET',"POST"])
def root___11():
    jp=post_get()
    f="/Approve Credit"
    menu=ceo(f)
    mid="receciving.html"
    s={}
    s["cons"]="Credit/Approve Credit" 
    if(menu):
         
              s_=[]
              mon=re_mogo("invoices")
              mon_=re_mogo("customer")
              mon__=re_mogo("job")
              mv=mon.find({"stage":1,"credit_type": 'credit'},{"total_net":1,"invoices":1,
              "customer_id":1,"doid":1,"total_net":1,"_id":1})
              for fx in mv:
                nv={}
                mv_=mon_.find_one({"_id":ObjectId(fx["customer_id"])},{"customer_name":1,"phone_number":1})
                mv__=mon__.find_one({"_id":ObjectId(fx["doid"])},{"phone":1,"fname":1})
                nv["id"]=fx["invoices"]
                nv["customerName"]=mv_["customer_name"]
                nv["cp"]=mv_["phone_number"]
                nv["salespersonName"]=mv__["fname"]
                nv["sp"]=mv__["phone"]
                nv["slipUrl"]=str(fx["_id"])
                nv["netTotal"]=float(fx["total_net"])
                s_.append(nv)
              s["s1"]=s_
        
            
              return render_template("sam.html",f=f,s=s,menu=menu,mid=mid)
    else:
        return redirect(url_for("login"))
    

@app.route('/Issues',methods=['GET',"POST"])
def root___12():
    jp=post_get()
    f="/Issues"
    menu=ceo(f)
    mid="Issues.html"
    s={}
    s["cons"]="Credit/Approve Credit" 
    if(menu):
         
              s_=[]
              mon=re_mogo("invoices")
              mon_=re_mogo("customer")
              mon__=re_mogo("job")
              mv=mon.find({"stage":2},{"total_net":1,"invoices":1,
              "customer_id":1,"doid":1,"total_net":1,"_id":1})
              for fx in mv:
                nv={}
                mv_=mon_.find_one({"_id":ObjectId(fx["customer_id"])},{"customer_name":1,"phone_number":1})
                mv__=mon__.find_one({"_id":ObjectId(fx["doid"])},{"phone":1,"fname":1})
                nv["id"]=fx["invoices"]
                nv["customerName"]=mv_["customer_name"]
                nv["cp"]=mv_["phone_number"]
                nv["salespersonName"]=mv__["fname"]
                nv["sp"]=mv__["phone"]
                nv["slipUrl"]=str(fx["_id"])
                nv["netTotal"]=float(fx["total_net"])
                s_.append(nv)
              s["s1"]=s_
              print(".............",s)
            
              return render_template("sam.html",f=f,s=s,menu=menu,mid=mid)
    else:
        return redirect(url_for("login"))
    


@app.route('/Rececivng Credit',methods=['GET',"POST"])
def root___13():
    jp=post_get()
    f="/Rececivng Credit"
    menu=ceo(f)
    mid="receciving.html"
    s={}
    s["cons"]="Sales/Rececivng Credit" 
    if(menu):
              s_=[]
              mon=re_mogo("invoices")
              mon_=re_mogo("customer")
              mon__=re_mogo("job")
              mv=mon.find({"stage":3,"credit_type": 'credit'},{"total_net":1,"invoices":1,
              "customer_id":1,"doid":1,"total_net":1,"_id":1})
              for fx in mv:
                nv={}
                mv_=mon_.find_one({"_id":ObjectId(fx["customer_id"])},{"customer_name":1,"phone_number":1})
                mv__=mon__.find_one({"_id":ObjectId(fx["doid"])},{"phone":1,"fname":1})
                nv["id"]=fx["invoices"]
                nv["customerName"]=mv_["customer_name"]
                nv["cp"]=mv_["phone_number"]
                nv["salespersonName"]=mv__["fname"]
                nv["sp"]=mv__["phone"]
                nv["slipUrl"]=str(fx["_id"])
                nv["netTotal"]=float(fx["total_net"])
                s_.append(nv)
              s["s1"]=s_
              print(".............",s)
            
              return render_template("sam.html",f=f,s=s,menu=menu,mid=mid)
    else:
        return redirect(url_for("login"))


@app.route('/Collect',methods=['GET',"POST"])
def root___14():
    jp=post_get()
    f="/Collect"
    menu=ceo(f)
    mid="Collect.html"
    s={}
    s["cons"]="Withholding/Collect" 
    if(menu):
              s_=[]
              mon=re_mogo("invoices")
              mon_=re_mogo("customer")
              mon__=re_mogo("job")
              mv=mon.find({"withcon": {"$exists": False}},{"total_net":1,"invoices":1,
              "customer_id":1,"doid":1,"withholding_tax":1,"_id":1})
            
              
              for fx in mv:
                nv={}
                mv_=mon_.find_one({"_id":ObjectId(fx["customer_id"])},{"customer_name":1,"phone_number":1})
                mv__=mon__.find_one({"_id":ObjectId(fx["doid"])},{"phone":1,"fname":1})
                nv["id"]=fx["invoices"]
                nv["customerName"]=mv_["customer_name"]
                nv["cp"]=mv_["phone_number"]
                nv["salespersonName"]=mv__["fname"]
                nv["sp"]=mv__["phone"]
                nv["slipUrl"]=str(fx["_id"])
                nv["netTotal"]=float(fx["withholding_tax"])
                s_.append(nv)
              s["s1"]=s_
              print(".............",s)
            
              return render_template("sam.html",f=f,s=s,menu=menu,mid=mid)
    else:
        return redirect(url_for("login"))




@app.route('/Expired bellow 90d',methods=['GET',"POST"])
def root___15():
    jp=post_get()
    f="/Expired bellow 90d"
    menu=ceo(f)
    mid="exp.html"
    s={}
    s["cons"]="Expired/Expired bellow 60d" 
    if(menu):
   

        today = datetime.now()
        future_date = today + timedelta(days=90)
        mon=re_mogo("drug")
        mon_=re_mogo("_drug")
        s_=[]
        mv=mon.find({
        "expiry_date": {
                    "$lt": future_date.strftime("%Y-%m-%d")
                },
        "disposal_date": {"$exists": False}
            },{"_id":1,"drug_id":1,"expiry_date":1,"amount":1,"cost_price":1,"date":1})
        for fx in mv:
            mv_=mon_.find_one({"_id":ObjectId(fx["drug_id"])},{"drug_name":1})
            nv={}
            nv["batchId"]=get_dateformat(fx["date"])
            nv["drugName"]=mv_["drug_name"]
            nv["stockQty"]=float(fx["amount"])
            nv["expiryDate"]=fx["expiry_date"]
            nv["unitCost"]=fx["cost_price"]
            nv["id_"]=str(fx["_id"])
            s_.append(nv)
        s["s1"]=s_
        return render_template("sam.html",f=f,s=s,menu=menu,mid=mid)
    else:
        return redirect(url_for("login"))

@app.route('/Total',methods=['GET',"POST"])
def root___16():
    #totale with holed
    jp=post_get()
    f="/Total"
    menu=ceo(f)
    mid="Totalwithholed.html"
    s={}
    s["cons"]="Withholding/Total" 
    if(menu):
              s_=[]
              mon=re_mogo("invoices")
              mon_=re_mogo("customer")
              mon__=re_mogo("job")
              mv=mon.find({},{"total_net":1,"invoices":1,
              "customer_id":1,"doid":1,"withholding_tax":1,"_id":1,"withcon":1})
              for fx in mv:
                nv={}
                mv_=mon_.find_one({"_id":ObjectId(fx["customer_id"])},{"customer_name":1,"phone_number":1})
                mv__=mon__.find_one({"_id":ObjectId(fx["doid"])},{"phone":1,"fname":1})
                nv["id"]=fx["invoices"]
                nv["customerName"]=mv_["customer_name"]
                nv["cp"]=mv_["phone_number"]
                nv["salespersonName"]=mv__["fname"]
                nv["sp"]=mv__["phone"]
                nv["slipUrl"]=str(fx["_id"])
                nv["netTotal"]=float(fx["withholding_tax"])
                if fx.get("withcon"):
                    nv["with_d"] = get_dateformat(fx["withcon"])
                else:
                    nv["with_d"] = "uncollected"
                s_.append(nv)
              s["s1"]=s_
              coler={
                        "collected":colors[3],
                        "uncollected":colors[7]
                      }
              s["s2"]=coler
             
              print(".............",s)
              return render_template("sam.html",f=f,s=s,menu=menu,mid=mid)
    else:
        return redirect(url_for("login"))

@app.route('/Edit',methods=['GET',"POST"])
def root___17():
    #totale with holed
    jp=post_get()
    f="/Edit"
    menu=ceo(f)
    mid="edit.html"
    s={}
    s["cons"]=" Dashboard/Edit" 
    if(menu):
     
        s_=[]
        mon=re_mogo("job")
        mv=mon.find()
      
        for fx in mv:
            nv={}
            nv["id"]=str(fx["_id"])
            nv["name"]=fx["fname"]
            nv["phone"]=fx["phone"]
            if(fx["employment_type"]=="Agent" and int(fx["department"])==4):
                 C_=int(fx["department"])+1
                 nv["department"]=job_[C_]
            else:
                nv["department"]=job_[int(fx["department"])]
            
            nv["sessionActive"]=fx["Session"]
            
            if fx.get("rate"):
                nv["ratePercentage"]=fx["rate"]
            else:
               nv["ratePercentage"]=0.0
            s_.append(nv)
        s["s1"]=s_
        return render_template("sam.html",f=f,s=s,menu=menu,mid=mid)
    else:
        return redirect(url_for("login"))


@app.route('/Total commution',methods=['GET',"POST"])
def root___18():
    #totale with holed
    jp=post_get()
    f="/Total commution"
    menu=ceo(f)
    mid="commution.html"
    s={}
    s["cons"]="Commution/Total" 
    if(menu):
          mon=re_mogo("invoices")
          mon_=re_mogo("job")
          mv=mon.find({},{"doid":1,"subtotal_price":1,"date1":1,"comution":1})
          nv_={}
         
          s_=[]
          for fx in mv:
            mv_=mon_.find_one({"_id":ObjectId(fx["doid"])},{"_id":1,"fname":1,"phone":1,"commutionp":1})
            nv={}
            nv["agentName"]=mv_["fname"]
            nv["phone"]=mv_["phone"]
            nv["salesAmount"]=float(fx["subtotal_price"])
            nv["date"]=get_dateformat(fx["date1"])
            nv["slipUrl"]=str(fx["_id"])
            if mv_.get("commutionp"):
                print("surafel adane",mv_["commutionp"])
                if mv_["commutionp"] >=fx["date1"]:
                    #it is paid bc last time is pay include the mv_["commutionp"] date
                    nv["status"]="paid"
                else:
                    nv["status"]="unpaid"

            else:
               nv["status"]="unpaid"
           
            price=(float(fx["comution"])*100)/float(fx["subtotal_price"])
            nv["ratePercentage"]=round(price, 2)
            s_.append(nv)
          s["s1"]=s_
          return render_template("sam.html",f=f,s=s,menu=menu,mid=mid)
    else:
        return redirect(url_for("login"))


@app.route('/Pay',methods=['GET',"POST"])
def root___19():
    #totale with holed
    jp=post_get()
    f="/Pay"
    menu=ceo(f)
    mid="pay_commution.html"
    s={}
    s["cons"]="Commution/pay" 
    if(menu):
          mon=re_mogo("invoices")
          mon_=re_mogo("job")
          mv=mon.find({},{"doid":1,"subtotal_price":1,"date1":1,"comution":1})
          nv_={}
          n_v={}
  
  
          mv__=mon_.find({"department":"4","employment_type":'Agent',},{"commutionp":1,"_id":1,"phone":1})
          for fx_ in mv__:
            if fx_.get("commutionp"):
              nv_[str(fx_["_id"])]=fx_["commutionp"]
              n_v[fx_["phone"]]=get_dateformat(fx_["commutionp"])
            else:
                nv_[str(fx_["_id"])]=1767225600
                n_v[fx_["phone"]]=get_dateformat(1767225600)
          s["s2"]=n_v
          s_=[]
          for fx in mv:
           if nv_.get(fx["doid"]):
            if nv_[fx["doid"]] < fx["date1"]:
                
                mv_=mon_.find_one({"_id":ObjectId(fx["doid"])},{"fname":1,"phone":1,"commutionp":1})
                nv={}
                nv["agentName"]=mv_["fname"]
                nv["phone"]=mv_["phone"]
                nv["salesAmount"]=float(fx["subtotal_price"])
                nv["date"]=get_dateformat(fx["date1"])
                price=(float(fx["comution"])*100)/float(fx["subtotal_price"])
                nv["ratePercentage"]=round(price, 2)
                s_.append(nv)
            else:
                pass
          s["s1"]=s_
          return render_template("sam.html",f=f,s=s,menu=menu,mid=mid)
    else:
        return redirect(url_for("login"))



@app.route('/Rececivng Report',methods=['GET',"POST"])
def root___20():
    #totale with holed
    jp=post_get()
    f="/Rececivng Report"
    menu=ceo(f)
    mid="Report.html"
    s={}
    s["cons"]="Report/Rececivng Report" 
    if(menu):
              s_=[]
              mon=re_mogo("invoices")
              mon_=re_mogo("customer")
              mon__=re_mogo("job")
              mv=mon.find({"date2": {"$exists": True}},{"total_net":1,"invoices":1,
              "customer_id":1,"doid":1,"total_net":1,"_id":1,"date2":1})
              for fx in mv:
                nv={}
                mv_=mon_.find_one({"_id":ObjectId(fx["customer_id"])},{"customer_name":1,"phone_number":1})
                mv__=mon__.find_one({"_id":ObjectId(fx["doid"])},{"phone":1,"fname":1})
                nv["id"]=fx["invoices"]
                nv["customerName"]=mv_["customer_name"]
                nv["cp"]=mv_["phone_number"]
                nv["salespersonName"]=mv__["fname"]
                nv["sp"]=mv__["phone"]
                nv["slipUrl"]=str(fx["_id"])
                nv["netTotal"]=float(fx["total_net"])
                nv["approvedDate"]=get_dateformat(fx["date2"])
                s_.append(nv)
              s["s1"]=s_
              return render_template("sam.html",f=f,s=s,menu=menu,mid=mid)
    else:
        return redirect(url_for("login"))



@app.route('/Report Issues',methods=['GET',"POST"])
def root___21():
    #totale with holed
    jp=post_get()
    f="/Report Issues"
    menu=ceo(f)
    mid="Report.html"
    s={}
    s["cons"]="Report/Report Issues" 
    if(menu):
              s_=[]
              mon=re_mogo("invoices")
              mon_=re_mogo("customer")
              mon__=re_mogo("job")
              mv=mon.find({"date3": {"$exists": True}},{"total_net":1,"invoices":1,
              "customer_id":1,"doid":1,"total_net":1,"_id":1,"date3":1})
              for fx in mv:
                nv={}
                mv_=mon_.find_one({"_id":ObjectId(fx["customer_id"])},{"customer_name":1,"phone_number":1})
                mv__=mon__.find_one({"_id":ObjectId(fx["doid"])},{"phone":1,"fname":1})
                nv["id"]=fx["invoices"]
                nv["customerName"]=mv_["customer_name"]
                nv["cp"]=mv_["phone_number"]
                nv["salespersonName"]=mv__["fname"]
                nv["sp"]=mv__["phone"]
                nv["slipUrl"]=str(fx["_id"])
                nv["netTotal"]=float(fx["total_net"])
                nv["approvedDate"]=get_dateformat(fx["date3"])
                s_.append(nv)
              s["s1"]=s_
              print(".............",s)
              return render_template("sam.html",f=f,s=s,menu=menu,mid=mid)
    else:
        return redirect(url_for("login"))


@app.route('/Report Sales',methods=['GET',"POST"])
def root___22():
    #totale with holed
    jp=post_get()
    f="/Report Sales"
    menu=ceo(f)
    mid="commution_.html"
    s={}
    s["cons"]="Report/Report Salestal" 
    if(menu):
          mon=re_mogo("invoices")
          mon_=re_mogo("job")
          mv=mon.find({"doid":session["pinfo"]["_id"]},{"doid":1,"subtotal_price":1,"date1":1,"comution":1})
          nv_={}
          tt=mon_.find_one({"_id":ObjectId(session["pinfo"]["_id"])},{"rate":1})
          if tt.get("rate"):
            s["per"]=tt["rate"]
          s["name"]=session["pinfo"]["fname"]
          s_=[]
          for fx in mv:
            mv_=mon_.find_one({"_id":ObjectId(fx["doid"])},{"_id":1,"fname":1,"phone":1,"commutionp":1})
            nv={}
            nv["agentName"]=mv_["fname"]
            nv["phone"]=mv_["phone"]
            nv["salesAmount"]=float(fx["subtotal_price"])
            nv["date"]=get_dateformat(fx["date1"])
            nv["slipUrl"]=str(fx["_id"])
            if mv_.get("commutionp"):
                print("surafel adane",mv_["commutionp"])
                if mv_["commutionp"] >=fx["date1"]:
                    #it is paid bc last time is pay include the mv_["commutionp"] date
                    nv["status"]="paid"
                else:
                    nv["status"]="unpaid"

            else:
               nv["status"]="unpaid"
           
            price=(float(fx["comution"])*100)/float(fx["subtotal_price"])
            nv["ratePercentage"]=round(price, 2)
            s_.append(nv)
          s["s1"]=s_
          return render_template("sam.html",f=f,s=s,menu=menu,mid=mid)
    else:
        return redirect(url_for("login"))

@app.route('/Edit prices',methods=['GET',"POST"])
def root___23():
    #totale with holed
    jp=post_get()
    f="/Edit prices"
    menu=ceo(f)
    mid="edit_prices.html"
    s={}
    s["cons"]="Product/Edit prices"
    if(menu):
        # { id: "MED-9021", name: "Amoxicillin 500mg (Capsule)", sku: "AMX-500-CAP", currentPrice: 14.50, category: "Antibiotic" },
        mon=re_mogo("_drug")
        mv=mon.find({},{"_id":1,"drug_name":1,"generic_name":1,"group_id":1,"price":1})
        s_=[]
        for nv in  mv:
            fx={}
            fx["id"]=str(nv["_id"])
            fx["name"]=nv["drug_name"]
            fx["sku"]=nv["generic_name"]
            fx["category"]=drug_categories[str(nv["group_id"])]
            fx["currentPrice"]=float(nv["price"])
            s_.append(fx)
        s["s1"]=s_
        if(jp==0):
                      medicine_id=request.form["medicine_id"]
                      new_price= float(request.form["new_price"])
                      mon.update_one(
                                {"_id":ObjectId(medicine_id)},
                                {
                                    "$set": {
                                        "price": new_price,
                                      
                                    }
                                }
                            )
                      return redirect(url_for("root___23"))
        return render_template("sam.html",f=f,s=s,menu=menu,mid=mid)
    else:
        return redirect(url_for("login"))




@app.route('/Otp',methods=['GET',"POST"])
def root___24():
    #totale with holed
    jp=post_get()
    f="/Otp"
    menu=ceo(f)
    mid="otpds.html"
    s={}
    s["cons"]="Otp/otp"
    if(menu):
        mon=re_mogo("otp")
        mon_=re_mogo("job")
        mv=mon.find()
        s_=[]
        for fx in mv:
            if get_time_number()-fx["time"] > 260:
                mon.delete_one({"_id":fx["_id"]})
                continue
            mo=mon_.find_one({"phone":fx["phone"]},{"fname":1}) 
            nv={}
            nv["userEmail"]=fx["phone"]
            nv["operationScope"]=mo["fname"]
            nv["rawToken"]=fx["number"]
            nv["status"]="active"
            s_.append(nv)
        s["s1"]=s_




        return render_template("sam.html",f=f,s=s,menu=menu,mid=mid)
    else:
        return redirect(url_for("login"))




#________________________________________________________________________________________________

@app.route("/slip/<id>")
def slip(id):
  
    sales_collection=re_mogo("invoices")
    sale = sales_collection.find_one({"_id": ObjectId(id)})
  
    
    customer_collection=re_mogo("customer")
    customer = customer_collection.find_one(
        {"_id": ObjectId(sale["customer_id"])},
        {"customer_name":1,"phone_number":1}

    )
    staff_collection=re_mogo("job")
    salesperson_ = staff_collection.find_one(
        {"_id": ObjectId(sale["doid"])},{"fname":1,"phone":1}
    )
    salesperson={
        "phone":salesperson_["phone"],
        "name":salesperson_["fname"]

    }
    if sale.get("credit_type") == "credit":
      bank = {"credit_return_date":sale["payment_due_date"]}
    bank_collection=re_mogo("banc")
    if sale.get("credit_type") == "cash":
        bank_ = bank_collection.find_one(
            {"_id": ObjectId(sale["bank_account"])},
            { "bank_name":1,"account_number":1,}
        )
        bank={
           "bank_name":bank_["bank_name"],
           "account_number":bank_["account_number"]
        }

    drugs = []
    drug_collection=re_mogo("_drug")
    for item in sale["drugs"]:
        drug = drug_collection.find_one(
            {"_id": ObjectId(item["drug_id"])}
            ,{"drug_name":1}
        )

        drugs.append({
            "name": drug["drug_name"],
            "unit_price": item["unit_price"],
            "quantity": item["quantity"],
            "total": float(item["unit_price"]) * float(item["quantity"])
        })

    return render_template(
        "slip.html",
        sale=sale,
        customer=customer,
        salesperson=salesperson,
        bank=bank,
        drugs=drugs
    )
  










@app.route('/passroot___10', methods=['POST'])
def pass___1():
    # Parse incoming raw JSON transmission requests packets strings mapping
    payload = request.get_json()
    
    invoice_id = payload.get('invoice_id')
    decision_action = payload.get('decision_action') # Contains either 'approve' or 'reject'
    
    if not invoice_id or not decision_action:
        return jsonify({"status": "error", "message": "Missing necessary payload elements."}), 400

    # Business Logic Processing Core Block
    if decision_action == 'approve':
        # Put your database execution queries here:
        # e.g., db.execute("UPDATE invoices SET status='approved' WHERE id=%s", invoice_id)
        print(f"Invoice {invoice_id} approved successfully.")
        mon=re_mogo("invoices")
        nv=2
        dbd="date2"
        mv=mon.find_one( {"invoices":invoice_id},{"stage":1,"credit_type":1})
        ###this is chake the request is come form correct sorces or not
        if(mv["credit_type"]=='credit' and 3!=float(mv["stage"])):
          print("from add min",valid_departmnet(1),"and",valid_departmnet(2))
          if(valid_departmnet(1)):
            return False
        else:
            print("form chashri",valid_departmnet(3))
            if(valid_departmnet(3)):
            
              return False
        if 3==float(mv["stage"]):
             nv=3.1
           
        mon.update_one(
                    {"invoices":invoice_id},
                    {
                        "$set": {
                            "stage": nv,
                            dbd:get_time_number()
                        }
                    }
                )
        
    elif decision_action == 'reject':
        # e.g., db.execute("UPDATE invoices SET status='rejected' WHERE id=%s", invoice_id)
        print(f"Invoice {invoice_id} rejected successfully.")
        mon=re_mogo("invoices")
        mon.delete_one({"invoices":invoice_id})

    # Return json dictionary mapping response down back cleanly to our JavaScript interface
    return jsonify({
        "status": "success",
        "processed_id": invoice_id,
        "resulting_state": decision_action
    }), 200





@app.route('/passroot___12', methods=['POST'])
def pass___2():
    # Parse incoming raw JSON transmission requests packets strings mapping
    if(valid_departmnet(2)):
            return False
    payload = request.get_json()
    
    invoice_id = payload.get('invoice_id')
    decision_action = payload.get('decision_action') # Contains either 'approve' or 'reject'
    
    if not invoice_id or not decision_action:
        return jsonify({"status": "error", "message": "Missing necessary payload elements."}), 400

    # Business Logic Processing Core Block
    if decision_action == 'approve':
        # Put your database execution queries here:
        # e.g., db.execute("UPDATE invoices SET status='approved' WHERE id=%s", invoice_id)
        print(f"Invoice {invoice_id} approved successfully.")
        mon=re_mogo("invoices")
      
        nv=3
        mv=mon.find_one({"invoices":invoice_id},{"drugs":1})
        crilance=False
        for fx in mv["drugs"]:  
          if(crilance_priorty_ex_reduction(fx["drug_id"],fx["quantity"])):
            crilance=True
            print("chake1")
            break
          
        if(crilance):
            print("what is wrong with u ")
            return jsonify({"status": "error", "message": "Stock is insufficient. Please check and approve before proceeding."}), 400
        for fx in mv["drugs"]:  
          priorty_ex_reduction(fx["drug_id"],fx["quantity"])
          mon.update_one(
                    {"invoices":invoice_id},
                    {
                        "$set": {
                            "stage": nv,
                            "date3":get_time_number()
                        }
                    }
                )
    elif decision_action == 'reject':
        # e.g., db.execute("UPDATE invoices SET status='rejected' WHERE id=%s", invoice_id)
           return jsonify({"status": "error", "message": "Missing necessary payload elements."}), 400
        

    # Return json dictionary mapping response down back cleanly to our JavaScript interface
    return jsonify({
        "status": "success",
        "processed_id": invoice_id,
        "resulting_state": decision_action
    }), 200




@app.route('/passroot___14', methods=['POST'])
def pass___3():
    # this is used to aapprove the with holed
    if(valid_departmnet(1)):
            return False
    payload = request.get_json()
    
    invoice_id = payload.get('invoice_id')
    decision_action = payload.get('decision_action') # Contains either 'approve' or 'reject'
    print("samson as distion",decision_action)
    
    if not invoice_id or not decision_action:
        return jsonify({"status": "error", "message": "Missing necessary payload elements."}), 400
    if decision_action == 'Collected':
        print(f"Invoice {invoice_id} approved successfully.")
        mon=re_mogo("invoices")
        mon.update_one(
                    {"invoices":invoice_id},
                    {
                        "$set": {
                           
                            "withcon":get_time_number()
                        }
                    }
                )
    return jsonify({
        "status": "success",
        "processed_id": invoice_id,
        "resulting_state": decision_action
    }), 200






@app.route("/passroot15", methods=["POST"])
def dispose_batch():
    if(valid_departmnet(1)):
            return False
    data = request.get_json()

    batch_id = data.get("batchId")

    print("Received batch:", batch_id)

    mon=re_mogo("drug")
    mon.update_one(
        {"_id": ObjectId(batch_id)},
        {"$set": {"disposal_date":get_time_number()}}
    )

    return jsonify({
        "success": True,
        "message": "Batch disposed"
    })



@app.route("/passroot17", methods=["POST"])
def pass___17():
    if(valid_departmnet(1)):
            return False
    data = request.get_json()

    print(data)

    staff_id = data.get("id")
    phone = data.get("phone")
  
    session = data.get("session")
  
  
    mon=re_mogo("job")
    c={"on":1,"off":0}
   
    rate = data.get("rate", "")

    if rate == "":
         mon.update_one(
        {"_id": ObjectId(staff_id)},
        {"$set": {"phone":phone,"Session":c[session]}}
    )
    else:
         mon.update_one(
        {"_id": ObjectId(staff_id)},
        {"$set": {"phone":phone,"Session":c[session],"rate":float(rate)}}
        )


    # MongoDB update here
    # collection.update_one(...)

    return jsonify({
        "success": True,
        "message": "Staff updated successfully"
    })




@app.route('/passroot19', methods=['POST'])
def pass___19():
    if(valid_departmnet(1)):
            return False
    # Capture transaction variables sent from the UI
    payload = request.get_json()
    
    agent_phone = payload.get('phone')
    start_date = payload.get('start_date')
    final_date = payload.get('final_date') # Read user's cutoff date window selection
    payout_sum = payload.get('settlement_amount')

    if not all([agent_phone, start_date, final_date]):
        return jsonify({"status": "error", "message": "Missing required date criteria."}), 400

    try:
        
        mon=re_mogo("job")
        dd=date_to_timestamp(final_date)
        print("blenas____",dd)
        mon.update_one(
        {"phone":agent_phone},
        {"$set": {"commutionp":dd}}
        )
        print(f"COMMISSION SETTLED: Agent={agent_phone}, Scope={start_date} to {final_date}, Paid={payout_sum} ETB")

        return jsonify({
            "status": "success",
            "message": "Commissions within specified date limits marked paid successfully.",
            "cutoff_synchronized": final_date
        }), 200

    except Exception as e:
        print(f"Database write exception: {str(e)}")
        return jsonify({"status": "error", "message": "Internal persistence tracking system crash."}), 500

#____________________________________therd party
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

from reportlab.lib.pagesizes import landscape, A4
from io import BytesIO
import random



@app.route("/generate_pdf", methods=["POST"])
def generate_pdf():
    from reportlab.lib import colors

    data = request.get_json()
    table_data = data["table"]
    
    table_data = [row for row in table_data if row]
    print("RAW REQUEST DATA:", data)
    buffer = BytesIO()

    page_width, page_height = landscape(A4)

    pdf = SimpleDocTemplate(
        buffer,
        pagesize=landscape(A4),
        rightMargin=20,
        leftMargin=20,
        topMargin=20,
        bottomMargin=20
    )

    # 🔥 number of columns
    col_count = len(table_data[0])

    # 🔥 distribute width evenly across page
    col_width = (page_width - 40) / col_count
    col_widths = [col_width] * col_count

    table = Table(table_data, colWidths=col_widths, repeatRows=1)

    style = TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),

        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 10),   # 🔥 bigger text

        ("ALIGN", (0, 0), (-1, -1), "CENTER"),

        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),

        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ])

    table.setStyle(style)

    pdf.build([table])

    buffer.seek(0)

    return send_file(
        buffer,
        mimetype="application/pdf",
        as_attachment=True,
        download_name="inventory_report.pdf"
    )
@app.route("/Forgot",  methods=["GET", "POST"])
def Forgot__():
      if request.method == "POST":
        phone = request.form.get("phone")
        mon=re_mogo("job")
        
        if(mon.count_documents({"phone":phone})):
            coll=re_mogo("otp")
            result = coll.insert_one({
                 "number":int(random.randint(100000, 999999)),
                 "time":get_time_number(),
                 "phone":phone
            })
            doc_id = result.inserted_id
            session["o_t_t"]=str(doc_id)
            return redirect(url_for("Forgot"))
      
        return redirect(url_for("Forgot__"))
        
      return render_template("Forgot.html")


@app.route("/password",  methods=["GET", "POST"])
def Forgot():
      if request.method == "POST":
      
       
        print(session["o_t_t"],"am found not it")
        return redirect(url_for("Forgot__"))
        
      return render_template("password.html")

@app.route('/auth/process-security-credential-update', methods=['POST'])
def process_security_credential_update():
    data = request.get_json()
    
    password = data.get('new_password', '').strip()
    otp_code = data.get('otp_token', '').strip()

   
    # (Mock condition: replacing with your actual database queries / Redis OTP verification checks)
    mon=re_mogo("otp")
    mv=mon.find_one({"_id":ObjectId(session["o_t_t"]),"number":int(otp_code)},{"time":1,"phone":1})
    is_otp_valid =True
    if mv:
        print("in the otp")
        is_otp_valid =False
        if get_time_number()-mv["time"] > 260:
            print("in the otp expired")
            is_otp_valid =True
    
    mon.delete_one({"_id":ObjectId(session["o_t_t"])})
    session.pop("o_t_t", None)
    if is_otp_valid:
        return jsonify({
            "status": "error", 
            "message": "Security token checkpoint authentication failed. The 2FA OTP code is invalid or expired."
        }), 200

    try:
      mon_=re_mogo("job")
      mon_.update_one(  {"phone":mv["phone"]},  {"$set": {     "password": password           }}      )
           
        
      return jsonify({
            "status": "success", 
            "message": "Security baseline profile updated successfully. Your new password hash is fixed."
        }), 200

    except Exception as db_error:
        print(f"Exception raised during system storage update operations: {str(db_error)}")
        return jsonify({"status": "error", "message": "Internal storage transaction failure execution error."}), 500



if __name__ == "__main__":
    pass
  