import os.path

userInput = input()
if os.path.exists(userInput):
    f = open(userInput, 'rt')
    flag = f.exists()

    if flag :
        print(f.listFiles())
else:
    print('file not exists.')