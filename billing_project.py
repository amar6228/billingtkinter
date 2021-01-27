from tkinter import *
from tkinter import messagebox
import random
import datetime
import time
import os

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1475x780+0+0")
        self.root.minsize(1450,770)
        self.root.title("Simple Billing Software--Created By:@amar6228")
        #self.root.wm_iconbitmap("billico.ico")
        bg_color1="orange"
        bg_color2="light blue"

        title=Label(self.root, text="Billing Software", 
        font=("times new roman", 30, "bold"),
        bd=10,bg=bg_color1,
        fg="white", relief=SUNKEN, pady=2).pack(fill=X)

        self.date_time1 = StringVar()
        self.date_time1.set(time.strftime("%d/%m/%y"))
        ############ Customer Details variable------------
        self.cname=StringVar()
        self.cphon=StringVar()

        self.cbill=StringVar()
        billl=random.randint(1000,99999)
        self.cbill.set(str(billl))

        self.search_bill=StringVar()
        ############ Variables----------------
        #1.electronic
        self.tv=IntVar()
        self.ac=IntVar()
        #2
        self.battery=IntVar()
        self.keyboard=IntVar()
        #3
        self.smartphone=IntVar()
        self.keypad=IntVar()
        #############product price & Tax variable----------------------
        self.electronic=StringVar()
        self.hardware=StringVar()
        self.mobile=StringVar()

        self.gst1=StringVar()
        self.gst2=StringVar()
        self.gst3=StringVar()

             ############------Customer details frame---------------
        f1=LabelFrame(self.root,bd=10,relief=GROOVE, text="Customer Details:",
        font=("times new roman", 12, "bold"),fg="white",
        bg=bg_color1)
        f1.place(x=0,y=75, relwidth=1)

        cname_lbl=Label(f1, text="Customer Name",
         font=("times new roman", 15, "bold"),
         bg=bg_color1).grid(row=0, column=0, padx=5, pady=5)
        cname_txt=Entry(f1,textvariable=self.cname, width=15, font="arial 10",bd=5,
         relief=SUNKEN).grid(row=0, column=1,padx=5, pady=5)

        phone_lbl=Label(f1, text="Phone No:",
         font=("times new roman", 15, "bold"),
         bg=bg_color1).grid(row=0, column=2, padx=5, pady=5)
        phone_txt=Entry(f1,textvariable=self.cphon, width=15, font="arial 10",bd=5,
         relief=SUNKEN).grid(row=0, column=3,padx=5, pady=5)

        bill_lbl=Label(f1, text="Bill No:",
         font=("times new roman", 15, "bold"),
         bg=bg_color1).grid(row=0, column=4, padx=5, pady=5)
        bill_txt=Entry(f1,textvariable=self.search_bill, width=20, font="arial 10 bold",bd=5,
         relief=SUNKEN).grid(row=0, column=5,padx=5, pady=5)
        bill_btn=Button(f1,command=self.search_saved_bill, text="Search",fg="black",width=8,
        bd=5, font="arial 10 bold").grid(row=0, column=6,padx=2, pady=5)



                   ###############-------Electronic Frame F2--
        f2=LabelFrame(self.root,bd=10,relief=GROOVE, text="Electronic:",
        font=("times new roman", 12, "bold"),fg="white",
        bg=bg_color1)
        f2.place(x=2,y=155,width=320, height=400)

        tv_lbl=Label(f2, text="TV:",
         font=("times new roman", 15, "bold"), bg=bg_color1,
         fg="green").grid(row=0, column=0,pady=2,sticky="w")
        tv_entry=Entry(f2,textvariable=self.tv, width=20, font="arial 10",
        bd=5, relief=SUNKEN).grid(row=0, column=1)

        ac_lbl=Label(f2, text="AC:",
         font=("times new roman", 15, "bold"), bg=bg_color1,
         fg="green").grid(row=1, column=0,pady=2,sticky="w")
        ac_entry=Entry(f2,textvariable=self.ac, width=20, font="arial 10",
        bd=5, relief=SUNKEN).grid(row=1, column=1)

                    ###########----------Hardware Frame F3-----
        f3=LabelFrame(self.root,bd=10,relief=GROOVE, text="Hardware:",
        font=("times new roman", 12, "bold"),fg="white",
        bg=bg_color1)
        f3.place(x=322,y=155,width=320, height=400)

        battery_lbl=Label(f3, text="Battery:",
         font=("times new roman", 15, "bold"), bg=bg_color1,
         fg="green").grid(row=0, column=0,pady=2,sticky="w")
        battery_entry=Entry(f3,textvariable=self.battery, width=20, font="arial 10",
        bd=5, relief=SUNKEN).grid(row=0, column=1)

        keyboard_lbl=Label(f3, text="Keyboard:",
         font=("times new roman", 15, "bold"), bg=bg_color1,
         fg="green").grid(row=1, column=0,pady=2,sticky="w")
        keyboard_entry=Entry(f3,textvariable=self.keyboard, width=20, font="arial 10",
        bd=5, relief=SUNKEN).grid(row=1, column=1)


        ###########----------Mobile-----
        f4=LabelFrame(self.root,bd=10,relief=GROOVE, text="Mobile:",
        font=("times new roman", 12, "bold"),fg="white",
        bg=bg_color1)
        f4.place(x=643,y=155,width=320, height=400)

        smartphone_lbl=Label(f4, text="smartphone:",
         font=("times new roman", 15, "bold"), bg=bg_color1,
         fg="green").grid(row=0, column=0,pady=2,sticky="w")
        smartphone_entry=Entry(f4,textvariable=self.smartphone, width=20, font="arial 10",
        bd=5, relief=SUNKEN).grid(row=0, column=1)

        keypad_lbl=Label(f4, text="keypad:",
         font=("times new roman", 15, "bold"), bg=bg_color1,
         fg="green").grid(row=1, column=0,pady=2,sticky="w")
        keypad_entry=Entry(f4,textvariable=self.keypad, width=20, font="arial 10",
        bd=5, relief=SUNKEN).grid(row=1, column=1)

                  #############-----------Bill View Area-----------
        f5=Frame(self.root,bd=10,relief=GROOVE)
        f5.place(x=971,y=155,width=485, height=400)
        bill_title=Label(f5, text="Bill",font="arial 15 bold",
        bd=5,relief=GROOVE).pack(fill=X)
        scroll_y=Scrollbar(f5, orient=VERTICAL)
        self.textarea=Text(f5, yscrollcommand=scroll_y.set)

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)
                      #############--------Total Sum, Frame F6-----------
        f6=LabelFrame(self.root,bd=10,relief=GROOVE, text="Button:",
        font=("times new roman", 12, "bold"),fg="white",
        bg=bg_color2)
        f6.place(x=2,y=560,relwidth=1, height=240)

        m1=Label(f6,text="Electronic:",bg=bg_color2,fg="black",
         font=("times new roman", 15,"bold")).grid(row=0, column=0,padx=5, pady=4,sticky="w")
        m1_txt=Entry(f6,textvariable=self.electronic, width=18, font="arial 10 bold", bd=5,
        relief=SUNKEN).grid(row=0, column=1,padx=10, pady=4)

        m2=Label(f6,text="Hardware:",bg=bg_color2,fg="black",
         font=("times new roman", 15,"bold")).grid(row=1, column=0,padx=5, pady=4,sticky="w")
        m2_txt=Entry(f6,textvariable=self.hardware, width=18, font="arial 10 bold", bd=5,
        relief=SUNKEN).grid(row=1, column=1,padx=5, pady=4)

        m3=Label(f6,text="Mobile:",bg=bg_color2,fg="black",
         font=("times new roman", 15,"bold")).grid(row=2, column=0,padx=5, pady=4,sticky="w")
        m3_txt=Entry(f6,textvariable=self.mobile, width=18, font="arial 10 bold", bd=5,
        relief=SUNKEN).grid(row=2, column=1,padx=5, pady=4)
                      #############tax column-------
        t1=Label(f6,text="GST-1:",bg=bg_color2,fg="black",
         font=("times new roman", 15,"bold")).grid(row=0, column=2,padx=5, pady=4,sticky="w")
        t1_txt=Entry(f6,textvariable=self.gst1, width=18, font="arial 10 bold", bd=5,
        relief=SUNKEN).grid(row=0, column=3,padx=10, pady=4)

        t2=Label(f6,text="GST-2:",bg=bg_color2,fg="black",
         font=("times new roman", 15,"bold")).grid(row=1, column=2,padx=5, pady=4,sticky="w")
        t2_txt=Entry(f6,textvariable=self.gst2, width=18, font="arial 10 bold", bd=5,
        relief=SUNKEN).grid(row=1, column=3,padx=5, pady=4)

        t3=Label(f6,text="GST-3:",bg=bg_color2,fg="black",
         font=("times new roman", 15,"bold")).grid(row=2, column=2,padx=5, pady=4,sticky="w")
        t3_txt=Entry(f6,textvariable=self.gst3, width=18, font="arial 10 bold", bd=5,
        relief=SUNKEN).grid(row=2, column=3,padx=5, pady=4)
                         ############ Cess------------

        # c1=Label(f6,text="CESS-1:",bg=bg_color2,fg="black",
        #  font=("times new roman", 15,"bold")).grid(row=0, column=4,padx=5, pady=4,sticky="w")
        # c1_txt=Entry(f6, width=18, font="arial 10 bold", bd=5,
        # relief=SUNKEN).grid(row=0, column=5,padx=10, pady=4)

        # c2=Label(f6,text="CESS-2:",bg=bg_color2,fg="black",
        #  font=("times new roman", 15,"bold")).grid(row=1, column=4,padx=5, pady=4,sticky="w")
        # c2_txt=Entry(f6, width=18, font="arial 10 bold", bd=5,
        # relief=SUNKEN).grid(row=1, column=5,padx=5, pady=4)

        # c3=Label(f6,text="CESS-3:",bg=bg_color2,fg="black",
        #  font=("times new roman", 15,"bold")).grid(row=2, column=4,padx=5, pady=4,sticky="w")
        # c3_txt=Entry(f6, width=18, font="arial 10 bold", bd=5,
        # relief=SUNKEN).grid(row=2, column=5,padx=5, pady=4)

        #         #########-----button in f6 frame-------
        btn_frame=Frame(f6,bd=6,bg="light blue", relief=GROOVE)
        btn_frame.place(x=750,width=700,height=170)

        total_btn=Button(btn_frame,command=self.total_price, text="Total",bg="red",width=12,height=2,font="aerial 15 bold", fg="black").grid(row=0,column=0,padx=5,pady=5)
        
        bill_btn=Button(btn_frame,command=self.bill_area,text="Generate Bill",bg="red",width=12,height=2,font="aerial 15 bold", fg="black").grid(row=0,column=1,padx=5,pady=5)
        self.welcome_bill()

        clear_btn=Button(btn_frame,command=self.clear_bill_data ,text="Clear",bg="red",width=12,height=2,font="aerial 15 bold", fg="black").grid(row=0,column=2,padx=5,pady=5)
       
        exit_btn=Button(btn_frame,command=self.exit_app,text="Exit",bg="red",width=12,height=2,font="aerial 15 bold", fg="black").grid(row=0,column=3,padx=5,pady=5)

        bill_btn2=Button(btn_frame, text="SAVE BILL",fg="black",width=12,height=2,bg="red",font="arial 15 bold").grid(row=1, column=3,padx=2, pady=5)

        calc_btn=Button(btn_frame,command=self.calc_wind, text="Calculator",fg="black",width=12,height=2,bg="red",font="arial 15 bold").grid(row=1, column=2,padx=2, pady=5)
#####################----Backend Function Logic----
    
    def total_price(self):

         self.t_v=self.tv.get()*100
         self.a_c=self.ac.get()*200 
         self.total_electronic_price=float( self.t_v + self.a_c)
         self.electronic.set("Rs: "+str(self.total_electronic_price))
         self.gst1_tax=round(( self.total_electronic_price*0.18),2) 
         self.gst1.set("Rs. "+str(self.gst1_tax))

         self.batt=self.battery.get()*5000
         self.keybo=self.keyboard.get()*150
         self.total_hardware_price=float(self.batt + self.keybo)
         self.hardware.set("Rs: "+str(self.total_hardware_price))
         self.gst2_tax=round(( self.total_hardware_price*0.12),2) 
         self.gst2.set("Rs. "+str(self.gst2_tax))

         self.smart=self.smartphone.get()*1000
         self.keypa=self.keypad.get()*500
         self.total_mobile_price=float(self.smart + self.keypa)
         self.mobile.set("Rs: "+str(self.total_mobile_price))
         self.gst3_tax=round((self.total_mobile_price*0.18 ),2)
         self.gst3.set("Rs. "+str(self.gst3_tax ))

         self.total_bill_value=float(
                                      self.total_electronic_price+
                                      self.total_hardware_price+
                                      self.total_mobile_price+
                                      self.gst1_tax+
                                      self.gst2_tax+
                                      self.gst3_tax

                                     )
    def welcome_bill(self):
                 self.textarea.delete('1.0', END)
                 self.textarea.insert(END,"\t\t\t Welcome\n")
                 self.textarea.insert(END,f"\n Bill No: {self.cbill.get()},\t\t\tDate:{self.date_time1.get()}")
                 self.textarea.insert(END,f"\n Name: {self.cname.get()}")
                 self.textarea.insert(END,f"\n Phone: {self.cphon.get()}")
                 self.textarea.insert(END,f"\n =========================================")
                 
                 self.textarea.insert(END,f"\n Products\t\tQty\t\tPrice")
                 
                 self.textarea.insert(END,f"\n -----------------------------------------")


    def bill_area(self):
            if self.cname.get()=="" or self.cphon.get()=="":
                messagebox.showerror("Error", "Customer Name and Phone is mandatory")
        #     elif self.electronic.get()=="Rs. 0.0" and self.hardware.get()=="Rs. 0.0" and self.mobile.get()=="Rs. 0.0":
        #                  messagebox.showerror("Error", "No product purchached")
            else:
                self.welcome_bill()
                      
                if self.tv.get()!=0:
                        self.textarea.insert(END,f"\n TV\t\t{self.tv.get()}\t\t{self.t_v}")
                        
                if self.ac.get()!=0:
                        self.textarea.insert(END,f"\n AC\t\t{self.ac.get()}\t\t{self.a_c}")
                        
                if self.battery.get()!=0:
                        self.textarea.insert(END,f"\n Battery\t\t{self.battery.get()}\t\t{self.batt}")
                
                if self.keyboard.get()!=0:
                        self.textarea.insert(END,f"\n Keyboard\t\t{self.keyboard.get()}\t\t{self.keybo}")
                        
                if self.smartphone.get()!=0:
                        self.textarea.insert(END,f"\n Smartphone\t\t{self.smartphone.get()}\t\t{self.smart}")
                        
                if self.keypad.get()!=0:
                        self.textarea.insert(END,f"\n Keypad\t\t{self.keypad.get()}\t\t{self.keypa}")

                        
                self.textarea.insert(END,f"\n -----------------------------------------")
                        
                if self.gst1 .get()!="Rs. 0.0":           
                        self.textarea.insert(END,f"\n Electronic Tax\t\t\t{self.gst1.get()}")

                if self.gst2 .get()!="Rs. 0.0":           
                        self.textarea.insert(END,f"\n Hardware Tax\t\t\t{self.gst2.get()}")

                if self.gst3 .get()!="Rs. 0.0":           
                        self.textarea.insert(END,f"\n Smartphone Tax\t\t\t{self.gst3.get()}")
                                
                self.textarea.insert(END,f"\n =========================================")
                self.textarea.insert(END,f"\n Total Amount\t\t\t\t{self.total_bill_value}")
                self.textarea.insert(END,f"\n =========================================")
                self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("save bil","Do you want to save fill??")
        if op>0:
                self.bill_saved=self.textarea.get('1.0',END)
                f1=open("Abhinav_Project_Billing/customerbill/"+str(self.cbill.get())+".txt", "w")
                f1.write(self.bill_saved)
                f1.close()
                messagebox.showinfo("Saved", f"Bill {self.cbill.get()} saved successfully!!")
        else:
                return

                    
    def search_saved_bill(self):
            present="yes"
            present="no"

            for i in os.listdir("bills/"):
                 if i.split('.')[0]==self.search_bill.get():
                        f1=open(f"Abhinav_Project_Billing/customerbill/{i}", "r")
                        self.textarea.delete('1.0', END)
                        for d in f1:
                             self.textarea.insert(END,d)
                        f1.close()
                        present="yes"
                 if present=="no":
                        messagebox.showerror("Error","Invalid bill number")

    def clear_bill_data(self):
                msg=messagebox.askyesno("Clear", "Are you sure to clear data..??")
                if msg>0:
                        self.cname.set("")
                        self.cphon.set("")

                        self.cbill.set("")
                        billl=random.randint(1000,99999)
                        self.cbill.set(str(billl))

                        self.search_bill.set("")
                        ############ Variables----------------
                        #1.electronic
                        self.tv.set(0)
                        self.ac.set(0)
                        #2
                        self.battery.set(0)
                        self.keyboard.set(0)
                        #3
                        self.smartphone.set(0)
                        self.keypad.set(0)
                        #############product price & Tax variable----------------------
                        self.electronic.set("")
                        self.hardware.set("")
                        self.mobile.set("")

                        self.gst1.set("")
                        self.gst2.set("")
                        self.gst3.set("")
                        self.welcome_bill()

    def exit_app(self):
            msg=messagebox.askyesno("EXIT", "Do you want to exit..??")
            if msg>0:
                self.root.destroy()

    def calc_wind(self):  
        self.top=Toplevel(root)
        call(["Abhinav_Project_billing", "calcu.py"])
        self.top.mainloop()


root = Tk() 
obj=Bill_App(root) 
root.mainloop()  