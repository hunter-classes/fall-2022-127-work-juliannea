time_now = input("what is the time now (in hours)")

alarm_time = input("how many hours until alarm")

time_now_int = int(time_now)

alarm_time_int = int(alarm_time)

t_time = time_now_int + alarm_time_int 

time_on_clock = t_time % 24 

print("the time on clock after alarm is", time_on_clock)
