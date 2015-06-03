#!/bin/bash
# -q quiet
# -c nb of ping to perform
ping -q -c5 192.168.0.22>/dev/null

if [ $? -eq 0 ]; then
	#echo "ok"
	# echo "Enviado em $(date)"|mail -s "Normal:Server On" aparanhoss@gmail.com
	echo "$(date +%Y-%m-%d:%H:%M:%S) normal">>/var/log/srv_status.log
else
	#echo "out"
	echo "Enviado em $(date)"|mail -s "Alert:Server Off" aparanhoss@gmail.com
	echo "$(date +%Y-%m-%d:%H:%M:%S) falha">>/var/log/srv_status.log
fi
