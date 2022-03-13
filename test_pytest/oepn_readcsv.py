import csv
def read_csv():
    readcsv=list()
    with open('login.csv','r',encoding='utf-8') as f:
        login=csv.reader(f)
        next(login)
        for line in login:
            # print(line)
            readcsv.append(line)
        print(readcsv)
        return readcsv
if __name__=='__main__':
    read_csv()