# This is basic
print("Hello World!")

# You can use functions as objects in Python!

def printer_function(st):
    print("This string is being printed from original function - ",st)

printer_function("Hello World!")

my_obj=printer_function

my_obj("Hello World!")