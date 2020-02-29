sumofsqr = 0
sqrofsum = 0

for i in range(1, 101):
    sumofsqr += pow(i, 2)

sqrofsum = sum(range(1, 101))
sqrofsum = pow(sqrofsum, 2)

print(sqrofsum)
print(sumofsqr)
print(sqrofsum-sumofsqr)
