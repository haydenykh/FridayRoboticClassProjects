import pwinput
import json

user_data_file = open("data_pw.json")
user_data = json.load(user_data_file)

id = pwinput.pwinput("Insert account registered name: ")

for i in user_data:
    if i.get("user") == id:
        print("Hi,", i.get("user"), "!")
        print("This is your balance:", i.get("balance"))
        break
    # else:
    #     print("This account is not found.\nPlease rerun this file again.")
    #     break

user_data_file.close()