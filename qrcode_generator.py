from tkinter import*
from PIL import ImageTk

import qrcode as qr


class qrimage:
    def __init__(self,root):
        self.root = root
        
        self.root.title("QR CODE GENERATOR")
        self.root.geometry("1000x500+180+70")
        # self.root.resizable(False,False)
        system_title = Label(self.root, text="QR CODE GENERATOR",font=("algerian",40,"bold","italic"),fg="black",bg="dodger blue")
        system_title.place(x=0,y=0,relwidth=1)
        
# ********************student details******************************
        df = Frame(self.root, bd = 10, relief=GROOVE)
        df.place(x = 60,y = 120,  width= 500,height = 340 )
        df_label = Label(df,font=("arial",18,"bold"),fg="black",bg="#FFEBCD",text ="Student Info")
        df_label.place(x=0,y=0,relwidth=1)

        self.name =StringVar()
        self.rollno= StringVar()
        self.prn= StringVar()
        self.classname = StringVar()

        df1 = Frame(self.root, bd = 10, relief=GROOVE)
        df1.place(x = 600,y = 120,  width= 300,height = 340 )
        df_label1 = Label(df1,font=("arial",18,"bold"),fg="black",bg="#FFEBCD",text ="Student info Qr code")
        df_label1.place(x=0,y=0,relwidth=1)

        self.qr_code = Label(df1,font=("times new roman",18,"bold"),fg="black",bg="#FFEBCD",text ="Qr not generated")
        self.qr_code.place(x=35,y=100,width=180,height=180)
        
# ******************************************************************************************************************************************************************************************************************************
        def getdata():
                print(self.name.get(),self.rollno.get(),self.prn.get(),self.classname.get())
                data = f"Student name:  {self.name.get()}\nRollno:      {self.rollno.get()}\nPrn:     {self.prn.get()}\nclass: {self.classname.get()}"
                img = qr.make(data)
                newimg = img.resize((180,180))
                newimg.save("rs.png")
                self.qrimage = ImageTk.PhotoImage(file="rs.png")  
                self.qr_code.config(image=self.qrimage)
# ***************************************************************************************************************************************************************************************************************************************

        buttons = Button(df,text="Generate QR",bg="deep sky blue",fg="black",font=("times new roman",12,"bold"),command=getdata ,width=23)
        buttons.place(x=90,y=270,width=200,height=40)
        
        st_name = Label(df,font=("arial",14,"bold"),fg="black",text ="Student Name",anchor="w")
        st_name.place(x=0,y=30,relwidth=1)
        st_name1 = Entry(df,font=("times new roman",12),bg="#FFF8DC",width=20,textvariable=self.name)
        st_name1.place(x= 170, y= 30,relwidth=1)

       
        st_rollno = Label(df,font=("arial",14,"bold"),fg="black",text ="Student rollno",anchor="w")
        st_rollno.place(x=0,y=60,relwidth=1)
        st_roll2 = Entry(df,font=("times new roman",12),bg="#FFF8DC",width=20,textvariable=self.rollno)
        st_roll2.place(x= 170, y= 60,relwidth=1)
        
        
        st_prn = Label(df,font=("arial",14,"bold"),fg="black",text ="Student prn",anchor="w")
        st_prn.place(x=0,y=90,relwidth=1)
        st_prn3 = Entry(df,font=("times new roman",12),bg="#FFF8DC",width=20,textvariable=self.prn)
        st_prn3.place(x= 170, y= 90,relwidth=1)
        
        
        st_classname = Label(df,font=("arial",14,"bold"),fg="black",text ="Student course",anchor="w")
        st_classname.place(x=0,y=120,relwidth=1)
        st_class4 = Entry(df,font=("times new roman",12),bg="#FFF8DC",width=20,textvariable=self.classname)
        st_class4.place(x= 170, y= 120,relwidth=1)

        

        
        


root = Tk()
obj = qrimage(root)
root.mainloop()
        