# 도움이 된 자료
## 1. sql파일의 내용을 모두 실행시키는 방법
- https://github.com/awesome5team/General-Resources-Box/issues/7
```
import mysql.connector
cnx = mysql.connector.connect(user='root',
                             password='YOUR-PASSWORD-FOR-MYSQL',
                             host='localhost',
                             database='YOUR-DATABASE-NAME')
cursor =cnx.cursor()

def executeScriptsFromFile(filename):
    # 파일 읽기
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()

    # sql 명령어 나누기
    sqlCommands = sqlFile.split(';')

    # 나눠진 명령어 하나씩 실행시키기
    for command in sqlCommands:
        try:
            if command.strip() != '':
                cursor.execute(command)
        except IOError, msg:
            print "Command skipped: ", msg

executeScriptsFromFile('SQL-FILE-LOCATION')
cnx.commit()

``` 