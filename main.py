import pandas as pd
import os

#checking whether csv already exist
if not os.path.exists("user.csv"):
    #creating csv file
    data = pd.DataFrame(columns=['unique_id','name','address','designation'])
    data.to_csv("user.csv",index = False)

else:
    print("User file already exist")    

def add_user():
    name = input("Enter your name :")
    address = input("Enter your address:")
    designation = input("Enter designation:")
    data = pd.read_csv("user.csv")

    #auto increment the unique id
    if not data.empty:
        initial_id = data["unique_id"].max()
    else:
        initial_id = 0
    unique_id = initial_id + 1

    #append data into csv file
    user_data = pd.DataFrame([{"unique_id":unique_id,"name":name,"address":address,"designation":designation}])
    data = pd.concat([data,user_data] )
    data.to_csv("user.csv",index = False)
    print("data entered successfully")

def update_user():
    data = pd.read_csv("user.csv")
    unique_id = int(input("Enter the unique id : "))

    if unique_id not in data["unique_id"].values:
        print("User not found")
        return
    user_index = data[data["unique_id"]== unique_id].index[0]
    print(user_index)
    print(f"Current details : Name {data.at[user_index,'name']} \n Address :{data.at[user_index,'address']} \n Designation : {data.at[user_index,'designation']}")
    name = input("Enter new name or skip : ")
    address = input("Enter new address or skip :") 
    designation = input("Enter new designation or skip :")

    if name:
        data.at[user_index, "name"] = name
    if address:
        data.at[user_index, "address"] = address
    if designation:
        data.at[user_index, "designation"] = designation

    data.to_csv("user.csv", index=False)
    print("User updated successfully")

def view_user_details():
    data = pd.read_csv("user.csv")
    unique_id = int(input("Enter the unique id : "))

    if unique_id not in data["unique_id"].values:
        print("User not found")
        return
    user_details = data[data["unique_id"]== unique_id]
    print(user_details.to_string(index = False))    
    
def list_all_user():
    data = pd.read_csv("user.csv")
    print(data.to_string(index = False))
    
def delete_user():
    data = pd.read_csv("user.csv")
    unique_id = int(input("Enter ur id : "))
    if unique_id not in data:
        print("User not found")

    user = data[data['unique_id']!=unique_id]
    user.to_csv("user.csv",index = False)
    print("User deleted successfully")

def search_user():
    data = pd.read_csv("user.csv")
    search_field = input("Enter 'unique id', 'name' , 'address','designation','any' : ").lower()
    search = input("Enter the Value to be searched : ").lower()

    if search_field == 'any':
        column_name = ['name','address','designation']
        matching_data = []
        for _,row in data.iterrows():
            for column in column_name:
                if row[column].startswith(search):
                    matching_data.append(row)
        list_of_data = pd.DataFrame(matching_data)
    else:
        list_of_data = data[data[search_field].str.contains(search)]

    if list_of_data.empty:
        print("Not found")
    else:
        print(list_of_data.to_string(index = False))    
    
    
def main():
    while True:
        print("******** User Information Management System **********")
        print("1. Add User\n 2. Update User \n 3. View User Details \n 4. List All Users \n 5. Delete User\n 6. Search User \n 7. Exit ")
        
        choice = int(input("Enter ur choice:"))

        match choice:
            case 1:
                add_user()
            case 2:
                update_user()
            case 3:
                view_user_details()
            case 4:
                list_all_user()
            case 5:
                delete_user()
            case 6:
                search_user()
            case 7:
                exit()
                



main()