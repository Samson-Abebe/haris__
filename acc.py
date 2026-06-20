job_={
    1:"Super Admin",
    2:"Store Manager",
    3:"Cashier",
    4:"sales(Staff)",
    5:"sales(agent)"
}
notf={
    "Collect":1,
    "Expired bellow 90d":1,
    "Approve Credit":1,
    "Otp":1,
    "Issues":1,
    "Rececivng Cash,Rececivng Credit":1
}
drug_categories = {
    "1": "Central Nervous System (CNS)",
    "2": "Anti-Infectives",
    "3": "Gastrointestinal System",
    "4": "Dermatologic",
    "5": "Cardiovascular System",
    "6": "Analgesics & Anti-Inflammatory",
    "7": "Endocrine System",
    "8": "Genitourinary System",
    "9": "Ophthalmic",
    "10": "Respiratory System",
    "11": "Hematologic System",
    "12": "Immunological & Vaccines"
}
Super_Admin={
    "Dashboard":{
        "submenu":["Stocks","Staff","Edit","Customer","Exhausted batch","Add Staf"],
        "icon":"fa-solid fa-gauge-high menu-icon-default",
        "noofn":False },
    
    "Bank":{
        "submenu":["Add Bank"],
        "icon":"fa-solid fa-building-columns menu-icon-default",
        "noofn":False},
    "Withholding":{   
        "submenu":["Collect","Total"],
        "icon":"fa-solid fa-file-invoice-dollar menu-icon-default",
        "noofn":False},
    "Expired":{
        "submenu":["Expired bellow 90d","Disposed"],
        "icon":"fa-solid fa-calendar-xmark menu-icon-default",
        "noofn":False},
    "Commution":{
        "submenu":["Total commution","Pay"],
        "icon":"fa-solid fa-coins menu-icon-default",
        "noofn":False },
    "Credit":{
        "submenu":["Approve Credit"],
        "icon":"fa-solid fa-circle-check menu-icon-default",
        "noofn":False},
    # "Expense":{
    #     "submenu":["Approve Expense","Expense Report"],
    #     "icon":"fa-solid fa-money-bill-wave menu-icon-default",
    #     "noofn":5},
    "Otp":{
        "submenu":["Otp"],
        "icon":"fa-solid fa-money-bill-wave menu-icon-default",
        "noofn":False}
 
}



Store_Manager={
    "Product":{
        "submenu":["Add Product","Rececivng Product","Issues","Stocks","Exhausted batch","Edit prices"],
        "icon":"fa-solid fa-box menu-icon-default",
        "noofn":False},
    "Expired":{
        "submenu":["Expired bellow 90d","Disposed"],
        "icon":"fa-solid fa-calendar-xmark menu-icon-default",
        "noofn":50},
    "Report":{
        "submenu":["Report Issues"],
        "icon":"fa-solid fa-file-lines menu-icon-default",
        "noofn":False},
}



cashier={
    "Sales":{
        "submenu":["Rececivng Cash","Rececivng Credit"],
        "icon":"fa-solid fa-cart-shopping",
        "noofn":False},
   "Expense":{
        "submenu":["Expense"],
        "icon":"fa-solid fa-money-bill-wave menu-icon-default",
        "noofn":False},
    "Petty Cash":{
        "submenu":["Deposit Petty Cash"],
        "icon":"fa-solid fa-money-bill",
        "noofn":False},
    "Report":{
        "submenu":["Rececivng Report","Expense Report"],
        "icon":"fa-solid fa-file-lines menu-icon-default",
        "noofn":False},

}
sales_={
    "Sales":{
        "submenu":["Sales"],
        "icon":"fa-solid fa-cart-shopping",
        "noofn":False},
    "Customer":{
        "submenu":["Add Customer" ],
        "icon":"fa-solid fa-user-plus",
        "noofn":False},
    "Report":{
        "submenu":["Report Sales"],
        "icon":"fa-solid fa-file-lines menu-icon-default",
        "noofn":False},

}

# 100 Attractive Hex Colors (No White Colors)

colors = [
    "#FF6B6B", "#4ECDC4", "#45B7D1", "#F7B801", "#5F27CD",
    "#EE5253", "#10AC84", "#2E86DE", "#FF9F43", "#341F97",
    "#E17055", "#00B894", "#0984E3", "#FDCB6E", "#6C5CE7",
    "#D63031", "#00CEC9", "#74B9FF", "#E84393", "#A29BFE",
    "#C0392B", "#16A085", "#2980B9", "#F39C12", "#8E44AD",
    "#E74C3C", "#1ABC9C", "#3498DB", "#F1C40F", "#9B59B6",
    "#2ECC71", "#34495E", "#E67E22", "#27AE60", "#D35400",
    "#7F8C8D", "#95A5A6", "#8E44AD", "#2C3E50", "#C0392B",
    "#FF7675", "#55EFC4", "#74B9FF", "#FFEAA7", "#A29BFE",
    "#FD79A8", "#00CEC9", "#6C5CE7", "#FAB1A0", "#81ECEC",
    "#E55039", "#4A69BD", "#78E08F", "#FA983A", "#B71540",
    "#60A3BC", "#82CCDD", "#F8C291", "#6A89CC", "#38ADA9",
    "#B33771", "#3B3B98", "#182C61", "#FC427B", "#BDC581",
    "#82589F", "#F97F51", "#1B9CFC", "#55E6C1", "#CAD3C8",
    "#F19066", "#786FA6", "#574B90", "#F8A5C2", "#63CDD7",
    "#EA2027", "#006266", "#1B1464", "#5758BB", "#ED4C67",
    "#F79F1F", "#A3CB38", "#1289A7", "#D980FA", "#B53471",
    "#833471", "#12CBC4", "#FDA7DF", "#EDC988", "#9980FA",
    "#8338EC", "#3A86FF", "#FF006E", "#FB5607", "#FFBE0B",
    "#264653", "#2A9D8F", "#E9C46A", "#F4A261", "#E76F51"
]

# Print all colors



tamps = [
    1764802205,
    1765129981,
    1765458120,
    1765894310,
    1766021107,
    1766349055,
    1766687402,
    1767015599,
    1767341204,
    1767669801,
    1767994506,
    1768323000,
    1768651908,
    1768980403,
    1769309209,
    1769637705,
    1769966102,
    1770294800,
    1770623307,
    1770952001
]



























# account_type_name={
#   "Name":{
#     "icon":"the clas name",
#     "submenu":["list1","list2","list3","list4"],
     
#   }


# }