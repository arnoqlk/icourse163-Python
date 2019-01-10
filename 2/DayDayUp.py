# the power of work
dayup = 1.0
dayfactor = 0.01

for i in range(365):
    if i % 7 in [0, 1]:
        dayup = dayup*(1-dayfactor)
    else:
        dayup = dayup*(1+dayfactor)
print("the power of work:{:.2f}".format(dayup))
    
