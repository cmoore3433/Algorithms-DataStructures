class HashEntry:    
    def __init__(self, key, value):        
        self.key = key        
        self.value = value
        
class HashTable:
    def __init__(self, length, tableType="Linear"):
        assert tableType=="Linear" or tableType=="Quadratic", 'tableType must be "Linear" or "Quadratic"'
        self.ttype=tableType
        self.entries=[]
        for i in range(length):
            self.entries.append(HashEntry(key=None, value=None))
        
    def put(self, key, value):
        assert type(key)==int, 'Key must be an integer.'
        i=7*key%len(self.entries)
        j=1
        if self.entries[i].key==None:
            self.entries[i].key=key
            self.entries[i].value=value
            return
        while key!=None:
            if self.ttype=="Linear":
                i=7*i%len(self.entries)+1
                while i>=len(self.entries):
                    i=i-len(self.entries)
                if self.entries[i].key==None:
                    self.entries[i].key=key
                    self.entries[i].value=value
                    return
                j+=1
                if j>len(self.entries)*3:
                    print("Insertion dumped")
                    return
            else:
                i=7*i%len(self.entries)+j**2
                while i>=len(self.entries):
                    i=i-len(self.entries)
                if self.entries[i].key==None:
                    self.entries[i].key=key
                    self.entries[i].value=value
                    return
                j+=1
                if j>2000:
                    print("Insertion dumped")
                    return

    def get(self,key):
        assert type(key)==int, 'Key must be an integer.'
        i=7*key%len(self.entries)
        j=1
        if self.entries[i-1].key==key:
            return self.entries[i-1].value
        while 2==2:
            if self.ttype=="Linear":
                i=7*i%len(self.entries)+1
                if i>=len(self.entries):
                    i=i-len(self.entries)
                if self.entries[i].key==key:
                    return self.entries[i].value
            else:
                i=7*i%len(self.entries)+j**2
                while i>=len(self.entries):
                    i=i-len(self.entries)
                if self.entries[i].key==key:
                    return self.entries[i].value
                j+=1