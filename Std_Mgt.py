import tkinter as tk
from tkinter import ttk
import pymysql
from tkinter import messagebox

win=tk.Tk()
win.geometry("1350x400+0+0")
win.title("Student Management System")
win.config(bg="blue")

title_label=tk.Label(win,text="Student Management System",font=("Arial",30,"bold"),border=12,relief=tk.GROOVE,bg="darkblue",foreground="yellow")
title_label.pack(side=tk.TOP,fill=tk.X)

detail_frame=tk.LabelFrame(win,text="Student Details",font=("Arial",22,"bold"),bg="Darkblue",fg="lightblue",bd=12,relief=tk.GROOVE)
detail_frame.place(x=20,y=90,width=420,height=590)

data_frame=tk.Frame(win,bd=12,bg="darkblue",relief=tk.GROOVE)
data_frame.place(x=475,y=100,width=1000,height=590)

#==========variable==========
rollno=tk.StringVar()
name=tk.StringVar()
class_var=tk.StringVar()
section=tk.StringVar()
contact=tk.StringVar()
city=tk.StringVar()
gender=tk.StringVar()
dob=tk.StringVar()

search_by=tk.StringVar()

#============================

#====entry=====

rollno_lbl=tk.Label(detail_frame,text="Roll No",font=("Arial",17),bg="darkblue", foreground="white")
rollno_lbl.grid(row=0,column=0,padx=2,pady=2)

rollno_ent=tk.Entry(detail_frame,bd=7,font=("Arial",17),textvariable=rollno)
rollno_ent.grid(row=0,column=1,padx=2,pady=2)

name_lbl=tk.Label(detail_frame,text="Name",font=("Arial",17),bg="darkblue", foreground="white")
name_lbl.grid(row=1,column=0,padx=2,pady=2)

name_ent=tk.Entry(detail_frame,bd=7,font=("Arial",17),textvariable=name)
name_ent.grid(row=1,column=1,padx=2,pady=2)

class_lbl=tk.Label(detail_frame,text="Class",font=("Arial",17),bg="darkblue", foreground="white")
class_lbl.grid(row=2,column=0,padx=2,pady=2)

class_ent=tk.Entry(detail_frame,bd=7,font=("Arial",17),textvariable=class_var)
class_ent.grid(row=2,column=1,padx=2,pady=2)

section_lbl=tk.Label(detail_frame,text="Section",font=("Arial",17),bg="darkblue", foreground="white")
section_lbl.grid(row=3,column=0,padx=2,pady=2)

section_ent=tk.Entry(detail_frame,bd=7,font=("Arial",17),textvariable=section)
section_ent.grid(row=3,column=1,padx=2,pady=2)

contact_lbl=tk.Label(detail_frame,text="Contact",font=("Arial",17),bg="darkblue", foreground="white")
contact_lbl.grid(row=4,column=0,padx=2,pady=2)

contact_ent=tk.Entry(detail_frame,bd=7,font=("Arial",17),textvariable=contact)
contact_ent.grid(row=4,column=1,padx=2,pady=2)

city_lbl=tk.Label(detail_frame,text="City",font=("Arial",17),bg="darkblue", foreground="white")
city_lbl.grid(row=5,column=0,padx=2,pady=2)

city_ent=tk.Entry(detail_frame,bd=7,font=("Arial",17),textvariable=city)
city_ent.grid(row=5,column=1,padx=2,pady=2)

gender_lbl=tk.Label(detail_frame,text="Gender",font=("Arial",17),bg="darkblue", foreground="white")
gender_lbl.grid(row=6,column=0,padx=2,pady=2)

gender_ent=ttk.Combobox(detail_frame,font=("Arial",17),state="readonly",textvariable=gender)
gender_ent['values']=("Male","Female","Other")
gender_ent.grid(row=6,column=1,padx=2,pady=2)

dob_lbl=tk.Label(detail_frame,text="D.O.B",font=("Arial",17),bg="darkblue", foreground="white")
dob_lbl.grid(row=7,column=0,padx=2,pady=2)

dob_ent=tk.Entry(detail_frame,bd=7,font=("Arial",17),textvariable=dob)
dob_ent.grid(row=7,column=1,padx=2,pady=2)


#==============
#==============function============
def fetch_data():
    conn=pymysql.connect(host="localhost",user="root",password="",database="studentmgt_system")
    curr=conn.cursor()
    curr.execute("SELECT * FROM students")
    rows=curr.fetchall()
    search_in['values']=[row[0] for row in rows]
    if len(rows)!=0:
        student_table.delete(* student_table.get_children())
        for row in rows:
            student_table.insert('',tk.END,values=row)
        conn.commit()
    conn.close()        
    
def add_func():
    if rollno.get()=="" or name.get()== "" or class_var.get()=="":
        messagebox.showerror("Error!","Please fill the feild")
    else:
        conn=pymysql.connect(host="localhost",user="root",password="",database="studentmgt_system")
        curr=conn.cursor()
        curr.execute("INSERT INTO students VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (rollno.get(), name.get(), class_var.get(), section.get(), contact.get(), city.get(), gender.get(), dob.get()))
        conn.commit()
        conn.close()
        
        fetch_data()
        
def get_cursor(event):
    cursor_row=student_table.focus()
    content=student_table.item(cursor_row)
    row=content['values']
    rollno.set(row[0])
    name.set(row[1])
    class_var.set(row[2])
    section.set(row[3])
    contact.set(row[4])
    city.set(row[5])
    gender.set(row[6])
    dob.set(row[7])
        
    
def clear():
    rollno.set("")
    name.set("")
    class_var.set("")
    section.set("")
    contact.set("")
    city.set("")
    gender.set("")
    dob.set("")
    

def update_func():
   conn=pymysql.connect(host="localhost",user="root",password="",database="studentmgt_system") 
   curr=conn.cursor()  
   #update_query = ("UPDATE students ""SET Name=%s, Class=%s, Section=%s, Contact=%d, City=%s, Gender=%s, DOB=%s " "WHERE Roll No=%s")
   update_query = ("UPDATE students SET Name=%s, Class=%s, Section=%s, Contact=%s, City=%s, Gender=%s, DOB=%s WHERE `Roll No`=%s")

   curr.execute(update_query, (name.get(), class_var.get(), section.get(), contact.get(), city.get(), gender.get(), dob.get(),rollno.get()))
   conn.commit()
   conn.close()
   fetch_data()
   clear()
   
        
def delete_func():
    selected_item = student_table.selection()
    conn = pymysql.connect(host="localhost", user="root", password="", database="studentmgt_system")
    curr = conn.cursor()        
    rollno_value = student_table.item(selected_item, 'values')[0]
    
    # Use a generic parameterized DELETE query
    delete_query = "DELETE FROM students WHERE `Roll No`=%s"
    curr.execute(delete_query, (rollno_value,))
    
    conn.commit()
    fetch_data()
    conn.close()

    
def search_func():
    search_id = search_in.get()
    conn = pymysql.connect(host="localhost", user="root", password="", database="studentmgt_system")
    curr = conn.cursor()
    curr.execute("SELECT * FROM students WHERE `Roll No` = %s", search_id)
    rows = curr.fetchall()
    if len(rows) != 0:
        student_table.delete(*student_table.get_children())
        for row in rows:
            student_table.insert('', tk.END, values=row)
        conn.commit()
    else:
        messagebox.showinfo("No Results", "No matching record found.")
    conn.close()
    
def show_all_func():
    fetch_data()    
    
#==================================

#============button frame==============

btn_frame=tk.Frame(detail_frame,bg="lightblue",bd=10,relief=tk.GROOVE)
btn_frame.place(x=20,y=390,width=360,height=130)

add_btn = tk.Button(btn_frame, bg="lightblue", text="Add", bd=7, font=("Arial", 14,"bold"), width=12, command=add_func)
add_btn.grid(row=0,column=0,padx=2,pady=2)

update_btn=tk.Button(btn_frame,bg="lightblue",text="Update",bd=7,font=("Arial",14,"bold"),width=12,command=update_func)
update_btn.grid(row=0,column=1,padx=3,pady=2)

delete_btn=tk.Button(btn_frame,bg="lightblue",text="Delete",bd=7,font=("Arial",14,"bold"),width=12,command=delete_func)
delete_btn.grid(row=1,column=0,padx=2,pady=2)

clear_btn=tk.Button(btn_frame,bg="lightblue",text="Clear",bd=7,font=("Arial",14,"bold"),width=12,command=clear)
clear_btn.grid(row=1,column=1,padx=3,pady=2)
#======================================

#==========search=============
search_frame=tk.Frame(data_frame,bg="darkblue",bd=10,relief=tk.GROOVE)
search_frame.pack(side=tk.TOP,fill=tk.X)

search_lbl=tk.Label(search_frame,text="Search Roll No",bg="darkblue",font=("Arial",15),foreground="white")
search_lbl.grid(row=0,column=0,padx=12,pady=2)

search_in=ttk.Combobox(search_frame,font=("Arial",15),state="readonly",values=[rollno.get()])
search_in.grid(row=0,column=1,padx=12,pady=2)

search_btn=tk.Button(search_frame,text="Search",font=("Arial",14,"bold"),bd=9,width=14,bg="lightblue",command=search_func)
search_btn.grid(row=0,column=2,padx=12,pady=2)

showall_btn=tk.Button(search_frame,text="Show",font=("Arial",14,"bold"),bd=9,width=14,bg="lightblue",command=show_all_func)
showall_btn.grid(row=0,column=3,padx=12,pady=2)

#==============================

#===================databse frame==========
main_frame=tk.Frame(data_frame,bg="darkblue",bd=11,relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH,expand=True)

Y_scroll=tk.Scrollbar(main_frame,orient=tk.VERTICAL)
X_scroll=tk.Scrollbar(main_frame,orient=tk.HORIZONTAL)

student_table = ttk.Treeview(main_frame,column=("Roll No","Name","Class","Section","Contact","City","Gender","D.O.B"),yscrollcommand=Y_scroll.set,xscrollcommand=X_scroll.set)

Y_scroll.config(command=student_table.yview)
X_scroll.config(command=student_table.xview)

Y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
X_scroll.pack(side=tk.BOTTOM,fill=tk.X)

student_table.heading("Roll No",text="Roll No")
student_table.heading("Name",text="Name")
student_table.heading("Class",text="Class")
student_table.heading("Section",text="Section")
student_table.heading("Contact",text="Contact")
student_table.heading("City",text="City")
student_table.heading("Gender",text="Gender")
student_table.heading("D.O.B",text="D.O.B")

student_table['show']='headings'

student_table.column("Roll No",width=100)
student_table.column("Name",width=100)
student_table.column("Class",width=100)
student_table.column("Section",width=100)
student_table.column("Contact",width=100)
student_table.column("City",width=100)
student_table.column("Gender",width=100)
student_table.column("D.O.B",width=100)


student_table.pack(fill=tk.BOTH,expand=True)

fetch_data()

student_table.bind("<ButtonRelease-1>",get_cursor)
#==========================================

win.mainloop()


