#把下面字串中的字和其詞類配對，建立一個字典，並回答以下問題。
def match(input_str):
    input_str = input_str.replace('.' , '')
    tmp = input_str.split(' ')
    part_of_speech = ['noun' , 'verb' , 'article' , 'adjective' , 'noun' , 'noun' , 'verb' , 'article' , 'adjective' , 'noun']
    return {key : value for key,value in zip(tmp , part_of_speech)}

#詞類配對，建立一個字典 : John is a smart student. Mary is a beautiful girl.
d = match('John is a smart student. Mary is a beautiful girl')
print(u'詞類配對 : ' , d , sep = '\n')
print()

#(a) 依單字的字母順序，把單字及其詞類的配對印在螢幕上。

a = sorted(d.keys() , key = lambda x : x.lower())
print(u'依單字的字母順序，把單字及其詞類的配對印在螢幕上 :' , '\n'.join(['{{{} : {}}}'.format(key , d[key]) for key in a]) , sep = '\n')
print()

#(b) 找出所有單字中包含 s 這個字母的字，並將其與詞類配對印在螢幕上。
print(u'找出所有單字中包含 s 這個字母的字 : ' , ''.join(['{{{} : {}}}\n'.format(key,value) for key,value in d.items() if 's' in key ]) , sep = '\n')




#假設你有下列資訊:
#(a) 將上面資料用最適當的結構儲存起來。記得，你選擇的結構要讓下面的幾項工作很容易、不需用太複雜的方式就能達成。請將姓與名分開儲存。
def insert_data(data , input_str , flag):
    if flag == True:
        data_tmp = []

        tmp = input_str.split(' ')

        number = tmp[0]
        data_tmp.append(number)
            
        last_name = tmp[1][0]
        name = tmp[1][1 : len(tmp[1])]
        d = {last_name : name}
        data_tmp.append(d)
            
        position = tmp[2]
        data_tmp.append(position)
            
        unit = tmp[3]
        data_tmp.append(unit)
        
        salary = int(tmp[4].replace(',' , ''))
        data_tmp.append(salary)

        data.append(data_tmp)            

    else:
        data = [input_str.split(' ')]
        
    return data

def open_file(filename , data):
    try:
        with open(filename) as f:
            line = f.readline()
            
            insert_data(data , line.rstrip('\n') , False)
            while True:
                data_tmp = []
                line = f.readline()
                if not line:
                    break
                insert_data(data , line.rstrip('\n') , True)
            return data
    except FileNotFoundError:
        print('File Not Found')
              
data = []
data = open_file('input2.txt' , data)
print(u'結構' , '\n'.join([str(i) for i in data]) ,sep = '\n')
print()

#(b) 假設又招入兩個新手：常遇春、朱元璋，分別被編為 A578、A579，職位是教徒，單位是巨木堂，月薪是 22,000。請將這些資訊加入你的結構中。請不要手動將資料鍵入哦！

new_empolyee0 = u'A578 常遇春 教徒 巨木堂 22,000'
new_empolyee1 = u'A579 朱元璋 教徒 巨木堂 22,000'
data = insert_data(data , new_empolyee0 , True)
data = insert_data(data , new_empolyee1 , True)
print(u'加入後 :' , '\n'.join([str(i) for i in data]) , sep='\n')
print()

#(c) 因為謝遜是教主的義父，常、朱兩人是教主的恩人，三人分別加薪 50%。請用程式執行此項工作。
def pay_raise(input_name , raise_number , data):
    lastname = input_name[0]
    for i in range(0 , len(data) , 1):
        for j in range(0 , len(data[i]) , 1):
            if isinstance(data[i][j] , dict):
                if not data[i][j].get(lastname) == None:
                    data[i][-1] *= raise_number
                    return data


data = pay_raise('謝遜' , 1.5 , data)
data = pay_raise('朱' , 1.5 , data)
data = pay_raise('常' , 1.5 , data)
print(u'加薪後:','\n'.join([str(i) for i in data]) , sep = '\n')
print()

#(d) 找出單位為總壇的成員，將其姓名、職位印在螢幕上。
def search(input_name , data):
    for i in range(0 , len(data) , 1):
        for j in range(0 , len(data[i]) , 1):
            if data[i][j] == input_name:
                print(u'姓名 : ' , data[i][1])
                print(u'職位 : ' , data[i][2])
                print()
print('總壇的成員 :')
search('總壇' , data)
