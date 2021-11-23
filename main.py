from pathlib import Path

in_file_path = Path.cwd / "webserver-june-2011.txt"
with in_file_path.open as my_file:
  for line in my_file.readlines():
    if "bobsmart.html" in line:
      location = line.find("domain1335920")+14
      ip_addr = line[location.location+15].split(" ")[0]
      print(f"{line[0:20]} {ip_addr}")
      
