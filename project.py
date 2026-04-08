"""
Hospital management system
"""
patients_data = {
    "101": {
        "Patient Name": "John Doe",
        "Age": 45,
        "Disease": "Hypertension",
        "Department": "Cardiology",
        "Doctor Assigned": "Dr. Smith"
    },
    "102": {
        "Patient Name": "Emily Johnson",
        "Age": 32,
        "Disease": "Diabetes",
        "Department": "Endocrinology",
        "Doctor Assigned": "Dr. Brown"
    },
    "103": {
        "Patient Name": "Michael Lee",
        "Age": 60,
        "Disease": "Asthma",
        "Department": "Pulmonology",
        "Doctor Assigned": "Dr. Wilson"
    },
    "104": {
        "Patient Name": "Sophia Patel",
        "Age": 27,
        "Disease": "Migraine",
        "Department": "Neurology",
        "Doctor Assigned": "Dr. Taylor"
    },
    "105": {
        "Patient Name": "David Kumar",
        "Age": 50,
        "Disease": "Arthritis",
        "Department": "Orthopedics",
        "Doctor Assigned": "Dr. Anderson"
    }
}

department_data = {
    'Orthopedics':['Dr. Anderson'],
    'Neurology':['Dr. Taylor'],
    'Pulmonology':['Dr. Wilson'],
    'Endocrinology':['Dr. Brown'],
    'Cardiology':['Dr. Smith']
}
doctor_fees = {
    'Dr. Anderson':500,
    'Dr. Taylor':450,
    'Dr. Wilson':700,
    'Dr. Brown':600,
    'Dr. Smith':300
}

def generate_id():
    pid = 101+len(patients_data)
    return pid

def add_patient():
    name = input("Name: ")
    age = int(input('Age of patient: '))
    disease = input('disease of patient: ')
    department = input('department: ')

    pid = generate_id()
    patients_data[pid] = {}
    patients_data[pid]['Patient Name']=name
    patients_data[pid]['Age']=age
    patients_data[pid]['Disease']= disease
    patients_data[pid]['Department']=department

    print("Doctors Available:")
    i=1
    for doctor in department_data[department]:
        print(f"{i}. {doctor}")
        i+=1
    doctors = department_data[department]
    ch = int(input("Select doctor: "))
    patients_data[pid]['Doctor Assigned']= doctors[ch-1]
    print("Patient add Sucessfuly")

def display_patient():
    for pid, details in patients_data.items():
        print(f"{pid} : {details}")

def update_patient():
    pid = input("Patient ID: ")
    print("""
    1. Name
    2. Age
    3. Disease
    4. Department
    5. Doctor
""")

    ch = int(input("What you want to update: "))
    if ch ==1:
        name = input("Patient Name: ")
        patients_data[pid]['Patient Name']= name
        print("Patient details updated")
    elif ch == 2:
        age = int(input("Age: "))
        patients_data[pid]['Age'] = age
        print("Patient details updated")
    elif ch == 3:
        Disease = input('Disease: ')
        patients_data[pid]['Disease'] = Disease
        print("Patient details updated")
    elif ch == 4:
        department = input("Department: ")
        patients_data[pid]['Department']= department
        print("Patient details updated")
    elif ch == 5:
        department =patients_data[pid]['Department']
        print("Doctors Available:")
        i=1
        for doctor in department_data[department]:
            print(f"{i}. {doctor}")
            i+=1
        doctors = department_data[department]
        ch = int(input("Select doctor: "))
        patients_data[pid]['Doctor Assigned']= doctors[ch-1]
        print("Patient details updated")

def pay_bill():
    pid = input("Enter patient id: ")
    # for id, details in patients_data.items():
    #     if pid == id:
    doctor = patients_data[pid]['Doctor Assigned']
    bill= doctor_fees[doctor]
    print(f"Bill amount: {bill}")
    d = input("Do you want to pay bill (y/n): ")
    if d.lower() == 'y':
        print("Bill Paid")
    else:
        print("bill not paid")

def search():
    name = input("Search name: ")
    for id , details in patients_data.items():
        if details['Patient Name']==name:
            print(f"\n{id} : {details}")

def delete_patient():
    pid = input("Patient ID to delete patient record: ")
    del patients_data[pid]
    print("Patient Data Deleted Successfuly.")

while True:

    print("""
        1. Add Patient details
        2. Display patient details
        3. Update patient deatails
        4. Pay bill
        5. Search patient by name
        6. Delete patient
        7. Exit 
""")
    ch = int(input("Enter your choice: "))
    choices = {1: add_patient,
               2: display_patient,
               3: update_patient,
               4: pay_bill,
               5: search,
               6: delete_patient}
    if ch in choices:
        choices[ch]()
    elif ch == 7:
        break
    else:
        print('Invalid Input')