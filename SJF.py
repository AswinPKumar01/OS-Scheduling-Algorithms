











bursts = []
n = int(input("Enter the number of processes: "))
for i in range(n):
    burst = int(input(f"Enter the burst time of P{i+1}: "))
    bursts.append(burst)

ord_burst = sorted(bursts)

s = 0
temp, wt, tat = [0], [], []

for i in ord_burst:
    s += i
    temp.append(s)

wt = temp[0:n]
tat = temp[1:n+1]

awt = sum(wt)/len(wt)

atat = sum(tat)/len(tat)

print("The Average Waiting Time is:",awt)
print("The Average Turnaround Time is:",atat)

