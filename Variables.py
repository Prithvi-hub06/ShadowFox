pi = 22 / 7
print("Value of pi:", pi)
print("Data type of pi:\n", type(pi))   
print("Trying to create a variable named 'for'...")
try:
    exec("for = 4")
except SyntaxError as e:
    print("Error:", e)
    print("'for' is a reserved keyword in Python and cannot be used as a variable name.")
for_value = 4
print("Correct variable name example: for_value =\n", for_value)
principal = 10000      
rate = 5              
time = 3               
simple_interest = (principal * rate * time) / 100
print("Principal:", principal)
print("Rate of Interest:", rate)
print("Time (years):", time)
print("Simple Interest for 3 years:", simple_interest)