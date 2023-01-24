
class segment:

    def __init__(self,List,func = lambda x,y : x+y):

        N = len(List)
        cnt = 1
        while cnt<N:
            cnt *= 2

        seg = [0]*cnt + List + [0]*(cnt-N)

        for i in range(cnt-1,0,-1):
            seg[i] = func(seg[i*2],seg[i*2+1])

        self.seg = seg
        self.len = cnt
        self.func = func
    def update(self,node,val):
        '''node위치의 값을 val로 바꾼다.'''
        
        idx = node+self.len
        self.seg[idx] = val
        idx//=2
        while idx:
            self.seg[idx] = self.func(seg[idx*2],seg[idx*2+1])
            idx//=2

    def query(self,s,e):
        '''s부터 e까지의 쿼리 결과를 반환'''
        s += self.len
        e += self.len+1
        rst = None #임시 항등원
        while s<e:
            if s%2:
                if rst == None:
                    rst = self.seg[s]
                else:
                    rst = self.func(rst,self.seg[s])
                s += 1
            if e%2:
                e -= 1
                if rst == None:
                    rst = self.seg[e]
                else:
                    rst = self.func(rst,self.seg[e])
            s //= 2
            e //= 2
        return rst
L=[1,2,3,4,5]

S=segment(L)
