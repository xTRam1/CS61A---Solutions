name = 'old value'

def print_name():
    print(name)

def change_name():
    name = 'new value'

def add_to_name():
    name = name + 'extran value'

'''

simdi python'da bir funksiyonu calistirdiginda ne yapiyordu?
once yeni bir frame olusturuyordu. sonra ise butun degiskenleri o olusturulan frame'nin icinde tutuyordu.

sen "x = ..." diye birsey yazdiginda frame'in icine yeni bir degisken ekliyor.
yani sen bir degiskene "yazmaya" calistiginda, yani sunu yazdiginda x = ....,
eger degisken framin icinde yok ise framenin icine yeni degisken ekliyor
eger var ise olan degiskenin degerini degistiyor.
'''

def d():
    x = "value" # framin icinde x diye bir degisken olusturdu.
    x = 'new value' # bu degiskenin degerini deggistirdi.

'''

sen bir degiskeni sadece "okudugunda" ise once kendi framine bakiyor orda var mi diye.
eger var ise o degeri aliyor eger yoksa bir onceki frame'e bakiyor. bu sekide kendiken kapsayan butun frame'leri geziyor.
eger bulamaz ise error veriyor.
'''

####################
def c():
    x = 34
    print(x) # bu durumda x f' fonkisyonun frame'nin icinde direk degeri alip print ediyor.
####################


####################
def a():
    print(x) # bu durunda ise f fonksiyonun frame'nin icinde x yok. bir onceki frame'e bakiyor. O framede gobal frame. ordada yok. bu sefer hata veriyor.

####################

####################
x = 124
def a():
    print(x) # bu durumda ise f fonksiyonun frame'nin icinde x yok. bir onceki frame'de var. onda degeri aliyor ve print ediyor.
####################


'''
problem asagikai durumda cikiyor.
simdi asadigaki durumda soyle bir problem var.
biz once x degerini okuyoruz.

x'i okudugumuz anda x f'in framinin icinde degil. bir onceki framede.yani 124
okuduktan sonra ise x f'in framinin icinde x diye bir degisken olusturuyor.3

iste python bu duruma izin vermiyor.

yani sen bir degiskenina yaziyorsan o degisken kesinlike o framin icinde olmak zorunda. 
'''

x = 124
def f():
    x = x + 10

