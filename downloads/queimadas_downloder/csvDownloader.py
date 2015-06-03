#!/usr/bin/python
# -*- coding: latin-1 -*-
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
"""
__author__="apararanhoss"
__date__ ="$18/09/2014 22:27:36$"

if __name__ == "__main__":
    print "Hello World"
"""

import urllib
import urllib2
import datetime
import os

import getpass
#import urllib.request
#import urllib.parse

#Proxy
use_proxy=False
if(use_proxy):
	usr=raw_input("Usuario: ")
	psw = getpass.getpass("Senha: ")
	#proxy = urllib.request.ProxyHandler({'http': "http://"+usr+":"+psw+"@172.16.107.1:3128"})
	proxy = urllib2.ProxyHandler({'http': "http://"+usr+":"+psw+"@172.16.107.1:3128"})
	auth = urllib2.ProxyBasicAuthHandler()
	opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
	#opener = urllib2.build_opener(proxy)
	urllib2.install_opener(opener)


# do POST

#<INPUT TYPE="hidden" NAME="sql" VALUE="SELECT Pais,Estado,Regiao,Municipio,count(*) as contagem FROM focosAtributos WHERE 1 AND LAT >= -55.0 AND LAT <= 55.0 AND LON >= -120.0 AND LON <= 65.0 AND Data >= '2014-09-17 00:00:00' AND Data <= '2014-09-18 23:59:59' AND Pais = 'Brasil'   AND Estado = 'AC' group by Municipio order by contagem desc">
#<INPUT TYPE="hidden" NAME="sql" VALUE="SELECT Pais,Estado,Regiao,Municipio,count(*) as contagem FROM focosAtributos WHERE 1 AND LAT >= -55.0 AND LAT <= 55.0 AND LON >= -120.0 AND LON <= 65.0 AND Data >= '2014-09-17 00:00:00' AND Data <= '2014-09-18 23:59:59' AND Pais = 'Brasil'   AND Estado = 'AM' group by Municipio order by contagem desc">
#<INPUT TYPE="hidden" NAME="sql" VALUE="SELECT Pais,Estado,Regiao,Municipio,count(*) as contagem FROM focosAtributos WHERE 1 AND LAT >= -55.0 AND LAT <= 55.0 AND LON >= -120.0 AND LON <= 65.0 AND Data >= '2014-09-17 00:00:00' AND Data <= '2014-09-18 23:59:59' AND Pais = 'Brasil'   AND Estado = 'AP' group by Municipio order by contagem desc">

#<INPUT TYPE="hidden" NAME="gby" VALUE="Municipio">
estados=['AC','AM','AP','MA','MT','PA','RO','RR','TO']
#url_1
url_2 = 'http://www.dpi.inpe.br/proarco/bdqueimadas/graf2csv.php'
now = datetime.datetime.now()
print now
now = now - datetime.timedelta(days=1)
for estado in estados:
    print estado
    values = dict(sql='SELECT Pais,Estado,Regiao,Municipio,count(*) as contagem FROM focosAtributos WHERE 1 AND LAT >= -55.0 AND LAT <= 55.0 AND LON >= -120.0 AND LON <= 65.0 AND Data >= \''+now.strftime("%Y-%m-%d")+' 00:00:00\' AND Data <= \''+now.strftime("%Y-%m-%d")+' 23:59:59\' AND Pais = \'Brasil\'   AND Estado = \''+estado+'\' group by Municipio order by contagem desc', gby='Municipio')
    data = urllib.urlencode(values)
    req = urllib2.Request(url_2, data)
    rsp = urllib2.urlopen(req)
    content = rsp.read()
    
    dia=now.strftime("%d")
    mes=now.strftime("%m-%B")
    ano=now.strftime("%Y")    
    #banco='/media/BancodeDados/Banco de Dados/'
    #raiz=banco+"01- ÁREA_FOCOS DE CALOR/Projeto SIG - Focos de Calor/Monitoramento/"
    raiz="Downloads/"
    path=raiz+ano+'/'+estado+'/'+mes+'/'+dia+'/'
    
    if not os.path.exists(path):
        os.makedirs(path)        
    fo = open(path+dia+'-'+estado+".csv", "w+")
    
    fo.write(content)
    oldstr="\r\r\n"
    #print oldstr
    #content=content.replace(oldstr, "\r\n")
    #print content
    print fo
    fo.close()
    
# print result
#import re
#pat = re.compile('Title:.*')
#print pat.search(content).group()