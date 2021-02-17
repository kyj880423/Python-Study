import sys
import urllib.request as req

strUrl = "https://files2.filesaveservice.club/redirect.php?path\u003d%2ffiles%2f2%2f20001~24000%2fid_21399.mp4"

data = req.urlopen(strUrl).readline()
print(data)