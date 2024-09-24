from tkinter import*
from PIL import Image, ImageTk   #pip install pillow


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
        
        cust_btn= Button(btn_frame, text= "Customer", width=22 , font=("Montserrat",14),bg="#618264",fg="white",bd=0, cursor ="hand1")
        cust_btn.grid(row=0,column=0, pady=1)

        room_btn= Button(btn_frame, text= "Room", width=22 , font=("Montserrat",14),bg="#618264",fg="white",bd=0, cursor ="hand1")
        room_btn.grid(row=1,column=0, pady=1)

        details_btn= Button(btn_frame, text= "Detail", width=22 , font=("Montserrat",14),bg="#618264",fg="white",bd=0, cursor ="hand1")
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


if __name__ == "__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()