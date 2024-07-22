import os
from glob import glob

def pre(r: int) -> None:
    os.makedirs("prepro", exist_ok=True)
    files = glob("data/*.txt")
    files = files * r
    with open("prepro/out.txt", 'w') as f:
        f.write('\n'.join(files))

if __name__=="__main__":
    pre(r=2)
