# 셀레니움 템플릿

# 템플릿 설명
- crawler : 데이터 수집을 맡는 부분, 수집한 데이터를 data/[파일 이름].json 으로 저장합니다.
- data : 수집한 데이터를 보관합니다.
- database : data/[파일 이름].json 데이터를 데이터베이스에 저장 및 관리합니다.
- DTO : 데이터 형식을 관리합니다.

# 순서
1. Crawler을 실행시켜 원하는 데이터를 수집합니다.
2. database 모델을 이용하여 수집한 데이터를 데이터 베이스에 저장합니다.

# 바뀐부분
## 크롤러
- json파일을 만들 때, w+ 모드를 사용하여 파일이 없을 경우에 파일을 생성하도록 했습니다.
## DTO
- baseDTO와 사용할 DTO(spotDTO)로 나누었습니다.
- 객체를 생성할 때 datetime.now().strftime("%Y-%m-%dT%H:%M:%S")을 사용하여 시간을 저장할 수 있도록 했습니다.
- 데이터구조를 id/name/address/create_at/update_at/\_\_version\_\_으로 구성했습니다.
## database
- 데이터베이스에 접근할 모델(MongoDB, Mysql)을 나누었습니다.
    ### MongoDB
    - DTO의 baseDTO에서 시간(create_at, update_at)을 저장함으로써 MongoDB의 \_\_init\_\_에서 schemize부분을 주석처리했습니다. 필요하다면 baseDTO부분과 schemize를 수정하여 사용할 수 있습니다.
    ### Mysql
    - 데이터 구조에 맞추어 schema.sql파일을 수정했습니다.