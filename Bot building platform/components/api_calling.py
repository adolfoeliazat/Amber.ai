import requests
from meya import Component
from meya.cards import Card, Button



class apicalling(Component):

    def start(self):
        
        checkin = self.db.flow.get("checkin-date") 
        checkout = self.db.flow.get("checkout-date") 
        city = self.db.flow.get("CITY1")


        url = "PASTE THE URLs OF YOUR TRAVEL APIs"
        payload = "{\n \"destination_code\": \""+city+"\",\n \"checkin\": \""+checkin+"\",\n \"checkout\": \""+checkout+"\",\n \"client_nationality\": \"IN\",\n \"response\": \"fast\",\n \"currency\": \"INR\",\n \"rates\": \"comprehensive\",\n \"hotel_category\": [2, 6],\n \"rooms\": [\n {\n \"adults\": 1\n },\n {\n \"adults\": 2,\n \"children_ages\": [3]\n }\n ]\n}"
        headers = {
            'api-key': "PASTE YOUR KEY HERE",
            'content-type': "application/json",
            'accept': "application/json",
            'cache-control': "no-cache",
            'postman-token': "2c0f1442-19fc-2cc3-8bfd-efcb806d23a7"
            }
        response = requests.request("POST", url, data=payload, headers=headers)

        url1= response.json()['hotels'][0]['images']['main_image']
        image_url1= 'https://cdn.grnconnect.com/' + url1
        title1 =response.json()['hotels'][0]['name']
        text1 =  response.json()['hotels'][0]['rates'][0]['price']
        text1=str(text1)
        text1='₹' + text1
        
        
        url2= response.json()['hotels'][1]['images']['main_image']
        image_url2= 'https://cdn.grnconnect.com/' + url2
        title2 =response.json()['hotels'][1]['name']
        text2 =  response.json()['hotels'][1]['rates'][0]['price']
        text2=str(text2)
        text2='INR ' + text2
        
        url3= response.json()['hotels'][2]['images']['main_image']
        image_url3= 'https://cdn.grnconnect.com/' + url3
        title3 =response.json()['hotels'][2]['name']
        text3 =  response.json()['hotels'][2]['rates'][0]['price']
        text3=str(text3)
        text3='INR ' + text3
        
        
        
        url4= response.json()['hotels'][3]['images']['main_image']
        image_url4= 'https://cdn.grnconnect.com/' + url4
        title4 =response.json()['hotels'][3]['name']
        text4 =  response.json()['hotels'][3]['rates'][0]['price']
        text4=str(text4)
        text4='INR ' + text4
        
        
        
        
        
        buttons = [
            Button(text='View details'),
            ]
            
        
        buttons_last = [
            Button(text='View details'),
            Button(text='Load more')
            ]
            
        card1 = Card(title=title1,
        text=text1,
        image_url=image_url1,
        buttons=buttons)
        message1 = self.create_message(card=card1)
        
        card2 = Card(title=title2,
        text=text2,
        image_url=image_url2,
        buttons=buttons)
        message2 = self.create_message(card=card2)
        
        
        card3 = Card(title=title3,
        text=text3,
        image_url=image_url3,
        buttons=buttons)
        message3 = self.create_message(card=card3)
        
        
        card4 = Card(title=title4,
        text=text4,
        image_url=image_url4,
        buttons=buttons_last)
        message4 = self.create_message(card=card4)
        
        

        # respond with the message and "next" action
        return self.respond(messages=[message1,message2,message3,message4], action="next")
