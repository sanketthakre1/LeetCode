class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        time=customers[0][0]
        l=[]
        for i in range(0,len(customers)):
            a=customers[i][0]
            b=customers[i][1]
            if(time<a):
                time=a
            time=time+b
            
            late=time-a
            l.append(late)
        su=sum(l)
        ans=su/len(customers)
        return ans



