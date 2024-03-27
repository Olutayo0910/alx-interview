#!/usr/bin/python3
"""Python script that reads stdin line by line and computes metrics."""

import sys


def print_metrics(total_file_size, status_counts):
    """Prints total file size and status counts."""
    print("Total file size: {:d}".format(total_file_size))
    for key, value in sorted(status_counts.items()):
        if value != 0:
            print("{}: {}".format(key, value))


status_counts = {'200': 0, '301': 0, '400': 0, '401': 0,
                 '403': 0, '404': 0, '405': 0, '500': 0}

total_file_size = 0
count = 0
try:
    for line in sys.stdin:
        args = line.split()

        if len(args) > 2:
            status_code = args[-2]
            file_size = int(args[-1])

            if status_code in status_counts:
                status_counts[status_code] += 1

            total_file_size += file_size
            count += 1

            if count == 10:
                print_metrics(total_file_size, status_counts)
                count = 0

except KeyboardInterrupt:
    pass

finally:
    print_metrics(total_file_size, status_counts)
