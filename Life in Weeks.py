# Life in Weeks
age = (input())
# considering total lifetime of a human as 90 years
yearsLeft = 90 - int(age)
weeksLeft = yearsLeft * 52
# using F strings to write any datatypes in a single line
print(f"Your have {weeksLeft} weeks left.")