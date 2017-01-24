#Óðinn Kristjánsson
#17.1.2017
#upprifjun1
print("Liður1")



"""Tekur inn tölur og prentar út summu og margfeldi þeirra"""
tala1=int(input("Sláðu inn tölu"))
tala2=int(input("Sláðu inn aðra tölu"))
utkoma1=tala1+tala2
utkoma2=tala1*tala2
print("Þetta er summa talananna",utkoma1)
print("Þetta er marfeldi talnanna",utkoma2)



print("Liður2")



"""Fær fornafn og eftirnafn og prentar síðan út Halló fyrir framan nafnið"""
fornafn=input("Sláðu inn fyrsta nafnið þitt")
eftirnafn=input("Sláðu inn eftirnafnið þitt")
print("Halló",fornafn,eftirnafn)



print("Liður3")



"""Breytir km í m"""
kilometrar=float(input("Sláðu inn km sem ég á að breyta í m"))
m=kilometrar*1000
print(kilometrar,"km""eru",m,"metrar")



print("Liður4 og Liður5")



"""Fær laun á tímann og tímann sjálfan og reiknar heildarlaun og ef launin
eru meira en 30þús þá er tekinn 20% skattur af því sem er umfram 30þús"""
launklst=int(input("Hver eru laun þín á klst?"))
vinna=int(input("Hversu marga klst vannstu?"))
samtals=vinna*launklst
skattur=samtals*0.20
print("Heildarlaun þín eru",samtals)
if samtals>30000:
   print("Skattur",round(skattur),"krónur")



print("Liður6")



"""Fær inn gráðu fjölda og reiknar hversu margir hringir og afgangs gráður eru"""
gradur=int(input("Hvað eru gráðurnar margar"))
hringur=print("Það gerir",str(gradur//360),"hringi og",str(gradur%360),"gráður")





