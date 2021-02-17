f = open('C:\\Users\\calla\\OneDrive\\바탕 화면\\number.txt', 'wt')
i = 0
for i in range(1, 11):
    data = str(i) + '\n'
    f.write(data)
f.close()
