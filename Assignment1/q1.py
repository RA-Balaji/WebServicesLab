 
class Date:
    def __init__(self, d, m, y, hr, minu, sec):
        self.d = d
        self.m = m
        self.y = y
        self.hr = hr
        self.minu = minu
        self.sec = sec
 
 

monthDays = [31, 28, 31, 30, 31, 30,
             31, 31, 30, 31, 30, 31]
 

 
def countLeapYears(d):
 
    years = d.y

    if (d.m <= 2):
        years -= 1
 

    return int(years / 4) - int(years / 100) + int(years / 400)
 
 

def getDifference(dt1, dt2):

    n1 = dt1.y * 365 + dt1.d
 

    for i in range(0, dt1.m - 1):
        n1 += monthDays[i]
 

    n1 += countLeapYears(dt1)
    sec_n1 = n1*86400 + dt1.hr*3600 + dt1.minu*360 + dt1.sec
 
    n2 = dt2.y * 365 + dt2.d
    for i in range(0, dt2.m - 1):
        n2 += monthDays[i]
    n2 += countLeapYears(dt2)
    sec_n2 = n2*86400 + dt2.hr*3600 + dt2.minu*360 + dt2.sec

    return (sec_n2-sec_n1)

def main_fun(date1, date2): 
    
    date1_days = date1.split(' ')[0]
    date1_days_li = date1_days.split('-')
    date1_time = date1.split(' ')[1]
    date1_time_li = date1_time.split(':')

    date2_days = date2.split(' ')[0]
    date2_days_li = date2_days.split('-')
    date2_time = date2.split(' ')[1]
    date2_time_li = date2_time.split(':')

    print(date1_days_li)
    print(date1_time_li)

    dt1 = Date(int(date1_days_li[0]), int(date1_days_li[1]), int(date1_days_li[2]), 
            int(date1_time_li[0]), int(date1_time_li[1]), int(date1_time_li[2]))
    dt2 = Date(int(date2_days_li[0]), int(date2_days_li[1]), int(date2_days_li[2]), 
            int(date2_time_li[0]), int(date2_time_li[1]), int(date2_time_li[2]))

    sec_diff = getDifference(dt1, dt2)
    days = sec_diff/86400
    
    return days

#main_fun('13-12-2018 5:30:45', '25-2-2019 6:20:30')
