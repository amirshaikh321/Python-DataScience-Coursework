"""
Types of arguments : 
1. Positional arguments
2. Keyword arguments
3. Default arguments
4. Arbitary arguments
    1. Positional arbitory arguments
    2. Keword arbitory arguments


    1.
    An argument is a variable, value or object passed to a function or method as input. Positional arguments are arguments that need to be included in the proper position or order. The first positional argument always needs to be listed first when the function is called.
    2.
    Keyword arguments (or named arguments) are values that, when passed into a function, are identifiable by specific parameter names. A keyword argument is preceded by a parameter and the assignment operator, = . Keyword arguments can be likened to dictionaries in that they map a value to a keyword.1
    3.
    In Python, default arguments allow you to assign a default value to a parameter in a function definition. This means that the default value is used instead if the function is called without a value for that parameter.
    4.
    You may want to define a function that is able to accept arbitrary or variable number of arguments. Moreover, the arbitrary number of arguments might be positional or keyword arguments. An argument prefixed with a single asterisk * for arbitrary positional arguments.
"""

def details(name,course,institute):
    print(f"""
            Name          :{name}
            course        :{course}
            institute     :{institute}          
""")

details('amir','Data science','The kiran academy') # positional args
details(name='john',course='java',institute='The kiran academy') # Keyword args

def details(name,course,institute='Java by kiran'):
    print(f"""
            Name          :{name}
            course        :{course}
            institute     :{institute}          
""")
details(name='sham',course='DevOps') # default args