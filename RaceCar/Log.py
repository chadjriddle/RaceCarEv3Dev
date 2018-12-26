import sys

class Log():
    logf = open("process.log", "w")

    def msg(self, message):
        self.logf.write(message + "\n")
        self.logf.flush()
        print(message, file=sys.stderr)