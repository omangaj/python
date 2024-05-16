input_date=input("Enter date in mm/dd/yyyy===")
date_list=input_date.split("/")

month=int(date_list[0])
day=int(date_list[1])
yr=int(date_list[2])

if month==1:
    month="january"
elif month==2:
    month="february"
elif month==3:
    month="march"
elif month==4:
    month="april"
elif month==5:
    month="may"
elif month==6:
    month="june"
elif month==7:
    month="july"
elif month==8:
    month="august"
elif month==9:
    month="september"
elif month==10:
    month="october"
elif month==11:
    month="november"
elif month==12:
    month="december"

date=month+" "+str(day)+" "+str(yr)
print(date)