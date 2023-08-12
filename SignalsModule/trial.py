from Signals import NETWORK

def onPrinted():
    print('printed lol!!!!')
def OnMOre():
    print("NONONONONONONO WAYYYYYY")
def part2(stuff, stuff2):
    print(stuff+stuff2)
    print("starting process 2")

N = NETWORK("A")
N.createSignal('doneWithP1')
N.connect('doneWithP1', "/Users/abc/Desktop/SignalsModule/a/trial2.py", "startPart2")

if __name__ == "__main__":
    input('start:')
    N.emit_signal("doneWithP1", True)