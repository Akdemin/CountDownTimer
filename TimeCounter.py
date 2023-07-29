import time
time_to_count = int(input("Enter an amount of time to count in seconds: "))
for x in range(time_to_count, 0, -1):
    seconds = x % 60
    minutes = int(x/60) % 60
    hours = int(x/3600) % 99
    print(f"{hours:02}.{minutes:02}.{seconds:02}")
    time.sleep(1)
