#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
 
total_cities=11
all_pairs_dis={}
source_dis={}
path_followed=[-1] * total_cities
mapping={'0':'a','1':'b','2':'c','3':'d','4':'e','5':'f','6':'g','7':'h','8':'i','9':'j','10':'k'}
rev_map={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10}

class city_city_via_capital():
    def __init__(self, cities):
        self.C = cities
        self.map = []
        for row in range(cities):
            self.map.append([])
            for column in range(cities):
                self.map[row].append(0)
 
    def make_source_dis(self, distance_arr):
        for city in range(self.C):
            source_dis[mapping[str(city)]]=distance_arr[city]
            
    #To find minimum distance vertex which is to be included in instantanious map
    def find_minimum_distance(self, updated_distance, curr_min_index):
        curr_minimum_distance = sys.maxsize
        for c in range(self.C):
            if updated_distance[c] < curr_minimum_distance and curr_min_index[c] == False:
                curr_minimum_distance = updated_distance[c]
                minimum_distance_index = c

        return minimum_distance_index
    
    #To print shortest path between two cities via capital
    def path_to_capital(self, predecessor, city):
        if predecessor[city] == -1 :
            print(mapping[str(city)],end=" ")
            with open('./output', 'a') as f:
                f.write(mapping[str(city)])
            return 
        print(mapping[str(city)],end=" ")
        with open('./output', 'a') as f:
            f.write(mapping[str(city)])
        self.path_to_capital(predecessor , predecessor[city])
        
    #To find shortest path between capital and other city using dijkstra algorithm
    def shortest_path_capital_to_cities(self, capital):
         
        updated_distance = [sys.maxsize] * self.C
        updated_distance[capital] = 0
        curr_min_index = [False] * self.C
        
        for c_no in range(self.C):
            u = self.find_minimum_distance(updated_distance, curr_min_index)
            curr_min_index[u] = True
            for v in range(self.C):
                if self.map[u][v] > 0 and curr_min_index[v] == False and updated_distance[v] > updated_distance[u] + self.map[u][v]:
                    updated_distance[v] = updated_distance[u] + self.map[u][v]
                    path_followed[v] = u
 
        self.make_source_dis(updated_distance)
            
        
        
# Main function
ccc = city_city_via_capital(total_cities)

# 'zro ' for no direct path between cities
zro = 0
ccc.map = [
          [ 0 , 5 ,zro,zro, 12,zro, 21,zro, 15, 1 ,zro],
          [ 5 , 0 , 9 ,zro,zro,zro, 18,zro,zro, 20,zro],
          [zro, 9 , 0 , 16,zro,zro, 17,zro,zro,zro, 8 ],
          [zro,zro, 16, 0 ,zro, 7 , 11, 14,zro,zro,zro],
          [ 12,zro,zro,zro, 0 , 6 , 2 ,zro, 10,zro,zro],
          [zro,zro,zro, 7 , 6 , 0 ,zro, 4 ,zro, 19, 13],
          [ 21, 18, 17, 11, 2 ,zro, 0 , 3 ,zro,zro,zro],
          [zro,zro,zro, 14,zro, 4 , 3 , 0 ,zro,zro,zro],
          [ 15,zro,zro,zro, 10,zro,zro,zro, 0 ,zro,zro],
          [ 1 , 20,zro,zro,zro, 19,zro,zro,zro,zro,zro],
          [zro,zro, 8 ,zro,zro, 13,zro,zro,zro,zro,zro] 
          ]
capital=0
ccc.shortest_path_capital_to_cities(capital);

for n in source_dis:
    for n2 in source_dis:
        if str(n)!=str(capital) and n2!=n:
            short_dis=source_dis[n]+source_dis[n2]
            if rev_map[n]!=0 and rev_map[n2]!=0:
                print(n+' distance to '+n2+' via '+mapping[str(capital)]+' is: '+str(short_dis))
                print("Shortest path from "+n+" to capital("+mapping[str(capital)]+") is =>",end=" ")
                with open('./output', 'a') as f:
                    f.write('\n\n'+n+' distance to '+n2+' via '+mapping[str(capital)]+' is: '+str(short_dis)+'\n')
                    f.write("Shortest path from "+n+" to capital("+mapping[str(capital)]+") is =>")
                ccc.path_to_capital(path_followed,rev_map[n])
                print("Shortest path from "+n2+" to capital("+mapping[str(capital)]+") is =>",end=" ")
                with open('./output', 'a') as f:
                    f.write("\nShortest path from "+n2+" to capital("+mapping[str(capital)]+") is =>")
                ccc.path_to_capital(path_followed,rev_map[n2])
                print("\n")
                


# In[ ]:




