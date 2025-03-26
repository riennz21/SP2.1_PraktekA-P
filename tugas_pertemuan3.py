#IF ELSE
#input
print("hasil ujian ")
nilai = int(input("masukan nilai:"))

#proses
if nilai >= 80 :
    status = 'lulus'
else :
    status = 'gagal'

#output
print('status :',status)

#NESTED IF

#input
print('hasil ujian')
nilai + int (input('masukan nilai :'))

#proses
if nilai >=70 :
    status = 'lulus'
    if nilai >=80 :
        predikat = 'memuaskan'
    else :
        predikat = 'cukup'
else:
    status = 'gagal'
    status = 'kurang'


#EL IF

#input
print('hasil ujian')
nilai = int(input('masukan nilai :'))

#proses
if nilai > 80 :
    transkip = 'A'
elif nilai > 60 :
    transkip = 'B'
elif nilai > 40 :
    transkip = 'C'
elif nilai > 20 :
    transkip = 'D'
elif :
    transkip = 'E'

#OUTPUT
print('nialai transkip :',transkip)
print('----------------')