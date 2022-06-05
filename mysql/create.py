
# 출처: https://www.fun-coding.org/mysql_basic6.html
import pymysql
import pandas as pd
import numpy as np 

conn = pymysql.connect(host="localhost", port=3306, user="root", password='1234',
                       database="practice", charset="utf8")


# cursor object 가져오기
curs = conn.cursor()      
    
try:
    with curs:             
        sql = ''' 
                create table music4 (
                id INT NOT NULL AUTO_INCREMENT,
                singer VARCHAR(20) NOT NULL,
                title VARCHAR(30) NOT NULL,
                country CHAR(20) NOT NULL,
                gender CHAR(10) NOT NULL,
                PRIMARY KEY(id)  
                );   
            '''       
        curs.execute(sql)      # sql문 실행
        conn.commit()       # mysql 서버에 확정  
except:
    print("해당테이블이 이미 있습니다")
finally:
    conn.close()


