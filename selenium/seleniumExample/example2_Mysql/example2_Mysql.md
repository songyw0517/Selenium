# example2_Mysql
데이터 수집을 위한 셀레니움 템플릿 만들기 (과정1)

# How?
- 셀레니움을 이용한 크롤러로 데이터를 수집한다.
- 수집한 데이터를 json 파일로 생성한다.
- 생성한 json파일을 mysql에 저장한다.


# 프로젝트 구조
```sh
├─src
│  │
│  ├─crawler
│  │      __init__.py
│  │      spotCrawler.py
│  ├─data
│  │      error.json
│  │      spot.json
│  ├─DB
│  │      __init__.py
│  │      spotModel.py
│  └─refData
│          ref.txt
```

# 역할
## Crawler 디렉토리
- \_\_init\_\_.py : 크롤러에서 상속받을 공통적인 역할
    - 드라이버에 사용할 옵션 초기화
    - 기다리는 시간(waitTime) 초기화
    - 드라이버 반환
- spotCrawler : spot 데이터를 수집하기 위한 크롤러
    - \_\_init\_\_의 드라이버를 이용하여 데이터 수집 및 모델에 저장 및 반환
    - save를 이용하여 json 파일로 생성
## data 디렉토리
- 수집된 데이터를 모아놓은 디렉토리

## DB 디렉토리
- \_\_init\_\_.py : db에 대한 정보 저장 및 모델에서 상속받을 공통적인 역할
    - mysql 연결을 위한 정보(host, port, user 등) 저장
    - mysql 연결 객체(\_\_db) 저장
    - mysql 커서(\_\_curosr) 저장
    - 커서, 연결객체 반환 메소드
- spotModel : Mysql을 상속받아, 데이터베이스에 접근하는 모델
    - insert_model을 이용하여 document의 값을 삽입
    - sql 파일의 쿼리문 수행

# 아쉬운 점
- DTO를 이용하여 데이터베이스에 데이터를 넣을 수 있으면 좋겠다.
- sql 파일을 실행하는 것은 db 공통적인 부분이므로, \_\_init\_\_에 추가하자
- Mysql연결하는 부분에서 개인정보(host, user, password 등)을 config 처리해야한다.