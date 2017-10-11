## ETL
Booking.com爬網

輸入爬取的條件，輸出飯店名稱，欲住宿日期、價錢、等等

可調整參數:
surveyRange = 爬幾天
travelPeriod = 每次間格幾日
adultNumber = 成人數量
roomNumber = 房間數
location = 目標地點 (ex.京都)

## DB備份
MongoDB檔案備份
用mongod啟動服務 -> 用mongo --dbpath 開啟資料

## 文本分析

1. TF-IDF generator
輸入目標文章群，輸出每篇文章特徵詞 keywords list & 不重複的keywords set 

可調整參數:
src = "Titlize_all" # mongoDB 讀取來源 collection
filePath = "C:\\Users\\Java\\Desktop\\TM" 自定字典位置(userDict資料夾位置)
focus = "allTags" # 欲加強權重的目標(檔案名稱)
multi = 100  # 加強目標的權重值
kwNum = 5 每天文章書出幾個關鍵詞

2. 分群 (清水寺Clustering)
輸入TF-IDF generator輸出的兩個檔案，做文章分群、PCA降維

3. 關聯分析 (Association_渡月橋)
輸入TF-IDF generator輸出的兩個檔案，做關聯分析
support和confidence可以自行設定

4. word2Vec (有一個tutorial，還有一個Kyoto的版本)
輸入所有語料庫資料，得到詞間的相似度  ex. 一蘭拉麵 金龍拉麵 cos-similarity = 0.7852
參考這篇 http://zake7749.github.io/2016/08/28/word2vec-with-gensim/
