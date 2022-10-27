class heap:
    def __init__(self,List=[],priority= lambda x: x):
        self.val=[None] #처음에는 더미 데이터
        self.hval=[None]
        self.len=0 #마지막 인덱스 번호가 됨
        self.priority=priority #우선순위의 기준이 되는 함수
                                #값이 높은 것이 높은 우선순위
                                #기본 우선순위는 기본 크기 비교
        
        for i in List: #리스트가 있었다면 어펜드
            self.push(i)

    def push(self,a):
        #밑에 넣고 올라감
        self.val.append(a) #실제 값 리스트 
        self.hval.append(self.priority(a))#우선순위 값 리스트 
        self.len+=1
        idx=self.len
        while idx>1:
            if self.hval[idx]<self.hval[idx//2]:
                break
            else:
                self.hval[idx],self.hval[idx//2]=self.hval[idx//2],self.hval[idx]
                self.val[idx],self.val[idx//2]=self.val[idx//2],self.val[idx]
                idx//=2

    def pop(self):
        if self.len==0:
            print("힙이 비었습니다.")
            return
        elif self.len==1:
            self.len-=1
            return self.val.pop()
        rst= self.val[1]
        self.val[1]=self.val.pop()
        self.hval[1]=self.hval.pop()
        my_hval=self.hval[1]
        self.len-=1
        idx=1
        while idx*2<=self.len:
            M= max(self.hval[idx*2:idx*2+2])
            if my_hval>=M:
                return rst

            if M==self.hval[idx*2]:
                self.val[idx],self.val[idx*2]=self.val[idx*2],self.val[idx]
                self.hval[idx],self.hval[idx*2]=self.hval[idx*2],self.hval[idx]
                idx=idx*2
            else:
                self.val[idx],self.val[idx*2+1]=self.val[idx*2+1],self.val[idx]
                self.hval[idx],self.hval[idx*2+1]=self.hval[idx*2+1],self.hval[idx]
                idx=idx*2+1
        return rst

    def newpriority(self,func):
        List=self.val[1:]
        self.priority=func
        self.val=[None]
        self.hval=[None]
        self.len=0
        for i in List:
            self.push(i)
        return self
                
    def __str__(self):
        return str(self.val[1:])

    def __repr__(self):
        return str(self.val[1:])
        
        


a=heap(priority= lambda x: x)
for i in [1,4,2,3,5,2,3,1]:
    a.push(i)

print(a)

print(a.newpriority(lambda x : -(x%2)))
for i in range(9):
	print(a.pop())
