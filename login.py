from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from hotel import HotelManagementSystem
from customer import Cust_Win
from room import Roombooking
from details import DetailsRoom
from config import SQL_USER, SQL_PASSWORD, SQL_HOST, SQL_DATABASE



def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg_image = Image.open(r"C:\Users\HP\OneDrive\Desktop\Hotel_Management_System\images\backlogin.jpg")
        self.bg_image = self.bg_image.resize((1550, 800), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.bg_image)


        lbl_bg=Label(self.root, image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1, relheight=1)

        frame=Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height =450)

        img1=Image.open(r"C:\Users\HP\OneDrive\Desktop\Hotel_Management_System\images\login.png")
        img1=img1.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730, y=175, width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #label 
        username=lbl=Label(frame,text="Username", font=("times new roman",15,"bold"), fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password", font=("times new roman",15,"bold"), fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        #=================icon imgs======================

        img2=Image.open(r"C:\Users\HP\OneDrive\Desktop\Hotel_Management_System\images\login.png")
        img2=img2.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=650, y=323, width=25,height=25)

        img3=Image.open(r"C:\Users\HP\OneDrive\Desktop\Hotel_Management_System\images\lockk.jpg")
        img3=img3.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=650, y=395, width=25,height=25)

#==========================login button========================
        loginbtn=Button(frame,command=self.login ,text="Login", font=("times new roman",15,"bold"),bd=3, relief=RIDGE,fg="white",bg="green",activeforeground="white",activebackground="green")
        loginbtn.place(x=110,y=300, width=120,height=35)

 #register btn
        registerbtn=Button(frame,text="New User Register",command=self.register_window, font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350, width=160)

        #forget pwd
        registerbtn=Button(frame,text="Forget Password",command=self.forgot_password_window, font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=10,y=370, width=160)


    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app= Register(self.new_window)


    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu": # type: ignore
            messagebox.showinfo("Success","Welcome to StaySense")
        else: 
            conn = mysql.connector.connect(
            host=SQL_HOST,
            user=SQL_USER,
            password=SQL_PASSWORD,
            database=SQL_DATABASE
        )
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                         self.txtuser.get(),
                                                         self.txtpass.get()
            ))
            row=my_cursor.fetchone()
            #print(row)
            if row==None:
                messagebox.showerror("Error","Invalid Username & password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app= HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()


#========================reset password=====================

    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error", "Select the security question ", parent= self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error", "Please enter the answer ", parent= self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error", "Please enter the new password ", parent= self.root2)
        else:
            conn = mysql.connector.connect(
            host=SQL_HOST,
            user=SQL_USER,
            password=SQL_PASSWORD,
            database=SQL_DATABASE
        )
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(), self.combo_security_Q.get(), self.txt_security.get())
            my_cursor.execute(query,value)
            row= my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct Answer", parent= self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(), self.txtuser.get())
                my_cursor.execute(query, value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info", "Your password has been reset, please login new password", parent= self.root2)
                self.root2.destroy()
      

#======================forgot pwd window=====================
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error", "Please enter the Email address to reset password")
        else:
            conn = mysql.connector.connect(
            host=SQL_HOST,
            user=SQL_USER,
            password=SQL_PASSWORD,
            database=SQL_DATABASE
        )
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror("My Error","Please enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"), fg="blue",bg="white")
                l.place(x=0, y=10,relwidth=1 )

                security_Q=Label(self.root2, text="Select Security Questions", font=("times new roman",15,"bold"), bg="white", fg="black")
                security_Q.place(x=50, y=80)

                self.combo_security_Q=ttk.Combobox(self.root2, font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("select","Your Birth Place", "Your School name","Your Pet name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                security_A =Label(self.root2, text="Security Answer", font=("times new roman",15,"bold"), bg="white", fg="black")
                security_A.place(x=50, y=150)

                self.txt_security=ttk.Entry(self.root2,  font=("times new roman",15))
                self.txt_security.place(x=50, y=180, width= 250)

                new_password =Label(self.root2, text="New Password", font=("times new roman",15,"bold"), bg="white", fg="black")
                new_password.place(x=50, y=220)

                self.txt_newpass=ttk.Entry(self.root2,  font=("times new roman",15))
                self.txt_newpass.place(x=50, y=250, width= 250)

                btn=Button(self.root2, text="Reset", font=("times new roman",15),fg="white", bg="green", command=self.reset_pass)
                btn.place(x=100, y=290)



class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #=================variables========================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
    

        #==========bg image========

        self.bg_image = Image.open(r"C:\Users\HP\OneDrive\Desktop\Hotel_Management_System\images\backlogin.jpg")
        self.bg_image = self.bg_image.resize((1550, 800), Image.Resampling.LANCZOS)
        
        # Convert to PhotoImage for tkinter
        self.bg = ImageTk.PhotoImage(self.bg_image)

        # Create label with the resized image, covering the entire window
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)
        
        
        
        #==========left image========

        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\HP\OneDrive\Desktop\Hotel_Management_System\images\imgg.png")

        bg_lbl=Label(self.root,image=self.bg1)
        bg_lbl.place(x=50, y=100, width=470, height=400)

        #====================main frame=============
        frame= Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl= Label(frame,text="REGISTER HERE", font =("times new roman",20,"bold"),fg="darkgreen", bg="white")
        register_lbl.place(x=20, y=20)

        #=========================labels and entry=========

        #---------------------row1
        fname=Label(frame, text="First Name",font =("times new roman",15,"bold"), bg="white")
        fname.place(x=50, y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname, font =("times new roman",15,"bold"))
        fname_entry.place(x=50, y=130, width=250)

        l_name=Label(frame, text="Last Name",font =("times new roman",15,"bold"), bg="white", fg="black")
        l_name.place(x=370, y=100)

        self.txt_lname=ttk.Entry(frame, textvariable=self.var_lname,font =("times new roman",15))
        self.txt_lname.place(x=370, y=130, width=250)

        #-----------------------row2

        contact=Label(frame, text="Contact No", font=("times new roman",15,"bold"), bg="white", fg="black")
        contact.place(x=50, y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact, font=("times new roman",15))
        self.txt_contact.place(x=50, y=200, width= 250)

        email=Label(frame, text="Email", font=("times new roman",15,"bold"), bg="white", fg="black")
        email.place(x=370, y=170)

        self.txt_email=ttk.Entry(frame, textvariable=self.var_email, font=("times new roman",15))
        self.txt_email.place(x=370, y=200, width= 250)

        #------------------------row3

        security_Q=Label(frame, text="Select Security Questions", font=("times new roman",15,"bold"), bg="white", fg="black")
        security_Q.place(x=50, y=240)

        self.combo_security_Q=ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("select","Your Birth Place", "Your School name","Your Pet name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A =Label(frame, text="Security Answer", font=("times new roman",15,"bold"), bg="white", fg="black")
        security_A.place(x=370, y=240)

        self.txt_security=ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman",15))
        self.txt_security.place(x=370, y=270, width= 250)

        #----------------------row4

        pswd=Label(frame, text="Password", font=("times new roman",15,"bold"), bg="white", fg="black")
        pswd.place(x=50, y=310)

        self.txt_pswd=ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman",15))
        self.txt_pswd.place(x=50, y=340, width= 250)

        confirm_pswd=Label(frame, text="Confirm Password", font=("times new roman",15,"bold"), bg="white", fg="black")
        confirm_pswd.place(x=370, y=310)

        self.txt_confirm_pswd=ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370, y=340, width= 250)

        #======================Checkbutton==============
       
        self.var_check = IntVar()
        self.checkbtn = Checkbutton(frame,variable=self.var_check, text="I Agree The Terms & Condition", font=("times new roman",12), onvalue=1, offvalue=0)
        self.checkbtn.place(x=50, y=380)

        #=======================buttons==================

        # Register Button Image
        img = Image.open(r"C:\Users\HP\OneDrive\Desktop\Hotel_Management_System\images\register.jpg")
        img = img.resize((200, 50), Image.Resampling.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img)
        
        # Create Button with image
        b1 = Button(frame, image=self.photoimage,command=self.register_data, borderwidth=0, cursor="hand2", font=("times new roman",15, "bold"), fg="white")
        b1.place(x=10, y=420, width=200)

        # Login Button Image
        img1 = Image.open(r"C:\Users\HP\OneDrive\Desktop\Hotel_Management_System\images\login.jpg")
        img1 = img1.resize((200, 50), Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        
        # Create Button with image
        b2 = Button(frame, image=self.photoimage1,command=self.return_login, borderwidth=0, cursor="hand2", font=("times new roman",15, "bold"), fg="white")
        b2.place(x=330, y=420, width=200)

        #==============function declaration=======================

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password & Confirm Password must be the same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to our terms and conditions")
        else:
            try:
                conn = mysql.connector.connect(
                host=SQL_HOST,
                user=SQL_USER,
                password=SQL_PASSWORD,
                database=SQL_DATABASE
            )
                my_cursor = conn.cursor()
            
                 # Check if the email already exists
                query = ("SELECT * FROM register WHERE email=%s")
                value = (self.var_email.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                if row is not None:
                    messagebox.showerror("Error", "User already exists, please try another email")
                else:
                    # Insert new user data
                    my_cursor.execute("INSERT INTO register (fname, lname, contact, email, securityQ, securityA, password) VALUES (%s,%s,%s,%s,%s,%s,%s)", (
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_securityQ.get(),
                        self.var_securityA.get(),
                        self.var_pass.get()
                    ))

                    conn.commit()  # Commit the transaction
                    messagebox.showinfo("Success", "Registered Successfully")

            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Database Error: {err}")
            finally:
                conn.close()  # Close the connection
    def return_login(self):
        self.root.destroy()



class HotelManagementSystem: 
    def __init__(self, root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1550x800+0+0")
           
      # =============1st img===============  
    
        img1=Image.open(r"C:\Users\HP\OneDrive\Desktop\Hotel_Management_System\images\hotel1.png")
        img1=img1.resize((1550,140),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg =Label(self.root,image=self.photoimg1,bd=0,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)
      # =============logo====================

        img2=Image.open(r"C:\Users\HP\OneDrive\Desktop\Hotel_Management_System\images\logohotel.png")
        img2=img2.resize((230,140),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg =Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)
      # ===================title============

        lbl_title=Label(self.root,text="Hotel Management System", font=("Montserrat",20),bg="#4A4947",fg="#D8D2C2",bd=0)
        lbl_title.place(x=0,y=140,width=1550, height=50)
      
      #===================== main Frame=============
        main_frame= Frame(self.root, bd=1)
        main_frame.place(x=0, y=190, width=1550, height=620)
      #======================menu=================

        lbl_menu=Label(main_frame,text="Dashboard", font=("Montserrat",20),bg="#4A4947",fg="#D8D2C2",bd=0)
        lbl_menu.place(x=0,y=0,width=230 )

       #===================== button Frame=============
        btn_frame= Frame(main_frame, bd=1)
        btn_frame.place(x=0, y=35, width=228, height=190)
        
        cust_btn= Button(btn_frame, text= "Customer", command=self.cust_details , width=22 , font=("Montserrat",14),bg="#618264",fg="white",bd=0, cursor ="hand1")
        cust_btn.grid(row=0,column=0, pady=1)

        room_btn= Button(btn_frame, text= "Room", command=self.roombooking, width=22 , font=("Montserrat",14),bg="#618264",fg="white",bd=0, cursor ="hand1")
        room_btn.grid(row=1,column=0, pady=1)

        details_btn= Button(btn_frame, text= "Detail", width=22 ,command=self.details_room, font=("Montserrat",14),bg="#618264",fg="white",bd=0, cursor ="hand1")
        details_btn.grid(row=2,column=0, pady=1)

        report_btn= Button(btn_frame, text= "Report", width=22 , font=("Montserrat",14),bg="#618264",fg="white",bd=0, cursor ="hand1")
        report_btn.grid(row=3,column=0, pady=1)

        logout_btn= Button(btn_frame, text= "Logout", width=22 , font=("Montserrat",14),bg="#618264",fg="white",bd=0, cursor ="hand1")
        logout_btn.grid(row=4,column=0, pady=1)
      # =============right img===================

        img3=Image.open(r"C:\Users\HP\OneDrive\Desktop\Hotel_Management_System\images\slide3.jpg")
        img3=img3.resize((1310,590),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg =Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg.place(x=225,y=0,width=1310,height=590)

     #===================down img=================

        img4=Image.open(r"C:\Users\HP\OneDrive\Desktop\Hotel_Management_System\images\food.jpg")
        img4=img4.resize((230,210),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg =Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=225,width=230,height=210)


        img5=Image.open(r"C:\Users\HP\OneDrive\Desktop\Hotel_Management_System\images\hall.jpg")
        img5=img5.resize((230,190),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg =Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=420,width=230,height=190)

    def cust_details(self):
      self.new_window = Toplevel(self.root)
      self.app = Cust_Win(self.new_window)
    
    def roombooking(self):
      self.new_window = Toplevel(self.root)
      self.app = Roombooking(self.new_window)

    def details_room(self):
      self.new_window = Toplevel(self.root)
      self.app = DetailsRoom(self.new_window)





if __name__=="__main__":
    main()
