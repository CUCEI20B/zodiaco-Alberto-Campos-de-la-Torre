signos = ["aries","tauro","geminis","cancer","leo","virgo","libra","escorpio","sagitario","capricornio","aquario","pisis"]
dia = int(input("Ingresa el dia de tu fecha de nacimiento = "))
mes = int(input("Ingresa el mes de tu nacimiento = "))

if  (31>= dia >=21 and mes ==3)or(1<= dia<=20 and mes==4):
       print(signos[0])
elif  (30>= dia >=21 and mes ==4)or(1<= dia<=20 and mes==5):
       print(signos[1])
elif  (31>= dia >=21 and mes ==5)or(1<= dia<=21 and mes==6):
       print(signos[2])
elif  (30>= dia >=22 and mes ==6)or(1<= dia<=22 and mes==7):
       print(signos[3])
elif  (31>= dia >=23 and mes ==7)or(1<= dia<=22 and mes==8):
       print(signos[4])
elif  (31>= dia >=23 and mes ==8)or(1<= dia<=22 and mes==9):
       print(signos[5])
elif  (30>= dia >=23 and mes ==9)or(1<= dia<=22 and mes==10):
       print(signos[6])
elif  (31>= dia >=23 and mes ==10)or(1<= dia<=22 and mes==11):
       print(signos[7])
elif  (30>= dia >=23 and mes ==11)or(1<= dia<=21 and mes==12):
       print(signos[8])
elif  (31>= dia >=22 and mes ==12)or(1<= dia<=20 and mes==1):
       print(signos[9])
elif  (31>= dia >=21 and mes ==1)or(1<= dia<=18 and mes==2):
       print(signos[10])
elif  (29>= dia >=19 and mes ==2)or(1<= dia<=20 and mes==3):
       print(signos[11])
