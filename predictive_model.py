#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import pickle
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns


# In[7]:


class Predict:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1560x768+0+0")
        self.root.minsize(1024,768)
        self.root.title("Dashboard")
        
        self.var_Sex_of_driver = StringVar()
        self.var_car_age = StringVar()
        self.var_Light_conditions = StringVar()
        self.var_Weather_conditions = StringVar()
        self.var_source = StringVar()
        self.var_destination = StringVar()
        self.var_age_of_driver = StringVar()
        
        
        title_lbl = Label(self.root,text="MODEL PREDICTION SYSTEM",font=("Helvetica",30,"bold"),bg="white",fg="dark turquoise")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        #main frame
        main_frame=Frame(self.root,bd=4,bg="white")
        main_frame.place(x=0,y=50,width=1480,height=640)

        #left label frame
        left_frame=LabelFrame(main_frame,bd=4,bg="white",relief=RIDGE,text="Road details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=660,height=620)
        
        #image
        self.img4= Image.open(r"C:\Users\MEER\Desktop\abishek india/road.png")
        self.img4= self.img4.resize((500,130),Image.ANTIALIAS)   #used to change high level image to low level image
        self.photoimg4=ImageTk.PhotoImage(self.img4)
        
        f_lbl = Label(left_frame,image=self.photoimg4)
        f_lbl.place(x=0,y=0,width=500,height=120)
        
        #cuurrent Record
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=120,width=620,height=120)
        
        
        #source combobox
        source_label=Label(current_course_frame,text="Source",font=("times new roman",12,"bold"),bg="white")
        source_label.grid(row=0,column=0,padx=10,sticky=W)
        
        source_combo=ttk.Combobox(current_course_frame,textvariable=self.var_source,state="readonly",font=("times new roman",12,"bold"),width=15)
        source_combo["values"]=("Select Source ",'Agra', 'Kanpur', 'Varanasi', 'delhi', 'Kolkata', 'Chennai',
                                   'Bengaluru', 'Hyderabad', 'Mumbai', 'Pune', 'Jaipur', 'Lucknow',
                                   'Patna') 
        source_combo.current(0)                                                     
        source_combo.grid(row=0,column=1,padx=0,pady=10,sticky=W)
        
        #destination combobox
        destination_label=Label(current_course_frame,text="Destination",font=("times new roman",12,"bold"),bg="white")
        destination_label.grid(row=0,column=2,padx=10,sticky=W)
        
        destination_combo=ttk.Combobox(current_course_frame,textvariable=self.var_destination,state="readonly",font=("times new roman",12,"bold"),width=15)
        destination_combo["values"]=("Select Destination ",'Delhi', 'Jaipur', 'Kanpur', 'Mathura', 'Lucknow', 'Allahabad',
                                       'agra', 'Varanasi', 'Chandigarh', 'Asansol', 'Durgapur',
                                       'Siliguri', 'Bhubaneswar', 'Bengaluru', 'Hyderabad', 'Coimbatore',
                                       'Madurai', 'Chennai', 'Mysuru', 'Mangaluru', 'Vijayawada',
                                       'Warangal', 'Visakhapatnam', ' Pune', 'Nashik', 'Surat',
                                       'Ahmedabad', 'Mumbai', 'Satara', 'Solapur', 'Ajmer', 'Udaipur',
                                       'Jodhpur', 'Patna', 'Gorakhpur', 'Gaya', 'Muzaffarpur') 
        destination_combo.current(0)                                                     
        destination_combo.grid(row=0,column=2,padx=150,sticky=W)
        
        #Road Information
        class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Road Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=245,width=630,height=350)
        
        
        #Gender label
        Gender_label=Label(class_student_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        Gender_label.grid(row=0,column=0,padx=5,sticky=W)
        
        #Gender combobox
        Gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_Sex_of_driver,state="readonly",font=("times new roman",12,"bold"),width=15)
        Gender_combo["values"]=("Select Gender",'Male', 'Unknown', 'Female') 
        Gender_combo.current(0)                                                     
        Gender_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)    
        
        
        #Light_conditions label
        Light_conditions_label=Label(class_student_frame,text="Light_condition",font=("times new roman",12,"bold"),bg="white")
        Light_conditions_label.grid(row=0,column=2,padx=5,sticky=W)
        
        # Light_conditions combobox
        Light_conditions_combo=ttk.Combobox(class_student_frame,textvariable=self.var_Light_conditions,state="readonly",font=("times new roman",12,"bold"),width=15)
        Light_conditions_combo["values"]=("Select Light_conditions",'Daylight', 'Darkness - lights lit')
        Light_conditions_combo.current(0)                                                     
        Light_conditions_combo.grid(row=0,column=3,padx=2,pady=15,sticky=W)
        
        
        #Weather_conditions label
        Weather_conditions_label=Label(class_student_frame,text="Weather_condition",font=("times new roman",12,"bold"),bg="white")
        Weather_conditions_label.grid(row=2,column=0,padx=5,sticky=W)
        
        # Weather_conditions combobox
        Weather_conditions_combo=ttk.Combobox(class_student_frame,textvariable=self.var_Weather_conditions,state="readonly",font=("times new roman",12,"bold"),width=15)
        Weather_conditions_combo["values"]=("Select Weather_conditions",'Normal', 'Raining', 'Cloudy')
        Weather_conditions_combo.current(0)                                                     
        Weather_conditions_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)
        
        
        #Service_year_of_vehicle label
        Service_year_of_vehicle_label=Label(class_student_frame,text="Car_Age",font=("times new roman",12,"bold"),bg="white")
        Service_year_of_vehicle_label.grid(row=2,column=2,padx=5,sticky=W)
        
        # Service_year_of_vehicle combobox
        Service_year_of_vehicle_combo=ttk.Combobox(class_student_frame,textvariable=self.var_car_age,state="readonly",font=("times new roman",12,"bold"),width=15)
        Service_year_of_vehicle_combo["values"]=("Select Car_Age",'Above 10yr', '5-10yrs', '1-2yr', '2-5yrs', 'Unknown', 'Below 1yr')
        Service_year_of_vehicle_combo.current(0)                                                     
        Service_year_of_vehicle_combo.grid(row=2,column=3,padx=2,pady=10,sticky=W)
        
        
        #age_of_driver label
        age_of_driver_label=Label(class_student_frame,text="age_of_driver",font=("times new roman",12,"bold"),bg="white")
        age_of_driver_label.grid(row=3,column=0,padx=5,sticky=W)
        
        # age_of_driver combobox
        age_of_driver_combo=ttk.Combobox(class_student_frame,textvariable=self.var_age_of_driver,state="readonly",font=("times new roman",12,"bold"),width=15)
        age_of_driver_combo["values"]=("Select age_of_driver",'18-30', '31-50', 'Over 51')
        age_of_driver_combo.current(0)                                                     
        age_of_driver_combo.grid(row=3,column=1,padx=2,pady=10,sticky=W)
        
        
        #Predict_btn
        predict_btn=Button(class_student_frame,text="PREDICT",command=self.predict,font=("times new roman",12,"bold"),bg="cyan",fg="black")
        predict_btn.place(x=200,y=180)
        
        #reset_btn
        reset_btn=Button(class_student_frame,text="RESET",command=self.reset_data,font=("times new roman",12,"bold"),bg="cyan",fg="black")
        reset_btn.place(x=300,y=180)
        
        #Result label
        self.result_label = Label(class_student_frame, text="", font=("times new roman", 12, "bold"), bg="white")
        self.result_label.place(x=100,y=250)

        
    def predict(self):
        
        with open('safe_road_final.pkl', 'rb') as file:
            model = pickle.load(file)
        source = self.var_source.get()
        destination = self.var_destination.get()
        Sex_of_driver = self.var_Sex_of_driver.get()
        Light_conditions = self.var_Light_conditions.get()
        Weather_conditions = self.var_Weather_conditions.get()
        age_of_driver = self.var_age_of_driver.get()
        car_age = self.var_car_age.get()
        
        data = pd.read_csv("./road_accident_final.csv")
        data = data[(data["source"] == source) & (data["destination"] ==destination)].iloc[:, :-2]
        if (len(data) == 0):
            
            messagebox.showerror("Error","No Road Exist Between Source & Destination",parent=self.root)
            
        else:
            data.drop(["Unnamed: 0"],axis=1,inplace=True)
            data["Sex_of_driver"] = Sex_of_driver
            data["car_age"] = car_age
            data["Light_conditions"] = Light_conditions
            data["Weather_conditions"] = Weather_conditions
            data["age_of_driver"] = age_of_driver
        

            prediction = model.predict(data)
            if prediction[0] == 1:
                self.result_label.config(text=f"Predicted value: {prediction[0]} ======> Model Suggesion: Road is Risky")  # Assuming the prediction is a single value
            elif prediction[0] == 2:
                self.result_label.config(text=f"Predicted value: {prediction[0]} ======> Model Suggesion: Road is Safe")
            else:
                self.result_label.config(text=f"Predicted value: {prediction[0]} ======> Model Suggesion: Road is Not Safe")




    def reset_data(self):
    
        self.var_source.set('Select Source')
        self.var_destination.set('Select Destination')
        self.var_Sex_of_driver.set('Select Gender')
        self.var_age_of_driver.set('Select age_of_driver')
        self.var_car_age.set('Select Car_Age')
        self.var_Light_conditions.set('Select Light_conditions')
        self.var_Weather_conditions.set('Select Weather_conditions')
            
        

        
    
if __name__ == "__main__":                                 
    root=Tk()
    obj = Predict(root)
    root.mainloop()


# In[ ]:




