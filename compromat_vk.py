import vk_api
from time import sleep
import random
from vk_api.longpoll import VkLongPoll, VkEventType
 
msgsave = ' ' 
uid = ' '
lang = ' '
authSim = ' '
authToken = ' '
vkID = ' '

#text format
nL = "\n"
pW = ">>> "
lQ = "["
rQ = "]"
lU = "{"
rU = "}"
aid = "ID: "


#text format end

#select the language
def langSelect():
    if lang == '0':
        print('Paste your VK-token:')
    elif lang == '1':
        print('Вставь свой VK-токен:')
    elif lang == '2':
        print('Wstaw swój VK-token:')
    else:
        print('Unknown value. Script shutdowned by:' + nL)
        print('3')
        sleep(1)
        print('2')
        sleep(1)
        print('1')
        sleep(1)
        exit()
#select the language end
        
#ask about language
def askedLang():
    print('Your language: 0' + nL + 'Твой язык: 1' + nL + 'Twoj jezyk: 2' + nL)
#ask about language end

def authorizedEN():
        print(nL + "Signed in profile ID:" + nL)
        print(lQ + str(vkID[0]['id']) + rQ)
        
def authorizedRU():
        print(nL + "Вы вошли под ID:" + nL)
        print(lQ + str(vkID[0]['id']) + rQ)
        
def authorizedPL():
        print(nL + "Identyfikator z profilu:" + nL)
        print(lQ + str(vkID[0]['id']) + rQ)
        
askedLang()
lang = input(pW)
langSelect()
authSim = input(pW)

auth = vk_api.VkApi(token=authSim)
longpoll = VkLongPoll(auth)
vkID = auth.method("users.get", {"text": "id"})

if lang == "0":
    authorizedEN()
elif lang == "1":
    authorizedRU()
else:
    authorizedPL()
    

#compromat function
def saveTodata():
    messages = auth.method('messages.getConversations', {"offset": 0, "count": 1, "filter": "all"})

    msgcount = messages['count']
    if messages['count'] >= 1:
        uid = messages['items'][0]['conversation']['peer']['id']
        msgsave = messages['items'][0]['last_message']['text']
    with open('data/database.dat', 'a+') as database:
        uid = database.write(nL + aid + lQ + str(uid) + rQ)
        msgsave = database.write(nL + lU +  str(msgsave) + rU)
        database.close()
#compromat function end

def msgLog():
    global lang
    if lang == '0':
        print('Got new data, gonna check it')
    elif lang == '1':
        print('Получены новые данные, проверь их')
    elif lang == '2':
        print('Otrzymano nowe dane, sprawdz to')

for event in longpoll.listen():
    
    if event.type == VkEventType.MESSAGE_NEW:
     
       if event.to_me:
          message = event.text.lower()
          id = event.user_id
    
          saveTodata()
          msgLog()