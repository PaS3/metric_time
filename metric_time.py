#!/usr/bin/python3

import pytz

#for tz in pytz.all_timezones: 
#  print(tz)


from datetime import datetime
from pytz import timezone    

def selectzone():
##   for z in enumerate(pytz.all_timezones):
##      print("{}\t".format(z).rstrip('\r\n'))
   seltz = [x for x in enumerate(pytz.all_timezones) ] 
##   #zin = int(input("zone number> "))
   zin = 578 #457 #587 
   if zin is None: 
      zin = 587 #zin = 457 587 
   zname = list(seltz[zin])[1]
   tz = zname                                     
   sel_tz = timezone(tz)
   stz_time = datetime.now(sel_tz)
   ms = (int(stz_time.strftime('%S'))/60)*100
   mm = (int(stz_time.strftime('%M'))/60)*100
   mh = (int(stz_time.strftime('%H'))/24)*10
   mmon = (int(stz_time.strftime('%m'))/12)*10
   mday = (int(stz_time.strftime('%d'))/31)*100  #  36*5 + 37*5 = 365/10 

   myear = (int(stz_time.strftime('%Y'))/24)*10
   print("Imperial time:\t", stz_time.strftime('%H:%M:%S'),"\tMetric time: {0:.0f}:{1:.0f}:{2:.0f}".format(mh,mm,ms),"\tTimezone:  ",tz)
   print("Imperial date:\t", stz_time.strftime('%m-%d-%Y'),"\tMetric date: {0:.0f}-{1:.0f}-{2:.0f}".format(mmon,mday,myear),"\tTimezone:  ",tz) #%Y %m %d
selectzone()

def listallzones():
   for zname in pytz.all_timezones:
      tz = zname
      sel_tz = timezone(tz)
      stz_time = datetime.now(sel_tz)
      ms = (int(stz_time.strftime('%S'))/60)*100
      mm = (int(stz_time.strftime('%M'))/60)*100
      mh = (int(stz_time.strftime('%H'))/24)*10
      print("Imperial time:\t", stz_time.strftime('%H:%M:%S'),"  Metric time:{0:.0f}:{1:.0f}:{2:.0f}".format(mh,mm,ms),"  Timezone:  ",tz)
'''
print("""Options:
	 List all zones (press)  \t 1 
	 Select your zone (press)\t 2""")
onum = int(input("> "))


if onum == 1:
   listallzones()
elif onum == 2:
   selectzone()
else:
   print("""Time out...""")

 
'''

#%Y %m %d
