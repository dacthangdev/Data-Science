import subprocess

data = subprocess.check_output('curl -F "SoBaoDanh=02000001" diemthi.hcm.edu.vn/Home/Show')
file = open("data.txt","w")

file.write(str(data))