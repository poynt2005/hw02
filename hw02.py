from hw01 import seating
#繼續使用第一次作業中的座位表來並用一行程式來處理下面問題
class seating2(seating):
    def __init__(self , filename):
        super().__init__(filename)
        
    def get_row_members(self , index):
        return [i[index] for i in self.seat]
        
    def delete_column(self , index):
        for i in self.seat : del(i[index])

    def add_lastname(self,lastname , index):
        return  [i[index] + ' ' + lastname for i in self.seat]
            
        
def main():
    a = seating2('input.txt')
    #(a) 取得每一列的第四個成員，依列序放在表列(list)。
    print('每一列的第四個成員 : ' , a.get_row_members(4-1))
    #(b) 刪除第一排，印出剩下的座位表。
    a.delete_column(0)
    print('刪除第一排後 : '  ,  '\n'.join([str(i) for i in a]),sep='\n')
    #(c) 利用 b 的結果。假設最後一排的人，都姓 Smith。請把他們姓加上去，並且把這一排的名字取出，依次放在新表列中。

    print('姓加上去後 : ' , a.add_lastname('Smith' , -1))
    a.search_seat(1 , 2)

if __name__ == '__main__':
    main()
