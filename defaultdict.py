#MY IMPLEMENTATION OF PYTHON'S DEFAULT DICTIONARY
#jgkattikatt@gmail.com


import random

class DefaultDict():
    """default dictionary implementation
    """

    def __init__(self, default_value=None):
        """instantiates a default dict instance
           assigns a random value as a default value, if nothing is passed
        """
        if default_value is None:
            default_value = random.random()
        self.default_value = default_value
        self.dictionary = {}
        
    def __getitem__(self, item=None):
        if item not in self.dictionary:
            self.dictionary[item] = self.default_value
        return self.dictionary[item]

    def __setitem__(self, key,value=None):
        if value is not None:
            self.dictionary[key] = value
        else:
            raise Exception
        
    def __repr__(self):        
        return str(self.dictionary)

    def __iter__(self):        
        self.dict_keys = self.dictionary.keys()
        return self
    
    def next(self):      
        if len(self.dict_keys) > 0:
            return self.dictionary[self.dict_keys.pop()]
        else:
            raise StopIteration
        
    def __len__(self):
        return len(self.dictionary)



if __name__ == '__main__':
    defdict = DefaultDict(1)
    defdict[1] = 2
    print defdict[2]
    print defdict
    print len(defdict)    


