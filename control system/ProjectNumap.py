import numbers
import serial
import folium

class Location():
    #Connect Port
    gps = serial.Serial("/dev/ttyUSB0", baudrate = 38400)
    while True:
        line = gps.readline()
        data = line.decode('utf').split(",")
        
     
        if data[0] == "$GNGGA":
            number = data[7]
            print ("จำนวนดาวเทียม:",(number))
            
        
        if data[0] == "$GNRMC":
            if data[2] == "A" :

                latgps = float(data[3])
                if data[4] == "S":
                    latgps = -latgps
                    
                latdeg = int(latgps/100)
                latmin = latgps - latdeg*100
                lat = latdeg+(latmin/60)

                longps = float(data[5])
                if data[6] == "W":
                    longps = -longps
                
                londeg = int(longps/100)
                lonmin = longps - londeg*100
                lon = londeg+(lonmin/60)

                print ("Latitude:",(lat))
                print ("Longitude:",(lon))
                

                #Save Data to myfile.txt --เปลี่ยนชื่อไฟล์ได้แต่ต้องแก้ไข Code บรรทัด 42 45
                file = open('40.txt', 'a') # w
                file.write('\n'+ str(lat)+ '\n')   #- '\n'+     
                file.write(str(lon) )
                #file = open('myfile.txt','a+')     # a+      
                file.seek(0)                 
                file.close()
               