#Óðinn Kristjánsson
#17.1.2017
#upprifjun2
print("Liður1")



nafn1=input("Fyrra nafn")
haed1=int(input("Hver er hæð þín í cm"))
nafn2=input("Seinna nafn")
haed2=int(input("Hver er hæð þín í cm"))
if haed1==haed2:
    print(nafn1,"og",nafn2,"eru jafn stór")
elif haed2>haed1:
    print(nafn2,"er stærri en",nafn1)
elif haed2<haed1:
    print(nafn1,"er stærri en",nafn2)



print("Liður2")



lengd=int(input("Sláðu inn lengd í m"))
breidd=int(input("Sláðu inn breidd í m"))
ekri=(lengd*breidd)/4046
print("Þessi reitur er",round(ekri,3),"ekrur")



print("Liður3")
breidd=int(input("Sláðu inn breidd í m"))
for x in range(0,201,10):
    print("Stærð"," ","Lengd í ekrum")\
    ekrur=(x*breidd)/4046
    print(x," ",round,6)



print("Liður5")



heild=int(input("Hver er heildin"))
prosenta=int(input("Hver er prósentan"))
niðurstaða=prosenta/heild








