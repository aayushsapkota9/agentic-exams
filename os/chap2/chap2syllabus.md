# Unit 2: Processes and Threads [10 hours]

## 2.1 Process

- Definition, states and transition diagram
- Process control block (PCB)
- Concurrent and Parallel processes

## 2.2 Interprocess Communication and Synchronization

- Introduction, Race Condition, Critical Regions and condition, Avoiding critical region: Mutual Exclusion and Serializability
- Mutual exclusion conditions
- Mutual exclusion: disabling interrupts, lock variable, strict alteration (Dekker’s algorithms, Peterson’s algorithms), The TSL instruction, sleep and wakeup, producer and consumer problem
- Types of mutual exclusion (Semaphore, Monitors, Bounded buffer(producer consumer), Message passing)
- Classical IPC Problems
  - The Dining Philosophers problem
  - The Readers and Writers problem
  - The Sleeping Barber Problem
- Serializability: Locking Protocols and Time Stamp Protocols

## 2.3 Process Scheduling

- Basic Concept
- Type of scheduling: Preemptive scheduling, Non-preemptive scheduling, Batch, Interactive, Real time scheduling
- Scheduling criteria and performance analysis
- Scheduling algorithm with examples:
  - First come first served
  - Shortest-job-first
  - Round-robin
  - Shortest process next
  - Shortest remaining time next
  - Real time
  - Priority fair share
  - Guaranteed
  - Lottery scheduling

## 2.4 Threads

- Definitions of Threads
- Types of thread process (Single and multithreaded process)
- Benefits of Multithreading
- Threads Models (Many-to-one model, One-to-one Model, Many-to many model)
- User Space and Kernel Space Threads
- Difference between Processes and Threads
