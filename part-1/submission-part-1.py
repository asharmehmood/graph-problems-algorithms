#!/usr/bin/env python
# coding: utf-8

# In[8]:


arr=[]
file1=open('./inputfile','r')
lines = file1.readlines()
first_sem=[]
required_by={}
all_courses=[]
course_counter={}

with open('./inputfile', 'r') as file:
    data = file.read().replace('\n', ' ')

for c in data.split():
    if c.startswith('cs') and c not in (all_courses):
        all_courses.append(c)

for c in all_courses:
    required_by[c]=[]
    course_counter[c]=0
    
for ln in lines:
    l = ln.replace('\n','')
    if 'requires' not in l:
        first_sem.append(str(l).strip())
    else:
        if 'and' in l:
            courses = l.split('requires')
            c1 = courses[0]
            cs = courses[1].split('and')
            cs_list = list(map(lambda x:required_by[x.strip()].append(c1.strip()), cs))
            cs_list2 = list(map(lambda x:exec("course_counter[c1.strip()]+=1"), cs))
        else:
            courses = l.split('requires')
            c1 = courses[0]
            c2 = courses[1]
            required_by[c2.strip()].append(c1.strip())
            course_counter[c1.strip()]+=1

# print(required_by)
# print(course_counter)


#Algorithm 1
sem_n=first_sem
print("semester 1 => ",sem_n)
with open('./output-file', 'a') as f:
        f.write("semester 1 => "+str(sem_n)+"\n")
x=2
while(True):
    temp_c=[]
    for c in sem_n:
        temp_c+=required_by[c]
        
    if temp_c==[]:
        break
  
    sem_n=[]
    for c in temp_c:
        if course_counter[c]!=0:
            course_counter[c]-=1
        if course_counter[c]==0:
            sem_n.append(c)   
    print("semester "+str(x)+" => ",sem_n)
    with open('./output-file', 'a') as f:
        f.write("semester "+str(x)+" => "+str(sem_n)+"\n")
    x+=1


# In[ ]:




