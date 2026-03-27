"""
Dictionary:

dict is a comma seperated key and value pairs within {}
sytax:
    var = {k1:v1, k2:v2}
"""

dict = {"name": "Amir", "age": 21, "marks": 7.5, "city": "wai"}
print(dict['name'])
print(dict)

course_details = {"course_name": "python with data science",
                  "batch": 1323,
                  "duration": "6 months",
                  "fees" : 0}

print(course_details)
marks =  {1:78,2:89,3:67,1:97}
print(marks)

fees = {"data science":45000,"web development": 30000,"devops":25000}
print(fees)
oops= {5.1: "introduction of python", 5.2: "class and object", 5.3: "pillars of oop"}
print(oops)

print("\nStudent details:")
print("**"*50)
details = {
    'name': 'pavan',
    'roll no': 34,
    'wt': 52.6,
    'lang': ['python','java','aws'],
    'per': 78,
    'marks':{'t1':56,'t2':89}
}
print(details)
print(details['lang'][1])
print("\nStates and capitals:")
print("**"*50)
states = {'maharashtra':'mumbai',
          'rajasthan':'jaipur',
          'madhay pradesh': 'bhopal0',
          'bihar':'patna',
          'gujrat':'gandhinagar'}
print(states)
print("\nCoding Language and founder:")
print("**"*50)
lang = {"Python":"Guido van Rossum",
        "c": "Dennis Ritchie",
        "C++":"Bjarne Stroustrup",
        "java":"James Gosling"}
print(lang)

print("\nDistrict & sub-district:")
print("**"*50)
district = {
    "Satara":["Satara","karad","Wai","Khandala","Mahabaleshwar","Phaltan","Koregaon"],
    "Pune":["Mulshi","Maval","Khed","Ambegaon","shirur"]
}
print(district)


print("\nMobile:")
print("**"*50)
mobile = {
    'model':'Vivo Y31',
    'Price': [15000,16500],
    'Ram': [6,8],
    'storage':[64,128]
}
print(mobile)

employee = {'name': "Amir",
            "salary": 5000}


java_by_kiran = {'dep': {'operation':{'name':['amir','sham','ram']},
                         'sale':['kunal','anand'],
                         'faculty':  ['vaibhav']}}

print(java_by_kiran)

"""
single std
batch std
multiple batch - batch_name -std
course - multiple batch - batch_name -std
"""