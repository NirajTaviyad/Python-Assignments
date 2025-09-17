s = input("Enter a string to reverse: ")
reversed_s = s[::-1]
print("Reversed (slice):", reversed_s)
reverse = ""
for i in range(len(s) - 1, -1, -1):
    reverse += s[i]
print("Reversed (loop index):", reverse)

reverse2 = ""
for ch in s:
    reverse2 = ch + reverse2
print("Reversed (prepend):", reverse2)

reversed_list = [ s[i] for i in range(len(s) - 1, -1, -1) ]
reverse3 = "".join(reversed_list)
print("Reversed (list comprehension):", reverse3)
