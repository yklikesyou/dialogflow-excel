### dialogflow에 대용량 엑셀파일(xlsx)을 한 번에 넣는 방법:+1:
0. 우선, 다음과 같은 형태의 엑셀파일에서 1 과 2는 서로다른 intent로 가정한다.

A | B | C | D
---------- | ----------- | ----------- | ----------- 
Family |1 | How many people are there in your family? | There are 5 people.
Family |2 | Does your family live in a house or apt? | We live in a apt. 

1. 현재의 agent에서 `설정` -> `Export and Import` -> `Export as zip`으로 내보내기를 한다. 
2. import 하려는 엑셀파일이름(sample.xlsx)을 `GetExcel_Info.py`에 넣고 돌린다 -> (질문: , 답변: )의 형식으로 값이 나올 것. 
3. `Export as zip`에서 받은 원본파일의 `intents`의 json들을 다 지우고 2를 통해 얻게된 json파일들로 채우기
4. 마지막으로, 해당파일을 다시 압축해서 `Import from zip`을 통해 업로드 하면, 새로운 intents들이 추가가 된다. 
5. 만약, import 할 때에 에러가 난다면, 원본 파일의 json형태와 비교해본다.
 >예를 들면, Family1_usersays는 count부터 그 아래 전부 원래 json에서값으로 변경했더니 됐음
