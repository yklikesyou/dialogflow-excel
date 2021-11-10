### dialogflow 활용하기 basic :+1:
intents 작성 후, 그에 따른 더 많은 intents를 추가하기  
>1. Intents page에서 `Add follow-up intent`  
>2. custom형태 = 자유롭게 만들 수 있는 형태로 생성하기 (이렇게 하면 연계된 intent 생성이 됨)  

entity 추가하기
>1. intent에서 단어를 드래그 하면 바로 뜸
>2. 해당 단어를 나타내는 entity로 같은 항목의 단어들을 묶을 수 있음 (ex. CourseName)
>* 같은 항목의 단어들을 같은 entity로 묶어주기 (ex.CourseName으로 python jsp등 묶기)

response에서 entity 활용하기
>1. 사용자가 입력한 entity를 response에서 집어내려면, `$CourseName` 이런식으로 entity앞에 `$`붙이기
(ex. 정말로 `$CourseName`을 신청하시겠습니까?)
>* 참고로, 자동적으로 잡는 entity가 있음 (ex. 네, 등) -> 안쓰겠다고 취소하면 됨

연계형 intent에서, 추가된 custom intent에서 상위 intent의 entity를 활용하기
>1. response에서, `#상위intent이름.entity이름` 으로 나타낼 수 있음. (ex. `#CourseReservation-custom-followup.CourseName` -> 참고로 # 만 쳐도 알아서 잘 뜸)
>* 이때, entity는 같이 공유하는 거지만, 상위 intent의 response로 받는 entity답변을 사용하는 걸 말하는 것임.

참고로, integrations에서 서버나 어플과 연동하기 쉬움.
<br><br><br>

### dialogflow에 대용량 엑셀파일(xlsx)을 한 번에 넣는 방법:+1:
0. 우선, 다음과 같은 형태의 엑셀파일에서 1 과 2는 서로다른 intent로 가정한다.

A | B | C | D
---------- | ----------- | ----------- | ----------- 
Family |1 | How many people are there in your family? | There are 5 people.
Family |2 | Does your family live in a house or apt? | We live in a apt. 

1. 현재의 agent에서 `설정` -> `Export and Import` -> `Export as zip`으로 내보내기를 한다. 
2. import 하려는 엑셀파일이름(sample.xlsx)을 `GetExcel_Info.py`에 넣고 돌린다 -> (질문: , 답변: )의 형식으로 값이 나올 것. 
3. `Export as zip`에서 받은 원본파일의 `intents`의 json들을 다 지우고, 2를 통해 얻게된 json파일들로 채우기
4. 마지막으로, 해당파일을 다시 압축해서 `Import from zip`을 통해 업로드 하면, 새로운 intents들이 추가가 된다. 
5. 만약, import 할 때에 에러가 난다면, 원본 파일의 json의 내용들과 비교해본다.
 >예를 들면, 에러가 나서 원본파일과 다른 부분을 보충했더니 잘 import가 됐다. 
 >`Family1.json`은 parameter값만 원본 json, 
 >`Family1_usersays`는 count부터 그 아래 전부 원본 json의 값으로 변경함.

:clap: 참고: [관련강의](https://www.youtube.com/watch?v=v7iclS28Urc&list=PLRx0vPvlEmdCb33sBZGXzVOMY_seqnWJT&index=5)
