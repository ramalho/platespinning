# spinner_thread.py

# credits: Adapted from Michele Simionato's
# multiprocessing example in the python-list:
# https://mail.python.org/pipermail/python-list/2009-February/538048.html

# BEGIN SPINNER_THREAD
import threading
import itertools
import time
import sys


class Signal:  # Ⓐ
    go = True


def spin(msg, signal):  # Ⓑ
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):  # Ⓒ
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))  # Ⓓ
        time.sleep(.1)
        if not signal.go:  # Ⓔ
            break
    write(' ' * len(status) + '\x08' * len(status))  # Ⓕ


def slow_function():  # Ⓖ
    # pretend waiting a long time for I/O
    time.sleep(3)  # Ⓗ
    return 42


def supervisor():  # Ⓘ
    signal = Signal()
    spinner = threading.Thread(target=spin,
                               args=('thinking!', signal))
    print('spinner object:', spinner)  # Ⓙ
    spinner.start()  # Ⓚ
    result = slow_function()  # Ⓛ
    signal.go = False  # Ⓜ
    spinner.join()  # Ⓝ
    return result


def main():
    result = supervisor()  # Ⓞ
    print('Answer:', result)


if __name__ == '__main__':
    main()
# END SPINNER_THREAD
