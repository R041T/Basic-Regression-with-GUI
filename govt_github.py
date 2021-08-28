# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 12:25:24 2019

@author: Rohit
"""

import mysql.connector
import numpy as np
import pandas as pd
import tkinter as tk
import array as arr
root = tk.Tk()












#####################################Merge sort code############################################


###################################### Mysql connection setup ############################
config = {
        'user' : 'root', 
        'password' :'Enter Password', 
        'host' : 'localhost',
        'ssl_ca' : 'Enter the certificate',
        'use_pure' : 'False'
    }
mydb = mysql.connector.connect(**config);


mycursor = mydb.cursor(buffered=True)

mycursor.execute("use dsa")

for x in mycursor:
  print(x)

################################################ Machine Learning Pre processing#####################

dataset = pd.read_csv('Project_data.csv')
X = (dataset.iloc[:, 1:3].values)
y = dataset.iloc[:, 3].values



from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
  
##########################Creating the UI#######################################################

class mainframe(tk.Tk):
    def __init__(self, *args, **kwargs): 
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        for F in (Login_Page,HomePage,ViewPage,Predict,AddEntry,UpdateEntry,RemoveEntry):
        
            frame = F(container, self)
    
            self.frames[F] = frame
    
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Login_Page)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class Login_Page(tk.Frame):
    def __init__(self,parent,controller):
        self.controller=controller
        tk.Frame.__init__(self,parent)
        usernamelabel=tk.Label(self,text="Name")
        passwordlabel=tk.Label(self,text="Password")
        self.user_entry=tk.Entry(self)
        self.pass_entry=tk.Entry(self,show="*")
        
        usernamelabel.grid(row=0)
        passwordlabel.grid(row=1)
        self.user_entry.grid(row=0,column=1)
        self.pass_entry.grid(row=1,column=1)
        
        login_button=tk.Button(self,text="Login",command=self.loginbuttonclick)
        login_button.grid(columnspan=2)
    
    def loginbuttonclick(self):
        username=self.user_entry.get()
        password=self.pass_entry.get()
        mycursor.execute("Select password from login where username=%s",[str(username)])
        result = mycursor.fetchall()
        if(int(result[0][0])==int(password)):   
            self.controller.show_frame(HomePage)
        else:
            print("Invalid Password")
        
        
class HomePage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        Viewpagebutton=tk.Button(self,text="View data",command=lambda:controller.show_frame(ViewPage))
        Viewpagebutton.grid(row=1,column=1)
        Addpagebutton=tk.Button(self,text="Add data",command=lambda:controller.show_frame(AddEntry))
        Addpagebutton.grid(row=1,column=5)
        Updatebutton=tk.Button(self,text="Update data",command=lambda:controller.show_frame(UpdateEntry))
        Updatebutton.grid(row=1,column=9)
        Predictpagebutton=tk.Button(self,text="Predict",command=lambda:controller.show_frame(Predict))
        Predictpagebutton.grid(row=1,column=14)
        Removepagebutton=tk.Button(self,text="Remove data",command=lambda:controller.show_frame(RemoveEntry))
        Removepagebutton.grid(row=1,column=19)
        Exitbutton=tk.Button(self,text="Exit",command=lambda:app.destroy())
        Exitbutton.grid(row=1, column=23)
        
class ViewPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        viewbutton=tk.Button(self,text="View ",command=self.showdata)
        viewbutton.grid(row=1)
        Addpagebutton=tk.Button(self,text="Add another entry",command=lambda:controller.show_frame(AddEntry))
        Addpagebutton.grid(row=0,column=4)
        Backbutton=tk.Button(self,text="Go Back",command=lambda:controller.show_frame(HomePage))
        Backbutton.grid(row=0,column=8)
        Exitbutton=tk.Button(self,text="Exit",command=lambda:app.destroy())
        Exitbutton.grid(columnspan=2)
        
        Removebutton=tk.Button(self,text="delete least polluted",command=self.removeleast) 
        Removebutton.grid(row=0,column=15)
       
        
       
        
        
    def removeleast(self):
        mycursor.execute("select * from pollute")
        result = mycursor.fetchall()
        l=result
        
        
        def mergeSort(arr): 
            if len(arr) >1: 
                mid = len(arr)//2 
                L = arr[:mid]
                R = arr[mid:]
                
                mergeSort(L) 
                mergeSort(R)  
          
                i = j = k = 0
                  
                
                while i < len(L) and j < len(R): 
                    if L[i][3] < R[j][3]: 
                        arr[k] = L[i] 
                        i+=1
                    else: 
                        arr[k] = R[j] 
                        j+=1
                    k+=1
                  
            
                while i < len(L): 
                    arr[k] = L[i] 
                    i+=1
                    k+=1
                  
                while j < len(R): 
                    arr[k] = R[j] 
                    j+=1
                    k+=1
                    
        mergeSort(l)
        least = l
        mycursor.execute("DELETE FROM pollute WHERE air = %s",[least[0][3]])
        mydb.commit()
        
    
    def showdata(self):
        mycursor.execute("select * from pollute")
        result = mycursor.fetchall()
        l=result
        
        
        def mergeSort(arr): 
            if len(arr) >1: 
                mid = len(arr)//2 
                L = arr[:mid]
                R = arr[mid:]
                
                mergeSort(L) 
                mergeSort(R)  
          
                i = j = k = 0
                  
                
                while i < len(L) and j < len(R): 
                    if L[i][3] < R[j][3]: 
                        arr[k] = L[i] 
                        i+=1
                    else: 
                        arr[k] = R[j] 
                        j+=1
                    k+=1
                  
            
                while i < len(L): 
                    arr[k] = L[i] 
                    i+=1
                    k+=1
                  
                while j < len(R): 
                    arr[k] = R[j] 
                    j+=1
                    k+=1
                    
        mergeSort(l)
        data = l
        
        for i in range(len(data)):
            print(data[i][0]," ",data[i][1]," ",data[i][2]," ",data[i][3])
        
        print("\n\n\n\n###########################################")

        
        
class AddEntry(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        
        Addlabel1=tk.Label(self,text="Enter City name")
        Addlabel1.grid(row=0,column=0)
        Addlabel2=tk.Label(self,text="Enter Number of vehicles in the region")
        Addlabel2.grid(row=1,column=0)
        Addlabel3=tk.Label(self,text="Enter Area of region")
        Addlabel3.grid(row=2,column=0)
        
        self.AddEntry1=tk.Entry(self)
        self.AddEntry2=tk.Entry(self)
        self.AddEntry3=tk.Entry(self)
        self.AddEntry1.grid(row=0,column=1)
        self.AddEntry2.grid(row=1,column=1)
        self.AddEntry3.grid(row=2,column=1)
        
        Addbutton=tk.Button(self,text="Add to database",command=self.addentry)
        Addbutton.grid(row=4,column=4)
        
        Backbutton=tk.Button(self,text="Go Back",command=lambda:controller.show_frame(HomePage))
        Backbutton.grid(row=0,column=8)
        
        Exitbutton=tk.Button(self,text="Exit",command=lambda:app.destroy())
        Exitbutton.grid(columnspan=2)
        
    def addentry(self):
        city = self.AddEntry1.get()
        num = self.AddEntry2.get()
        area = self.AddEntry3.get()
        z=[int(num),float(area)]
        a = arr.array('f', z)
        air = regressor.predict(np.reshape(a,(-1,2)))
        mycursor.execute("insert into pollute values(%s,%s,%s,%s)",[str(city),int(num),float(area),float(air)])
        mydb.commit()
         
        
        
class UpdateEntry(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        
        Updatelabel1=tk.Label(self,text="Enter City name You'd like to update details of")
        Updatelabel1.grid(row=0,column=0)
        Updatelabel2=tk.Label(self,text="Enter new Number of vehicles in the region")
        Updatelabel2.grid(row=1,column=0)
        Updatelabel3=tk.Label(self,text="Enter new Area of region")
        Updatelabel3.grid(row=2,column=0)
        
        
        self.UpdateEntry1=tk.Entry(self)
        self.UpdateEntry2=tk.Entry(self)
        self.UpdateEntry3=tk.Entry(self)
        self.UpdateEntry1.grid(row=0,column=1)
        self.UpdateEntry2.grid(row=1,column=1)
        self.UpdateEntry3.grid(row=2,column=1)
        
        Updatebutton=tk.Button(self,text="Update the entry",command=self.updateentry)
        Updatebutton.grid(row=4,column=4)
        
        Backbutton=tk.Button(self,text="Go Back",command=lambda:controller.show_frame(HomePage))
        Backbutton.grid(row=0,column=8)
        
        Exitbutton=tk.Button(self,text="Exit",command=lambda:app.destroy())
        Exitbutton.grid(columnspan=2)
        
    def updateentry(self):
        city = self.UpdateEntry1.get()
        num = self.UpdateEntry2.get()
        area = self.UpdateEntry3.get()
        z=[int(num),float(area)]
        a = arr.array('f', z)
        air = regressor.predict(np.reshape(a,(-1,2)))
        mycursor.execute("UPDATE pollute SET num = %s,area=%s,air=%s WHERE city = %s",[int(num),float(area),float(air),str(city)])
        mydb.commit()        
        
class RemoveEntry(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        
        Removelabel1=tk.Label(self,text="Enter City name You'd like to remove details of")
        Removelabel1.grid(row=0,column=0)
        self.RemoveEntry1=tk.Entry(self)
        self.RemoveEntry1.grid(row=0,column=1)

        
        Updatebutton=tk.Button(self,text="Remove the entry",command=self.removeentry)
        Updatebutton.grid(row=4,column=4)
        
        Backbutton=tk.Button(self,text="Go Back",command=lambda:controller.show_frame(HomePage))
        Backbutton.grid(row=0,column=8)
        
        Exitbutton=tk.Button(self,text="Exit",command=lambda:app.destroy())
        Exitbutton.grid(columnspan=2)
        
    def removeentry(self):
        city = self.RemoveEntry1.get()
        mycursor.execute("DELETE FROM pollute WHERE city = %s",[str(city)])
        mydb.commit() 
        
class Predict(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        
        Addlabel1=tk.Label(self,text="Enter City name")
        Addlabel1.grid(row=0,column=0)
        Addlabel2=tk.Label(self,text="Enter Number of vehicles in the region")
        Addlabel2.grid(row=1,column=0)
        Addlabel3=tk.Label(self,text="Enter Area of region")
        Addlabel3.grid(row=2,column=0)
        
        
        self.AddEntry1=tk.Entry(self)
        self.AddEntry2=tk.Entry(self)
        self.AddEntry3=tk.Entry(self)
        self.AddEntry1.grid(row=0,column=1)
        self.AddEntry2.grid(row=1,column=1)
        self.AddEntry3.grid(row=2,column=1)
        
        
        predictbutton=tk.Button(self,text="Predict pollution index",command=self.Predictval)
        predictbutton.grid(row=4,column=0)
        Addbutton=tk.Button(self,text="Add to database",command=self.addentry)
        Addbutton.grid(row=4,column=4)
        
        Backbutton=tk.Button(self,text="Go Back",command=lambda:controller.show_frame(HomePage))
        Backbutton.grid(row=0,column=8)
                
        Exitbutton=tk.Button(self,text="Exit",command=lambda:app.destroy())
        Exitbutton.grid(row=1,column=8)
        
    def Predictval(self):
        num = self.AddEntry2.get()
        area = self.AddEntry3.get()
        z=[int(num),float(area)]
        a = arr.array('f', z)
        air = regressor.predict(np.reshape(a,(-1,2)))
        OutputLabel=tk.Label(self,text=air)
        OutputLabel.grid(row=4,column=1)
        mydb.commit()
        
    def addentry(self):
        city = self.AddEntry1.get()
        num = self.AddEntry2.get()
        area = self.AddEntry3.get()
        z=[int(num),float(area)]
        a = arr.array('f', z)
        air = regressor.predict(np.reshape(a,(-1,2)))
        mycursor.execute("insert into pollute values(%s,%s,%s,%s)",[str(city),int(num),float(area),float(air)])
        mydb.commit()
        

   
    

        
app=mainframe()
app.mainloop()

#########################

#########################
