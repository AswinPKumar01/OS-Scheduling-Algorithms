def waiting_time(processes, n, bt, wt, quantum):
    rem_bt = [0] * n
    for i in range(n):
        rem_bt[i] = bt[i]
    t = 0  
    while True:
        done = True
        for i in range(n):
            if rem_bt[i] > 0:
                done = False
                if rem_bt[i] > quantum:
                    t += quantum
                    rem_bt[i] -= quantum
                else:
                    t += rem_bt[i]
                    wt[i] = t - bt[i]
                    rem_bt[i] = 0
        if done:
            break


def turnaround_time(processes, n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]


def findavgTime(processes, n, bt, quantum):
    wt = [0] * n
    tat = [0] * n

    waiting_time(processes, n, bt, wt, quantum)
    turnaround_time(processes, n, bt, wt, tat)

    total_wt = sum(wt)
    total_tat = sum(tat)

    avg_wt = total_wt / n
    avg_tat = total_tat / n

    return avg_wt, avg_tat


def main():
    num_processes = int(input("Enter the number of processes: "))
    processes = []
    burst_times = []
    for i in range(num_processes):
        burst_time = int(input(f"Enter burst time for process {i + 1}: "))
        processes.append(i + 1)
        burst_times.append(burst_time)
    quantum = int(input("Enter time quantum: "))
    avg_waiting_time, avg_turnaround_time = findavgTime(processes, num_processes, burst_times, quantum)
    print(f"Average Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")


if __name__ == "__main__":
    main()
