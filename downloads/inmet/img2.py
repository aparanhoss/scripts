from PIL import Image
import subprocess
import time
horas=[24,27,30,33,36,39,42,45,48,51,54,57,60,63,66,69,72]
while(1):
	for k in horas:
		nome='img/%d.png'%k
		p = subprocess.Popen(["display", nome])
		time.sleep(1)
		#raw_input("Give a name for image:")
		p.kill()
	
