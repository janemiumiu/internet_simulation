from matplotlib import pyplot as plt
import numpy as np
import random
from scipy.stats import poisson
from scipy.stats import norm
import math
car_info=[]              #record car's information
station_info=[]          #record station's information
res =0                   #calculate the numbers of handoff
entropy_number =15       #decide entropy number (used in algo 3)
mathod = 3               #choose algorithm 1:Minium 2:Best effort 3:Entropy 4:Best effort +distance 
car_number = 0           #count car number and print out
calling_number = 0       #count calling number and print out

#function of counting distance of car and base stand
def calculation_dist(carx,cary,stationx,stationy):
    return((stationx-carx)**2+(stationy-cary)**2)**0.5
#function of calculating the db between car and base stand 
def path_loss(dist,freq):
    return 120-(32.45+20*math.log(freq,10)+20*math.log(dist,10))
#decide car's connected base stand by highest db
def decide_db_and_connect_station(car_id):
    temp=0
    b=0
    for b in range(len(station_info)):
        if b == 0:
            max_db=path_loss(calculation_dist(car_info[car_id]['position'][0],car_info[car_id]['position'][1],station_info[b]['position'][0],station_info[b]['position'][1]),station_info[b]['frequency'])
        else:
            db = path_loss(calculation_dist(car_info[car_id]['position'][0],car_info[car_id]['position'][1],station_info[b]['position'][0],station_info[b]['position'][1]),station_info[b]['frequency'])
            if max_db < db:
                temp = car_info[b]['connect_station']
                max_db = db
                car_info[a]['db']=max_db
                car_info[a]["connect_station"]=b
        b+=1
    return
#decide car base stand by highest db in entropy algorithm
def decide_db_and_connect_station_entropy(car_id):
    b=0
    for b in range(len(station_info)):
        if b == 0:
            max_db=path_loss(calculation_dist(car_info[car_id]['position'][0],car_info[car_id]['position'][1],station_info[b]['position'][0],station_info[b]['position'][1]),station_info[b]['frequency'])
            stationid=b
        else:
            db = path_loss(calculation_dist(car_info[car_id]['position'][0],car_info[car_id]['position'][1],station_info[b]['position'][0],station_info[b]['position'][1]),station_info[b]['frequency'])
            if max_db < db:
                max_db = db
                stationid=b   
        b+=1
    if(max_db-car_info[car_id]['db']>=entropy_number):
        car_info[car_id]['db']=max_db
        car_info[car_id]['connect_station']=stationid
    return
#draw map
plt.ion()
plt.subplots()
plt.xlim(0,25)
plt.ylim(0,25)
plt.xticks(np.arange(0,25,2.5))
plt.yticks(np.arange(0,25,2.5))
plt.grid()
plt.show()

#create base stand station
i=1.25
j=1.25
station_x = []
station_y = []
station_num = 0
while i < 25:
    while j < 25:
        if random.random()<=0.1:  #because probability is 1/10
            freq = random.randint(1,10)*100
            p=random.random()
            if p<=0.25: #up 0.1
                station_info.append({"position":[i,j+0.1],"frequency":freq})
            elif p>0.25 and p<=0.5: #down 0.1
                station_info.append({"position":[i,j-0.1],"frequency":freq})
            elif p>0.5 and p<=0.75: #left 0.1
                station_info.append({"position":[i-0.1,j],"frequency":freq})
            elif p>0.75 and p<=1: #right 0.1
                station_info.append({"position":[i+0.1,j],"frequency":freq})
            station_num+=1
        j+=2.5
    i+=2.5 
    j=1.25   

for b in range(len(station_info)):
    station_x.append(station_info[b]["position"][0])
    station_y.append(station_info[b]["position"][1])
#decide car's generate rate
miu = 1/12
car_generate_rate = poisson.pmf(1,miu)

while 1:
    plt.clf() #clear map
    plt.xlim(0,25)
    plt.ylim(0,25)
    plt.xticks(np.arange(0,25,2.5))
    plt.yticks(np.arange(0,25,2.5))
    plt.grid()

    #create new car according to its initial position and set its direction
    i=2.5
    while i <= 22.5:
        if random.random() <= car_generate_rate:
            car_number+=1
            p=random.random()
            if p <= 0.5:
                car_info.append({'position':[i,0],'direction':"UP",'call':0,'db':0,'connect_station':1000,'calling_time':0})
            if p > 0.5 and p <= 0.5625:
                car_info.append({'position':[i,0],'direction':"DOWN",'call':0,'db':0,'connect_station':1000,'calling_time':0})
            if p > 0.5625 and p <= 0.78125:
                car_info.append({'position':[i,0],'direction':"LEFT",'call':0,'db':0,'connect_station':1000,'calling_time':0})
            if p > 0.78125 and p <=1:
                car_info.append({'position':[i,0],'direction':"RIGHT",'call':0,'db':0,'connect_station':1000,'calling_time':0})
        if random.random() <= car_generate_rate:
            car_number+=1
            p = random.random()
            if p <= 0.5:
                car_info.append({'position':[i,25],'direction':"DOWN",'call':0,'db':0,'connect_station':1000,'calling_time':0})
            if p > 0.5 and p <= 0.5625:
                car_info.append({'position':[i,25],'direction':"UP",'call':0,'db':0,'connect_station':1000,'calling_time':0})
            if p > 0.5625 and p <= 0.78125:
                car_info.append({'position':[i,25],'direction':"LEFT",'call':0,'db':0,'connect_station':1000,'calling_time':0})
            if p > 0.78125 and p <=1:
                car_info.append({'position':[i,25],'direction':"RIGHT",'call':0,'db':0,'connect_station':1000,'calling_time':0})
        if random.random() <= car_generate_rate:
            car_number+=1
            p = random.random()
            if p <= 0.5:
                car_info.append({'position':[0,i],'direction':"RIGHT",'call':0,'db':0,'connect_station':1000,'calling_time':0})
            if p > 0.5 and p <= 0.5625:
                car_info.append({'position':[0,i],'direction':"LEFT",'call':0,'db':0,'connect_station':1000,'calling_time':0})
            if p > 0.5625 and p <= 0.78125:
                car_info.append({'position':[0,i],'direction':"UP",'call':0,'db':0,'connect_station':1000,'calling_time':0})
            if p > 0.78125 and p <=1:
                car_info.append({'position':[0,i],'direction':"DOWN",'call':0,'db':0,'connect_station':1000,'calling_time':0})
        if random.random() <= car_generate_rate:
            car_number+=1
            p = random.random()
            if p <= 0.5:
                car_info.append({'position':[25,i],'direction':"RIGHT",'call':0,'db':0,'connect_station':1000,'calling_time':0})
            if p > 0.5 and p <= 0.5625:
                car_info.append({'position':[25,i],'direction':"LEFT",'call':0,'db':0,'connect_station':1000,'calling_time':0})
            if p > 0.5625 and p <= 0.78125:
                car_info.append({'position':[25,i],'direction':"UP",'call':0,'db':0,'connect_station':1000,'calling_time':0})
            if p > 0.78125 and p <=1:
                car_info.append({'position':[25,i],'direction':"DOWN",'call':0,'db':0,'connect_station':1000,'calling_time':0})
        i += 2.5        
    car_x=[]
    car_y=[]
    
    for a in range(len(car_info)):
        car_x.append(car_info[a]['position'][0])
        car_y.append(car_info[a]['position'][1])

    #change car's position at cross
    for b in range(len(car_info)):
        if(((car_info[b]["position"][0])%2.5==0)and(((car_info[b]["position"][1])%2.5)==0)):
            if car_info[b]["direction"] == "RIGHT":
                p = random.random()
                if p <= 0.5:
                    car_info[b]["direction"] == "RIGHT"
                    car_info[b]["position"][0]+=0.02 
                if p > 0.5 and p <= 0.5625:
                    car_info[b]["direction"] == "LEFT"
                    car_info[b]["position"][0]-=0.02 
                if p > 0.5625 and p <= 0.78125:
                    car_info[b]["direction"] == "UP"
                    car_info[b]["position"][1]+=0.02 
                if p > 0.78125 and p <=1:
                    car_info[b]["direction"] == "DOWN"
                    car_info[b]["position"][1]-=0.02 
            if car_info[b]["direction"] == "LEFT":
                p = random.random()
                if p <= 0.5:
                    car_info[b]["direction"] == "LEFT"
                    car_info[b]["position"][0]-=0.02 
                if p > 0.5 and p <= 0.5625:
                    car_info[b]["direction"] == "RIGHT"
                    car_info[b]["position"][0]+=0.02 
                if p > 0.5625 and p <= 0.78125:
                    car_info[b]["direction"] == "UP"
                    car_info[b]["position"][1]+=0.02 
                if p > 0.78125 and p <=1:
                    car_info[b]["direction"] == "DOWN"
                    car_info[b]["position"][1]-=0.02 
            if car_info[b]["direction"] == "UP":
                p = random.random()
                if p <= 0.5:
                    car_info[b]["direction"] == "UP"
                    car_info[b]["position"][1]+=0.02 
                if p > 0.5 and p <= 0.5625:
                    car_info[b]["direction"] == "DOWN"
                    car_info[b]["position"][1]-=0.02 
                if p > 0.5625 and p <= 0.78125:
                    car_info[b]["direction"] == "RIGHT"
                    car_info[b]["position"][0]+=0.02 
                if p > 0.78125 and p <=1:
                    car_info[b]["direction"] == "LEFT"
                    car_info[b]["position"][0]-=0.02 
            if car_info[b]["direction"] == "DOWN" :
                p = random.random()
                if p <= 0.5:
                    car_info[b]["direction"] == "DOWN"
                    car_info[b]["position"][1]-=0.02 
                if p > 0.5 and p <= 0.5625:
                    car_info[b]["direction"] == "UP"
                    car_info[b]["position"][1]+=0.02 
                if p > 0.5625 and p <= 0.78125:
                    car_info[b]["direction"] == "RIGHT"
                    car_info[b]["position"][0]+=0.02 
                if p > 0.78125 and p <=1:
                    car_info[b]["direction"] == "LEFT"
                    car_info[b]["position"][0]-=0.02 
        else:
            if car_info[b]["direction"]=="UP":
                car_info[b]["position"][1]+=0.02
            if car_info[b]["direction"]=="DOWN":
                car_info[b]["position"][1]-=0.02
            if car_info[b]["direction"]=="RIGHT":
                car_info[b]["position"][0]+=0.02
            if car_info[b]["direction"]=="LEFT":
                car_info[b]["position"][0]-=0.02
    
    #delete the car whose location is out of scopes(x,y < 0 or x,y >25)
    for a in range(len(car_info)):
        if a >= len(car_info):
            break
        if(car_info[a]["position"][1]>25 or car_info[a]["position"][1]<0 or car_info[a]["position"][0]>25 or car_info[a]["position"][0]<0):
            del car_info[a]
            car_number-=1
    #decide normal distribution time
    i=0
    for i in range(200):
        rate = norm.pdf(i,180,10)
        if random.random()<=rate:
            normal_time=i
            break
        
    #car makes call 0:no call 1:calling
    a=0
    for a in range(len(car_info)):
        if(car_info[a]['call']==0):
            if random.randint(1,1800)<=1:
                car_info[a]['call']=1
                car_info[a]['calling_time']=normal_time
                calling_number+=1
        
    #connect calling car and station (1:minium 2:best_effort 3:entropy 4:)
    a=0
    for a in range(len(car_info)):
        if car_info[a]['call']==1:
            if mathod == 1:
                if(car_info[a]['db']<=100):
                    temp = car_info[a]['connect_station']
                    decide_db_and_connect_station(a)
                    if temp!=car_info[a]['connect_station'] and temp!=1000:
                        res+=1
                
            elif mathod == 2:
                temp = car_info[a]['connect_station']
                decide_db_and_connect_station(a)
                if temp!=car_info[a]['connect_station'] and temp!=1000:
                    res+=1
            elif mathod == 3:
                temp = car_info[a]['connect_station']
                decide_db_and_connect_station_entropy(a)
                if temp!=car_info[a]['connect_station'] and temp!=1000:
                    res+=1
            elif mathod == 4:
                temp = car_info[a]['connect_station']
                if temp ==1000:
                    decide_db_and_connect_station(a)
                else:
                    if calculation_dist(car_info[a]['position'][0],car_info[a]['position'][1],station_info[car_info[a]['connect_station']]['position'][0],station_info[car_info[a]['connect_station']]['position'][1])<=15:
                        decide_db_and_connect_station(a)
                if temp!=car_info[a]['connect_station'] and temp!=1000:
                    res+=1
            #draw the line between car and base stand
            if(car_info[a]['connect_station']<1000):        
                plt.plot([car_info[a]['position'][0],station_info[car_info[a]['connect_station']]['position'][0]],[car_info[a]['position'][1],station_info[car_info[a]['connect_station']]['position'][1]]) 
    #minus 1's calling time.
    #if it is equal to zero ,then change its calling status to 0 and calling number -1
    a = 0
    for a in range(len(car_info)):
        if car_info[a]['call']==1:
            car_info[a]['calling_time']-=1
            if car_info[a]['calling_time']<=0:
                car_info[a]['call']=0  
                calling_number-=1          
    
    #print information
    print("*********************************")
    print("policy:%s"%mathod)
    print("number of base stand:%s"%station_num)
    print("number of cars:%s"%car_number)
    print("number of callings:%s"%calling_number)
    print("handoff:%s"%res)
    print("*********************************")
    plt.scatter(station_x,station_y,c='r')    
    plt.scatter(car_x,car_y)
    plt.pause(0.0001)
    plt.show()
