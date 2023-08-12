import os
import time
import json



# function to add to JSON
def write_json(new_data, filename='Signals.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["SignalDetails"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
class NETWORK:
    SIGNALS = []
    def __init__(self, path):
        self.netowrk_path = path
    def deleteSignals(self):
        with open("Signals.JSON", "r") as f:
            data = json.load(f)
        data["SignalDetails"] = [
            
        ]
        with open("Signals.JSON", "w") as file:
            json.dump(data, file, indent = 4)
    def connect(self, signalName, reciever, recieverFunction):
        with open("Signals.JSON", "r") as file:
            data = json.load(file)
            newData = {
                "name":f"{signalName}",
                "reciever":f"{reciever}",
                "recieverFunc":f"{recieverFunction}"
            }

            write_json(newData)
    def createSignal(self, signalName):
        if not(signalName in self.SIGNALS):
            with open("Signals.JSON","r") as file:
                data = json.load(file)
                signals = data["SignalDetails"]
                for signal in signals:
                    if signal["name"] == signalName:
                        print("Signal has already been created, the last one was overwritted.")
            self.SIGNALS.append(signalName)
        else:
            index = self.SIGNALS.index(signalName)
            self.SIGNALS[index] = signalName
            print(f"{signalName}: has already been created, it has been overwritted")
    def emit_signal(self, signalName, *args):
        if signalName in self.SIGNALS:
            with open("Signals.JSON","r") as file:
                data = json.load(file)
                signals = data["SignalDetails"]
                for signal in signals:
                    if signal["name"] == signalName:

                        reciever = signal["reciever"]
                        R = reciever
                        recieverFunc = signal["recieverFunc"]
                        fileName = os.path.basename(reciever)
                        with open('t.txt', "w") as f:
                            f.write('''import importlib.machinery
module_path = 'PATH'
loader = importlib.machinery.SourceFileLoader('FILE_NAME', module_path)
FILE_NAME = loader.load_module()
result = FILE_NAME.FUNC_NAME(PARAM)''')
                        with open("t.txt", "r") as f:
                            content = f.read()

                        file_name_without_extension = os.path.splitext(fileName)[0]
                        replacemenets = {
                            "FUNC_NAME":f"{recieverFunc}",
                            "FILE_NAME":f"{file_name_without_extension}",
                            "PATH":f"{R}",
                            "PARAM":f"{str(args)[1:-1]}"
                        }
                        for old, new in replacemenets.items():
                            content = content.replace(old, new)

                        with open("t.txt", "w") as r:
                            # r.write("\n    ")
                            r.write(content)
                        with open("t.txt","r") as y:
                            code = y.read()
                            print('asdf')
                            exec(code)
                        os.remove("t.txt")

                        break

N = NETWORK("sup")
N.deleteSignals()