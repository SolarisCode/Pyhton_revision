"""Keypress - A module for detecting a single keypress"""

try :
    import msvcrt

    def get_key():
        """Wait for a keypress and return a single character string"""
        return (msvcrt.getch())
except ImportError:
    import sys
    import tty
    import termios

    def get_key():
        """Wait for a keypress and return a single character string"""
        fd = sys.stdin.fileno()
        original_attributes = termios.tcgetattr(fd)
        try :
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally :
            termios.tcsetattr(fd, termios.TCSADRAIN, original_attributes)
        return (ch)


def main():
    print(get_key())


if __name__ == "__main__":
    main()
