import random, os, requests, hashlib
from time import *

def download(nbdownload):
    for i in range(nbdownload):
        if not os.path.exists(os.getcwd()+"/pictures/"):
            os.makedirs(os.getcwd()+"/pictures/")
            os.chmod(os.getcwd()+"/pictures/", 0o0777)
        url = 'https://thispersondoesnotexist.com/image'
        pp = requests.get(url, headers={'User-Agent': 'My User Agent 1.0'}).content
        sleep(2)
        file = hashlib.sha256(pp).hexdigest() + ".jpeg"
        print(file)
        with open(os.getcwd()+"/pictures/"+file, "wb") as f:
            f.write(pp)

download(20) #choose a number to generate fake pp images with ai