import sys
import numpy as np
import math

algo=int(sys.argv[1])   # input algorithm to implement

m=int(sys.argv[2]) # input number of processors to use


# Sorting -----------------------------------------------------------------

class pe: # programming element
    def __init__(self):
        self.prev=[]
        self.data=10**9
        self.next=[]
    
    def declare(self, data, prev, next):
        self.next=next
        self.data=data
        self.prev=prev

class thread:
    def __init__(self, num_of_elem) :
        
        self.num_of_elem=num_of_elem
        self.array=[]
        
        for i in range(self.num_of_elem):
            prog_elem=pe()
            self.array.append(prog_elem)
        
        self.output=[]
        
    def compute(self, temp, iter):
        
        for rank in range(self.num_of_elem):

            elem=temp.pop(-1)
            
            l=[]

            for i in range(rank+1):

                if i==0:

                    if elem <= self.array[i].data:

                        if self.array[i].data != 10**9:
                            self.array[i].next=[self.array[i].data]+self.array[i].next
                        else:
                            self.array[i].next=[]

                        self.array[i].data=elem
    
                    else:
                        self.array[i].next=[elem]+self.array[i].next
                    
                else:   
                    
                    if len(self.array[i-1].next) !=0: 

                        elem= self.array[i-1].next.pop(-1)

                        if elem <= self.array[i].data:

                            if self.array[i].data != 10**9:
                                self.array[i].next=[self.array[i].data]+self.array[i].next
                            else:
                                self.array[i].next=[]

                            self.array[i].data=elem
                         
                        else:
                            self.array[i].next=[elem]+self.array[i].next
                        
                    
                l.append(self.array[i].data)
                
                iter=iter+1

                print(f"cycle {iter}: {self.array[i].prev}__{l}__{self.array[i].next}")


        self.output=self.array[-1].next
        
        if len(self.array[self.num_of_elem-1].next)>0:


            for rank in range(0, self.num_of_elem):
                
                l=[]

                for i in range (rank+1, self.num_of_elem):

                    elem=self.array[i-1].next.pop(-1)

                    if elem <= self.array[i].data:

                        if i==self.num_of_elem-1:

                            self.array[i].next=[self.array[i].data]+self.array[i].next

                        else:
                            self.array[i].next=[self.array[i].data]+self.array[i].next

                        self.array[i].data=elem

                               
                    else:

                        if i==self.num_of_elem-1:

                            self.array[i].next=[elem]+self.array[i].next
                        
                        else:
                            self.array[i].next=[elem]+self.array[i].next
                                  
                    l.append(self.array[i].data) 
                    
                    iter=iter+1 

                    print(f"cycle {iter}: {self.array[i].prev}__{l}__{self.array[i].next}")

            self.output=self.array[-1].next

        return self.output,iter
    

def sorting(m):
    N=30

    nos=(np.random.rand(N)*100)
    to_sort=[]

    for i in range(N):
        to_sort.append(int(nos[i]))
    
    print(f"Numbers to sort: {to_sort}")

    print (f"Beginning systolic array simulation of sorting with {m} processors and {N} numbers to sort")
    
    print(f"------------------------------------------------------------------------------------------")
    
    N=30

    if m>=N:

        m=N
    
    num_of_elem=math.floor((N/m))

    excess= N-num_of_elem*(m)

    # m thread elements
    proc=[]

    for i in range(m):

        proc_elem=thread(num_of_elem)
        proc.append(proc_elem)
    
    iter=0
    
    output=[]

    for rank in range(m):
        
        temp=[]

        for j in range(num_of_elem):

            elem=to_sort.pop(-1)
            temp=[elem]+temp

        for i in range(rank+1):
            

            if i==0:
                
                print(f"data entering processor {i+1}: {temp}")

                output,time=proc[i].compute(temp,iter)    
                
                
            else:

                print(f"data entering processor {i+1}: {output}")

                output,time=proc[i].compute(output,iter)
            
        iter=time

    answer=[]
    
    print("Producing the final answer: ")

    for rank in range(m):

        for i in range(len(proc[rank].array)):

            iter=iter+1

            answer.append(proc[rank].array[i].data)

            print(f"cycle {iter}: {answer}")
    
    print(f"Simulation ends in {iter} cycles")

    print("-----------------------------------------------------------------")


# ---End of sorting algo---------------------------------------------------

#sorting(m)

#----Matrix-vector multiplication-------------------------------------------

class pe_mult_vec: # programming element
    def __init__(self):
        self.prev=[]
        self.data=10**9
        self.next=[]
    
    def declare(self, data, prev, next):
        self.next=next
        self.data=data
        self.prev=prev

class thread_mult_vec:

    def __init__(self, num_of_elem) :
        
        self.num_of_elem=num_of_elem
        self.array=[]
        
        for i in range(self.num_of_elem):
            prog_elem=pe_mult_vec()
            self.array.append(prog_elem)
        
        self.output=[]
        self.mat=None
        
    def compute(self, mat_temp, vec_temp, iter):

        if (self.mat)==None:
            self.mat=mat_temp

        print(f"{self.mat}")

        vec=[]

        for rank in range(self.num_of_elem):
     
            xj=vec_temp[rank]
            vec.append(xj)

            l=[]

            for i in range(self.num_of_elem):

                aij=self.mat[rank].pop(0)

                if i==0:

                    if self.array[i].data==10**9:
                        self.array[i].data= aij*xj 
                    
                    else:
                        self.array[i].data=self.array[i].data+aij*xj
                    
                    
                    #self.array[i].next=[xj]+self.array[i].next

                else:

                   # xj= self.array[i-1].next.pop(0)

                    if self.array[i].data==10**9:
                        self.array[i].data= aij*xj 
                    
                    else:
                        self.array[i].data=self.array[i].data+aij*xj
                    
                    #self.array[i].next=[xj]+self.array[i].next

                iter=iter+1

                #self.array[-1].next=vec
                
                l.append(self.array[i].data)
                print(f"cycle {iter}: {l}__ ")
        
        self.output=vec
        #self.array[-1].next=[]
        
        return self.output,iter

def matrix_vector(m):

    N=10
    
    mat=[]
    vec=[]

    matrix=np.random.randint(0,10,(N,N))
    vector=np.random.randint(0,10, (N,1))

    m_t=matrix.T

    for i in range(N):
        l=[]
        for j in range(N):
            l.append(m_t[i][j])

        mat.append(l)
        vec.append(vector[i][0])

    answer=np.dot(matrix,vector)

    print(f"Answer should be: {answer}")

    print (f"Beginning systolic array simulation of matrix multiplication with {m} processors and {N}*{N} matrix multiplication with {N}*1 vector")
    
    print(f"------------------------------------------------------------------------------------------")

    print(f"Matrix: {matrix} ")
    print(f"Vector:{vector}")
    
    if m>=N:

        m=N
    
    num_of_elem=math.floor((N/m))

    excess= N-num_of_elem*(m)

    # m thread elements
    proc=[]

    for i in range(m):

        proc_elem=thread_mult_vec(num_of_elem)
        proc.append(proc_elem)
    
    iter=0

    v=[]
    
    for rank in range(m):

        vec_temp=[]
        mat_temp=[]

        for i in range(num_of_elem):

            vec_temp.append(vec.pop(0))      
            mat_temp.append(mat.pop(0))  

        for i in range(rank+1):
    
            if i==0:

                print(f"vector entering processor {i+1}: {vec_temp} + matrix : ")

                
                output,time=proc[i].compute(mat_temp,vec_temp,iter)    
            
                v.append(output)

            else:
                
                v_=v.pop(0)
                print(f"data entering processor {rank+1}: {v_}+  matrix :  ")
                
                output,time=proc[i].compute(mat_temp,v_,iter)

                v.append(v_)
   
        iter=time

    answer=[]
    
    print("Producing the final answer: ")

    for rank in range(m):

        for i in range(len(proc[rank].array)):

            iter=iter+1

            answer.append(proc[rank].array[i].data)

            print(f"cycle {iter}: {answer}")
    
    print(f"Simulation ends in {iter} cycles")

    print("-----------------------------------------------------------------")

#-End of matrix vector------------------------------------------------------

#matrix_vector(m)

#-1D Convolution-------------------------------------------------------------

class pe_conv: # programming element
    def __init__(self):
        self.right=[]
        self.data=[]
        self.val=0
        self.left=[]
    
class thread_conv:

    def __init__(self, num_of_elem) :
        
        self.num_of_elem=num_of_elem
        self.array=[]
        self.rev=[]

        for i in range(self.num_of_elem):
            prog_elem=pe_conv()
            self.array.append(prog_elem)
        
        self.output=[]
        
    def compute(self, right,left, iter):
        
        for rank in range(0,self.num_of_elem,2):
            l=[]
            right_elem=left.pop(0)

            for i in range(rank+1):

                if i==0:

                    if len(self.array[i].data)==0:
                        self.array[i].data=[right_elem]
                        self.array[i].right=[right_elem]

                    else:
                        el=self.array[i].data.pop(0)

                        prod=right_elem*el

                        self.array[i].data=[right_elem]

                        self.array[i].val+=prod
                        
                        self.array[i].right=[el]

                else:
                    if len(self.array[i-1].right)>0:
                        right_elem= self.array[i-1].right[0]

                        if len(self.array[i].data)==0:
                            self.array[i].data=[right_elem]
                            self.array[i].right=[right_elem]

                        else:
                            el=self.array[i].data.pop(0)

                            prod=right_elem*el

                            self.array[i].data=[right_elem]

                            self.array[i].val+=prod
                            
                            self.array[i].right=[el]
            
            right_elem=right.pop(0)

            for i in range(self.num_of_elem-1,self.num_of_elem-rank-2,-1):

                if i==self.num_of_elem-1:

                    if len(self.array[i].data)==0:
                        self.array[i].data=[right_elem]
                        self.array[i].right=[right_elem]

                    else:
                        el=self.array[i].data.pop(0)

                        prod=right_elem*el

                        self.array[i].data=[right_elem]

                        self.array[i].val+=prod
                        
                        self.array[i].right=[el]

                else:
                    
                    if len(self.array[i+1].right)>0:
                        right_elem= self.array[i+1].right[0]

                        if len(self.array[i].data)==0:
                            self.array[i].data=[right_elem]
                            self.array[i].right=[right_elem]

                        else:
                            el=self.array[i].data.pop(0)

                            prod=right_elem*el

                            self.array[i].data=[right_elem]

                            self.array[i].val+=prod
                            
                            self.array[i].right=[el]
            
            
            for k in range(self.num_of_elem):
                l.append(self.array[k].val)
                iter+=1
                print(f"cycle {iter}: {left}__{l}__{right}")

        return self.array,iter

def conv():

    N=3
    
    a=[]
    b=[]

    matrix=np.random.randint(0,10,(N))
    vector=np.random.randint(0,10, (N))

    for i in range(N):
        
        a.append(matrix[i])

        b.append(vector[i])

    m=2*N

    print (f"Beginning systolic array simulation of 1D Convolution with {m} processors and {N} sized a, b vectors")

    print(f"Answer should be {np.convolve(a,b)}")
    
    print(f"------------------------------------------------------------------------------------------")

    print(f"a: {matrix} ")
    print(f"b:{vector}")
    
    
    # m thread elements

    proc_elem=thread_conv(m)
        
    iter=0
    
    output,time=proc_elem.compute(b,a,iter)

    answer=[]
    
    print("Producing the final answer: ")

    iter=time

    for rank in range(m):

        iter=iter+1

        answer.append(output[rank].val)

        print(f"cycle {iter}: {answer}")
    
    print(f"Simulation ends in {iter} cycles")

    print("-----------------------------------------------------------------")

# End of 1D Convolution------------------------------------------------------

#conv(m)

# Integer-Integer Multiplication----------------------------------------------

class pe_int: # programming element
    def __init__(self):
        self.right=[]
        self.data=[]
        self.val=0
        self.left=[]
    
class thread_int:

    def __init__(self, num_of_elem) :
        
        self.num_of_elem=num_of_elem
        self.array=[]
        self.rev=[]

        for i in range(self.num_of_elem):
            prog_elem=pe_int()
            self.array.append(prog_elem)
        
        self.output=[]
        
    def compute(self, right,left, iter):
        
        for rank in range(0,self.num_of_elem,2):
            l=[]
            right_elem=left.pop(0)

            for i in range(rank):

                if i==0:

                    if len(self.array[i].data)==0:
                        self.array[i].data=[right_elem]
                        self.array[i].right=[right_elem]

                    else:
                        el=self.array[i].data.pop(0)

                        prod=right_elem*el

                        self.array[i].data=[right_elem]
                        
                        if self.array[i].val==1 and prod==1:
                            self.array[i].val=0
                        
                            self.array[i].right=[1]
                        else:
                            self.array[i].val+=prod
                            self.array[i].right=[el]

                     
                else:
                    if len(self.array[i-1].right)>0:
                        right_elem= self.array[i-1].right[0]

                        if len(self.array[i].data)==0:
                            self.array[i].data=[right_elem]
                            self.array[i].right=[right_elem]

                        else:
                            el=self.array[i].data.pop(0)

                            prod=right_elem*el

                            self.array[i].data=[right_elem]

                            if self.array[i].val==1 and prod==1:
                                self.array[i].val=0
                            
                                self.array[i].right=[1]
                            else:
                                self.array[i].val+=prod
                                self.array[i].right=[el]

                         
            right_elem=right.pop(0)

            for i in range(self.num_of_elem-1,self.num_of_elem-rank-2,-1):

                if i==self.num_of_elem-1:

                    if len(self.array[i].data)==0:
                        self.array[i].data=[right_elem]
                        self.array[i].right=[right_elem]

                    else:
                        el=self.array[i].data.pop(0)

                        prod=right_elem*el

                        self.array[i].data=[right_elem]

                        if self.array[i].val==1 and prod==1:
                            self.array[i].val=0
                        
                            self.array[i].right=[1]
                        else:
                            self.array[i].val+=prod

                else:
                    
                    if len(self.array[i+1].right)>0:
                        right_elem= self.array[i+1].right[0]

                        if len(self.array[i].data)==0:
                            self.array[i].data=[right_elem]
                            self.array[i].right=[right_elem]

                        else:
                            el=self.array[i].data.pop(0)

                            prod=right_elem*el

                            if self.array[i].val==1 and prod==1:
                                self.array[i].val=0
                            
                                self.array[i].right=[1]
                            else:
                                self.array[i].val+=prod
                                self.array[i].right=[el]            
            
            for k in range(self.num_of_elem):

                
                l.append(self.array[k].val)
                iter+=1
                print(f"cycle {iter}: {left}__{l}__{right}")

        return self.array,iter

def int_mul():

    N=3
    
    a=[1,1,0]
    b=[1,1,1]

    m=2*N

    print (f"Beginning systolic array simulation of Integer-Integer multiplication with {m} processors and {N} sized a, b vectors")

    print(f"Answer should be {[1,0,1,0,1,0]}")
    
    print(f"------------------------------------------------------------------------------------------")

    print(f"a: {a} ")
    print(f"b:{b}")
    
    
    # m thread elements

    proc_elem=thread_int(m)
        
    iter=0
    
    output,time=proc_elem.compute(b,a,iter)

    answer=[]
    
    print("Producing the final answer: ")

    iter=time

    for rank in range(m):

        iter=iter+1

        answer.append(output[rank].val)

        print(f"cycle {iter}: {answer}")
    
    print(f"Simulation ends in {iter} cycles")

    print("-----------------------------------------------------------------")
# End-------------------------------------------------------------------------
if algo==1:
    sorting(m)

elif algo==2:
    matrix_vector(m)

elif algo==3:
    conv()

elif algo==4:
    int_mul()

else:
    print("Invalid choice")
