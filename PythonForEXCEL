#대용량 엑셀파일 데이터를 dialogflow로
#python Code

import openpyxl

class Conversation:
  #질문, 응답 두 변수로 구성됩니다.
  def __init__(self, contentName, contentType, question, answer) :
    self.contentName = contentName
    self.contentType = contentType
    self.question = question
    self.answer = answer

  def __str__(self):
    return "질문: "+self.question + "\n답변: " + self.answer + '\n';
  
#엑셀파일 열기
wb = openpyxl.load_workbook('sample.xlsx')

ws = wb.active

conversations = []

#시트 내에 존재하는 모든 영어 데이터를 객체로 담기
for r in ws.rows:
  c = Conversation(r[0].value, r[1].value, r[2].value, r[3].value)
  conversations.append(c)

wb.close()

for c in conversations:
  print(str(c))
