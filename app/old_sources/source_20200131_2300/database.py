# -*- coding:utf-8 -*-
import cx_Oracle
from crawler import files
import os

#files = ['E:/python/python_project/DataCollect/app/files/yrt.xlsx']
def insertData():
   # print('daum')
    #print(files[1])


    con     =   cx_Oracle.connect('workout/workout@127.0.0.1/orcl')
    cur     =   con.cursor()

    print('for1')

    for i,v in enumerate(files):
        print(v)
        f = open(v, mode='r',encoding='utf-8')
        datas = f.readlines()

        f.close()

        print('for2')
        for i, v in enumerate(datas):
            if( i !=0):
                list = v.replace('\n','').split('\t')
                print(list)

                target =str(list[0])
                dt = str(list[1])
                time = str(list[2])
                rank = int(list[3])
                keyword = list[4].encode('euc-kr','ignore').decode('euc-kr')
                url = list[5]

                sql_insert = 'INSERT INTO WORKOUT.EXER_DAUM(TARGET,DT,TIME,RANK,KEYWORD,KEYWORD_URL) ' \
                             'VALUES(:TARGET, :DT, :TIME, :RANK, :KEYWORD, :URL)'

                print(sql_insert)

                cur.execute(sql_insert, (target, dt, time, rank, keyword,url))
        con.commit()
        print('end')

insertData()