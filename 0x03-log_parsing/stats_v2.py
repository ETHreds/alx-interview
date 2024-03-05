#!/usr/bin/python3
"""
sys: to read line from stdin
"""
import sys


def get_log():
    """
    Getting the line input from stdin and computing the
    metrics
    """
    # Initialize variables
    total_size = 0
    status_counts = {}

    try:
        # Read input line by line
        for line_number, line in enumerate(sys.stdin, start=1):
            line = line.strip()

                # Parse the line
            parts = line.split()
            if len(parts) != 7:
                continue  # Skip invalid lines

            ip_address, date, request, status_code, file_size = parts

            # Update total file size
            try:
                file_size = int(file_size)
                total_size += file_size
            except ValueError:
                continue  # Skip invalid file sizes

            # Update status code counts
            if status_code.isdigit():
                status_code = int(status_code)
                status_counts[status_code] = status_counts.get(status_code, 0) + 1

            # Print statistics every 10 lines
            if line_number % 10 == 0:
                print("Total file size:", total_size)
                for code in sorted(status_counts):
                    print(f"{code}: {status_counts[code]}")

    except KeyboardInterrupt:
        # Handle keyboard interruption (CTRL + C)
        print("Total file size:", total_size)
        for code in sorted(status_counts):
            print(f"{code}: {status_counts[code]}")


if __name__ == '__main__':
    get_log()
