
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from cryptography.fernet import Fernet
def SignUp():
    Window_SignUp = Tk()
    Window_SignUp.title("INPUT (sign up)")
    Window_SignUp.config(bg="#353535")
    Window_SignUp.geometry("600x300")
    Window_SignUp.resizable(False, False)
    Window_SignUp.iconbitmap("C:\\creative1\\PasswordApp\\PS.ico")
    Passam_Image_Icon = Image.open("C:\\creative1\\PasswordApp\\logo.jpg")
    Passam_Image_Icon = Passam_Image_Icon.resize((320, 210))
    Tk_Passam_Image = ImageTk.PhotoImage(Passam_Image_Icon)
    Passam_Image_Lable = Label(Window_SignUp, image=Tk_Passam_Image)
    Passam_Image_Lable.place(x=50, y=140)
    Text_Welcome = Label(Window_SignUp, text="Приветствую", bg="#353535", fg="white", width=10)
    Text_Welcome.pack()
    Text_Welcome_Style = ("Caveat", 50, "bold")
    Text_Enter_Password = Label(Window_SignUp, text="Введите пароль для входа", bg="#353535", fg="white")
    Text_Enter_Password.pack()
    Text_Enter_Password.place(x=440, y=150)
    Text_Enter_Password_Style = ("Comic Sans Ms", 15, "bold")
    Text_Enter_Password.configure(font=Text_Enter_Password_Style)
    Password_Entry = Entry(Window_SignUp, width=33)
    Password_Entry.pack()
    Password_Entry.place(x=395, y=220)
    Password_Entry_Style = ("Arial")
    Password_Entry.configure(font=Password_Entry_Style)
    def signUp_password_input():
        valueEditText = Password_Entry.get()
        if valueEditText == "":
            messagebox.showerror("Ошибка", "введите пароль!")
        else:
            messagebox.showinfo("Поздравляем", "вы успешно вошли!")
            Write_value_checkUser()
            App_Password_Encrypt = fernet.encrypt(valueEditText.encode()).decode()
            File_App_Password = open('App_Password', 'a')
            File_App_Password.write(App_Password_Encrypt)
            File_App_Password.close()
            Window_SignUp.destroy()
            Login()
    Button_SignUp = Button(Window_SignUp, text="Войти", width=20, bg="green", fg="white",
                           command=signUp_password_input)
    Button_SignUp.pack()
    Button_SignUp.place(x=450, y=280)
    Button_SignUp_Style = ("Centaur", 17, "bold")
    Button_SignUp.configure(font=Button_SignUp_Style)
    Window_SignUp.mainloop()
def Login():
    Window_Login = Tk()
    Window_Login.title("INPUT (login)")
    Window_Login.config(bg="#353535")
    Window_Login.geometry("600x300")
    Window_Login.resizable(False, False)
    Window_Login.iconbitmap("PS.ico")
    Text_Login = Label(Window_Login, text="Войти", bg="#353535", fg="white", width=10)
    Text_Login.pack()
    Text_Login_Style = ("Caveat", 50, "bold")
    Text_Login.configure(font=Text_Login_Style)
    frame = Frame(Window_Login, bg="#555454", height=350, width=400)
    frame.pack()
    frame.place(x=200, y=120)
    Text_Enter_Password = Label(frame, text="Введите пароль для входа", bg="#555454", fg="white")
    Text_Enter_Password.pack()
    Text_Enter_Password.place(x=70, y=50)
    Text_Enter_Password_Style = ("Comic Sans Ms", 15, "bold")
    Text_Enter_Password.configure(font=Text_Enter_Password_Style)
    Password_Entry = Entry(frame, width=25)
    Password_Entry.pack()
    Password_Entry.place(x=65, y=110)
    Password_Entry_Style = ("Arial")
    Password_Entry.configure(font=Password_Entry_Style)
    def get_login_enter_password():
        valueEditText = Password_Entry.get()
        if valueEditText == "":
            messagebox.showerror("Ошибка", "введите пароль!")
        else:
            Check_App_Password()
            if valueEditText == App_Password_Decrypt:
                messagebox.showinfo("Поздравляем", "пароль верный")
            else:
                messagebox.showerror("Ошибка", "пароль неверный")
    # Button login
    Button_Login = Button(frame, text="Войти", width=20, bg="green", fg="white", command=get_login_enter_password)
    Button_Login.pack()
    Button_Login.place(x=68, y=180)
    Button_Login_Style = ("Centaur", 17, "bold")
    Button_Login.configure(font=Button_Login_Style)
    Window_Login.mainloop()
File_Check_User = open('Check_New_User.txt', 'a')
File_Check_User = open('Check_New_User.txt', 'r')

def Write_value_checkUser():
    File_Check_User = open('Check_New_User.txt', 'w')
    File_Check_User.write("1")
    File_Check_User.close()
def Write_Key_File():
    if File_Check_User.read() == "":
        Key = Fernet.generate_key()
        Key_File = open("key.key", "wb")
        Key_File.write(Key)


def Load_key_File():
    global fernet
    Key_File = open("key.key", "rb")
    key = Key_File.read()
    Key_File.close()
    fernet = Fernet(key)

def Check_App_Password():
    global App_Password_Decrypt
    File_App_Password = open('App_Password', 'r')
    File_App_Password = File_App_Password.read()
    Load_key_File()
    App_Password_Decrypt = fernet.decrypt(File_App_Password.encode()).decode()

if File_Check_User.read() == "":
    Write_Key_File()
    Load_key_File()
    SignUp()
else:
    Login()