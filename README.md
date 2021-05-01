# For Juan

## 다음주 월욜 저녁까지 각자 맡은 거 + 게임 조금 구현 or 리서치



## 0. 준비

#### 1. 역할

- 이다영: 프론트엔드. 조장 (ux flow)
- 이규정: 백엔드. 홍보 담당 (data miner - 조례 멘트(시간 포함), 밸런스 게임 질문 10개 이하, 교수님 주접멘트)
- 조혜인: 백엔드. 리드미 담당 (db, url)
- 한상길: 프론트엔드. 서기 (survey)

#### 2. 아이디어

- 카드 맞추기
- 사진에 맞는 이름 넣어야지 메시지 보이기
- 교수님이 누가 쓴건지 맞추기
- 산성비 타이핑
- 교수님 조례 멘트 보여주기  (1 조례를 코인처럼 투입해서 플레이 할 수 있는 게임?)
- 합친거(10개정도 카드 맞추면, 산성비로 넘어가는 형식)
- 이 퍼즐을 풀어서 귀하가 교수님이라는 것을 알 수 있게 해주십시오
- 타이밍 맞춰서 엔터빰
- 단계별 인물 공개(8명, 8명, 7명/ 총 3단계, 23명)
- 마지막에는 인스타처럼 3반 정보 간단하게(사진 + 이름 + 기타등등) + 롤페, 소장용
- 교수님께 벽이 느껴져요. 완벽 / 교수님 맨날 같은티만 입으시네요 프리티 / 교수님 김 묻었어요, 잘생김 / 교수님 좋아하는 사람 손 접으라 했는데 지구가 반으로 접혔어 / 

#### 3. 확정
- 일정 : 5/13 목요일
- 구성 : 3개의 미니 게임 -> 각 게임을 클리어하면 7~8개의 롤링페이퍼 메세지
- 교수님이 작성하셨던 조례가 교수님의 코인(게임에 필요한 재화)가 된다
- 게임1 : 반 친구들 사진 맞추는 카드 뒤집기
- 게임2 : 엔터 빰
- 게임3 : 존잘 juan
- 게임4 : 지각은 누구?
- 보상 : 게임 종료 후 반 사람들의 프로필, 롤페이퍼, 깃허브나
-  인스타그램 같은 SNS 링크가 있는 웹페이지

- Github 아이디 찾기 화면처럼 '이 퍼즐을 풀어서 귀하가 교수님이라는 것을 알 수 있게 해주십시오'
- 추가 개발 : 1학기 말까지 / 각자에게 롤링 페이퍼 남길 수 있게 추가 개발

##### * 결정할 사항
- 익명 vs 실명 vs 별명



## 1. 요구사항

#### 1. 프로젝트 구조

> game/은 game을 하는 디렉토리입니다.
>
> ssafy5_3/은 학생 정보, 메세지 등이 있는 디렉토리입니다.

```bash
$ django-admin startproject rollingpaper .
$ python manage.py startapp game
$ python manage.py startapp ssafy5_3
```



#### 2. Model

1. Student

   |     id      |     integer      |       id       |
   | :---------: | :--------------: | :------------: |
   |    name     |   varchar(10)    |   학생 이름    |
   |  nickname   |   varchar(20)    |      별명      |
   |  webex_img  | image_url (text) | 웹엑스 이미지  |
   | profile_img | image_url (text) | 프로필 이미지  |
   |    flag     |     boolean      | 게임 성공 여부 |
   |    song     |   varchar(50)    |   노래 제목    |
   |  song_url   |   varchar(100)   |   노래 링크    |

2. Professor

   |     id     |     integer      |          id          |
   | :--------: | :--------------: | :------------------: |
   |    name    |   varchar(10)    |     교수님 성함      |
   | webex_img  | image_url (text) | 웹엑스 이미지 (로켓) |
   |   coins    |     integer      | 쓸 수 있는 코인 개수 |
   | game_clear |     boolean      |    게임 성공 여부    |

3. Greeting

   > 1:N 구조
   
   |      id      | integer  |        pk        |
   | :----------: | :------: | :--------------: |
   | professor_id | integer  |  교수님 아이디   |
   |   content    |   Text   | 교수님 조례 멘트 |
   |  created_at  | DateTime |    올린 시간     |

4. Comment

   > M:N 구조

   |    id    | integer |     pk      |
   | :------: | :-----: | :---------: |
   | from_msg | integer | 보내는 사람 |
   |  to_msg  | integer |  받는 사람  |
   | content  |  Text   |  올린 시간  |



#### 3. URL

##### 1. ssafy5_3 app

| HTTP verb |  URL 패턴  |              설명               |
| :-------: | :--------: | :-----------------------------: |
|    GET    |     /      |           시작 페이지           |
|    GET    | messages/  | 롤링페이퍼 페이지 (실명 + 익명) |
|    GET    | collegues/ |        학생 정보 페이지         |
|    GET    | greetings/ |        교수님 조례 멘트         |

##### 2. game app

| HTTP verb | URL 패턴 |                  설명                  |
| :-------: | :------: | :------------------------------------: |
|   POST    | stage1/  |   Enter Baam!! 맞는 별명 채우기 게임   |
|   POST    | stage2/  |            카드 맞추기 게임            |
|   POST    | stage3/  |        지각한 사람 맞추기 게임         |
|   POST    |  bonus/  |  Youtube 스타일의 교수님 주접 페이지   |
|   POST    | rewards/ | 스테이지 클리어할 때마다 나오는 페이지 |





