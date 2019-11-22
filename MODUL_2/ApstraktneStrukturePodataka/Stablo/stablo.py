class BTree:
    def __init__(self, k = None, l = None, d = None):
        self.Korijen = k 
        self.Lijevo = l
        self.Desno = d
        return

    def preorder(self):
        s = self.Korijen
        if self.Lijevo != None:
            s += self.Lijevo.preorder()
        if self.Desno != None:
            s += self.Desno.preorder()
        return s
