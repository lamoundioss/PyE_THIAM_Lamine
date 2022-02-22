

date = '171/12/1993'

def datevalide():
    global date
    
    Mois = date[1]
    Test = 0
    if date[0].isdigit() and date[2].isdigit():
        J = int(date[0])
        A = int(date[2])
    
        if len(Mois) == 2 or len(Mois) == 1:
            i = (0, 1)
            M = int(Mois)
            if Mois.isdigit():
                if (J<1)or(J>31)or(((M==4)or(M==6)or(M==9)or(M==11))and(J>30))or(M<1)or(M >12)or(A<=0) :
                    print("La date que vous avez saisi est incorrect")
                elif ((M==2)and((A%4==0)or(A%100!=0)or(A%400==0))and(J>29))or(((A%4!=0)or(A%100==0)or(A%400!=0))and(J>28)):
                    print("La date que vous avez saisi est incorrect")
                else:
                    Test = 1
            else:
                print("La date ist invalide")
        elif len(Mois)==3:
            mois = ''
            for i in range(3):
                mois = mois + Mois[i]
            if Mois=='jan' or Mois=='fev' or Mois=='mai' or Mois=='oct' or Mois=='dec':
                if J > 0 and J <= 31 and A > 0 :
                    Test = 1
                else:
                    print("La date est incorrect")
            if Mois=='avr' or  Mois=='sep' or Mois=='nov':
                if J > 0 and J <= 30 and A > 0:
                    Test = 1
                else:
                    print("La date est incorrect")
            if (Mois == 'fev') and ((((A%4==0)or(A%100!=0)or(A%400==0))and(J>29)) or (((A%4!=0)or(A%100==0)or(A%400!=0))and(J>28))):
                Test = 1
            else:
                print("La date est incorrect")
        elif len(Mois)==4:
            mois = ''
            for i in range(4):
                mois = mois + Mois[i]
            if Mois=='mars' or Mois == 'janv' or Mois=='juil' or Mois=='aout':
                if J > 0 and J <= 31 and A > 0 :
                    Test = 1
                else:
                    print("La date est incorrect")
            if Mois=='juin' and J > 0 and J <= 31 and A > 0 :
                Test = 1
            else:
                print("La date est invalide")
        else:
            if Mois=='janvier' and  Mois=='juillet' and Mois=='octobre' and Mois=='decembre':
                if J > 0 and J <= 31 and A > 0 : 
                    Test = 1
                else:
                    print("La date est incorrect")
            if Mois=='avril' and Mois=='septembre' and Mois=='novembre':
                if J > 0 and J <= 30 and A > 0:
                    Test = 1
                else:
                    print("La date est incorrect")
            if Mois=='fevrier' and (((A%4==0)or(A%100!=0)or(A%400==0)and(J>29))or(((A%4!=0)or(A%100==0)or(A%400!=0))and(J>28))):
                Test = 1
            else:
                print("La date est invalide")
    else:
        print("La date est invalide")
    
    return Test
