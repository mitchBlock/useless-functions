import sys
import time

def recursive_timing(num_calls):
	print ('Time for non-recursive loop Fibonacci to calculate n={}'.format(num_calls));
	start = time.perf_counter();
	loop_fib_at_num = loop_fibonacci(num_calls);
	end = time.perf_counter();
	print ('Loop Fibonacci found the number: {} in {} fractional seconds'.format(loop_fib_at_num, (end-start)));

	print ('Time for recursive Fibonacci to calculate n={}'.format(num_calls));
	start = time.perf_counter();
	recursive_fib_at_num = recursive_fibonacci(num_calls);
	end = time.perf_counter();
	print ('Recursive Fibonacci found the number: {} in {} fractional seconds'.format(recursive_fib_at_num, (end-start)));

def recursive_fibonacci(num_in_seq):
	if (num_in_seq == 0):
		return 0;
	if (num_in_seq == 1 or num_in_seq == 2):
		return 1;
	return recursive_fibonacci(num_in_seq-1) + recursive_fibonacci(num_in_seq-2);

def loop_fibonacci(num_in_seq):
	if (num_in_seq == 0):
		return 0;
	if (num_in_seq == 1 or num_in_seq == 2):
		return 1;
	prev_num = 1;
	prev_prev_num = 1;
	for i in range (3, num_in_seq):
		curr_num = prev_num + prev_prev_num;
		prev_prev_num = prev_num;
		prev_num = curr_num;

	return prev_num + prev_prev_num;


if __name__ == '__main__':
	range_end = int(sys.argv[1]) if len(sys.argv) > 1 else 25;
	range_step = int(sys.argv[2]) if len(sys.argv) > 2 else 1;
	for num_calls in range (0, range_end, range_step):
		print ('Calculating time of loop and recursive implementations of Fibonacci function for n={}'.format(num_calls));
		recursive_timing(num_calls);

