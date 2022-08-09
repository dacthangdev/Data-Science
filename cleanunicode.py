file = open("unicode.txt",'r',encoding="utf8")
datas = file.read().split("\n")
for data in datas:
    for i in range(len(data)):
        points = []
        for j in range(len(data[i])):
            if data[i][j] == "U":
                begin = j
            if data[i][j] == " ":
                end = j
                points.append(data[i][begin:end])

        for point in points:
            print(str(point))


file = open("unicoder.txt","w",encoding="utf8")
for i in range(len(data)):
    file.write(str(data[i])+"\n")
    

