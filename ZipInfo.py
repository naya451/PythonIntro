import sys
import zipfile
import io


s = sys.stdin.readline()
data = "".join(s.split())
s = sys.stdin.readline()
while s:
    s = "".join(s.split())
    data += s
    s = sys.stdin.readline()
data = int(data, 16).to_bytes(len(data), byteorder='big')
f = io.BytesIO(data)

zip_file = zipfile.ZipFile(f)

file_list = zip_file.namelist()
info_list = zip_file.infolist()

file_count = 0

for i in info_list:
    if not i.is_dir():
        file_count+=1
total_size = sum(zip_file.getinfo(name).file_size for name in file_list)

print(file_count, total_size)

