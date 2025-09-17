from datetime import date

d1 = date(2005,5,5)
d2 = date(2023, 9, 11)
diff = d2 - d1   
print(f"Difference is:",diff.days)
