from datetime import datetime

cur_date_time=datetime.now()
print(cur_date_time)

formatted_date= cur_date_time.strftime('%Y=%m=%d')
print(formatted_date)

