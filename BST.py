class BST:
    def __init__(self):
        self.val={}

    def append(self,a):
        node=1
        while node in self.val:
            if a>self.val[node]:
                node=node*2+1
            else:
                node*=2
        self.val[node]=a

    def __repr__(self):
        return str(self.val)
