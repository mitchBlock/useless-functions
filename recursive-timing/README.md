# Recursive Timing #

## How It Works ##
A small program to exemplify how quickly the runtime of a recursive function can escalate. This program takes up to two command-line arguments for range_end and range_step, respectively, then calculates the Fibonacci number for every number in the range using two Fibonacci sequence function implementations. The non-recursive implementation is calculated and timed first, with the timing results being reported in 'fractional seconds' (the unconverted time returned by time.perf_counter), followed by the recursive implementation.

### Default Execution and Results ###
The default execution of the program (`python3 recursive-timing.py`) will have a range_end value of 25, a range_step value of 1, and should show that the recursive implementation is ~6 orders of magnitude (~10^6) slower than the loop implementation as n approaches 25.
