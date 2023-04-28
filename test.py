from datetime import datetime

# melihat waktu hari ini
# today = datetime.now()
# print(today)

today = datetime.now()
date_time = today.strftime("%Y-%m-%d-%H-%M-%S")
print(date_time)