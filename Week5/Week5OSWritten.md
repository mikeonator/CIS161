# Operating Systems Written Assignment

## Summarize the booting procedure (include steps including CPU, ROM, RAM, secondary storage) Identify 3 things that get loaded into RAM in order

The machine is turned on. The bootloader instructions tell the CPU to transfer the Operating System from its location (usually mass storage) into main memory. The boot loader directs the CPU to jump to that area of memory. The operating system then takes over the machine's activities. Thus the computer hath booted.

---

## Summarize the difference between a program and a process and a thread

A program is a STATIC SET of directions. A process is a dynamic activity 'whose properties change as time progresses.'  
For example: A program can be equated to a piece of piano music. While a process would be a pianist performing that piece by following said sheet music.

---

## If each time slice in a multiprogramming system is 50 milliseconds and each context switch requires at most a microsecond, how many processes can the machine service in a single second?

Millisecond:microsecond 1:1000  
50001 Microseconds per slice + switch  
about ~20 processes per second?

---

## Suppose a two-lane road converges to one lane to pass through a tunnel

To coordinate the use of the tunnel, the following signal system has been installed:

    A car entering either end of the tunnel causes red lights above the tunnel entrances to be turned on. As the car exits the tunnel, the lights are turned off. If an approaching car finds a red light on, it waits until the light is turned off before entering the tunnel.

### What is the flaw in this system?

Waiting time always sucks but more importantly: Basically, the checking of the light and the act of entering the tunnel are separate operations, which can lead to both cars checking the light, seeing it as off, and both entering the tunnel
