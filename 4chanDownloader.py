#!/usr/bin/python
# # TODO: 
# #       1) Checar se arquivo ja existe antes de baixar novamente
# ###################################################################

import requests
import sys
import os
from bs4 import BeautifulSoup

def baixar(pasta,foto):
    fotoTrim = foto[2:] # remove link feio com // na frente
    fotoTrim = 'http://'+fotoTrim

    print(fotoTrim)
    
    salvar = requests.get(fotoTrim)

    fotoNome = fotoTrim.split('/')
    fp = open(pasta+fotoNome[4],'wb')
    for arq in salvar.iter_content(10000):
        fp.write(arq)
    print ('='*80)
    fp.close()

########################################################################
if(len(sys.argv) < 2):
    print('\nFalta URL do 4chan\n')
    print('='*30)
    print('\nModo de usar:')
    print(sys.argv[0]+' [URL da thread] [Diretorio]')
    print('Saindo... \n\n\n')
    exit()

pasta = ""

if(len(sys.argv) > 2):
    if not os.path.exists(sys.argv[2]):
        os.makedirs(sys.argv[2])
        pasta=sys.argv[2]+'/'
        print("Salvando no diretorio: "+pasta)


url = sys.argv[1]
req = requests.get(url).text
soup = BeautifulSoup(req,'lxml')

info = soup.select('a[class="fileThumb"]')
for href in info:
    baixar(pasta, href.get("href"))

