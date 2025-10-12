import datetime
def distance_time(distance, speed):
    time = distance / speed
    return time
def convert(n):
    return str(datetime.timedelta(seconds = n*3600))
cal = input("Enter number for place: \n 1.PP to SR 314km \n 2.PP to KPC 91km \n")
if cal == '1':
    distance = 314
elif cal == '2':
    distance = 91
else:
    print("Invalid selection.")
    exit()

speed = int(input("Enter speed in km/h: "))
time = distance_time(distance, speed)
print(f"Time taken to travel from PP to destination is: {convert(time)}")
