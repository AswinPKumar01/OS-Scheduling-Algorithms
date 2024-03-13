def fcfs(process, bursts):
    n = len(process)
    
    wt = [0] 
    for i in range(1, n):

        wt.append(wt[i - 1] + bursts[i - 1])

    tat = [bursts[i] + wt[i] for i in range(n)]

    awt = sum(wt) / n
    atat = sum(tat) / n

    return awt, atat


def main():

    n = int(input("Enter the number of processes: "))

    process = []
    bursts = []

    for i in range(n):
        burst = int(input(f"Enter burst time for process {i + 1}: "))
        process.append(i + 1)
        bursts.append(burst)

    awt, atat = fcfs(process, bursts)

    print(f"Average Waiting Time: {awt}")
    print(f"Average Turnaround Time: {atat}")


if __name__ == "__main__":
    main()
