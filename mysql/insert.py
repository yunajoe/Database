import pymysql
import pandas as pd
import numpy as np 


conn = pymysql.connect(host="localhost", port=3306, user="root", password='1234',
                       database="practice", charset="utf8")

curs = conn.cursor()
sql = "INSERT INTO music (singer,title,country,gender) VALUES (%s, %s, %s, %s)"

singers = {"아이유":"자장가","지코":"아무노래","블랙핑크":"마지막처럼","소녀시대":"소녀시대"}

lis = []
for k, v in singers.items():
    temp = [k,v]
    lis.append(temp)
try:
    with curs:        
        for i in range(len(lis)):
            s = lis[i][0]
            t = lis[i][1]
            curs.execute(sql, (f"{s}",f"{t}","IT","yuna"))
            conn.commit()
            
finally:
    conn.close()
        
        
    
            

    

    