#tugas no. 4 membuat program menghitung keliling lingkaran dan volume kubus
#program menghitung keliling lingkaran

#import 'math' agar 'pi' mempunyai nilai 
import math

#membuat inputan jari-jari berupa float
r = float(input("Masukan Jari-jari = "))

#membuat rumus keliling
keliling = 2*math.pi*r

#membuat output
print ("Keliling Lingkaran = ",keliling)