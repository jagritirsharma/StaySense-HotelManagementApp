from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from config import SQL_USER, SQL_PASSWORD, SQL_HOST, SQL_DATABASE

class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Customer Management System")
        self.root.geometry("1295x550+230+220")

        # =================== Variables =======================
        self.var_ref=StringVar()
        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()
        self.var_address=StringVar()

        # =================== Title ============================
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS", font=("Montserrat",20),bg="#4A4947",fg="#D8D2C2",bd=0)
        lbl_title.place(x=0,y=0,width=1295, height=50)

        # =================== Logo =============================
        img2=Image.open(r"C:\Users\HP\OneDrive\Desktop\Hotel_Management_System\images\logohotel.png")
        img2=img2.resize((100,40),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg =Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        # =================== LabelFrame =======================
        labelframeleft=LabelFrame(self.root,bd=0,relief=RIDGE,text="Customer Details",font=("Montserrat",12))
        labelframeleft.place(x=5,y=50,width=425,height=490)

        # =================== Labels and Entry fields =======================
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=("Montserrat",12),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=29,font=("Montserrat",11))
        enty_ref.grid(row=0,column=1)

        # Customer Name
        cname=Label(labelframeleft,font=("Montserrat",12),text="Customer Name:",padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,width=29,font=("Montserrat",11))
        txtcname.grid(row=1,column=1)

        # Mother Name
        lblmname=Label(labelframeleft,font=("Montserrat",12),text="Mother Name:",padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)
        txtmname=ttk.Entry(labelframeleft,textvariable=self.var_mother,width=29,font=("Montserrat",11))
        txtmname.grid(row=2,column=1)

        # Gender Combobox
        label_gender=Label(labelframeleft,font=("Montserrat",12),text="Gender:",padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("Montserrat",11),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.grid(row=3,column=1)
        combo_gender.current(0)

        # PostCode
        lblPostCode=Label(labelframeleft,font=("Montserrat",12),text="PostCode:",padx=2,pady=6)
        lblPostCode.grid(row=4,column=0,sticky=W)
        txtPostCode=ttk.Entry(labelframeleft,textvariable=self.var_post,width=29,font=("Montserrat",11))
        txtPostCode.grid(row=4,column=1)

        # Mobile Number
        lblMobile=Label(labelframeleft,font=("Montserrat",12),text="Mobile Number:",padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W)
        txtMobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,width=29,font=("Montserrat",11))
        txtMobile.grid(row=5,column=1)

        # Email
        lblEmail=Label(labelframeleft,font=("Montserrat",12),text="Email:",padx=2,pady=6)
        lblEmail.grid(row=6,column=0,sticky=W)
        txtEmail=ttk.Entry(labelframeleft,textvariable=self.var_email,width=29,font=("Montserrat",11))
        txtEmail.grid(row=6,column=1)

        # Nationality
        lblNationality=Label(labelframeleft,font=("Montserrat",12),text="Nationality:",padx=2,pady=6)
        lblNationality.grid(row=7,column=0,sticky=W)

        combo_Nationality=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("Montserrat",11),width=27,state="readonly")
        combo_Nationality["value"]=("Indian","American","British")
        combo_Nationality.grid(row=7,column=1)
        combo_Nationality.current(0)

        # ID Proof Combobox
        lblIdProof=Label(labelframeleft,font=("Montserrat",12),text="ID Proof Type:",padx=2,pady=6)
        lblIdProof.grid(row=8,column=0,sticky=W)

        combo_id=ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font=("Montserrat",11),width=27,state="readonly")
        combo_id["value"]=("AadharCard","DrivingLicense","Passport")
        combo_id.grid(row=8,column=1)
        combo_id.current(0)

        # ID Number
        lblIdNumber=Label(labelframeleft,font=("Montserrat",12),text="ID Number:",padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,textvariable=self.var_id_number,width=29,font=("Montserrat",11))
        txtIdNumber.grid(row=9,column=1)

        # Address
        lblAddress=Label(labelframeleft,font=("Montserrat",12),text="Address:",padx=2,pady=6)
        lblAddress.grid(row=10,column=0,sticky=W)
        txtAddress=ttk.Entry(labelframeleft,textvariable=self.var_address,width=29,font=("Montserrat",11))
        txtAddress.grid(row=10,column=1)

        # ===================== Buttons ==========================
        btn_frame=Frame(labelframeleft,bd=0,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11, "bold"), bg="green", fg="white", width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",11, "bold"), bg="green", fg="white", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)


        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",11, "bold"), bg="green", fg="white", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11, "bold"), bg="green", fg="white", width=10)
        btnReset.grid(row=0, column=3, padx=1)

        # ==================== Table Frame ===========================
        Table_Frame=LabelFrame(self.root,bd=0,relief=RIDGE,text="View Customer Details",font=("arial",12,"bold"), padx=2)
        Table_Frame.place(x=435,y=50,width=860,height=490)

        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(Table_Frame,column=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("mother",text="Mother Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("post",text="PostCode")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="ID Proof")
        self.Cust_Details_Table.heading("idnumber",text="ID Number")
        self.Cust_Details_Table.heading("address",text="Address")

        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("mother",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("post",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("address",width=100)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    # ======================= Add Data Function =====================
    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                conn = mysql.connector.connect(
                host=SQL_HOST,
                user=SQL_USER,
                password=SQL_PASSWORD,
                database=SQL_DATABASE
    )
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.var_ref.get(),
                                                                                                        self.var_cust_name.get(),
                                                                                                        self.var_mother.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_post.get(),
                                                                                                        self.var_mobile.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_nationality.get(),
                                                                                                        self.var_id_proof.get(),
                                                                                                        self.var_id_number.get(),
                                                                                                        self.var_address.get()
                                                                                                    ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

    # ========================= Fetch Data ==========================
    def fetch_data(self):
        conn = mysql.connector.connect(
        host=SQL_HOST,
        user=SQL_USER,
        password=SQL_PASSWORD,
        database=SQL_DATABASE
    )
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # ========================== Get Cursor ========================
    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])

    # ======================= Update Function ======================
    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn = mysql.connector.connect(
            host=SQL_HOST,
            user=SQL_USER,
            password=SQL_PASSWORD,
            database=SQL_DATABASE
        )
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set Name=%s,Mother=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,IdProof=%s,IdNumber=%s,Address=%s where Ref=%s",(
                                                                                                                            self.var_cust_name.get(),
                                                                                                                            self.var_mother.get(),
                                                                                                                            self.var_gender.get(),
                                                                                                                            self.var_post.get(),
                                                                                                                            self.var_mobile.get(),
                                                                                                                            self.var_email.get(),
                                                                                                                            self.var_nationality.get(),
                                                                                                                            self.var_id_proof.get(),
                                                                                                                            self.var_id_number.get(),
                                                                                                                            self.var_address.get(),
                                                                                                                            self.var_ref.get()
                                                                                                                        ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details have been updated successfully",parent=self.root)

    # ======================== Delete Function ======================
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent=self.root)
        if mDelete>0:
            conn = mysql.connector.connect(
            host=SQL_HOST,
            user=SQL_USER,
            password=SQL_PASSWORD,
            database=SQL_DATABASE
        ) 
            my_cursor=conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    # ======================== Reset Function =======================
    def reset(self):
        self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        self.var_nationality.set(""),
        self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")

        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

if __name__ == "__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()
