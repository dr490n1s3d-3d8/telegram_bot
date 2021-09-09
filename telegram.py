import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser , InputPeerChannel
from telethon import TelegramClient,sync,events

api_id="7864301"
api_hash="2e87d70666b435a4c5c7466a0b02db58"
token="1950380275:AAGCocBrvpBK_aXbr7uSOnp52N3sy4G1a3c"
message=""

phone = "+917036713119"

client=TelegramClient('session',api_id,api_hash)
client.connect()

userDetails = {
    'naresh':[1314777821,7485496572124439954],
    'legend':[890212626,4748363324848580725],
    'sriram':[815263621,8801960034024802572],
    'ajay':[1271502498,-8956853554939345458]
}


if not client.is_user_authorized():
    
    client.send_code_request(phone)
    client.sign_in(phone,input('Enter the code for authorization'))

try:
    
   target=InputPeerUser(userDetails['sriram'][0],userDetails['sriram'][0])
#    client.send_message(target, message , parse_mode='html')

   #Getting the user id and hash details using below code 
#    print(client.get_entity(815263621))
#    print("\n")                                   
   print(client.get_entity(1271502498))

#Getting myself Details user_id and access_hash(user_hash)
#    me=client.get_me()
#    print(me)

except Exception as e :
    print(e)
    
client.disconnect()