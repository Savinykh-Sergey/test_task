from datetime import datetime

datetime = datetime.strptime(datetime.now().strftime("%d-%m-%Y %H:%M:%S"), "%d-%m-%Y %H:%M:%S")
print(type(datetime))