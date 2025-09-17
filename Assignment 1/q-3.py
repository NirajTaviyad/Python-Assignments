from datetime import datetime
from dateutil. relativedelta import relativedelta 
d1 = datetime(2023, 5, 10)
d2 = datetime(2025, 7, 20)
rd = relativedelta(d2, d1)
print(f"{rd.years} years, {rd.months} months, {rd.days} days")
