inp = input("N, R, SR, UR, & N° de Packs :  ")
input_list = []
input_list.extend([int(x) for x in inp.split(',')])
N = input_list[0]/(input_list[0]+input_list[1])
R = 1-N
GR = ((input_list[1]-1)/((input_list[1]-1)+input_list[2]+input_list[3])+(input_list[1])/((input_list[1])+input_list[2]+input_list[3]))/2
SR = input_list[2]/(input_list[1]+input_list[2]+input_list[3])
UR = 1-SR-GR
Total =[]
if input_list[4] > 1 :
    T0 = 0
    while T0 <= input_list[4] :
        N = round((input_list[0]/(input_list[0]+input_list[1]))*(0.001311*T0)*100, 1)
        R = round((1-N)*(0.001311*(T0+1))*100, 1)
        if N > R :
            Total.append('N')
        else :
            Total.append('R')
        SR = round((input_list[2]/(input_list[1]+input_list[2]+input_list[3]))*(0.001311*T0)*100, 1)
        UR = round((1-SR-R)*(0.001311*T0)*100, 1)
        if R > SR :
            Total.append('R')
        else :
            Total.append('SR')
        T0 += 1
P = 0
while P < (input_list[4]*3) :
    Total.sort()
    print(Total.pop())
    P += 1

