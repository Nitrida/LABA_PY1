rost = input("Введите ваш рост - ")
ves = input("Введите ваш вес - ")
kol_h = input("Введите количество пройденых шагов - ")
vr = input("Введите время вашей ктивности - ")

dl_h =int(rost)/4+0.37
dist=dl_h*int(kol_h)
scor=dist/int(vr)#скорость ходьбы(
call=0.035*int(ves)+(scor*scor/int(rost))*0.029*int(ves)
print("Вы прошли "+ str(dist) + "м и потратили " + str(call) + "калл")