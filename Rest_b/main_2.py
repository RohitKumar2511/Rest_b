from tkinter import *
import random
import math
import os
from tkinter import messagebox
import login

class Bill:
    
    def __init__(self, root):
    
        self.root=root
        
        self.root.geometry("3558x1024+0+0")
        self.root.title("Billing Software")
        title= Label(self.root, text= "Billing Software", bd=12, relief=FLAT, bg="cyan4", fg= "white", font=("arial", 30, "bold"),pady=2).pack(fill=X)
        #####  creating customer frame    #####

        F1 = LabelFrame(self.root,bd=10, relief= FLAT, text = "Customer Details", font=("arial", 15, "bold"), fg="white", bg="cyan3")
        F1.place(x=0,y=74,relwidth=1)
        #####    creating customers items / products 
        F2 = LabelFrame(self.root,bd=10, relief= FLAT, text = "Starter", font=("arial", 15, "bold"), fg="white", bg="turquoise3")
        F2.place(x=1,y=173,width=330,height=380)

        #####   creating frame for grocerry product    #######

        F3 = LabelFrame(self.root,bd=10, relief= FLAT, text = "Main-Menu", font=("arial", 15, "bold"), fg="white", bg="turquoise3")
        F3.place(x=332,y=173,width=330,height=380)


        #####   creating frame for Cold Drinks   #######

        F4 = LabelFrame(self.root,bd=10, relief= FLAT, text = "Drinks & Drinks", font=("arial", 15, "bold"), fg="white", bg="turquoise3")
        F4.place(x=663,y=173,width=335,height=380)



        
        #####   Bill Area   #######

        F5 = Frame(self.root,bd=10, relief= GROOVE)
        F5.place(x=1005,y=175,width=361,height=380)


        #########~~~~~~~~~~~~~~    Varialbles  ~~~~~~~~~~~~~~~#########
        ###########            Cosmetics                 #####
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.loshan=IntVar()
        
        ##########    Grocery vars ############
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()

        ##########     Cold Drinks    #############

        self.mazaa = IntVar()
        self.cock = IntVar()
        self.frooti = IntVar()
        self.thumbs_up = IntVar()
        self.limca = IntVar()
        self.sprite = IntVar()

        #########       Total Product Price & Tax Variable          ################

        self.cosmetics_price  = StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()


        self.cosmetics_pric_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()

        ###########    Customer    #########

        self.c_name = StringVar()
        self.c_phon = StringVar()
        self.bill_no = StringVar()
        x=random.randint(1000,99999)
        self.bill_no.set(str(x))

        self.search_bill = StringVar()
    

        # customer label

        c_name_lbl= Label(F1, text="Customer Name",bg="cyan3", fg="white", font=("arial", 16)).grid(row=0, column=0,padx=15,pady=5)
        c_name_txt = Entry(F1, width=20,textvariable = self.c_name, font="arial 15",bd=7, relief=FLAT).grid(row=0,column=1, padx=7, pady=5)

        # for phone no

        c_phone_lbl= Label(F1, text="Phone No",bg="cyan3", fg="white", font=("arial", 16)).grid(row=0, column=2,padx=15,pady=5)
        c_phone_txt = Entry(F1, width=20,textvariable = self.c_phon, font="arial 15",bd=7, relief=FLAT).grid(row=0, column=3, padx=10, pady=5)

        # for order no

        c_order_no_lbl= Label(F1, text="Order No", bg="cyan3", fg="white", font=("arial", 16)).grid(row=0, column=4, padx=15, pady=5)
        c_order_no_txt = Entry(F1, width=20, textvariable = self.search_bill, font="arial 15",bd=7, relief=FLAT).grid(row=0, column=5, padx=10, pady=10)

        bill_btn= Button(F1, text="SEARCH", command=self.find_bill, relief=RAISED, bg="grey84", bd= 2, width=11, pady=11, font= ("arial", 12,"bold")).grid(row=0, column=6, padx= 20, pady=10)


    #######  Cosmetics Frame   ########


    
  #  F2 = LabelFrame(self.root,bd=10, relief= GROOVE, text = "Cosmetics Frame", font=("times new roman", 15, "bold"), fg="coral", bg="royalblue2")
  #   F2.place(x=0,y=80,width=1, height=)

        ##########   Cosmetics Items    ####################
        
        bath_lbl= Label(F2, text="Chaat", font=("arial",16),bg= "turquoise3", fg="white").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        bath_txt= Entry(F2, width=10, textvariable = self.soap, font=("arial",16),bd=5, relief=FLAT).grid(row=0, column=1 , padx=10, pady=10)

        face_cream_lbl = Label(F2, text="Chana", font=("arial",16),bg= "turquoise3", fg="white").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        face_cream_txt= Entry(F2, width=10, textvariable = self.face_cream, font=("arial",16),bd=5, relief=FLAT).grid(row=1, column=1 , padx=10, pady=10)
        

        Face_wah_lbl= Label(F2, text="Litti Chokha", font=("arial",16),bg= "turquoise3", fg="white").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        Face_wah_txt= Entry(F2, width=10, textvariable = self.face_wash ,font=("arial",16),bd=5, relief=FLAT).grid(row=2, column=1 , padx=10, pady=10)


        hair_spray_lbl= Label(F2, text="Masala Chicken", font=("arial",16),bg= "turquoise3", fg="white").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        hair_spray_txt= Entry(F2, width=10, textvariable = self.spray, font=("arial",16),bd=5, relief=FLAT).grid(row=3, column=1 , padx=10, pady=10)


        Hair_Gel_lbl= Label(F2, text="French Fries", font=("arial",16),bg= "turquoise3", fg="white").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        Hair_gel_txt= Entry(F2, width=10,textvariable = self.gell, font=("arial",16),bd=5, relief=FLAT).grid(row=4, column=1 , padx=10, pady=10)


        body_lotion_lbl= Label(F2, text="Samosha", font=("arial",16),bg= "turquoise3", fg="white").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        body_lotion_txt= Entry(F2, width=10, textvariable = self.loshan, font=("arial",16),bd=5, relief=FLAT).grid(row=5, column=1 , padx=10, pady=10)



##########   Grocery  items    ####################
       
        rice_lbl= Label(F3, text="Biryani", font=("arial",16),bg= "turquoise3", fg="white").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        rice_txt= Entry(F3, width=10, textvariable = self.rice, font=("arial",16),bd=5, relief=FLAT).grid(row=0, column=1 , padx=10, pady=10)

        food_oil_lbl = Label(F3, text="Tangri Kabab", font=("arial",16),bg= "turquoise3", fg="white").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        food_oil_txt= Entry(F3, width=10, textvariable = self.food_oil, font=("arial",16),bd=5, relief=FLAT).grid(row=1, column=1 , padx=10, pady=10)
        

        Daal_lbl= Label(F3, text="Chhole Chatore", font=("arial",16),bg= "turquoise3", fg="white").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        Daal_txt= Entry(F3, width=10,  textvariable = self.daal, font=("arial",16),bd=5, relief=FLAT).grid(row=2, column=1 , padx=10, pady=10)


        Wheat_lbl= Label(F3, text="Daal Chawal", font=("arial",16),bg= "turquoise3", fg="white").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        Wheat_spray_txt= Entry(F3, width=10,  textvariable = self.wheat, font=("arial",16),bd=5, relief=FLAT).grid(row=3, column=1 , padx=10, pady=10)


        sugar_lbl= Label(F3, text="Pav Bhaji", font=("arial",16),bg= "turquoise3", fg="white").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        sugar_txt= Entry(F3, width=10, textvariable = self.sugar, font=("arial",16),bd=5, relief=FLAT).grid(row=4, column=1 , padx=10, pady=10)


        Tea_lbl= Label(F3, text="Dal Puri", font=("arial",16),bg= "turquoise3", fg="white").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        Tea_txt= Entry(F3, width=10,  textvariable = self.tea, font=("arial",16),bd=5, relief=FLAT).grid(row=5, column=1 , padx=10, pady=10)


##########  Cold Drinks    ####################
       
        maza_lbl= Label(F4, text="Apple Juice", font=("arial",16),bg= "turquoise3", fg="white").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        maza_txt= Entry(F4, width=10,  textvariable = self.mazaa, font=("arial",16),bd=5, relief=FLAT).grid(row=0, column=1 , padx=10, pady=10)

        cock_lbl = Label(F4, text="Barfi", font=("arial",16),bg= "turquoise3", fg="white").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        cock_txt= Entry(F4, width=10,  textvariable = self.cock, font=("arial",16),bd=5, relief=FLAT).grid(row=1, column=1 , padx=10, pady=10)
        

        frooti_lbl= Label(F4, text="Cold Drink", font=("arial",16),bg= "turquoise3", fg="white").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        frooti_txt= Entry(F4, width=10, textvariable = self.frooti, font=("arial",16),bd=5, relief=FLAT).grid(row=2, column=1 , padx=10, pady=10)


        thumbs_up_lbl= Label(F4, text="Grape Juice", font=("arial",16),bg= "turquoise3", fg="white").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        thumbs_up_txt= Entry(F4, width=10,  textvariable = self.thumbs_up, font=("arial",16),bd=5, relief=FLAT).grid(row=3, column=1 , padx=10, pady=10)


        limca_lbl= Label(F4, text="Ice-Cream", font=("arial",16),bg= "turquoise3", fg="white").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        limca_txt= Entry(F4, width=10,  textvariable = self.limca, font=("arial",16),bd=5, relief=FLAT).grid(row=4, column=1 , padx=10, pady=10)


        sprite_lbl= Label(F4, text="Ice Tea", font=("arial",16),bg= "turquoise3", fg="white").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        sprite_txt= Entry(F4, width=10, textvariable = self.sprite, font=("arial",16),bd=5, relief=FLAT).grid(row=5, column=1 , padx=10, pady=10)



       #############     Bill Area      #############


        bill_title = Label(F5, text="Bill Area", font= "arial 15 bold", bd="7", relief= GROOVE).pack(fill=X)
        scrlbr = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scrlbr.set)
        scrlbr.pack(side=RIGHT, fill=Y)
        scrlbr.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)






        ###################   Button Area   ###########################

        F6 = LabelFrame(self.root,bd=10, relief= FLAT, text = "Total Taxes", font=("arial", 15, "bold"), fg="white", bg="cyan3")
        F6.place(x=0,y=554,relwidth=1, height=185)

        m1_lbl = Label(F6, text="Total Starter Price", bg="cyan3", fg="white", font=("arial",14)).grid(row=0, column=0, padx=20, pady=1, sticky="w")
        m1_txt = Entry(F6, width=18, textvariable = self.cosmetics_price, font="arial 10 bold", bd=7, relief=FLAT).grid(row=0, column=1, padx=10, pady=10)

        m2_lbl = Label(F6, text="Total Main-Course Price", bg="cyan3", fg="white", font=("arial",14)).grid(row=1, column=0, padx=20, pady=1, sticky="w")
        m2_txt = Entry(F6, width=18, textvariable = self.grocery_price, font="arial 10 bold", bd=7, relief=FLAT).grid(row=1, column=1, padx=10, pady=10)

        m3_lbl = Label(F6, text="Total Drinks Price", bg="cyan3", fg="white", font=("arial",14)).grid(row=2, column=0, padx=20, pady=1, sticky="w")
        m3_txt = Entry(F6, width=18, textvariable = self.cold_drink_price, font="arial 10 bold", bd=7, relief=FLAT).grid(row=2, column=1, padx=10, pady=10)



        c1_lbl = Label(F6, text="Starter Tax", bg="cyan3", fg="white", font=("arial",14)).grid(row=0, column=2, padx=20, pady=1, sticky="w")
        c1_txt = Entry(F6, width=18, textvariable = self.cosmetics_pric_tax, font="arial 10 bold", bd=7, relief=FLAT).grid(row=0, column=3, padx=10, pady=10)

        c2_lbl = Label(F6, text="Main-Course Tax", bg="cyan3", fg="white", font=("arial",14)).grid(row=1, column=2, padx=20, pady=1, sticky="w")
        c2_txt = Entry(F6, width=18, textvariable = self.grocery_tax, font="arial 10 bold", bd=7, relief=FLAT).grid(row=1, column=3, padx=10, pady=10)

        c3_lbl = Label(F6, text="Drinks Tax", bg="cyan3", fg="white", font=("arial",14)).grid(row=2, column=2, padx=20, pady=1, sticky="w")
        c3_txt = Entry(F6, width=18, textvariable = self.cold_drink_tax, font="arial 10 bold", bd=7, relief=FLAT).grid(row=2, column=3, padx=10, pady=10)


        #################    Button #########################

        btn = Frame(F6, bd=7, relief=GROOVE, bg="cyan2")
        btn.place(x=760,y= 0, width=585, height=160)


        total_btn = Button(btn, text="Total", command=self.total, bg="slategray4", fg="white", pady=11, width=10,bd=2, font="arial 15 bold").grid(row=0, column=0, padx=4, pady=5)

        B_bill_btn = Button(btn,command=self.bill_area, text="Generate Bill", bg="slategray4", fg="white", pady=11, width=12,bd=2, font="arial 15 bold").grid(row=0, column=1, padx=5, pady=5)
        Clear_btn = Button(btn,command=self.clear_data, text="Reset", bg="slategray4", fg="white", pady=11, width=10,bd=2, font="arial 15 bold").grid(row=0, column=2, padx=5, pady=5)
        Exit_btn = Button(btn, command=self.Exit, text="Exit", bg="slategray4", fg="white", pady=11, width=9,bd=2, font="arial 15 bold").grid(row=0, column=3, padx=5, pady=5)
        # menu_btn = Button(btn, text="Menu", bd=2, bg= "slategray4", fg="white", pady=11,width=10, fon="arial 15 bold").grid(row=1, column=0,padx=5, pady=4)
        self.welcome_bill()
    def total(self):
        self.c_s_p=self.soap.get()*39
        self.c_c_p=self.face_cream.get()*149
        self.c_f_p=self.face_wash.get()*29
        self.c_sp_p=self.spray.get()*129
        self.c_gl_p=self.gell.get()*65
        self.c_l_p=self.loshan.get()*49
        
        self.total_cosmetic_price = float(
                                self.c_s_p+
                                self.c_c_p+
                                self.c_f_p+
                                self.c_sp_p+
                                self.c_gl_p+
                                self.c_l_p
                                )
        self.cosmetics_price.set("Rs. "+str(self.total_cosmetic_price ))
        self.c_tax=round(self.total_cosmetic_price*0.05,3)
        self.cosmetics_pric_tax.set("Rs. "+str(self.c_tax))
                            
        self.g_r_p=self.rice.get()*59
        self.g_foil_p=self.food_oil.get()*79
        self.g_dl_p=self.daal.get()*29
        self.g_wht_p=self.wheat.get()*29
        self.g_sg_p=self.sugar.get()*65
        self.g_t_p=self.tea.get()*49

        self.total_grocery_price = float(                             
                                self.g_r_p+
                                self.g_foil_p+
                                self.g_dl_p+
                                self.g_wht_p+
                                self.g_sg_p+
                                self.g_t_p
                                )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price ))
        self.g_tax=round(self.total_grocery_price*0.05,3)
        self.grocery_tax.set("Rs. "+str(self.g_tax))

        self.cd_mz_p=self.mazaa.get()*25
        self.cd_ck_p=self.cock.get()*79
        self.cd_frt_p=self.frooti.get()*29
        self.cd_th_p=self.thumbs_up.get()*29
        self.cd_lim_p=self.limca.get()*65
        self.cd_sp_p=self.sprite.get()*49

        self.total_drinks_price = float(
                                self.cd_mz_p+
                                self.cd_ck_p+
                                self.cd_frt_p+
                                self.cd_th_p+
                                self.cd_lim_p+
                                self.cd_sp_p
                                )
        self.cold_drink_price.set("Rs. "+str(self.total_drinks_price ))
        self.cd_tax=round(self.total_drinks_price*0.05,3)
        self.cold_drink_tax.set("Rs. "+str(self.cd_tax))

        self.total_bill = float(self.total_cosmetic_price + self.total_drinks_price + self.total_grocery_price + self.c_tax + self.g_tax + self.cd_tax)



    def Exit(self):       
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:                                              #====================== exit fn ============================#
            self.root.destroy()

    def welcome_bill(self):
        self.txtarea.delete("1.0",END)
        self.txtarea.insert(END,"\n \tWELCOME TO OURS RESTAURENT\t \n")
        self.txtarea.insert(END,f"\nBill no: {self.bill_no.get()}")
        self.txtarea.insert(END,f"\nCustomer Name : {self.c_name.get()}")  
        self.txtarea.insert(END,f"\nPhone no : {self.c_phon.get()}")
        self.txtarea.insert(END,f"\n======================================")
        self.txtarea.insert(END,f"\n Products \t\tQTY \t\tPrice")
        self.txtarea.insert(END,f"\n======================================")


    def bill_area(self):
        self.welcome_bill()
        if self.c_name.get() == "" or self.c_phon.get() == "":
            messagebox.showerror("Error", "Customer details are must")
        elif self.cosmetics_price == "Rs. 0.0" or self.grocery_price == "Rs. 0.0" or self.cold_drink_price == "Rs. 0.0":
            messagebox.showerror("Error", "No product purchased")
        else:
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\n Chaat\t\t{self.soap.get()}\t\t{self.c_s_p}")
            if self.face_cream.get()!=0:
                self.txtarea.insert(END,f"\n Chana Masala\t\t{self.face_cream.get()}\t\t{self.c_c_p}")
            if self.face_wash.get()!=0:
                self.txtarea.insert(END,f"\n Litti Chokha\t\t{self.face_wash.get()}\t\t{self.c_f_p}")
            if self.spray.get()!=0:
                self.txtarea.insert(END,f"\n Masala Chicken\t\t{self.spray.get()}\t\t{self.c_sp_p}")
            if self.gell.get()!=0:
                self.txtarea.insert(END,f"\n French Fries \t\t{self.gell.get()}\t\t{self.c_gl_p}")
            if self.loshan.get()!=0:
                self.txtarea.insert(END,f"\nSamosa\t\t{self.loshan.get()}\t\t{self.c_l_p}")

            if self.rice.get()!=0:
                self.txtarea.insert(END,f"\n Biryani\t\t{self.rice.get()}\t\t{self.g_r_p}")
            if self.food_oil.get()!=0:
                self.txtarea.insert(END,f"\n Tangri Kabab\t\t{self.food_oil.get()}\t\t{self.g_foil_p}")
            if self.daal.get()!=0:
                self.txtarea.insert(END,f"\n Chhole Bhatore\t\t{self.daal.get()}\t\t{self.g_dl_p}")
            if self.wheat.get()!=0:
                self.txtarea.insert(END,f"\n Daal Chawal\t\t{self.wheat.get()}\t\t{self.g_wht_p}")
            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\n Pav Bhaji \t\t{self.sugar.get()}\t\t{self.g_sg_p}")
            if self.tea.get()!=0:
                self.txtarea.insert(END,f"\n Dal Puri\t\t{self.tea.get()}\t\t{self.g_t_p}")

            if self.mazaa.get()!=0:
                self.txtarea.insert(END,f"\n Apple Juice\t\t{self.mazaa.get()}\t\t{self.cd_mz_p}")
            if self.cock.get()!=0:
                self.txtarea.insert(END,f"\n Barfi\t\t{self.cock.get()}\t\t{self.cd_ck_p}")
            if self.frooti.get()!=0:
                self.txtarea.insert(END,f"\n Cold Drink\t\t{self.frooti.get()}\t\t{self.cd_frt_p}")
            if self.thumbs_up.get()!=0:
                self.txtarea.insert(END,f"\n Grape Juice\t\t{self.thumbs_up.get()}\t\t{self.cd_th_p}")
            if self.limca.get()!=0:
                self.txtarea.insert(END,f"\n Ice Cream \t\t{self.limca.get()}\t\t{self.cd_lim_p}")
            if self.sprite.get()!=0:
                self.txtarea.insert(END,f"\n Ice Tea\t\t{self.sprite.get()}\t\t{self.cd_sp_p}")


            self.txtarea.insert(END,f"\n--------------------------------------")
            if self.cosmetics_pric_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END,f"\n Starter Tax\t\t\t{self.cosmetics_pric_tax.get()}")

            if self.grocery_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END,f"\nMain-Course Tax\t\t\t{self.grocery_tax.get()}")

            if self.cold_drink_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END,f"\n Drinks & Deserts Tax\t\t\t{self.cold_drink_tax.get()}")

            self.txtarea.insert(END,f"\n Total Bill : \t\t\tRs. {self.total_bill}")
            self.txtarea.insert(END,f"\n--------------------------------------")

            self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data = self.txtarea.get("1.0",END)
            #   f1 = open("D:\\A1 Ideas\\bills/"+str(self.bill_no.get())+".txt","w")
            f1 = open("D:\\Pro_Grammer\\rest_bill\\bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. : {self.bill_no.get()} save successfully")
        else:
            return


    def find_bill(self):
        present="no"
        for I in os.listdir("D:\\Pro_Grammer\\rest_bill\\bills/"):
            if( I.split(".")[0])==self.search_bill.get():
                f1=open(f"D:\\Pro_Grammer\\rest_bill\\bills/{I}","r")
                self.txtarea.delete("1.0",END)
                #   self.txtarea.insert(END,f1)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")

    def clear_data(self):
        op=messagebox.askyesno("Reset","Do you really want to Reset data?")
        if op>0:                                              #====================== exit fn ============================#
                    
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gell.set(0)
            self.loshan.set(0)
            
            ##########    Grocery vars ############
            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)

            ##########     Cold Drinks    #############

            self.mazaa.set(0)
            self.cock.set(0)
            self.frooti.set(0)
            self.thumbs_up.set(0)
            self.limca.set(0)
            self.sprite.set(0)

            #########       Total Product Price & Tax Variable          ################

            self.cosmetics_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")


            self.cosmetics_pric_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")

            ###########    Customer    #########

            self.c_name.set("")
            self.c_phon.set("")
            self.bill_no.set("")
            x=random.randint(1000,99999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()




root= Tk()
obj = Bill(root)
root.mainloop()

