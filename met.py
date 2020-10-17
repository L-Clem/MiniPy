import requests

url = 'http://api.openweathermap.org/data/2.5/forecast?q=Loupes,fr&units=metric&appid=9f6f1223c49ec066233727939ce02668'
res = requests.get(url)
data = res.json()
count = 0
J = {}
while count < 40 :
    ny = 'J' + format(count + 1)  
    l = []
    l.append(data['list'][count]['main']['temp'])
    l.append(data['list'][count]['main']['humidity'])
    try:
        l.append(data['list'][count]['rain']['3h'])
    except KeyError:
        pass
    l.append(data['list'][count]['wind']['speed'])
    l.append(data['list'][count]['clouds']['all'])
    J[ny] = sum(l)
    l.clear()
    count += 1           
j = []
k = []
for cle in J.values():
    j.append(int(cle))
d1 = round((j[0]+j[1]+j[2]+j[3]+j[4]+j[5]+j[6]+j[7])/8, 2)
d2 = round((j[8]+j[9]+j[10]+j[11]+j[12]+j[13]+j[14]+j[15])/8, 2)
d3 = round((j[16]+j[17]+j[18]+j[19]+j[20]+j[21]+j[22]+j[23])/8, 2)
d4 = round((j[24]+j[25]+j[26]+j[27]+j[28]+j[29]+j[30]+j[31])/8, 2)
d5 = round((j[32]+j[33]+j[34]+j[35]+j[36]+j[37]+j[38]+j[39])/8, 2)
day = []
def biblio(d) :
    if 105.2555556 < d < 118.6333333 :
        day.append('A')
    if 118.6333333 < d < 132.0111111 :
        day.append('A')       
    if 91.87777778 < d < 105.2555556 :
        day.append('B')
    if 132.0111111 < d < 145.3888889 :
        day.append('B')        
    if 78.5 < d < 91.87777778 :
        day.append('C')
    if 145.3888889 < d < 158.7666667 :
        day.append('C')
    if 65.12222222 < d < 78.5 :
        day.append('D')            
    if 158.7666667 < d < 172.1444444 :
        day.append('D')            
    if 51.74444444 < d < 65.12222222 :
        day.append('E')           
    if 172.1444444 < d < 185.5222222 :
        day.append('E')            
    if 38.36666667 < d < 51.74444444 :
        day.append('F')            
    if 185.5222222 < d < 198.9 :
        day.append('F')             
biblio(d1)
biblio(d2)
biblio(d3)
biblio(d4)
biblio(d5)
print('Notes de 24h en 24h : ', day)