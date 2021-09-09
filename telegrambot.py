import requests
# while True:
#     msg=input('Enter message to send \n')
#     # if msg="exit":
#     #     quit()
#     def sendmsg(msg):
#         url="https://api.telegram.org/bot1950380275:AAGCocBrvpBK_aXbr7uSOnp52N3sy4G1a3c/sendMessage?chat_id=890212626&text={}".format(msg)
#         requests.get(url)

#     sendmsg(msg)
    


for  i in range(0,150):
    msg="FuckOff"
    url="https://api.telegram.org/bot1950380275:AAGCocBrvpBK_aXbr7uSOnp52N3sy4G1a3c/sendMessage?chat_id=1314777821&text={}".format(msg)
    
    requests.get(url)
    if i >=50 :
        msg="dengey ra pilla pikachu"
    elif i>= 50 and i<101:
        msg="Moddaguduvu ra puka "
    else:
        msg="from dr490n1s3d_3d8"
    print(i)
