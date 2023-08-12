import sys
sys.path.append('.')
from Signals import NETWORK

def a():
    print("AYYYYYYY")
def part1():
    N.emit_signal("aaa", 105, 21)
def startPart2(check):
    if check == True:
        print("SUPPP")
if __name__ == "__main__":
    N = NETWORK("A")
    N.createSignal('aaa')
    N.connect('aaa', "/Users/abc/Desktop/SignalsModule/trial.py", "part2")

    input("start?:  ")
    part1()