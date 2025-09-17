import time

sse = time.time()
totalseconds = int(sse)
hours = totalseconds // 3600
minutes = (totalseconds % 3600) // 60
print(f"Time since epoch: {hours} hours, {minutes} minutes")
