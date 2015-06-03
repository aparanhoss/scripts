#!/usr/bin/python
# -*- coding: latin-1 -*-
from HTMLParser import HTMLParser
import urllib
import urllib2
import datetime
import httplib, mimetypes
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import zipfile
import os
import getpass
#from poster.encode import multipart_encode



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


#print content
#fo.close()
#dados={"sql":"select * from focosAtributos WHERE 1 AND LAT >= -55 AND LAT <= 55 AND LON >= -120 AND LON <= -30 AND Data >= '2014-09-22 00:00:00' AND Data <= '2014-09-23 23:59:59' AND Satelite = 'AQUA_M-T'"}

#dados={}
# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    dados={}
    def getDados(self):
        return self.dados
    def handle_starttag(self, tag, attrs):
      if tag=='input':
	#print "Start tag:", tag
	name=""
	value=""
        for attr in attrs:	  
            #print "     attr:", attr
            if attr[0]=='name':
	      name=attr[1]
	    elif attr[0]=='value':
	      value=attr[1]
	if name:      
	  self.dados.update({name:value})
	#print dados
	    
            #dados.update(attr)
            #print type(attr)
  
# instantiate the parser and fed it some HTML
def download(conteudo):#!/usr/bin/python
# -*- coding: latin-1 -*-
    now1 = datetime.datetime.now()
    now1 = now1 - datetime.timedelta(days=1)
    dia1=now1.strftime("%Y-%m-%d")
    parser = MyHTMLParser()
    parser.feed(conteudo)
  
    da=parser.getDados()
    #print da
    da.update({'endereco':'aparanhoss@gmail.com'})
    #print da
    url_2="http://www.dpi.inpe.br/proarco/bdqueimadas/tabela.php"
    nome=da.get('filename')
    data, headers = multipart_encode(da)

    data = urllib.urlencode(da)
    req = urllib2.Request(url_2, data)
    rsp = urllib2.urlopen(req)
    content = rsp.read()
    
    
    dia=now1.strftime("%d")
    mes=now1.strftime("%m-%B")
    ano=now1.strftime("%Y")    
    #banco='/media/BancodeDados/Banco de Dados/'
    #raiz=banco+"01- ÁREA_FOCOS DE CALOR/Projeto SIG - Focos de Calor/Monitoramento/"
    raiz="Downloads/"
    path=raiz+ano+'/'+estado+'/'+mes+'/'+dia+'/'
    
    
    #path='Downloads/'+estado+'/'+dia+'/'
    if not os.path.exists(path):
        os.makedirs(path)
    fope = open(path+nome, "wb+")
    fope.write(content)
    fope.close()
    print fope.name    
    with zipfile.ZipFile(fope.name, "r") as z:
      z.extractall(path)
    
     

# do POST

#<INPUT TYPE="hidden" NAME="sql" VALUE="SELECT Pais,Estado,Regiao,Municipio,count(*) as contagem FROM focosAtributos WHERE 1 AND LAT >= -55.0 AND LAT <= 55.0 AND LON >= -120.0 AND LON <= 65.0 AND Data >= '2014-09-17 00:00:00' AND Data <= '2014-09-18 23:59:59' AND Pais = 'Brasil'   AND Estado = 'AC' group by Municipio order by contagem desc">
#<INPUT TYPE="hidden" NAME="sql" VALUE="SELECT Pais,Estado,Regiao,Municipio,count(*) as contagem FROM focosAtributos WHERE 1 AND LAT >= -55.0 AND LAT <= 55.0 AND LON >= -120.0 AND LON <= 65.0 AND Data >= '2014-09-17 00:00:00' AND Data <= '2014-09-18 23:59:59' AND Pais = 'Brasil'   AND Estado = 'AM' group by Municipio order by contagem desc">
#<INPUT TYPE="hidden" NAME="sql" VALUE="SELECT Pais,Estado,Regiao,Municipio,count(*) as contagem FROM focosAtributos WHERE 1 AND LAT >= -55.0 AND LAT <= 55.0 AND LON >= -120.0 AND LON <= 65.0 AND Data >= '2014-09-17 00:00:00' AND Data <= '2014-09-18 23:59:59' AND Pais = 'Brasil'   AND Estado = 'AP' group by Municipio order by contagem desc">

#<INPUT TYPE="hidden" NAME="gby" VALUE="Municipio">
estados=['AC','AM','AP','MA','MT','PA','RO','RR','TO']
#url_1
url_2 = 'http://www.dpi.inpe.br/proarco/bdqueimadas/tabela.php'
now = datetime.datetime.now()
print now
now = now - datetime.timedelta(days=1)
dia=now.strftime("%Y-%m-%d")
for estado in estados:
    print estado
    values = dict(
      #sql='SELECT Pais,Estado,Regiao,Municipio,count(*) as contagem FROM focosAtributos WHERE 1 AND LAT >= -55.0 AND LAT <= 55.0 AND LON >= -120.0 AND LON <= 65.0 AND Data >= \''+now.strftime("%Y-%m-%d")+' 00:00:00\' AND Data <= \''+now.strftime("%Y-%m-%d")+' 23:59:59\' AND Pais = \'Brasil\'   AND Estado = \''+estado+'\' group by Municipio order by contagem desc',
      output="shp",
      sql="select * from focosAtributos WHERE 1 AND LAT >= -55.0 AND LAT <= 55.0 AND LON >= -120.0 AND LON <= 65.0 AND Data >= '"+dia+" 00:00:00' AND Data <= '"+dia+" 23:59:59' AND Estado = '"+estado+"' AND Pais = 'Brasil'  ",
      IDATE=dia,
      FDATE=dia,
      SATELITE="NOAA-15,NOAA-15D,NOAA-12,NOAA-12D,NOAA-14,NOAA-1I6,NOAA-16N,NOAA-17,NOAA-18D,NOAA-18,NOAA-19D,NOAA-19,GOES-08,GOES-10,GOES-12,GOES-13,AQUA-T,AQUA-M,TERRA-T,TERRA-M,METEOSAT-02,AQUA_M-M,AQUA_M-T,TERRA_M-M,TERRA_M-T,AQUA-MEX,TERRA-MEX,ATSR,TRMM,NPP",
      UF=estado,
      PAIS="Brasil"
      )
    data = urllib.urlencode(values)
    req = urllib2.Request(url_2, data)
    rsp = urllib2.urlopen(req)
    content = rsp.read()
    #print content
    
    if not "Nao encontrei focos para gerar a tabela/arquivo..." in content:
      download(content)
    else:
      print "Sem Focos"
    
# print result
#import re
#pat = re.compile('Title:.*')
#print pat.search(content).group()
