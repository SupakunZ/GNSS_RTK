from logging import makeLogRecord
import numbers
from os import remove
from turtle import clear
import folium
import webbrowser
from tkinter.messagebox import * 
from tkinter import *
import tkinter as tk
import numpy as np
import time
import serial
import string
import serial.tools.list_ports
import tkintermapview
from tkinter import ttk
import tkinter
from geopy import distance
import customtkinter
from tkinter import messagebox



# Main window
root = tkinter.Tk()
root.title('MapView')
root.geometry("950x950")

#ตัวแปร
variable1=StringVar() #ตัวแปรเก็บค่า Latitude ณ ตำแหน่งปัจจุบัน
variable2=StringVar() #ตัวแปรเก็บค่า Lontitude ณ ตำแหน่งปัจจุบัน
variable3=StringVar() #ตัวแปร Check การเชื่อมต่อ Port
variable4=StringVar() #ตัวแปรเก็บค่า Latitude ณ ตำแหน่งTarget
variable5=StringVar() #ตัวแปรเก็บค่า Latitude ณ ตำแหน่งTarget
Distance = StringVar() #ตัวแปรเก็บค่าระยะห่างระหว่างสองจุด
marker_list = []
marker_list1 = []
marker_path = None



#Port Function
def check_port():
    comlist = serial.tools.list_ports.comports()
    connected = []
    for element in comlist:
        connected.append(element.device)
    if connected==['/dev/ttyUSB0'] :
        print("Connect")
        c ='Connected'
        variable3.set(str(c))
        port2 = Label(my_frame, textvariable=variable3, font=("Helvetica", 16),fg='green')
        port2.grid(row=3, column=1, pady=10, padx=10)
        
    if connected==[] :
        print("Disconnect")
        b = 'Disconnected'
        variable3.set(str(b))
        port2 = Label(my_frame, textvariable=variable3, font=("Helvetica", 16),fg='red')
        port2.grid(row=3, column=1, pady=10, padx=10)

        tkinter.messagebox.showwarning(title="Error", message="Please check the RTK connection and try again.")
        
    root.update()


#Lat,Lon Fucntion ณ ตำแหน่วงปัจจุบัน
def carte():
    F = open('myfile.txt','r') #อ่านค่า Lat,Lon ณ ตำแน่งปัจจุบันจาก myfile.txt --สามารถเใช้ชื่อไฟล์อื่นได้แต่ต้องแก้ไข Code ที่บรรทัด 69 80 113 ให้เหมือนกับชื่อไฟล์ที่เปลี่ยน
    M = F.readlines()
    str=M
    number0 =[]
    i=0
    for item in str:
        number0.append(float(item))
       
    map_widget.set_position(number0[0],number0[1])

    while True:
        F = open('myfile.txt','r') #เปลี่ยนชื่อได้
        M = F.readlines()
        str=M
        number0 =[]
        for item in str:
            number0.append(float(item))

        for x in range(0,len(number0)):
            i='%.5f'%(number0[0])
            variable1.set(float(i))
            j='%.5f'%(number0[1])
            variable2.set(float(j))
        
        marker_list.append(map_widget.set_marker(number0[0],number0[1]))
        
        
        for marker in marker_list:
            marker.delete()            
            time.sleep(0.15)# Delay  


        root.update()

#Generate Path สร้างเส้นทาง
def part():
    a=0
    b=1
 
    #Meter
    lon3=Label(my_frame, text = 'm', font=("Helvetica", 16))
    lon3.grid(row=1, column=5,pady=10, padx=10)
    
    while True:
        F1 = open('myfile.txt','r') #เปลี่ยนชื่อได้
        M1 = F1.readlines()
        str=M1
        number1 =[]
        position_list = []
        
        for item in str:
            number1.append(float(item))

        #lat,lon
        for item in str:
            number1.append(float(item))
        for x in range(0,len(number1)):
            i='%.5f'%(number1[0])
            variable1.set(float(i))
            j='%.5f'%(number1[1])
            variable2.set(float(j))
                
    #point
        f3 = open('Lat-Longv.txt','r') #อ่านค่าจากข้อมูล path ที่เก็บมาเป็น Text file --สามารถใช้ชื่อไฟล์อื่นได้โดยแก้ไข code แค่ที่บรรทัดนี้ 
        m3 = f3.readlines()
        str3=m3
        number3 =[]
        
        for item in str3:
            number3.append(float(item))
        for x in range(0,len(number3)):
                i='%.4f'%(number3[a])
                variable4.set(float(i))
                j='%.4f'%(number3[b])
                variable5.set(float(j))                          

    #marker map
        map_widget.set_position(number1[0],number1[1])
        marker_list.append(map_widget.set_marker(number1[0],number1[1]))
        marker_list.append(map_widget.set_marker(number3[a],number3[b]))
                

    #marker part           
        for marker in marker_list:
            position_list.append(marker.position)
            
        print(position_list)

               
    #part
        if len(position_list) > 0:
           marker_path = map_widget.set_path(position_list)
           
        for marker in marker_list:
            #map_widget.delete(marker)
            marker.delete()    
            map_widget.delete(marker_path)
            #marker_path.clear()
            marker_list.clear()                                    
            time.sleep(0.08)# Delay

        
        #CheckArea
        center_point = [{'lat': number3[a], 'lng': number3[b]}]
        test_point = [{'lat': number1[0], 'lng': number1[1]}]
        radius = 0.004 # in kilometer --สามารถเปลี่ยนรัศมีของเงื่อนไขเมื่อเข้าใกล้จุดเป้าหมายที่อยูในรัศมีน้อยกว่า 4 เมตรจะไปจุดต่อไป

        center_point_tuple = tuple(center_point[0].values()) 
        test_point_tuple = tuple(test_point[0].values()) 

        dis = distance.distance(center_point_tuple, test_point_tuple).km
        dis1 = dis*1000 #m
        print("Distance: {}".format(dis1)) 

        i2='%.2f'%(dis1)
        Distance.set(format(i2))
              
        
        if dis <= radius:
            print("Inside")
            a+=2
            b+=2
            area2 = Label(my_frame,text = ' Inside ', font=("Helvetica", 16),fg='green')
            area2.grid(row=0, column=4, pady=10, padx=10)            

        else:
            print("Outside")
            
            area2 = Label(my_frame,text = 'Outside', font=("Helvetica", 16),fg='red')
            area2.grid(row=0, column=4, pady=10, padx=10)  
                    
        root.update()

#
def change_map(event):
        if option_menu.get() == "OpenStreetMap":
            map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
        elif option_menu.get() == "Google Maps":
            map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
        elif option_menu.get() == "Google Satellite":
            map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)        


# Set A Zoom Map

frame = tkinter.Frame(root)
frame.pack()

map_widget = tkintermapview.TkinterMapView(frame, width=800, height=600, corner_radius=0,pady=25)
map_widget.set_zoom(20)
map_widget.pack()
#---------- GUI PROGRAM ----------

my_frame = tkinter.LabelFrame(frame,text="Data",padx=5)
my_frame.pack(pady=10)

# widget Latitude
lat1 = tkinter.Label(my_frame,text=" Latitude      :", font=("Helvetica", 16))
lat1.grid(row=0, column=0, pady=10, padx=10,)
lat2 = tkinter.Label(my_frame,textvariable=variable1, font=("Helvetica", 16))
lat2.grid(row=0, column=1, pady=10, padx=10)
lat3=tkinter.Label(my_frame, text = '*', fg = 'red', font=("Helvetica", 16))
lat3.grid(row=0, column=2,pady=10, padx=10)

# widget Longitude
lon1 = tkinter.Label(my_frame,text="Longitude     : ", font=("Helvetica", 16))
lon1.grid(row=1, column=0, pady=10, padx=10)
lon2 = tkinter.Label(my_frame,textvariable=variable2, font=("Helvetica", 16))
lon2.grid(row=1, column=1, pady=10, padx=10)
lon3=tkinter.Label(my_frame, text = '*', fg = 'red', font=("Helvetica", 16))
lon3.grid(row=1, column=2,pady=10, padx=10)

# widget Position
area1 = tkinter.Label(my_frame,text="Position : ", font=("Helvetica", 16))
area1.grid(row=0, column=3, pady=10, padx=10)
area3=tkinter.Label(my_frame, text = '*', fg = 'red', font=("Helvetica", 16))
area3.grid(row=0, column=9,pady=10, padx=10)

#lat,long Poit
lon4 = tkinter.Label(my_frame,text="Lat,Long : ", font=("Helvetica", 16))
lon4.grid(row=2, column=3, pady=10, padx=10)
lon4 = tkinter.Label(my_frame,textvariable=variable4 , font=("Helvetica", 16))
lon4.grid(row=2, column=4, pady=10, padx=5)
lon4 = tkinter.Label(my_frame,textvariable=variable5 , font=("Helvetica", 16))
lon4.grid(row=3, column=4, pady=10, padx=5)
lon5=tkinter.Label(my_frame, text = '*', fg = 'red', font=("Helvetica", 16))
lon5.grid(row=2, column=9,pady=10, padx=10)

# widget Distance
lon1 = tkinter.Label(my_frame,text="Distance : ", font=("Helvetica", 16))
lon1.grid(row=1, column=3, pady=10, padx=10)
lon2 = tkinter.Label(my_frame,textvariable=Distance , font=("Helvetica", 16))
lon2.grid(row=1, column=4, pady=10, padx=10)
lon3=tkinter.Label(my_frame, text = '*', fg = 'red', font=("Helvetica", 16))
lon3.grid(row=1, column=9,pady=10, padx=10)

# widget Port
port1 = tkinter.Label(my_frame,text="    Port          : ", font=("Helvetica", 16))
port1.grid(row=3, column=0, pady=10, padx=10)
port3=tkinter.Label(my_frame, text = '*', fg = 'red', font=("Helvetica", 16))
port3.grid(row=3, column=2,pady=10, padx=10)

# widget Quite
my_button = tkinter.Button(my_frame, text="Quite", font=("Helvetica", 16), command=root.destroy)
my_button.grid(row=4, column=5, padx=10,pady=15)

# widget Refresh
my_button2 = tkinter.Button(my_frame, text="Connect", font=("Helvetica", 16), command=carte)
my_button2.grid(row=4, column=3, padx=10,pady=15)

# widget Check
my_button3 = tkinter.Button(my_frame, text="Check", font=("Helvetica", 16), command=check_port)
my_button3.grid(row=4, column=2, padx=20,pady=15)

# GenPart
my_button4 = tkinter.Button(my_frame, text="Path", font=("Helvetica", 16), command=part)
my_button4.grid(row=4, column=4, padx=20,pady=15)

# MapSelected
port1 = tkinter.Label(my_frame,text="Map Server :", font=("Helvetica", 16))
port1.grid(row=2, column=0, pady=10, padx=10)
option_menu = ttk.Combobox(my_frame, values=["OpenStreetMap", "Google Maps", "Google Satellite"],state="readonly")
option_menu.grid(row=2, column=1, padx=10, pady=10)
option_menu.set("OpenStreetMap")
option_menu.bind('<<ComboboxSelected>>', change_map)
#option_menu.pack()


root.mainloop()