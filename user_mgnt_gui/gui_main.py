from tkinter import *
from tkinter import messagebox
import pandas as pd
import os

#checking whether user file exist or not
if not os.path.exists("user.csv"):
    #creating csv file
    data = pd.DataFrame(columns=['unique_id','name','address','designation'])
    data.to_csv("user.csv",index = False)

#clearing data after entering in the field
def clear_data():
    unique_id1.delete(0,END)
    name1.delete(0,END)
    add.delete(0,END)
    desig.delete(0,END)
    searching.delete(0,END)
    
# Add user function
def add_user():
    name = name1.get()
    address = add.get()
    designation = desig.get()

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
    messagebox.showinfo(title = 'success',message="data entered successfully")
    clear_data()
    
    
#update function
def update_user():
    data = pd.read_csv("user.csv")
    unique_id = int(unique_id1.get())

    if unique_id not in data["unique_id"].values:
        messagebox.showerror(message="User not found")
        return
    user_index = data[data["unique_id"]== unique_id].index[0]
    # print(user_index)
    # messagebox.showinfo(message=f"Current details : Name {data.at[user_index,'name']} \n Address :{data.at[user_index,'address']} \n Designation : {data.at[user_index,'designation']}/n update the required field")
    name = name1.get()
    address = add.get() 
    designation = desig.get()

    if name:
        data.at[user_index, "name"] = name
    if address:
        data.at[user_index, "address"] = address
    if designation:
        data.at[user_index, "designation"] = designation

    data.to_csv("user.csv", index=False)
    messagebox.showinfo(message="User updated successfully")
    clear_data()


#view user function
def view_user_details():
    data = pd.read_csv("user.csv")
    unique_id = int(unique_id1.get())

    if unique_id not in data["unique_id"].values:
        details_text.delete(1.0,END)
        details_text.insert(END,"User not found")
        return
    else:
        user_details = data[data["unique_id"]== unique_id]
        user_details_string=user_details.to_string(index = False)
        
        details_text.delete(1.0,END)
        details_text.insert(END,user_details_string)
        clear_data()

#list all user function
def list_all_user():
    data = pd.read_csv("user.csv")
    details = data.to_string(index = False)
    
    details_text.delete(1.0,END)
    details_text.insert(END,details)

#deleting user
def delete_user():
    data = pd.read_csv("user.csv")
    unique_id = int(unique_id1.get())
    if unique_id not in data["unique_id"].values:
        messagebox.showerror(message="User not found")
    else:    
        user = data[data['unique_id']!=unique_id]
        user.to_csv("user.csv",index = False)
        messagebox.showinfo(message="User deleted successfully ")
        clear_data()

#search function 
def search_user():
    
    data = pd.read_csv("user.csv")

    search = searching.get().lower()

    matching_data = pd.DataFrame()

    
    for column in data.columns:
        
        if column != "unique_id":  
            
            search_value = data[data[column].str.contains(search,case=False)]
            
            matching_data = pd.concat([matching_data, search_value])

    # Display results or notify the user if no matches found
    if matching_data.empty:
        messagebox.showerror(message="No matches found!")
    else:
        search_string = matching_data.to_string(index=False)
        details_text.delete(1.0,END)
        details_text.insert(END,search_string)
        clear_data()


#creating window 
window = Tk()
window.title("User management system")
window.config(padx = 20,pady = 20)



#creating labels 
title_1 = Label(text="USER MANAGEMENT SYSTEM",font=('arial',20,'bold'))
title_1.grid(column=0,row=0,columnspan=2)

unique_id = Label(text='unique_id:',font=('arial',10,'bold'))
unique_id.grid(row=1,column =0)
name = Label(text='Name:',font=('arial',10,'bold'))
name.grid(row=2,column =0)
address = Label(text='Address:',font=('arial',10,'bold'))
address.grid(row=3,column =0)
designation = Label(text='Designation:',font=('arial',10,'bold'))
designation.grid(row=4,column =0)

#creating entries
unique_id1 = Entry(width=35)
unique_id1.grid(row=1,column=1)

name1 = Entry(width=35)
name1.grid(row=2,column=1)

add = Entry(width=35)
add.grid(row=3,column=1)

desig = Entry(width=35)
desig.grid(row=4,column=1)

searching = Entry(width=40)
searching.grid(row=9,column=0,padx=20,pady=20)



#creating buttons
adduser = Button(text='Add ',width=15,command=add_user)
adduser.grid(row=6,column=0,padx=20,pady=20)

updateuser = Button(text='Update ',width=15,command=update_user)
updateuser.grid(row=6,column=1,padx=20,pady=20)

listall = Button(text='List All ',width=15,command=list_all_user)
listall.grid(row=7,column=0,padx=20,pady=20)

viewuser = Button(text='View user ',width=15,command=view_user_details)
viewuser.grid(row=7,column=1,padx=20,pady=20)

delete = Button(text='Delete ',width=15,command=delete_user)
delete.grid(row=8,column=0,columnspan=2,padx=20,pady=20)

search = Button(text='Search',width=15,command=search_user)
search.grid(row=9,column=1,padx=20,pady=20)

#text box
details_text = Text(window, width=50, height=10, wrap=WORD)
details_text.grid(row=10, column=0, columnspan=2, pady=10)




















window.mainloop()
