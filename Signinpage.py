from tkinter import *
from tkinter import messagebox

import pymysql
from PIL import ImageTk


# Functionality part

def forget_pass():
    def change_password():
        if user_Entry.get() == '' or newpass_Entry.get() == '' or confirmpass_Entry.get == '':
            messagebox.showerror('Error', 'All Fields are Required', parent=window)
        elif newpass_Entry.get() != confirmpass_Entry.get():
            messagebox.showerror('Error', 'Password and Confirm Password are not matching', parent=window)
        else:
            con = pymysql.Connect(host="localhost", user='root', password='root', database='userdata')
            mycursor = con.cursor()
            query = 'select * from data where username=%s'
            mycursor.execute(query, (user_Entry.get()))
            row = mycursor.fetchone()
            if row is None:
                messagebox.showerror('Error', 'Incorrect Username', parent=window)
            else:
                query = 'update data set password=%s where username=%s'
                mycursor.execute(query, (newpass_Entry.get(), user_Entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Password is reset, please login with new password', parent=window)
                window.destroy()

    window = Toplevel()
    window.title("change password")

    bgpic = ImageTk.PhotoImage(file='background.jpg')
    bglabel = Label(window, image=bgpic)
    bglabel.grid()

    heading_label = Label(window, text='RESET PASSWORD', font=('arial', 18, 'bold'), bg='white', fg='violet red')
    heading_label.place(x=480, y=60)

    username_label = Label(window, text='Username', font=('arial', 12, 'bold'), bg='white', fg='violet red')
    username_label.place(x=470, y=130)

    user_Entry = Entry(window, width=25, font=('arial', 11, 'bold'), bd=0, fg='violet red')
    user_Entry.place(x=470, y=160)

    Frame(window, width=250, height=2, bg='violet red').place(x=470, y=180)

    passwordlabel = Label(window, text='New Password', font=('arial', 12, 'bold'), bg='white', fg='violet red')
    passwordlabel.place(x=470, y=210)

    newpass_Entry = Entry(window, width=25, font=('arial', 11, 'bold'), bd=0, fg='violet red')
    newpass_Entry.place(x=470, y=240)

    Frame(window, width=250, height=2, bg='violet red').place(x=470, y=260)

    confirmpasslabel = Label(window, text='Confirm Password', font=('arial', 12, 'bold'), bg='white', fg='violet red')
    confirmpasslabel.place(x=470, y=290)

    confirmpass_Entry = Entry(window, width=25, font=('arial', 11, 'bold'), bd=0, fg='violet red')
    confirmpass_Entry.place(x=470, y=320)

    Frame(window, width=250, height=2, bg='violet red').place(x=470, y=340)

    submitButton = Button(window, text='submit', bd=0, bg='violet red', fg='white', font=('open sans', '16', 'bold'),
                          width=19, cursor='hand2', activebackground='violet red', activeforeground='white',
                          command=change_password)
    submitButton.place(x=470, y=390)

    window.mainloop()


def login_user():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'All fields Are Required')

    else:
        try:
            con = pymysql.Connect(host="localhost", user='root', password='root')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Connection is not established try again')
            return
        query = 'use userdata'
        mycursor.execute(query)
        query = 'select * from data where username=%s and password=%s'
        mycursor.execute(query, (usernameEntry.get(), passwordEntry.get()))
        row = mycursor.fetchone()
        if row is None:
            messagebox.showerror('Error', 'Invalid username or password')
        else:
            messagebox.showinfo('Welcome', 'Login is successful')


def signup_page():
    login_window.destroy()
    import signup


def hide():
    openeye.config(file="C://Users//kumar//Downloads//closeye.png")
    passwordEntry.config(show='*')
    eyebutton.config(command=show)


def show():
    openeye.config(file="C://Users//kumar//Downloads//openeye.png")
    passwordEntry.config(show='')
    eyebutton.config(command=hide)


def user_enter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)


def password_enter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)


# GUI part
login_window = Tk()
login_window.title("Login Page")

#  login_window.geometry('990x660+50+50')
# login_window.resizable(0, 0) # used for fixed size
# login_window.maxsize(width=850, height=575)
login_window.minsize(width=850, height=575)
# login_window.title('Login Page')
login_window.grid()

bgImage = ImageTk.PhotoImage(file="C://Users//kumar//Downloads//bg.jpg")

bgLabel = Label(login_window, image=bgImage, bg='pink', bd=30)
bgLabel.place(x=0, y=0)

heading = Label(login_window, text="USER LOGIN", font=('Microsoft YaHei UI Light', 23, 'bold'), bg='white',
                fg='firebrick1')
heading.place(x=500, y=100)

usernameEntry = Entry(login_window, width=25, font=('Microsoft YaHei UI Light', 11, 'bold'), bd=0, fg='firebrick1')
usernameEntry.place(x=510, y=160)
usernameEntry.insert(0, 'Username')  # username will be written in entrybox
usernameEntry.bind('<FocusIn>',
                   user_enter)  # with the help of this  user write any word in entrybox then automatically username hide

Frame1 = Frame(login_window, width=250, height=2, bg='firebrick1')
Frame1.place(x=490, y=190)

passwordEntry = Entry(login_window, width=25, font=('Microsoft YaHei UI Light', 11, 'bold'), bd=0, fg='firebrick1')
passwordEntry.place(x=510, y=209)
passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>', password_enter)

Frame2 = Frame(login_window, width=250, height=2, bg='firebrick1')
Frame2.place(x=490, y=240)

openeye = PhotoImage(file='C://Users//kumar//Downloads//openeye.png')
eyebutton = Button(login_window, image=openeye, bd=0, bg='white', activebackground='white', cursor='hand2',
                   command=hide)
eyebutton.place(x=700, y=205)

forgetbutton = Button(login_window, text='Forgot Password?', bd=0, bg='white', activebackground='white', cursor='hand2',
                      font=('Microsoft Yahei UI Light', 11, 'bold'), fg='firebrick1', activeforeground='firebrick1',
                      command=forget_pass)
forgetbutton.place(x=600, y=250)

LoginButton = Button(login_window, text='Login', font=('Open Sans', 16, 'bold'), fg='white', bg='firebrick1',
                     activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=18,
                     command=login_user)
LoginButton.place(x=490, y=300)

orLabel = Label(login_window, text="---------------OR---------------", font=('Open Sans', 16), fg='firebrick1',
                bg='white')
orLabel.place(x=489, y=351)

facebook_logo = PhotoImage(file="C://Users//kumar//Downloads//facebook.png")
fblabel = Label(login_window, image=facebook_logo, bg='white')
fblabel.place(x=520, y=400)

Google_logo = PhotoImage(file="C://Users//kumar//Downloads//google.png")
googlelabel = Label(login_window, image=Google_logo, bg='white')
googlelabel.place(x=580, y=400)

Twitter_logo = PhotoImage(file="C://Users//kumar//Downloads//twitter.png")
twitlabel = Label(login_window, image=Twitter_logo, bg='white')
twitlabel.place(x=640, y=400)

signupLabel = Label(login_window, text="Don't have an account?", font=('Open Sans', 9, 'bold'), fg='firebrick1',
                    bg='white')
signupLabel.place(x=495, y=440)

newaccountButton = Button(login_window, text='Create New One', font=('Open Sans', 9, 'bold underline'), fg='blue',
                          bg='white', activeforeground='white', activebackground='white', cursor='hand2', bd=0,
                          command=signup_page)
newaccountButton.place(x=635, y=440)

login_window.mainloop()
