import csv


file = open('raw_data.txt',"r")

with open("clean_data.csv","w",encoding="utf8") as file_csv:
    header = ["sbd","tên","toán","ngữ văn", "khxh", "khtn","lịch sử", "địa lí","gdcd", "sinh học", "vật lí","hóa học","tiếng anh"]
    writer = csv.writer(file_csv)
    writer.writerow(header)
datas = file.read().split("\n")
file = open("test.txt",'w',encoding="utf8")

sbd = 2000000
for data in datas:
    sbd += 1
    if sbd in [2000317,2000880,2000961,2001045,2001095,2001223,2001626,2001634,2001692,2001839,2002380,2002515,2002957,2003635,2004616,2004675,2004925,2005197,2005404,2005456,2006022,2006589,2006713,2007352,2008489,2008696,2009061,2010084,2010183,2010694,2011601,2011978,2014405,2014615,2014990,2015139,2015442,2015533,2016083,2016109,2016316,2016494,2016638,2016654,2016684,2016697,2017268,2018222,2018467,2019713,2020945,2021437,2021672,2023238,2023484,2023915,2023982,2024137,2024158,2024160,2025247,2025419,2025795,2025898,2025979,2027868,2029286,2030377,2030997,2030998,2031078,2031344,2032645,2033286,2033685,2033860,2034025,2035561,2035974,2036301,2038385,2038506,2038507,2038569,2038685,2039064,2039980,2041154,2041659,2041803,2042010,2043735,2044177,2044298,2044418,2044421,2044445,2045401,2045600,2045763,2046190,2046681,2046856,2047002,2047052,2047150,2047174,2047183,2047210,2047211,2047221,2047241,2047627,2047658,2048136,2048150]:
        continue
    sbd_str = "0"+ str(sbd)
    # make data becom a list
    data = data.split("\\n")



    # remove \r, \t
    for i in range(len(data)):
        data[i] = data[i].replace("\\r","")
        data[i] = data[i].replace("\\t","")
    
    # remove tags
    for i in range(len(data)):
        tags = []
        for j in range(len(data[i])):
            if data[i][j] == "<":
                begin = j
            if data[i][j] == ">":
                end = j
                tags.append(data[i][begin:end+1])
        for tag in tags:
            data[i] = data[i].replace(str(tag),"")
    # remove leading whitespace
    for i in range(len(data)):
        data[i] = data[i].strip()

    # remove empty line
    unempty_lines = []
    for i in range(len(data)):
        if data[i] != "":
            unempty_lines.append(data[i])
    data = unempty_lines

    # choose relevant information
    name = data[6]
    scores = data[7]


    # load unicode table 
    chars = []
    codes = []

    file = open('unicode.txt','r',encoding="utf8")
    unicode_table = file.read().split('\n')

    for code in unicode_table:
        x = code.split(" ")
        chars.append(x[0])
        codes.append(x[1])

    # replace special character in name and score
    for i in range(len(chars)):
        name = name.replace(codes[i], chars[i])
        scores = scores.replace(codes[i], chars[i])

    for i in range(len(name)):
        if name[i:i+2] == "&#":
            name = name[:i] + chr(int(name[i+2:i+5])) + name[i+6:]
    for i in range(len(scores)):
        if scores[i:i+2] == "&#":
            scores = scores[:i] + chr(int(scores[i+2:i+5])) + scores[i+6:]        

    # change to lower case
    name = name.lower()
    scores = scores.lower()

    # process scores
    # remove:
    scores = scores.replace(":","")

    scores = scores.replace("khxh ","khxh   ")
    scores = scores.replace("khtn ","khtn   ")


    scores_list = scores.split("   ")
    data  = [sbd_str,name.title()]
    # add score to data
    for subject in ["toán","ngữ văn", "khxh", "khtn","lịch sử", "địa lí","gdcd", "sinh học", "vật lí","hóa học","tiếng anh"]:
        if subject in scores_list:
            data.append(str(float(scores_list[scores_list.index(subject)+1])))
        else:
            data.append(str(-1))

    #write data to csv file
    with open("clean_data.csv","a", encoding= "utf8",newline='') as file_csv:
        writer = csv.writer(file_csv)
        writer.writerow(data)
    

