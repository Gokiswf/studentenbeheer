from tkinter import *
from tkinter import ttk,messagebox
import CRUD 
import re
import json
import requests

url= "https://raw.githubusercontent.com/Gokiswf/studentenbeheer/refs/heads/main/students.json"

response = requests.get(url)
def toongeg(*event):

        for item in mijn_tree.get_children():
            mijn_tree.delete(item)
        for lijn in matrix:
            mijn_tree.insert(parent="",index="end",values=lijn)
            
if response.status_code == 200:
    data = response.json()
    leesbare_json = json.dumps(data,indent=4)
    matrix = []
    for product in data:
        matrix.append([product['id'],product['name'],product['age'],product['email'],product['course']])
def herladen():
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        leesbare_json = json.dumps(data,indent=4)
        matrix = []
        for product in data:
            matrix.append([product['id'],product['name'],product['age'],product['email'],product['course']])
    for item in mijn_tree.get_children():
            mijn_tree.delete(item)
    for lijn in matrix:
            mijn_tree.insert(parent="",index="end",values=lijn)
def sluiten():
    root.destroy()

root=Tk()
root.geometry('600x360')
root.title('Studentbeheer')
root.bind("<Map>",toongeg)

mijn_tree=ttk.Treeview(root)
mijn_tree['columns']=('id','naam','leeftijd','email','opleiding')

mijn_tree.heading("id", text = "ID", anchor = W)
mijn_tree.heading("naam", text = "Naam", anchor = W)
mijn_tree.heading("leeftijd", text = "Leeftijd", anchor = W)
mijn_tree.heading("email", text = "E-mail", anchor = W)
mijn_tree.heading("opleiding", text = "Opleiding", anchor = W)

mijn_tree.column("#0", width=0, stretch = NO)
mijn_tree.column("id",width = 50, anchor = W)
mijn_tree.column("naam",width = 150, anchor = W)
mijn_tree.column("leeftijd",width = 50, anchor = W)
mijn_tree.column("email",width = 200, anchor = W)
mijn_tree.column("opleiding",width = 100, anchor = W)


herladen_button=Button(root,text='Herladen',command=herladen)
sluiten_button=Button(root,text='Sluiten',command=sluiten)

mijn_tree.pack(ipady=40,pady=5)

herladen_button.place(x=25,y=322)
sluiten_button.place(x=530,y=322)
mijn_tree.bind('<')

root.mainloop()