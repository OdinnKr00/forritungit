#Óðinn Kristjánsson
#24.1.2017


#Dæmi 2
#Fær fornafn og eftirnafn og prentar út halló með fullu nafni
fornafn=input("Sláðu inn fyrsta nafnið þitt")
eftirnafn=input("Sláðu inn eftirnafnið þitt")
print("Halló",fornafn,eftirnafn)


#Dæmi 1
#Fær tölur og birtir summu og margfeldi þeirra
tala1=int(input("Sláðu inn tölu"))
tala2=int(input("Sláðu inn aðra tölu"))
utkoma1=tala1+tala2
utkoma2=tala1*tala2
print("Þetta er summa talananna",utkoma1)
print("Þetta er marfeldi talnanna",utkoma2)


#Dæmi 3
#Fær setningu og segir hversu margir lág og hástafir eru í henni og hversu oft lágstafir koma á eftir hástöfum
lagstafur=0
hastafur=0
laghastafur=0
texti=input("Sláðu in setningu")
for staf in texti:
    if staf.islower():
        lagstafur=lagstafur+1
    if staf.isupper():
        hastafur=hastafur+1
for i in range(len(texti)):
    if texti[i].isupper():
        hastafur=hastafur+1
    if texti[i+1].islower():
        laghastafur=laghastafur+1
print("Það eru",lagstafur,"lágstafir")
print("Það eru",hastafur,"hástafir")
print("Það eru",laghastafur,"lágstafir sem koma á eftir hástaf")