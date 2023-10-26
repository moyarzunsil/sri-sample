class Document:
    def __init__(self, doc, freq) -> None:
        self.doc = doc 
        self.freq = freq

class InvertedList:
    def __init__(self) -> None:
        self.index = dict()

    def load_index(self, path: str):
        with open(path, "r") as f:
            #for x in f:
            #    print(f"===>{x}")
            line = f.readline()
            while line:
               if(len(line) > 2):
                   elems = line.split()
                   word = elems[0]
                   count_docs = elems[1]
                   print(f"{word}<====>{count_docs}")
                   for elem in elems[2:]:
                       print(elem)
               line = f.readline()