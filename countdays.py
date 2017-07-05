dateStart = raw_input('please start')
datelist = dateStart.split('.')
yearStart = int(datelist[0])
monthStart = int(datelist[1])
dayStart = int(datelist[2])
dateEnd = raw_input('please end')
datelist2 = dateEnd.split('.')
yearEnd = int(datelist2[0])
monthEnd = int(datelist2[1])
dayEnd = int(datelist2[2])
year = 2000
month = 1
day = 1
yearD1 = abs(yearEnd - year)
monthD1 = abs(monthEnd - month)
dayD1 = abs(dayEnd - day)
yearD2 = abs(year - yearStart)
monthD2 = abs(yearStart - year)
dayD2 = abs(dayStart - day)
if yearEnd >= 2000 and yearStart < 2000:
    if yearD1==0:
        if monthEnd==1:
            day1=dayEnd-day
        elif monthEnd==2:
            day1=dayEnd+31
        elif monthEnd==3:
            day1=dayEnd-day+60
        elif monthEnd==4:
            day1=dayEnd-day+91
        elif monthEnd==5:
            day1=dayEnd-day+121
        elif monthEnd==6:
            day1=dayEnd-day+152
        elif monthEnd==7:
            day1=dayEnd-day+182
        elif monthEnd==8:
            day1=dayEnd-day+213
        elif monthEnd==9:
            day1=dayEnd-day+244
        elif monthEnd==10:
            day1=dayEnd-day+274
        elif monthEnd==11:
            day1=dayEnd-day+305
        elif monthEnd==12:
            day1=dayEnd-day+335
    if yearD1>0:
        if monthEnd == 1:
            day1 = dayEnd - day+yearD1*365+yearD1/4+yearD1/400-yearD1/100
        elif monthEnd == 2:
            day1 = dayEnd + 31+yearD1*365+yearD1/4+yearD1/400-yearD1/100
        elif monthEnd == 3:
            day1 = dayEnd - day + 60+yearD1*365+yearD1/4+yearD1/400-yearD1/100
        elif monthEnd == 4:
            day1 = dayEnd - day + 91+yearD1*365+yearD1/4+yearD1/400-yearD1/100
        elif monthEnd == 5:
            day1 = dayEnd - day + 121+yearD1*365+yearD1/4+yearD1/400-yearD1/100
        elif monthEnd == 6:
            day1 = dayEnd - day + 152+yearD1*365+yearD1/4+yearD1/400-yearD1/100
        elif monthEnd == 7:
            day1 = dayEnd - day + 182+yearD1*365+yearD1/4+yearD1/400-yearD1/100
        elif monthEnd == 8:
            day1 = dayEnd - day + 213+yearD1*365+yearD1/4+yearD1/400-yearD1/100
        elif monthEnd == 9:
            day1 = dayEnd - day + 244+yearD1*365+yearD1/4+yearD1/400-yearD1/100
        elif monthEnd == 10:
            day1 = dayEnd - day + 274+yearD1*365+yearD1/4+yearD1/400-yearD1/100
        elif monthEnd == 11:
            day1 = dayEnd - day + 305+yearD1*365+yearD1/4+yearD1/400-yearD1/100
        elif monthEnd == 12:
            day1 = dayEnd - day + 335+yearD1*365+yearD1/4+yearD1/400-yearD1/100
    if yearD2<4:
        if monthStart==1:
            day2=yearD2*365-dayD2
        elif monthStart==2:
            day2=yearD2*365-dayD2-31
        elif monthStart==3:
            day2=yearD2*365-dayD2-59
        elif monthStart==4:
            day2=yearD2*365-dayD2-90
        elif monthStart==5:
            day2=yearD2*365-dayD2-120
        elif monthStart==6:
            day2=yearD2*365-dayD2-151
        elif monthStart==7:
            day2=yearD2*365-dayD2-181
        elif monthStart==8:
            day2=yearD2*365-dayD2-212
        elif monthStart==9:
            day2=yearD2*365-dayD2-243
        elif monthStart==10:
            day2=yearD2*365-dayD2-273
        elif monthStart==11:
            day2=yearD2*365-dayD2-304
        elif monthStart==12:
            day2=yearD2*365-dayD2-334
    if yearD2>=4:
        if monthStart==1:
            day2=yearD2*365-dayD2+yearD2/4-yearD2/100+yearD2/400
        elif monthStart==2:
            day2=yearD2*365-dayD2+yearD2/4-yearD2/100+yearD2/400-31
        elif monthStart==3:
            day2=yearD2*365-dayD2+yearD2/4-yearD2/100+yearD2/400-59
        elif monthStart==4:
            day2=yearD2*365-dayD2+yearD2/4-yearD2/100+yearD2/400-90
        elif monthStart==5:
            day2=yearD2*365-dayD2+yearD2/4-yearD2/100+yearD2/400-120
        elif monthStart==6:
            day2=yearD2*365-dayD2+yearD2/4-yearD2/100+yearD2/400-151
        elif monthStart==7:
            day2=yearD2*365-dayD2+yearD2/4-yearD2/100+yearD2/400-181
        elif monthStart==8:
            day2=yearD2*365-dayD2+yearD2/4-yearD2/100+yearD2/400-212
        elif monthStart==9:
            day2=yearD2*365-dayD2+yearD2/4-yearD2/100+yearD2/400-243
        elif monthStart==10:
            day2=yearD2*365-dayD2+yearD2/4-yearD2/100+yearD2/400-273
        elif monthStart==11:
            day2=yearD2*365-dayD2+yearD2/4-yearD2/100+yearD2/400-304
        elif monthStart==12:
            day2=yearD2*365-dayD2+yearD2/4-yearD2/100+yearD2/400-334
    countDays=day1+day2
elif yearEnd>=2000 and yearStart>=2000:
    if yearD1==0:
        if monthEnd==1:
            day1=dayEnd-day
        elif monthEnd==2:
            day1=dayEnd+31
        elif monthEnd==3:
            day1=dayEnd-day+60
        elif monthEnd==4:
            day1=dayEnd-day+91
        elif monthEnd==5:
            day1=dayEnd-day+121
        elif monthEnd==6:
            day1=dayEnd-day+152
        elif monthEnd==7:
            day1=dayEnd-day+182
        elif monthEnd==8:
            day1=dayEnd-day+213
        elif monthEnd==9:
            day1=dayEnd-day+244
        elif monthEnd==10:
            day1=dayEnd-day+274
        elif monthEnd==11:
            day1=dayEnd-day+305
        elif monthEnd==12:
            day1=dayEnd-day+335
    if yearD1>0:
        if monthEnd == 1:
            day1 = dayEnd - day+yearD1*365+yearD1/4+1+yearD1/400-yearD1/100
        elif monthEnd == 2:
            day1 = dayEnd + 31+yearD1*365+yearD1/4+1+yearD1/400-yearD1/100
        elif monthEnd == 3:
            day1 = dayEnd - day + 60+yearD1*365+yearD1/4+1+yearD1/400-yearD1/100
        elif monthEnd == 4:
            day1 = dayEnd - day + 91+yearD1*365+yearD1/4+1+yearD1/400-yearD1/100
        elif monthEnd == 5:
            day1 = dayEnd - day + 121+yearD1*365+yearD1/4+1+yearD1/400-yearD1/100
        elif monthEnd == 6:
            day1 = dayEnd - day + 152+yearD1*365+yearD1/4+1+yearD1/400-yearD1/100
        elif monthEnd == 7:
            day1 = dayEnd - day + 182+yearD1*365+yearD1/4+1+yearD1/400-yearD1/100
        elif monthEnd == 8:
            day1 = dayEnd - day + 213+yearD1*365+yearD1/4+1+yearD1/400-yearD1/100
        elif monthEnd == 9:
            day1 = dayEnd - day + 244+yearD1*365+yearD1/4+1+yearD1/400-yearD1/100
        elif monthEnd == 10:
            day1 = dayEnd - day + 274+yearD1*365+yearD1/4+1+yearD1/400-yearD1/100
        elif monthEnd == 11:
            day1 = dayEnd - day + 305+yearD1*365+yearD1/4+1+yearD1/400-yearD1/100
        elif monthEnd == 12:
            day1 = dayEnd - day + 335+yearD1*365+yearD1/4+1+yearD1/400-yearD1/100
    if yearD2==0:
        if monthStart==1:
            day2=dayStart-day
        elif monthStart==2:
            day2=dayStart+31
        elif monthStart==3:
            day2=dayStart-day+60
        elif monthStart==4:
            day2=dayStart-day+91
        elif monthStart==5:
            day2=dayStart-day+121
        elif monthStart==6:
            day2=dayStart-day+152
        elif monthStart==7:
            day2=dayStart-day+182
        elif monthStart==8:
            day2=dayStart-day+213
        elif monthStart==9:
            day2=dayStart-day+244
        elif monthStart==10:
            day2=dayStart-day+274
        elif monthStart==11:
            day2=dayStart-day+305
        elif monthStart==12:
            day2=dayStart-day+335
    if yearD2>0:
        if monthStart == 1:
            day2 = dayStart - day+yearD2*365+yearD2/4+1+yearD2/400-yearD2/100
        elif monthStart == 2:
            day2 = dayStart + 31+yearD2*365+yearD2/4+1+yearD2/400-yearD2/100
        elif monthStart == 3:
            day2 = dayStart - day + 60+yearD2*365+yearD2/4+1+yearD2/400-yearD2/100
        elif monthStart == 4:
            day2 = dayStart - day + 91+yearD2*365+yearD2/4+1+yearD2/400-yearD2/100
        elif monthStart == 5:
            day2 = dayStart - day + 121+yearD2*365+yearD2/4+1+yearD2/400-yearD2/100
        elif monthStart == 6:
            day2 = dayStart - day + 152+yearD2*365+yearD2/4+1+yearD2/400-yearD2/100
        elif monthStart == 7:
            day2 = dayStart - day + 182+yearD2*365+yearD2/4+1+yearD2/400-yearD2/100
        elif monthStart == 8:
            day2 = dayStart - day + 213+yearD2*365+yearD2/4+1+yearD2/400-yearD2/100
        elif monthStart == 9:
            day2 = dayStart - day + 244+yearD2*365+yearD2/4+1+yearD2/400-yearD2/100
        elif monthStart == 10:
            day2 = dayStart - day + 274+yearD2*365+yearD2/4+1+yearD2/400-yearD2/100
        elif monthStart == 11:
            day2 = dayStart - day + 305+yearD2*365+yearD2/4+1+yearD2/400-yearD2/100
        elif monthStart == 12:
            day2 = dayStart - day + 335+yearD2*365+yearD2/4+1+yearD2/400-yearD2/100
    countDays=abs(day1-abs(day2))
elif yearEnd<2000 and yearStart<2000:
    if yearD2<4:
        if monthStart==1:
            day2=yearD2*365-dayD2
        elif monthStart==2:
            day2=yearD2*365-dayD2-31
        elif monthStart==3:
            day2=yearD2*365-dayD2-59
        elif monthStart==4:
            day2=yearD2*365-dayD2-90
        elif monthStart==5:
            day2=yearD2*365-dayD2-120
        elif monthStart==6:
            day2=yearD2*365-dayD2-151
        elif monthStart==7:
            day2=yearD2*365-dayD2-181
        elif monthStart==8:
            day2=yearD2*365-dayD2-212
        elif monthStart==9:
            day2=yearD2*365-dayD2-243
        elif monthStart==10:
            day2=yearD2*365-dayD2-273
        elif monthStart==11:
            day2=yearD2*365-dayD2-304
        elif monthStart==12:
            day2=yearD2*365-dayD2-334
    if yearD2>=4:
        if monthStart==1:
            day2=yearD2*365-dayD2+yearD2/4-yearD2/100+yearD2/400
        elif monthStart==2:
            day2=yearD2*365-dayD2+yearD2/4-yearD2/100+yearD2/400-31
        elif monthStart==3:
            day2=yearD2*365-dayD2+yearD2/4-yearD2/100+yearD2/400-59
        elif monthStart==4:
            day2=yearD2*365-dayD2+yearD2/4-yearD2/100+yearD2/400-90
        elif monthStart==5:
            day2=yearD2*365-dayD2+yearD2/4-yearD2/100+yearD2/400-120
        elif monthStart==6:
            day2=yearD2*365-dayD2+yearD2/4-yearD2/100+yearD2/400-151
        elif monthStart==7:
            day2=yearD2*365-dayD2+yearD2/4-yearD2/100+yearD2/400-181
        elif monthStart==8:
            day2=yearD2*365-dayD2+yearD2/4-yearD2/100+yearD2/400-212
        elif monthStart==9:
            day2=yearD2*365-dayD2+yearD2/4-yearD2/100+yearD2/400-243
        elif monthStart==10:
            day2=yearD2*365-dayD2+yearD2/4-yearD2/100+yearD2/400-273
        elif monthStart==11:
            day2=yearD2*365-dayD2+yearD2/4-yearD2/100+yearD2/400-304
        elif monthStart==12:
            day2=yearD2*365-dayD2+yearD2/4-yearD2/100+yearD2/400-334
    if yearD1<4:
        if monthEnd==1:
            day1=yearD1*365-dayD1
        elif monthStart==2:
            day1=yearD1*365-dayD1-31
        elif monthEnd==3:
            day1=yearD1*365-dayD1-59
        elif monthEnd==4:
            day1=yearD1*365-dayD1-90
        elif monthEnd==5:
            day1=yearD1*365-dayD1-120
        elif monthEnd==6:
            day1=yearD1*365-dayD1-151
        elif monthEnd==7:
            day1=yearD1*365-dayD1-181
        elif monthEnd==8:
            day1=yearD1*365-dayD1-212
        elif monthEnd==9:
            day1=yearD1*365-dayD1-243
        elif monthEnd==10:
            day1=yearD1*365-dayD1-273
        elif monthEnd==11:
            day1=yearD1*365-dayD1-304
        elif monthEnd==12:
            day1=yearD1*365-dayD2-334
    if yearD1>=4:
        if monthEnd==1:
            day1=yearD1*365-dayD1+yearD1/4-yearD1/100+yearD1/400
        elif monthStart==2:
            day1=yearD1*365-dayD1-31+yearD1/4-yearD1/100+yearD1/400
        elif monthEnd==3:
            day1=yearD1*365-dayD1-59+yearD1/4-yearD1/100+yearD1/400
        elif monthEnd==4:
            day1=yearD1*365-dayD1-90+yearD1/4-yearD1/100+yearD1/400
        elif monthEnd==5:
            day1=yearD1*365-dayD1-120+yearD1/4-yearD1/100+yearD1/400
        elif monthEnd==6:
            day1=yearD1*365-dayD1-151+yearD1/4-yearD1/100+yearD1/400
        elif monthEnd==7:
            day1=yearD1*365-dayD1-181+yearD1/4-yearD1/100+yearD1/400
        elif monthEnd==8:
            day1=yearD1*365-dayD1-212+yearD1/4-yearD1/100+yearD1/400
        elif monthEnd==9:
            day1=yearD1*365-dayD1-243+yearD1/4-yearD1/100+yearD1/400
        elif monthEnd==10:
            day1=yearD1*365-dayD1-273+yearD1/4-yearD1/100+yearD1/400
        elif monthEnd==11:
            day1=yearD1*365-dayD1-304+yearD1/4-yearD1/100+yearD1/400
        elif monthEnd==12:
            day1=yearD1*365-dayD2-334+yearD1/4-yearD1/100+yearD1/400
    countDays=abs(day1-day2)
print countDays