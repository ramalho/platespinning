# ¡Py3!

import fcntl
import os
import sys
import termios
import tty

# some keyboard codes
K_ESC = '\x1b'
K_CTRL_C = '\x03'


def getch():
    """Get a single char, not waiting anything else."""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
        if ch == K_ESC:
            fl = fcntl.fcntl(fd, fcntl.F_GETFL)
            try:
                fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)
                ch += sys.stdin.read(2)
            finally:
                fcntl.fcntl(fd, fcntl.F_SETFL, fl)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


while True:
    char = getch()
    print(repr(char))
    if char == K_CTRL_C:
        break