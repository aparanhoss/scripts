dir="img"
#dir="/var/www/animacao/img"
dia=$(date +'%Y%m%d')


url="http://www.inmet.gov.br/projetos/cga/capre/cosmo7/AS/prec24h/web_AS_prec24h_"$dia"0000_+"
ext=".png"
for i in 24 27 30 33 36 39 42 45 48 51 54 57 60 63 66 69 72;
do
	wget -O "$dir/$i$ext" "$url$i$ext";
	#echo "http://www.inmet.gov.br/projetos/cga/capre/cosmo7/AS/prec24h/web_AS_prec24h_201501110000_+"$i".png"
done
