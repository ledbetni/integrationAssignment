import requests
import json

def main():
    getItem = input("Enter the topic you would like to learn more about, enter exit to quit: ")
    while (getItem != ("exit" or "Exit")):
        if (getItem == ("exit" or "Exit")):
            break
        url = "http://localhost:1400"
        urlTrans = "http://localhost:4500/translate"
        urlDetect = "http://localhost:3000"
        itemDict = {'item': str(getItem)}
        postItem = requests.post(url,data=itemDict)
        postRes = postItem.json()
        resStr = str(postRes["item"])
        print(resStr)
        #print(type(postRes))
        print("-------------------------------------")
        #Caroline Microservice, Functional
        detectDict = {"text": resStr}
        postDetect = requests.post(urlDetect, data=detectDict)
        detectRes = postDetect.text
        print(detectRes)
        print("-------------------------------------")

        #Luis Microservice, not yet functional
        # getTrans = input("Would you like to translate this into Spanish? Enter 'Y' for yes or 'N' for no: ")
        # if (getTrans == ("Y" or "y")):
        #     postTrans = requests.post(urlTrans, json=resStr)
        #     transRes = json.loads(postTrans.text)
        #     transText = transRes['translated']
        #     print(str(transText))
            
        getItem = input("Enter the topic you would like to learn more about, enter exit to quit: ")
        #itemStr = postItem.text

main()
    