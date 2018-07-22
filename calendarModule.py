import calendar

cal = calendar.Calendar(firstweekday=0)
'''STUPID VERSION'''
'''
days = {0:'MONDAY', 1:'TUESDAY',2:'WEDNESDAY',3:'THURSDAY',4:'FRIDAY',5:'SATURDAY',6:'Sunday'}
month, day, year = map(int,input().split())
res = calendar.weekday(year,month,day)
for k,v in days.items():
    if k==res:
        print(v)
'''

'''PYTHONIC WAY'''
month, day, year = map(int,input().split())
res1 = calendar.day_name[calendar.weekday(year,month,day)].upper()
print(res1)
