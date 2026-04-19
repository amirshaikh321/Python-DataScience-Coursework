import datetime

# ------------------ DATABASE ------------------ #
patient_db = {}

departments = {
    "Cardiology": ["Dr. Sharma", "Dr. Mehta"],
    "Orthopedic": ["Dr. Patil", "Dr. Deshmukh"],
    "General": ["Dr. Khan", "Dr. Singh"]
}

doctor_fees = {
    "Dr. Sharma": 3000,
    "Dr. Mehta": 3500,
    "Dr. Patil": 2500,
    "Dr. Deshmukh": 2800,
    "Dr. Khan": 1500,
    "Dr. Singh": 1800
}

# ------------------ FUNCTIONS ------------------ #

# Generate Patient ID
def generate_id():
    return 1001 + len(patient_db)

# Calculate bill with GST and discount
def calculate_bill(base_fee, discount):
    gst = 0.18 * base_fee
    total = base_fee + gst
    final = total - (total * discount / 100)
    return round(final, 2)

# Display departments
def show_departments():  
    for i, dept in enumerate(departments, 1):
        print(f"{i}. {dept}")

# Get department
def get_department(choice):
    return list(departments.keys())[choice - 1]

# Show doctors
def show_doctors(dept):
    for i, doc in enumerate(departments[dept], 1):
        print(f"{i}. {doc}")

# Get doctor
def get_doctor(dept, choice):
    return departments[dept][choice - 1]

# Add patient
def add_patient():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    disease = input("Enter Disease: ")

    show_departments()
    dept_choice = int(input("Select Department: "))
    dept = get_department(dept_choice)

    show_doctors(dept)
    doc_choice = int(input("Select Doctor: "))
    doctor = get_doctor(dept, doc_choice)

    base_fee = doctor_fees[doctor]
    discount = float(input("Enter Discount %: "))

    final_bill = calculate_bill(base_fee, discount)

    paid = float(input("Enter Paid Amount: "))
    remaining = final_bill - paid

    appointment = datetime.datetime.now()

    pid = generate_id()

    patient_db[pid] = {
        "name": name,
        "age": age,
        "disease": disease,
        "department": dept,
        "doctor": doctor,
        "bill": final_bill,
        "paid": paid,
        "remaining": remaining,
        "appointment": appointment.strftime("%d-%m-%Y %H:%M")
    }

    print("Patient Added Successfully")

# Display patients
def display_patients():
    for pid, data in patient_db.items():
        print(pid, data)

# Search by name
def search_by_name():
    name = input("Enter Name: ").lower()

    results = list(filter(lambda x: x[1]['name'].lower() == name, patient_db.items()))

    if results:
        for r in results:
            print(r)
    else:
        print("Not Found")

# Sort by bill
def sort_by_bill():
    sorted_data = sorted(patient_db.items(), key=lambda x: x[1]['bill'])
    for s in sorted_data:
        print(s)

# Update payment
def pay_bill():
    pid = int(input("Enter Patient ID: "))

    if pid in patient_db:
        amount = float(input("Enter amount: "))
        patient_db[pid]['paid'] += amount
        patient_db[pid]['remaining'] -= amount
        print("Payment Updated")
    else:
        print("Invalid ID")

# Delete
def delete_patient():
    pid = int(input("Enter Patient ID: "))
    if pid in patient_db:
        patient_db.pop(pid)
        print("Deleted")
    else:
        print("Not Found")

# ------------------ LOGIN ------------------ #

def login():
    username = "admin"
    password = "1234"

    for _ in range(3):
        u = input("Username: ")
        p = input("Password: ")

        if u == username and p == password:
            return True
        else:
            print("Invalid")

    return False

# ------------------ MAIN ------------------ #

if not login():
    print("Access Denied")
    exit()

while True:
    print("""
    1. Add Patient
    2. Display Patients
    3. Search by Name
    4. Sort by Bill
    5. Pay Bill
    6. Delete Patient
    7. Exit
    """)

    choice = input("Enter Choice: ")

    menu = {
        "1": add_patient,
        "2": display_patients,
        "3": search_by_name,
        "4": sort_by_bill,
        "5": pay_bill,
        "6": delete_patient
    }

    if choice in menu:
        menu[choice]()   
    elif choice == "7":
        print("Thank You!")
        break
    else:
        print("Invalid Choice")