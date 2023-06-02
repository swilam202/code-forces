
from tkinter import *

# Create the Tkinter window
root = Tk()
proc = []
current = 0


class fifs:

    def calculateFIFS(pid,at,bt,n):
        top = 0
        a_tat = 0.0
        a_wt = 0.0
        ct = []
        tat = []
        wt = []

        for i in range(n):
            if i == 0:
                top = top + bt[i]
                ct.append(top)
            elif i > 0:
                if top < at[i]:
                    top = at[i] + bt[i]
                    ct.append(top)
                else:
                    top = top + bt[i]
                    ct.append(top)
       
        for i in range(n):
            var = ct[i] - at[i]
            tat.append(var)
            var = tat[i] - bt[i]
            wt.append(var)
        
        Label(root,text = "\t PID \t\t AT \t\t BT \t\t CT \t\t TAT \t\t WT").pack()

        
        for i in range(n):
            Label(root,text = "\t" + str(pid[i]) + "\t\t" + str(at[i]) + "\t\t" + str(bt[i]) + "\t\t" + str(ct[i]) + "\t\t" + str(tat[i]) + "\t\t" + str(wt[i]) ).pack()
            a_tat = a_tat + tat[i]
            a_wt = a_wt + wt[i]

        a_tat = a_tat/n
        a_wt = a_wt /n
        Label(root,text = "avg turnaround time : " + a_tat).pack()
        Label(root,text = "avg waiting time : " + a_wt).pack()
       

    def inputProcesses():
        
        
        processNumberEntery.config(state="disabled")
        global current
        global proc
        num = int(processNumberEntery.get())
        proc.append([idEntry.get(), int(arrivalEntry.get()), int(burstEntry.get())])
        idEntry.delete(0, END)
        arrivalEntry.delete(0, END)
        burstEntry.delete(0, END)
        current += 1

        if current == num:
            idEntry.config(state="disabled")
            arrivalEntry.config(state="disabled")
            idEntry.config(state="disabled")
            burstEntry.config(state="disabled")
            processNumberEntery.delete(0, END)
            button.config(state="disabled")
            processes = [p[0] for p in proc]
            n = len(proc)
            burst_time = [p[2] for p in proc]
            arrival_time = [p[1] for p in proc]
            fifs.calculateFIFS(processes,arrival_time,burst_time,n)


    def main():
        global processNumberEntery
        global idEntry
        global arrivalEntry
        global burstEntry
        global button
        
        Label(root, text="Enter number of processes").pack()
        processNumberEntery = Entry(root, width=50)
        processNumberEntery.pack()

        Label(root, text="Enter process id: ").pack()
        idEntry = Entry(root, width=50)
        idEntry.pack()

        Label(root, text="Enter arrival time: ").pack()
        arrivalEntry = Entry(root, width=50)
        arrivalEntry.pack()

        Label(root, text="Enter burst time: ").pack()
        burstEntry = Entry(root, width=50)
        burstEntry.pack()

        button = Button(root, text="Next", fg="green", bg="white", command=fifs.inputProcesses, padx=30, pady=5)
        button.pack()

class sjfp:
    
    def calculateSJFPWaitingTime(processes, n, wt):
       
        rt = [0] * n
       
        for i in range(n):
            rt[i] = processes[i][1]
        complete = 0
        t = 0
        minm = 999999999
        short = 0
        check = False

        while complete != n:
           
            for j in range(n):
                if int(processes[j][2]) <= t and rt[j] < minm and rt[j] > 0:
                    minm = rt[j]
                    short = j
                    check = True
            if not check:
                t += 1
                continue

            rt[short] -= 1

            minm = rt[short]
            if minm == 0:
                minm = 999999999

            if rt[short] == 0:

                complete += 1
                check = False

                fint = t + 1

                wt[short] = fint - proc[short][1] - proc[short][2]

                if wt[short] < 0:
                    wt[short] = 0

            t += 1


    def calculateSJFPTurnAroundTime(processes, n, wt, tat):

        for i in range(n):
            tat[i] = processes[i][1] + wt[i]


    def calculateSJFPavgTime(processes, n):

        wt = [0] * n
        tat = [0] * n

        sjfp.calculateSJFPWaitingTime(processes, n, wt)

        sjfp.calculateSJFPTurnAroundTime(processes, n, wt, tat)

        Label(root, text="Process id \t Burst Time\t Waiting Time\t Turn-Around Time").pack()
        total_wt = 0
        total_tat = 0
        for i in range(n):
            total_wt += wt[i]
            total_tat += tat[i]
            Label(root, text=str(processes[i][0]) + "\t\t" + str(processes[i][1]) + "\t\t" + str(wt[i]) + "\t\t" + str(tat[i])).pack()
        Label(root, text="\nAverage waiting time =  " + str(total_wt / n)).pack()
        Label(root, text="Average turn around time = " + str(total_tat / n)).pack()


    def inputProcesses():

        processNumberEntery.config(state="disabled")
        global current
        num = int(processNumberEntery.get())
        proc.append([idEntry.get(), int(arrivalEntry.get()), int(burstEntry.get())])
        idEntry.delete(0, END)
        arrivalEntry.delete(0, END)
        burstEntry.delete(0, END)
        current += 1

        if current == num:
            idEntry.config(state="disabled")
            arrivalEntry.config(state="disabled")
            idEntry.config(state="disabled")
            burstEntry.config(state="disabled")
            processNumberEntery.delete(0, END)
            button.config(state="disabled")
            sjfp.calculateSJFPavgTime(proc, num)

    def main():
        global processNumberEntery
        global idEntry
        global arrivalEntry
        global burstEntry
        global button

        Label(root, text="Enter number of processes").pack()
        processNumberEntery = Entry(root, width=50)
        processNumberEntery.pack()

        Label(root, text="Enter process id: ").pack()
        idEntry = Entry(root, width=50)
        idEntry.pack()

        Label(root, text="Enter arrival time: ").pack()
        arrivalEntry = Entry(root, width=50)
        arrivalEntry.pack()

        Label(root, text="Enter burst time: ").pack()
        burstEntry = Entry(root, width=50)
        burstEntry.pack()

        button = Button(root, text="Next", fg="green", bg="white", command=sjfp.inputProcesses,padx = 30,pady = 5)
        button.pack()

class rr:
    def calculateRRWaitingTime(processes, n, bt,
                             wt, quantum):
        rem_bt = [0] * n

        for i in range(n):
            rem_bt[i] = bt[i]
        t = 0 

        while(1):
            done = True

            for i in range(n):

                if (rem_bt[i] > 0) :
                    done = False
                     
                    if (rem_bt[i] > quantum) :

                        t += quantum
     
                        rem_bt[i] -= quantum

                    else:

                        t = t + rem_bt[i]

                        wt[i] = t - bt[i]

                        rem_bt[i] = 0

            if (done == True):
                break
 
    def calculateRRAroundTime(processes, n, bt, wt, tat):
         
        # Calculating turnaround time
        for i in range(n):
            tat[i] = bt[i] + wt[i]

    def calculateRRavgTime(processes, n, bt, quantum):
        wt = [0] * n
        tat = [0] * n

        rr.calculateRRWaitingTime(processes, n, bt,
                             wt, quantum)

        rr.calculateRRAroundTime(processes, n, bt,
                                    wt, tat)

        Label(root,text = "\t Processes \t Burst Time \t Waiting Time \t Turn-Around Time").pack()
        
        total_wt = 0
        total_tat = 0
        for i in range(n):
            total_wt = total_wt + wt[i]
            total_tat = total_tat + tat[i]
            Label(root,text = str(processes[i]) + "\t\t" + str(bt[i]) + "\t\t" + str(wt[i]) + "\t\t" + str(tat[i])).pack()
        Label(root,text = "Average waiting time : " + str(total_wt /n)).pack()
        Label(root,text = "Average turn around time : " + str(total_tat / n)).pack()

       
        
    def inputProcesses():

        processNumberEntery.config(state="disabled")
        quantumEntery.config(state="disabled")
        global current
        num = int(processNumberEntery.get())
        proc.append([idEntry.get(),  int(burstEntry.get())])
        idEntry.delete(0, END)
        #arrivalEntry.delete(0, END)
        burstEntry.delete(0, END)
        current += 1

        if current == num:
            idEntry.config(state="disabled")
            idEntry.config(state="disabled")
            burstEntry.config(state="disabled")
            processNumberEntery.delete(0, END)
            button.config(state="disabled")
            processes = [p[0] for p in proc]
            n = len(proc)
            burst_time = [p[1] for p in proc]
            rr.calculateRRavgTime(processes, n, burst_time, int(quantumEntery.get()))


    def main():
        global processNumberEntery
        global quantumEntery
        global idEntry
        global burstEntry
        global button
        # Add UI elements to the window
        Label(root, text="Enter number of processes").pack()
        processNumberEntery = Entry(root, width=50)
        processNumberEntery.pack()
        
        Label(root, text="Enter quantum").pack()
        quantumEntery = Entry(root, width=50)
        quantumEntery.pack()

        Label(root, text="Enter process id: ").pack()
        idEntry = Entry(root, width=50)
        idEntry.pack()

        Label(root, text="Enter burst time: ").pack()
        burstEntry = Entry(root, width=50)
        burstEntry.pack()

        button = Button(root, text="Next", fg="green", bg="white", command=rr.inputProcesses,padx = 30,pady = 5)
        button.pack()

class sjfn:
    def sjf_non_preemptive(processes):

        n = len(processes)

        processes = sorted(processes, key=lambda x: x[2])

        waiting_time = [0] * n
        completion_time = processes[0][2] + processes[0][1]

        schedule = [(processes[0][0], processes[0][2], completion_time, waiting_time[0])]

        for i in range(1, n):
            burst_time = processes[i][1]
            arrival_time = processes[i][2]
            if arrival_time > completion_time:
                completion_time = arrival_time
            waiting_time[i] = completion_time - arrival_time
            completion_time += burst_time

            shortest_job = min([p for p in processes[i:] if p[2] <= completion_time], key=lambda x: x[1])
            shortest_job_index = processes.index(shortest_job)

            waiting_time[shortest_job_index] = completion_time - shortest_job[2]
            completion_time += shortest_job[1]

            schedule.append((shortest_job[0], shortest_job[2], completion_time, waiting_time[shortest_job_index]))

        Label(root,text = "Process ID \t Start Time \t End Time \t Waiting Time").pack()
        for p in schedule:
            Label(root,text = str(p[0]) +"\t\t"+ str(p[1]) +"\t\t"+ str(p[2]) +"\t\t"+ str(p[3])).pack()

        total_waiting_time = sum([p[3] for p in schedule])
        total_turnaround_time = sum([p[2] - p[1] for p in schedule])
        Label(root,text = "Average waiting time = " + str(total_waiting_time / n)).pack()
        Label(root,text = "Average turnaround time = " + str(total_turnaround_time / n)).pack()
    
    def inputProcesses():

        processNumberEntery.config(state="disabled")
        global current
        num = int(processNumberEntery.get())
        proc.append([idEntry.get(), int(burstEntry.get()), int(arrivalEntry.get())])
        idEntry.delete(0, END)
        arrivalEntry.delete(0, END)
        burstEntry.delete(0, END)
        current += 1

        if current == num:
            idEntry.config(state="disabled")
            arrivalEntry.config(state="disabled")
            idEntry.config(state="disabled")
            burstEntry.config(state="disabled")
            processNumberEntery.delete(0, END)
            button.config(state="disabled")
            sjfn.sjf_non_preemptive(proc)
     
        
     
    def main():
        global processNumberEntery
        global idEntry
        global arrivalEntry
        global burstEntry
        global button
        # Take input from the user
        Label(root, text="Enter number of processes").pack()
        processNumberEntery = Entry(root, width=50)
        processNumberEntery.pack()

        Label(root, text="Enter process id: ").pack()
        idEntry = Entry(root, width=50)
        idEntry.pack()

        Label(root, text="Enter arrival time: ").pack()
        arrivalEntry = Entry(root, width=50)
        arrivalEntry.pack()

        Label(root, text="Enter burst time: ").pack()
        burstEntry = Entry(root, width=50)
        burstEntry.pack()

        button = Button(root, text="Next", fg="green", bg="white", command=sjfn.inputProcesses,padx = 30,pady = 5)
        button.pack()


  
if __name__ =="__main__":
   Button(root, text="first in first served", fg="white", bg="teal", command=fifs.main,width = 30,height = 3).pack()
   Button(root, text="shortest job first preemptive", fg="white", bg="teal", command=sjfp.main,width = 30,height = 3).pack()
   Button(root, text="round robin", fg="white", bg="teal", command=rr.main,width = 30,height = 3).pack()
   Button(root, text="shortest job first non-preemptive", fg="white", bg="teal", command=sjfn.main,width = 30,height = 3).pack()
   root.mainloop() 
