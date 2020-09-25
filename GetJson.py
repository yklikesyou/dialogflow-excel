# -*- coding: utf-8 -*-


# Family1.json은 parameter값만 변경함
# Family1_usersays는 count부터 그 아래 전부 원래 json에서값으로 변경했더니 됐음
# 파일로 출력하기

i = 1

# 출력, 입력 값 JSON 파일을 생성합니다.

prev = str(conversations[0].contentName) + str(conversations[0].contentType)

f = open(prev + '.json', 'w', encoding='UTF-8')

f.write('{ "id": "10d3155d-4468-4118-8f5d-15009af446d0", "name": "' + prev + '", "auto": true, "contexts": [], "responses": [ { "resetContexts": false, "affectedContexts": [], "parameters": [], "messages": [ { "type": 0, "lang": "ko", "speech": "' + conversations[0].answer + '" } ], "defaultResponsePlatforms": {}, "speech": [] } ], "priority": 500000, "webhookUsed": false, "webhookForSlotFilling": false, "fallbackIntent": false, "events": [] }')

f.close()

f = open(prev + '_usersays_ko.json', 'w', encoding='UTF-8')

f.write("[")

f.write('{ "id": "3330d5a3-f38e-48fd-a3e6-000000000001", "data": [ { "text": "' + conversations[0].question + '", "userDefined": false } ], "isTemplate": false, "count": 0 },')



while True:

    if i >= len(conversations):

        f.write("]")

        f.close()

        break;

    c = conversations[i]

    if prev == str(c.contentName) + str(c.contentType):

        f.write('{ "id": "3330d5a3-f38e-48fd-a3e6-000000000001", "data": [ { "text": "' + c.question + '", "userDefined": false } ], "isTemplate": false, "count": 0 },')

    else:

        f.write("]")

        f.close()

        # 출력, 입력 값 JSON 파일을 생성합니다.

        prev = str(c.contentName) + str(c.contentType)

        f = open(prev + '.json', 'w', encoding='UTF-8')

        f.write('{ "id": "10d3155d-4468-4118-8f5d-15009af446d0", "name": "' + prev + '", "auto": true, "contexts": [], "responses": [ { "resetContexts": false, "affectedContexts": [], "parameters": [], "messages": [ { "type": 0, "lang": "ko", "speech": "' + c.answer + '" } ], "defaultResponsePlatforms": {}, "speech": [] } ], "priority": 500000, "webhookUsed": false, "webhookForSlotFilling": false, "fallbackIntent": false, "events": [] }')

        f.close()

        f = open(prev + '_usersays_ko.json', 'w', encoding='UTF-8')

        f.write("[")

        f.write('{ "id": "3330d5a3-f38e-48fd-a3e6-000000000001", "data": [ { "text": "' + c.question + '", "userDefined": false } ], "isTemplate": false, "count": 0 },')

    i = i + 1
