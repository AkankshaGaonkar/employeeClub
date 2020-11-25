from tkinter import*
import tkinter.messagebox
import EmpDatabase_backend
#Frontend

class Employee:
        def __init__(self, root):
                self.root =root
                self.root.title("Employee Database Management System")
                self.root.geometry("1350x750+0+0")
                self.root.config(bg="cadet blue")
                EmpID = StringVar()
                Firstname = StringVar()
                Surname = StringVar()
                DOB = StringVar()
                Age = StringVar()
                Gender = StringVar()
                Address = StringVar()
                Mobile = StringVar()
                #===========================================================================Function Declaration=========================================================================
                def iExit():
                        iExit = tkinter.messagebox.askyesno("Students Database Management Systems","Confirm if you want to exit")
                        if iExit > 0:
                                root.destroy()
                        return

                def clearData():
                        self.txtEmpID.delete (0,END)
                        self.txtfna.delete (0,END)
                        self.txtSna.delete (0,END)
                        self.txtDOB.delete (0,END)
                        self.txtAge.delete (0,END)
                        self.txtGender.delete (0,END)
                        self.txtAdr.delete (0,END)
                        self.txtMobile.delete (0,END)

                def addData():
                        if(len(EmpID.get())!=0):
                                EmpDatabase_backend.addEmpRec(EmpID.get(), Firstname.get(), Surname.get(), DOB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get())
                        employeelist.delete(0,END)
                        employeelist.insert(END,(EmpID.get(), Firstname.get(), Surname.get(), DOB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get()))
                     
                def DisplayData():
                        employeelist.delete(0,END)
                        for row in EmpDatabase_backend.viewData():
                                employeelist.insert(END,row,str(""))

                def EmployeeRec(event):
                        global ed
                        searchEmp = employeelist.curselection()[0]
                        ed = employeelist.get(searchEmp)

                        self.txtEmpID.delete (0,END)
                        self.txtEmpID.insert (END,ed[1])
                        self.txtfna.delete (0,END)
                        self.txtfna.insert(END,ed[2])
                        self.txtSna.delete (0,END)
                        self.txtSna.insert (END,ed[3])
                        self.txtDOB.delete (0,END)
                        self.txtDOB.insert (END,ed[4])
                        self.txtAge.delete (0,END)
                        self.txtAge.insert (END,ed[5])
                        self.txtGender.delete (0,END)
                        self.txtGender.insert (END,ed[6])
                        self.txtAdr.delete (0,END)
                        self.txtAdr.insert (END,ed[7])
                        self.txtMobile.delete (0,END)
                        self.txtMobile.insert (END,ed[8])

                def deleteData():
                        if(len(EmpID.get())!=0):
                                EmpDatabase_backend.deleteRec(ed[0])
                        clearData()
                        DisplayData()

                def searchDatabase():
                        employeelist.delete(0,END)
                        for row in EmpDatabase_backend.searchData(EmpID.get(), Firstname.get(), Surname.get(), DOB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get() ):
                                employeelist.insert(END,row,str(""))

                def update():
                        if(len(EmpID.get())!=0):
                                EmpDatabase_backend.deleteRec(ed[0])
                        if(len(EmpID.get())!=0):
                                EmpDatabase_backend.addEmpRec(EmpID.get(), Firstname.get(), Surname.get(), DOB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get())
                                employeelist.delete(0,END)
                                employeelist.insert(END,(EmpID.get(), Firstname.get(), Surname.get(), DOB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get()))
                #===========================================================================Frame=========================================================================
                MainFrame = Frame(self.root, bg="cadet blue")
                MainFrame.grid()

                TitFrame = Frame(MainFrame, bd=2, padx=54,pady=8, bg="Ghost White", relief=RIDGE)
                TitFrame.pack(side=TOP)

                self.lblTit = Label(TitFrame, font=('arial',47,'bold'), text="Employee Database Management System", bg="Ghost White")
                self.lblTit.grid(sticky=W)

                ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=18,pady=10, bg="Ghost White", relief=RIDGE)
                ButtonFrame.pack(side=BOTTOM)

                DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, bg="cadet blue", relief=RIDGE)
                DataFrame.pack(side=BOTTOM)

                DataFrameLEFT =LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20, bg="Ghost White", relief=RIDGE, font=('arial', 20,'bold'), text="Employee Membership Info:\n")
                DataFrameLEFT.pack(side=LEFT)

                DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31,pady=3, bg="Ghost White", relief=RIDGE, font=('arial', 20,'bold'), text="Employee Details\n")
                DataFrameRIGHT.pack(side=RIGHT)
                #===========================================================================Labels and Entry Widget========================================================
                self.lblEmpID =Label(DataFrameLEFT, font=('arial',20,'bold'), text="Employee ID:", padx=2,pady=2, bg="Ghost White")
                self.lblEmpID.grid(row=0, column=0, sticky=W)
                self.txtEmpID =Entry(DataFrameLEFT, font=('arial',20,'bold'), textvariable=EmpID, width=39)
                self.txtEmpID.grid(row=0, column=1)
	    
                self.lblfna =Label(DataFrameLEFT, font=('arial',20,'bold'), text="Firstname:", padx=2,pady=2, bg="Ghost White")
                self.lblfna.grid(row=1, column=0, sticky=W)
                self.txtfna =Entry(DataFrameLEFT ,font=('arial',20,'bold'),textvariable = Firstname, width=39)
                self.txtfna.grid(row=1, column=1)

                self.lblSna =Label(DataFrameLEFT, font=('arial',20,'bold'), text="Surname:", padx=2,pady=2, bg="Ghost White")
                self.lblSna.grid(row=2, column=0, sticky=W)
                self.txtSna =Entry(DataFrameLEFT, font=('arial',20,'bold'), textvariable = Surname, width=39)
                self.txtSna.grid(row=2, column=1)

                self.lblDOB =Label(DataFrameLEFT, font=('arial',20,'bold'), text="Date of Birth:", padx=2,pady=3, bg="Ghost White")
                self.lblDOB.grid(row=3, column=0, sticky=W)
                self.txtDOB =Entry(DataFrameLEFT, font=('arial',20,'bold'), textvariable = DOB, width=39)
                self.txtDOB.grid(row=3, column=1)

                self.lblAge =Label(DataFrameLEFT ,font=('arial',20,'bold'),text="Age:", padx=2,pady=3,bg="Ghost White")
                self.lblAge.grid(row=4, column=0, sticky=W)
                self.txtAge =Entry(DataFrameLEFT ,font=('arial',20,'bold'),textvariable = Age, width=39)
                self.txtAge.grid(row=4, column=1)
        
                self.lblGender =Label(DataFrameLEFT ,font=('arial',20,'bold'),text="Gender:", padx=2,pady=3,bg="Ghost White")
                self.lblGender.grid(row=5, column=0, sticky=W)
                self.txtGender =Entry(DataFrameLEFT ,font=('arial',20,'bold'),textvariable = Gender, width=39)
                self.txtGender.grid(row=5, column=1)
	
                self.lblAdr = Label(DataFrameLEFT ,font=('arial',20,'bold'),text="Address:", padx=2,pady=3,bg="Ghost White")
                self.lblAdr.grid(row=6, column=0, sticky=W)
                self.txtAdr =Entry(DataFrameLEFT ,font=('arial',20,'bold'),textvariable = Address, width=39)
                self.txtAdr.grid(row=6, column=1)

                self.lblMobile =Label(DataFrameLEFT, font=('arial',20,'bold'),text="Mobile:", padx=2,pady=3, bg="Ghost White")
                self.lblMobile.grid(row=7, column=0, sticky=W)
                self.txtMobile =Entry(DataFrameLEFT, font=('arial',20,'bold'), textvariable = Mobile, width=39)
                self.txtMobile.grid(row=7, column=1)
                #===========================================================================ListBox & ScrollBar Widget========================================================
                scrollbar = Scrollbar(DataFrameRIGHT)
                scrollbar.grid(row=0, column=1, sticky='ns')

                employeelist = Listbox(DataFrameRIGHT, width=41, height=16, font=('arial',12,'bold'), yscrollcommand=scrollbar.set)
                employeelist.bind('<<ListboxSelect>>', EmployeeRec)
                employeelist.grid(row=0, column=0, padx=8)
                scrollbar.config(command = employeelist.yview)
                #===========================================================================Button Widget========================================================
                self.btnaddData = Button(ButtonFrame, text="Add New", font=('arial',20,'bold'),width=10, height=1, bd=4, command=addData)
                self.btnaddData.grid(row=0, column=0)
        
                self.btnDisplayData = Button(ButtonFrame, text="Display", font=('arial',20,'bold'),width=10, height=1, bd=4, command=DisplayData)
                self.btnDisplayData .grid(row=0, column=1)
        
                self.btnClearData = Button(ButtonFrame, text="Clear", font=('arial',20,'bold'),width=10, height=1, bd=4, command = clearData)
                self.btnClearData.grid(row=0, column=2)
        
                self.btndeleteData = Button(ButtonFrame, text="Delete", font=('arial',20,'bold'),width=10, height=1, bd=4, command = deleteData)
                self.btndeleteData.grid(row=0, column=3)
        
                self.btnSearchData = Button(ButtonFrame, text="Search", font=('arial',20,'bold'),width=10, height=1, bd=4, command =searchDatabase)
                self.btnSearchData.grid(row=0, column=4)
        
                self.btnUpdateData = Button(ButtonFrame, text="Update", font=('arial',20,'bold'),width=10, height=1, bd=4, command =update)
                self.btnUpdateData.grid(row=0, column=5)
        
                self.btnExit = Button(ButtonFrame, text="Exit", font=('arial',20,'bold'),width=10, height=1, bd=4, command=iExit)
                self.btnExit.grid(row=0, column=6)
        
if __name__=='__main__':
    root = Tk()
    application = Employee(root)
    root.mainloop()
