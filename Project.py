from tkinter import *
root = Tk()
root.geometry("900x400")
root.maxsize(1366, 768)
root.minsize(200, 300)
root.title("Online Job application Portal")
root.configure(bg="#8eb1ed")


def searchJob():
    hill= Toplevel()
    hill.geometry("900x400")
    hill.maxsize(1366,768)
    hill.minsize(200,300)
    hill.configure(bg="#8eb1ed")
    
    
    jobpreference = Label(hill,text = "JOB PREFERENCE", font=("algeria", 30 ,"bold" ,"italic"),bd=5,bg="#c3c7c6")
    jobpreference.grid(row=0, column=2)
    
    field= Label(hill,text= "FIELD",font=('algeria',12),bg="#8eb1ed")
    field_in= Entry(hill)
    field_in.grid(row=4,column=2)
    
    company= Label(hill, text = "COMPANY",font=('algeria',12),bg="#8eb1ed")
    company_in= Entry(hill)
    company_in.grid(row=6,column=2)
    
    salaryexpected= Label(hill, text = "SALARYEXPECTED",font=('algeria',12),bg="#8eb1ed")
    salaryexpected_in= Entry(hill)
    salaryexpected_in.grid(row=8,column=2)
    
    
    area= Label(hill, text = "AREA",font=('algeria',12),bg="#8eb1ed")
    area_in= Entry(hill)
    area_in.grid(row=10,column=2)
    
    worktype= Label(hill, text = "WORK TYPE",font=('algeria',12),bg="#8eb1ed")
    worktype_in= Entry(hill)
    worktype_in.grid(row=12,column=2)
    
    field.grid(row=4,column=1)
    company.grid(row=6,column=1)
    salaryexpected.grid(row=8,column=1)
    area.grid(row=10,column=1)
    worktype.grid(row=12,column=1)
    
    b2=Button(hill, text = "APPLY",command=Message)
    b2.grid(row=16,column=2)



def apply():
    hi= Toplevel()

    hi.geometry("900x400")
    hi.maxsize(1366,768)
    hi.minsize(200,300)
    hi.configure(bg="#8eb1ed")
    
    
    jobseekercredentials = Label(hi,text = "JOB SEEKER CREDENTIALS", font=("algeria", 36 ,"bold" ,"italic"),bd=5,bg="#c3c7c6")
    jobseekercredentials.grid(row=0, column=2)
    
    jobrequired= Label(hi,text= "JOB REQUIRED",font=('algeria',12),bg="#8eb1ed")
    jobrequired_in= Entry(hi)
    jobrequired_in.grid(row=4,column=2)
    
    qualifications= Label(hi, text = "QUALIFICATIONS",font=('algeria',12),bg="#8eb1ed")
    qualifications_in= Entry(hi)
    qualifications_in.grid(row=6,column=2)
    
    experience= Label(hi, text = "EXPERERIANCE",font=('algeria',12),bg="#8eb1ed")
    experience_in= Entry(hi)
    experience_in.grid(row=8,column=2)
    
    
    mobile= Label(hi, text = "MOBILE",font=('algeria',12),bg="#8eb1ed")
    mobile_in= Entry(hi)
    mobile_in.grid(row=10,column=2)
    
    description= Label(hi, text = "DESCRIPTION",font=('algeria',12),bg="#8eb1ed")
    description_in= Entry(hi)
    description_in.grid(row=12,column=2)
    
    jobrequired.grid(row=4,column=1)
    qualifications.grid(row=6,column=1)
    experience.grid(row=8,column=1)
    mobile.grid(row=10,column=1)
    description.grid(row=12,column=1)
    
    b1=Button(hi, text = "SUBMIT",command=Onclick)
    b1.grid(row=16,column=2)
    



def contactus():
    cu = Toplevel()
    cu.geometry("900x400")
    cu.maxsize(1366, 768)
    cu.minsize(200, 300)
    cu.configure(bg="#8eb1ed")
    f1 = LabelFrame(cu, borderwidth=15, relief=SUNKEN, padx=80, pady=60)
    msg = Label(cu, text="CONTACT OUR TOLL FREE NUMBER",font=("arial", 16, 'bold'), anchor=CENTER, fg="#000000",bg="#D6E4E5")

  
    num = Label(cu, text="+4573-222-333",width=41, font=("arial", 12), anchor=CENTER, fg="#000000",bg="#D6E4E5")


    email = Label(cu, text="CONTACT US AT OUR MAIL ID, mail to: JobPortal123@gmail.com",width=41,
                  wraplength=300, font=("arial", 12), anchor=CENTER, fg="#000000",bg="#D6E4E5")
    msg.pack()
    num.pack()
    email.pack()
    f1.pack()



def register():
    hell= Toplevel()

    hell.geometry("900x400")
    hell.maxsize(1366,768)
    hell.minsize(200,300)
    hell.configure(bg="#8eb1ed")
    
    
    registrationform = Label(hell,text = "REGISTRATION FORM", font=("algeria", 36 ,"bold" ,"italic"),bd=5,bg="#c3c7c6")
    registrationform.grid(row=0, column=2)
    
    name= Label(hell,text= "NAME",font=('algeria',12),bg="#8eb1ed")
    name_in= Entry(hell)
    name_in.grid(row=4,column=2)
    
    contact= Label(hell, text = "CONTACT",font=('algeria',12),bg="#8eb1ed")
    contact_in= Entry(hell)
    contact_in.grid(row=6,column=2)
    
    password= Label(hell, text = "PASSWORD",font=('algeria',12),bg="#8eb1ed")
    password_in= Entry(hell)
    password_in.grid(row=8,column=2)
    
    
    confirmpassword= Label(hell, text = "CONFIRM PASSWORD",font=('algeria',12),bg="#8eb1ed")
    confirmpassword_in= Entry(hell)
    confirmpassword_in.grid(row=10,column=2)
    
    email= Label(hell, text = "EMAIL",font=('algeria',12),bg="#8eb1ed")
    email_in= Entry(hell)
    email_in.grid(row=12,column=2)
    
    name.grid(row=4,column=1)
    contact.grid(row=6,column=1)
    password.grid(row=8,column=1)
    confirmpassword.grid(row=10,column=1)
    email.grid(row=12,column=1)
    
    b3=Button(hell, text = "REGISTER",command=hell.destroy)
    b3.grid(row=16,column=2)

def Onclick():
    new=Toplevel()
    new.geometry("900x400")
    new.maxsize(1366, 768)
    new.minsize(200, 300)
    new.configure(bg="#8eb1ed")
    hi = Button(new, text="Information saved. We will soon notify you about your desired job as soon as we find it ",bd=20,borderwidth=10,font=('algeria',12),command=new.destroy)
    hi.pack()


def click_user_login():
    helo=Toplevel()
    helo.geometry("900x400")
    helo.maxsize(1366, 768)
    helo.minsize(200, 300)
    helo.configure(bg="#8eb1ed")

    to_register=Label(helo,text="Click here to register",bd=5,borderwidth=10,font=('algeria',12),fg='#000000',bg="#8eb1ed")
    to_register_btn = Button(helo, text="Sign Up",bd=4,borderwidth=5,font=('algeria',12),fg='#000000',command=register)
    to_register.grid(row=2,column=0)
    to_register_btn.grid(row=2,column=3)

     

    username= Label(helo, text="USERNAME",bd=5,font=('algeria',16),fg='#000000',width=23,bg="#8eb1ed")
    username_in = Entry(helo)
    username.grid(row=4,column=0)
    username_in.grid(row=4,column=3)

    password= Label(helo, text="PASSWORD",bd=5,font=('algeria',16),fg='#000000',width=23,bg="#8eb1ed")
    password_in = Entry(helo)
    password.grid(row=6,column=0)
    password_in.grid(row=6,column=3)

    submit = Button(helo,text="SUBMIT",font=('algeria', 16),bd=4,borderwidth=5,fg='#000000',command=apply)
    submit.grid(row=9,column=3)

welcome = Label(root,text="JOB PORTAL", font=('algeria', 16, "italic"), bd=5)
welcome.pack()



top_buttons = LabelFrame(root, borderwidth=10, bd=5,padx=80, pady=30,fg='#915403',bg="#8eb1ed")
home_button = Button(top_buttons, text="HOME",bd=5,borderwidth=10,font=('algeria',12),fg='#000000',bg="#FFFFFF") 
user_button = Button(top_buttons, text="USER LOGIN",bd=5,borderwidth=10,font=('algeria',12),bg="#FFFFFF",fg='#000000',command=click_user_login)
ContactUS_button = Button(top_buttons, text="CONTACT US",bd=5,borderwidth=10,font=('algeria',12),bg="#FFFFFF",fg='#000000',command=contactus)

home_button.grid(row= 3, column=2     ,padx=50, pady=20)
user_button.grid(row= 3, column=6     ,padx=50, pady=20)
ContactUS_button.grid(row=3 , column=8,padx=50, pady=20)
top_buttons.pack()



root.mainloop()