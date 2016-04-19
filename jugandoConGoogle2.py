


import basesinfonierspout
import json

class JugandoConGoole(basesinfonierspout.BaseSinfonierSpout):

    def __init__(self):

        basesinfonierspout.BaseSinfonierSpout().__init__()

    def useropen(self):

        # TO-DO: Init values. Code here runs once.
        # In Spouts this function is very important. Must get an object than can
        # iterate to use it in usernextTuple()

        f = open(self.getParam("file"))
        self.it = iter(f.read().splitlines())
        f.close()

    def usernextTuple(self):

        # TO-DO: Write code here. This code reads an input tuple by each execution
        # You can use the same functions as in the Bolts to process it.
        # Tipically is to use self.addField to build the Tuple to emit.

        try:
            st = self.it.next().split(",")
            self.addField(st[0],st[1])

            self.emit()

        except StopIteration:
            pass

().run()
