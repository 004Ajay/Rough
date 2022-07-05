# formula: ((O-E)^2) / E

# sample values used...
obs = [50,60,47,48,70]
exp = 50
y = 0
for i in obs:
    y += (((i-exp) * (i-exp)) / exp) 
print("value: ", y)