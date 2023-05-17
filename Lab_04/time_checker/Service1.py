import time
import datetime

while True:
    current_time = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S').replace(':', '_'))
    with open(f'./times/{current_time}.txt', 'a') as file:
        file.write(current_time)
    print(f"Створено файл: {current_time}.txt")
    time.sleep(10)
