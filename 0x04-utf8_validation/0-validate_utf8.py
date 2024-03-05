#!/usr/bin/python3

"""
this method validates the given data whether or not its utf8
encoded
"""


def validUTF8(data):
    """
    method that validates the given data if its utf-8
    Args:
      data - list of integers to be validated
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    for byte in data:
        # Check if the byte is a continuation byte
        if num_bytes == 0:
            if byte >> 7 == 0b0:
                # Single-byte character (ASCII)
                continue
            elif byte >> 5 == 0b110:
                # Two-byte character
                num_bytes = 1
            elif byte >> 4 == 0b1110:
                # Three-byte character
                num_bytes = 2
            elif byte >> 3 == 0b11110:
                # Four-byte character
                num_bytes = 3
            else:
                # Invalid UTF-8 encoding
                return False
        else:
            # Check if the byte is a continuation byte
            if byte >> 6 != 0b10:
                # Invalid UTF-8 encoding
                return False

            # Decrement the number of remaining bytes in the current character
            num_bytes -= 1

    # All bytes have been processed, and no invalid sequences found
    return num_bytes == 0
