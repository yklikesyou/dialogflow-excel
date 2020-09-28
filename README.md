### dialogflow에 대용량 엑셀파일(xlsx)을 한 번에 넣는 방법:+1:
0. 우선, 다음과 같은 형태의 엑셀파일에서 1 과 2는 서로다른 intent로 가정한다.

A | B | C | D
---------- | ----------- | ----------- | ----------- 
Family |1 | How many people are there in your family? | There are 5 people.
Family |2 | Does your family live in a house or apt? | We live in a apt. 

1. 현재의 agent에서 설정 -> Export and Import -> Export as zip으로 내보내기를 한다. 
2. import 하려는 엑셀파일(xlsx)
