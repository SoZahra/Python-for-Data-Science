import time

times_since = time.time()

time_date = time.localtime(times_since)
date = time.strftime("%b %d %Y", time_date)

print("Seconds since January 1, 1970:", f"{times_since:,.4f}", "or",  f"{times_since:.2e}" " in scientific notation")
print(date)