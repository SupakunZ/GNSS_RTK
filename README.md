# GNSS_RTK

This program is a program developed for research projects related to unmanned aerial vehicles. There is cooperation in the development of many parts. This program will be used to extract data from satellites using [GNSS-RTK](https://www.ardusimple.com/product/simplertk2blite/). and process the data to create accurate routes for unmanned vehicles.
 
## Research tools
--> Software
<ul>
   <li>Ubuntu 20.04 LTS ( require ) </li>
   <li>Python 3.8.10 ( recommend )</li>
</ul>

--> Hardware
<ul>
   <li>SimpleRTK2B Lit</li>
</ul>
<img src="https://github.com/SupakunZ/GNSS_RTK/assets/168329218/9d1c6172-f1e7-482b-804c-a12da48d5eb3" alt="status" width="375"/> <img src="https://github.com/SupakunZ/GNSS_RTK/assets/168329218/3426ee5a-7d3b-4fae-a394-a6bb6d542cb0" alt="settings" width="375"/>

## Flow Chart
<img src="https://github.com/SupakunZ/GNSS_RTK/assets/168329218/4323387b-3ea9-4794-96f7-649031daab41" alt="status" width="750"/>

#### The Flow Chart will show the work in two parts as follows.
1.Flow Chart on the left side shows the work process.
<ul>
   <li>Connect the SimpleRTK2B Lite device to the computer used for data collection. To receive and transmit satellite signals.</li>
   <li>Data transmission follows the NMEA 0183 standard. NMEA specifies data in many ways. But in this experiment, only GNGGA and GNRMC.</li>
   <li>Get and display the number of satellites. Latitude and longitude position on the computer screen and export data using text file.</li>                                                                                                  
</ul>
2.Flow Chart on the right side shows the work process.
<ul>
   <li>Make sure the SimpleRTK2B Lite device is connected to the computer. To prevent various errors.</li>
   <li>The map shows the current latitude and longitude and when moving, a line and distance information will be created between the current location and the next location.</li>
   <li>When approaching the target point within a radius of less than 4 meters, it will move to the next point.</li>                                                                                                  
</ul>

## Base example
<img src="https://github.com/SupakunZ/GNSS_RTK/assets/168329218/9268214f-fe91-43cf-80f7-509b2f3b1daa" alt="status" width="750"/> <img src="https://github.com/SupakunZ/GNSS_RTK/assets/168329218/3b4154c6-2a84-4a3f-b54c-d913a07f8d61" alt="settings" width="375"/>
