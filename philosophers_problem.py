import threading
import time

class Philosopher(threading.Thread):

    def __init__(self, index, right_fork, left_fork):
        threading.Thread.__init__(self)
        self._index = index
        self._right_fork = right_fork
        self._left_fork = left_fork

    def run(self):
        while True:
            print(f"Philosopher {self._index} is thinking.")
            time.sleep(1)
            print(f"Philosopher {self._index} is hangry.")
            self._right_fork.acquire()
            self._left_fork.acquire()
            print(f"Philosopher {self._index} is eating.")
            time.sleep(1)
            self._right_fork.release()
            self._left_fork.release()


def main():
    forks = [threading.Lock() for _ in range(5)]
    philosophers = [Philosopher(x, forks[x], forks[(x + 1) % 5]) 
                for x in range(5)]
    for philosopher in philosophers:
        philosopher.start()
