# Chapter 2 Past Questions

## 2.1 Process

- Define a process. How is it different from a program?
- Explain the various states of a process with a state transition diagram.
- What is a Process Control Block (PCB)? What information does it contain?
- Explain the difference between independent and co-operating processes.
- Define process. Explain process control block (PCB) and explain process states and its transition. (IMG_9330.jpg)
- Define process. Explain PCB, process states and its transition with figures. (IMG_9316.jpg)
- Define process. Differentiate between process and program. (IMG_9332.jpg)

## 2.2 Interprocess Communication and Synchronization

- What is IPC? Why is it important in operating systems?
- Explain Message Passing IPC. Why is it considered one of the best methods for IPC? Provide pseudo-code for its implementation.
- Explain the concepts of Direct and Indirect communication in message passing.
- Differentiate between Blocking (Synchronous) and Non-blocking (Asynchronous) communication.
- What is Remote Procedure Call (RPC)? Illustrate its operation in a client-server environment with a diagram.
- What is a Race Condition? Illustrate with an example.
- Define the Critical Section problem and the requirements for a valid solution (Mutual Exclusion, Progress, Bounded Waiting).
- Explain the Test-and-Set Lock (TSL) instruction and how it provides mutual exclusion.
- Describe the Producer-Consumer problem and its solution using semaphores/monitors.
- Describe the Readers-Writers problem.
- Explain the Dining Philosophers problem.
  - _Variation:_ Consider n philosophers with n+1 forks (extra fork in the middle). Is deadlock possible? Explain. (IMG_9332.jpg)
- What is the problem associated with sleep and wake up based solution for achieving mutual exclusion? Explain how monitor overcomes this problem? (IMG_9330.jpg)
- What make message passing IPC as one among the best method of IPC implementation? Explain with pseudo code details. (IMG_9332.jpg)

## 2.3 Process Scheduling

- Explain the following scheduling algorithms with examples:
  - First-Come, First-Served (FCFS)
  - Shortest Job First (SJF)
  - Shortest Remaining Time First (SRTF) / SRT
  - Round Robin (RR) - include the impact of time quantum sizes.
  - Priority Scheduling (Preemptive and Non-preemptive).
  - Highest Response Ratio Next (HRRN).
- Consider the following set of processes that arrives at time 0, with the length of the CPU burst given in milliseconds: Construct Gantt chart and calculate average waiting time for: (IMG_9330.jpg)
  | Process | Burst Time | Priority |
  | :--- | :--- | :--- |
  | P1 | 30 | 2 |
  | P2 | 7 | 6 |
  | P3 | 5 | 1 |
  | P4 | 18 | 3 |
  | P5 | 5 | 5 |
  | P6 | 8 | 4 |
- Compare and contrast: Round Robin (quantum = 5), Priority Scheduling (1 highest priority), FCFS, Shortest job first. (IMG_9331.jpg)
- Consider 5 processes P1, P2, P3, P4, and P5 which arrives at time 2, 6, 4, 5 and 0 units to the waiting queue. And burst time of processes are 8, 4, 6, 8, 4 units respectively. Find throughputs of the following algorithms: i. HRRN, ii. Round Robin, iii. SRT. (IMG_9332.jpg)
- Calculate Average Waiting Time and Average Turnaround Time for given process arrival and burst times using various algorithms.
- Draw Gantt Charts for given sets of processes.
- Multilevel feedback queues (IMG_9323.jpg)

## 2.4 Threads

- What is a thread? Differentiate between a process and a thread.
- Explain the advantages of multithreading.
- Compare and contrast User-Level Threads (ULT) and Kernel-Level Threads (KLT).
- Explain the different multithreading models (Many-to-One, One-to-One, Many-to-Many).
- What do you mean by thread? Differentiate between user level and kernel level threads. (IMG_9330.jpg)
- Explain difference between thread and process? Explain different multithreading model? (IMG_9332.jpg)
