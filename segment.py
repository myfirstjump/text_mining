# -*- coding: utf-8 -*-

import jieba
import logging
import time


def main():

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    filePath = "C:\\Users\\Java\\Desktop\\TM"
    # jieba custom setting.
    #jieba.set_dictionary('jieba_dict/dict.txt.big')

    jieba.load_userdict(filePath + "\\userDict\\dict.txt") # taiba字典
    jieba.load_userdict(filePath + "\\userDict\\hotel.txt")
    jieba.load_userdict(filePath + "\\userDict\\people.txt")
    jieba.load_userdict(filePath + "\\userDict\\stopwords.txt") # stopwords先當作字典讓 jieba 切出來，之後再排除
    jieba.load_userdict(filePath + "\\userDict\\京都市町名.txt")
    jieba.load_userdict(filePath + "\\userDict\\京都駅名.txt")

    jieba.load_userdict(filePath + "\\userDict\\tags\\TAGactivity.txt")
    jieba.load_userdict(filePath + "\\userDict\\tags\\TAGsite.txt")
    jieba.load_userdict(filePath + "\\userDict\\tags\\TAGrestaurant.txt")
    jieba.load_userdict(filePath + "\\userDict\\tags\\TAGshopping.txt")
    jieba.load_userdict(filePath + "\\userDict\\tags\\TAGwearing.txt")

    # load stopwords set
    stopwordset = set()
    with open(filePath + "\\userDict\\stopwords.txt",'r',encoding='utf-8') as sw:
        for line in sw:
            stopwordset.add(line.strip('\n'))

    texts_num = 0

    output = open(filePath + '\\word2Vec\\KyotoW2V\\segedv3.txt','w', encoding="utf-8")
    with open(filePath + '\\word2Vec\\KyotoW2V\\Titlize.txt','r', encoding="utf-8") as content :
        for line in content:
            line = line.strip('\n')
            words = jieba.cut(line, cut_all=False)
            for word in words:
                if word not in stopwordset:
                    output.write(word +' ')

            texts_num += 1
            if texts_num % 10000 == 0:
                logging.info("已完成前 %d 行的斷詞" % texts_num)
    output.close()

if __name__ == '__main__':
    main()
