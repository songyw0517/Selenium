# example2_Mysql_refactoring
데이터 수집을 위한 셀레니움 템플릿 만들기(과정2)

# 과정1에서 아쉬웠던 점
- DTO를 이용하여 데이터베이스에 데이터를 넣을 수 있으면 좋겠다.
- sql 파일을 실행하는 것은 db 공통적인 부분이므로, \_\_init\_\_.py에 추가하자

## DTO(Data Transfer Object) 만들기
- 이 클래스는 crawler, database에서 사용되므로 DTO 디렉토리를 만들어 관리할 수 있도록 했습니다.
- DTO 디렉토리의 \_\_init\_\_.py에는 DTO가 가져야할 필수 요소들을 갖춘 baseDTO 클래스가 있습니다.
- 이 프로젝트에서는 spotDTO하나만 있기에, \_\_init\_\_.py 파일에 spotDTO 클래스를 같이 두었습니다. (여러개의 DTO를 사용할 경우) 파일을 만들어 관리하기

## sql 파일을 실행하는 기능은 db 공통적인 부분이므로, \_\_init\_\_.py에 추가하자
```python
class Mysql:

    ...

    #############################
    # path에 있는 sql 파일 실행 #
    #############################
    def exeSqlFile(self, path:str):
        with open(self.BASE_DIR+path, 'r', encoding='UTF-8-sig') as f:
            # 쿼리문 나누기 및 반복
            for query in f.read().split(';'):
                try:
                    if query.strip() != '':
                        self.getCursor().execute(query)
                except Exception as msg:
                    print("Query Except : ", msg)
```
- 이로써 Mysql을 상속받는 모든 클래스에서 sql파일을 실행할 수 있게 되었습니다.

## 그 외 달라진 부분
1. DTO를 import하기 위한 부분이 추가되었습니다.
    ```python
    # DTO 추가를 위한 경로 지정
    path = os.path.abspath(os.path.dirname(__file__))+'/..'
    import sys
    sys.path.append(path)
    from DTO import *
    ```
2. 크롤러에서 model에 추가하는 부분이 달라졌습니다.
    ```python
    # spotCrawler.py
    model.append(spotDTO(spotName, address)) # 객체 생성후 모델에 추가
    ```
3. DTO를 json으로 바꾸기 위해 save메소드 부분이 달라졌습니다.
    ```python
    'items':list(map(lambda x:x.__dict__, self.collector('https://map.kakao.com/')))
    ```