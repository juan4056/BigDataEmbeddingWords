with open("./mycsv.csv") as file:
    line = file.readline()
    line = file.readline()
    arr = line[2:]
    arr=arr.replace("\"","")
    arr=arr.replace("[","")
    arr=arr.replace("]","")
    arr=arr.split(",")
    print(len(arr))
