import json
import requests
import csv
class Post():
    def __init__(self,link):
        self.link = link
        
        
        self.get_a_post()

    def get_a_post(self):
        #getting the SP credentials
        with open("credentials.csv","r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                username = row['Username']
                password = row['Password']

        #this is just how an API call for SP is being performed usinng username+password as an auth method
        headers = {
            'Content-Type': 'application/json'
        }

        task_params = {
            'url': self.link,
            'target': 'instagram_post',
            'locale': 'en-gb',
            'geo': 'Italy'
        }
        
        response = requests.post(
            'https://scraper-api.smartproxy.com/v1/scrape',
            headers = headers,
            json = task_params,
            auth = (username, password)
        )


        post_json = json.loads(response.text)
        #number of likes
        self.likes = post_json["data"]["content"]["likes"].replace(",","")

        #date and time of creation
        self.created_date = post_json["data"]["content"]["createdAt"]
        try:
            self.date = self.created_date.split("T")[0]
            self.time = self.created_date.split("T")[1][:-5]
        except:
            self.date = "Not provided"
            self.time = "Not provided"

        self.comments = post_json["data"]["content"]["commentCount"]
        self.username = post_json["data"]["content"]["username"]
        #visual of the post
        self.image = post_json["data"]["content"]['image']
        
        self.hashtags = post_json["data"]["content"]["hashtags"]
        #list of images in the post
        self.imgs = post_json["data"]["content"]["images"]
        #list of videos in the post
        self.videos = post_json["data"]["content"]["videos"]

        #checking for which type of the visual the post employs 
        
#sometimes mistakengly assigns "No Visual" - check why
        if len(self.imgs) !=0 and len(self.videos) !=0:
            self.type = "mixed"
        elif len(self.imgs) != 0:
            self.type = "image"
        elif len(self.videos) != 0:
            self.type = "video"
        else: 
            self.type = "NO Visual"
        """
                self.engagement_rate
        """
        print(self.likes,self.comments,self.created_date,self.username)



    