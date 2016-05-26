
#!/usr/bin/python

from datetime import datetime
import numpy as np
import RPi.GPIO as gp
from time import sleep

conv_date = lambda x: datetime.strptime(x,"%Y-%m-%d")
conv_temp = lambda x: x
conv_str = lambda x: x

def conv_time(x):
    if '.' in x:
        t = datetime.strptime(x,'%H:%M:%S.%f')
        # print t
    else:
        t = datetime.strptime(x,'%H:%M:%S')
    return t
        
# Piove?
def piove(filename_dati, filename_soglia):
    f = open(filename_soglia)
    soglia_pioggia = np.genfromtxt(f)
    f.close()
    f = open(filename_dati)
    sensore =  np.genfromtxt(f, delimiter=" ", converters={0: conv_date,1: conv_time,2: conv_temp})
    return sensore[-1][2] > soglia_pioggia

def secco(filename_dati, filename_secco):
    f = open(filename_secco)
    soglia_secco = np.genfromtxt(f)
    f.close()
    f = open(filename_dati)
    sensore =  np.genfromtxt(f, delimiter=" ", converters={0: conv_date,1: conv_time,2: conv_temp})
    return sensore[-1][2] > soglia_secco

gp.setup(18,gp.OUT)
gp.setup(7,gp.OUT)

filename_dati_pioggia = 'dati_pioggia.txt'
filename_dati_umido = 'dati_umido.txt'
filename_soglia_pioggia = 'soglia_pioggia.txt'
filename_soglia_umido = 'soglia_umido.txt'



if piove(filename_dati_pioggia,filename_soglia_pioggia) & secco(filename_dati_umido,filename_soglia_umido):
    print 'Attivo elettrovalvola per irrigare'
    gp.setup(18,True)
    sleep(0.030)
    gp.setup(18,False)
else:
    print "Terreno troppo umido o pioggia in atto: chiudo l'elettrovalvola"
    gp.setup(7,True)
    sleep(0.030)
    gp.setup(7,False)


    
