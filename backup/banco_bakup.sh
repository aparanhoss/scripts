#scp root@192.168.0.22:/root/bkps/$(date +"%Y-%m-%d").sql /home/monitoramento/bkp_banco/
echo "================================================================================="
date
echo "================================================================================="
rsync -Cravzp root@192.168.0.22:/root/bkps /home/monitoramento/bkp_banco

