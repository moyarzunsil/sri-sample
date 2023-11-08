class Document:
    def __init__(self, doc, freq) -> None:
        self.doc = doc 
        self.freq = freq

class PostingList:
    def __init__(self) -> None:
        self.docs = dict()

    def add_doc(self, doc, freq):
        self.docs[doc] = freq

    def __str__(self):
        str_to_print = " ".join(f"{key} {value}" for key, value in self.docs.items())
        return str_to_print
    
    def get_keys(self):
        return self.docs.keys()

class InvertedList:
    def __init__(self) -> None:
        self.index = dict()

    def load_index(self, path: str):
        with open(path, "r", encoding="utf-16") as f:
            line = f.readline()
            while line:
               current_post = PostingList()
               if(len(line) > 2):
                    elems = line.split()
                    word = elems[0]
                    count_docs = elems[1]
                    print(f"Loading word {word} in {count_docs} documents.")
                    pares = list(zip(elems[2::2], elems[3::2]))
                    for par in pares:
                       current_post.add_doc(par[0], par[1])
                       #print(par[0], par[1])
                    self.index[word] = current_post
               line = f.readline()

    def __str__(self):
        str_to_print = "\n".join(f"{key} {value}" for key, value in self.index.items())

        return str_to_print
    
    def find(self, word):
        return self.index[word] if self.index.get(word) is not None else ""
    
    def query_or(self, intersection_list: PostingList, word: str):
        if intersection_list is not None:
            if self.index.get(word) is not None:
                return self.intersection(intersection_list, self.index[word])
            else:
                return intersection_list
        else:
            if self.index.get(word) is not None:
                return self.index[word]
            else:
                return None
            
    def intersection(self, list1: PostingList, list2: PostingList):
        keys1 = list(list1.get_keys())
        keys2 = list(list2.get_keys())

        idx1 = idx2 = 0

        final_list = list()

        while(idx1 < len(keys1) and idx2 < len(keys2)):
            if keys1[idx1] == keys2[idx2]:
                final_list.append(keys1[idx1])
                idx1 += 1
                idx2 += 1
            elif keys1[idx1] < keys2[idx2]:
                idx1 += 1
            elif keys1[idx1] > keys2[idx2]:
                idx2 += 1
            else:
                raise("the impossible happens")
            
        current_post = PostingList()
        for doc in final_list:
            current_post.add_doc(doc, 0)
            
        return current_post