from datetime import datetime

birthday = datetime(1995, 10, 26)
age = datetime.now().year - birthday.year - ((datetime.now().month, datetime.now().day) < (birthday.month, birthday.day))
print("Your age is:", age)


