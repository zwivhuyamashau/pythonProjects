"code that uses AWS SNS to send a lot of messages to her aunt on her birthday so that she leaves me alone"

import boto3
import time

class SendToAunt():
    def __init__(self,filename,number):
        self.client=client = boto3.client('sns')
        self.filename=filename
        self.number=number
    
    def openFileAndSend(self):
        file = open(self.filename, "r",encoding="utf8")
        listOfLines=file.readlines()
        
        for line in listOfLines:
            response = self.client.publish(PhoneNumber=self.number,Message=line)
            print(line)
            time.sleep(1)

messageObject=SendToAunt("sns.txt","+2779XXXXXXX")
messageObject.openFileAndSend()
