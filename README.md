# hw02
## 1. 繼續使用第一次作業中的座位表來並用一行程式來處理下面問題：
>### *The class "seating2" in hw02.py is inheritance from hw01.py "seating" and data is stored in "input.txt" <br>Get seating by calling super class' constructor*
>### (a) 取得每一列的第四個成員，依列序放在表列(list)。

>>*method "get_row_members(self , index)" return the specific element from every row*

>### (b) 刪除第一排，印出剩下的座位表。

>>*method "delete_column(self , index)" delete specific column from self instance*

>### (c) 利用 b 的結果。假設最後一排的人，都姓 Smith。請把他們姓加上去，並且把這一排的名字取出，依次放在新表列中。

>>*method "add_lastname_column(self, lastname , index)" can add the lastname to the specific column*


## 2.把下面字串中的字和其詞類配對，建立一個字典，並回答以下問題
>### *hw02-1.py*
>### *John is a smart student. Mary is a beautiful girl.*

>> *match function return a  dictionary "{word : part of speech}"*

>### (a) 依單字的字母順序，把單字及其詞類的配對印在螢幕上。

>> *sort by lowercase*

>### (b) 找出所有單字中包含 s 這個字母的字，並將其與詞類配對印在螢幕上。

>> *print dictionary value if key contains "s" word*


## 3. 假設你有下列資訊：

| 員工編號 | 姓名 | 職位 | 單位 | 月薪 |
| ------ | ------ | ------ | ------ | ------ |
| A001 | 張無忌 | 教主 | 總壇 | 200,000 |
| A002 | 楊逍 | 光明左使 | 總壇 | 100,000 |
| A003 | 范遙 | 光明右使 | 總壇 | 100,000 |
| A004 | 謝遜 | 金毛獅王 | 護教法王 | 80,000 |
| A005 | 吳金 | 掌旗使 | 五行旗(銳金旗) | 50,000 |

>### *hw02-1.py*

>### (a) 將上面資料用最適當的結構儲存起來 請將姓與名分開儲存。

>> *I used list to store the data , every element is string type except name <br> I used dictionary to store firstname and lastname <br> The form is in "input2.txt"*

>### (b) 假設又招入兩個新手：常遇春、朱元璋，分別被編為 A578、A579，職位是教徒，單位是巨木堂，月薪是 22,000。請將這些資訊加入你的結構中

>> *function insert_data(data , input_str , flag) <br> When flag is set to false , input_str is the title of the form ; and input_str separated by space<br> Ex : A578 常遇春 教徒 巨木堂 22,000*

>### (c) 因為謝遜是教主的義父，常、朱兩人是教主的恩人，三人分別加薪 50%。請用程式執行此項工作。

>> *function pay_raise(input_name , raise_number , data) search by the lastname and update the salary*

>### (d) 找出單位為總壇的成員，將其姓名、職位印在螢幕上。

>> *function search(input_name , data) print name and position by searching the unit*






