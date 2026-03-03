def format_number(num, rep):
    return format(num, rep)
formatted_result = format_number(145, 'o')
print("1. Formatted Result:", formatted_result)
print("Representation Used: Octal\n")
radius = 84
pi = 3.14
area = pi * (radius ** 2)
water_per_sqm = 1.4
total_water = area * water_per_sqm
print("2. Total water in the pond (liters):", int(total_water))
distance = 490 
time_minutes = 7
time_seconds = time_minutes * 60
speed = distance / time_seconds
print("3. Speed (m/s):", int(speed))
