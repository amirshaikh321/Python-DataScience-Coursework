def show_numbers(*args):
    for num in args:
        print(num)
show_numbers(10,20,30,40,50)

def show_name(*names):
    for name in names:
        print(name)
show_name("kiran","swaraj","karishma")


def show_details(**kwargs):
    print("Keyword arguments:")
    for key, value in kwargs.items():
        print(key, "=", value)
show_details(name="Rahul", age=21, city="Pune")