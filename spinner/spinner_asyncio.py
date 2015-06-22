# spinner_asyncio.py

# credits: Example by Luciano Ramalho inspired by
# Michele Simionato's multiprocessing example in the python-list:
# https://mail.python.org/pipermail/python-list/2009-February/538048.html

# BEGIN SPINNER_ASYNCIO
import asyncio
import itertools
import sys


@asyncio.coroutine  # Ⓐ
def spin(msg):  # Ⓑ
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        try:
            yield from asyncio.sleep(.1)  # Ⓒ
        except asyncio.CancelledError:  # Ⓓ
            break
    write(' ' * len(status) + '\x08' * len(status))


@asyncio.coroutine
def slow_function():  # Ⓔ
    # pretend waiting a long time for I/O
    yield from asyncio.sleep(3)  # Ⓕ
    return 42


@asyncio.coroutine
def supervisor():  # Ⓖ
    spinner = asyncio.async(spin('thinking!'))  # Ⓗ
    print('spinner object:', spinner)  # Ⓘ
    result = yield from slow_function()  # Ⓙ
    spinner.cancel()  # Ⓚ
    return result


def main():
    loop = asyncio.get_event_loop()  # Ⓛ
    result = loop.run_until_complete(supervisor())  # Ⓜ
    loop.close()
    print('Answer:', result)


if __name__ == '__main__':
    main()
# END SPINNER_ASYNCIO
