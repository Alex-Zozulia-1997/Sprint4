#work on engagement rate +
#think of potential trend-building all profiles > all posts by column> about 500 concurrent requests at a time 

import requests
import concurrent.futures
import json
import csv
import os
from engagement_rate import engagement_calculation




def get_the_profiles(url):
    headers = {
        'Content-Type': 'application/json'
    }
    with open("credentials.csv","r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            username = row['Username']
            password = row['Password']
  
    
    task_params = {
        'url': url,
        'target': 'instagram_profile',
        'locale': 'en-us',
        'geo': 'Brazil'
    }

    
    response = requests.post(
        'https://scraper-api.smartproxy.com/v1/scrape',
        headers = headers,
        json = task_params,
        auth = (username, password)
    )
    #print(response.text)
    try:
        parsed_data = json.loads(response.text)
        
        #parsed_data = response_post

        print(parsed_data)
        username = parsed_data['data']['content']['account']['username']

        followers = parsed_data['data']['content']['stats']['followers']
        following = parsed_data['data']['content']['stats']['following']
        description = parsed_data['data']['content']['biography']['description']
        post_count = parsed_data['data']['content']['stats']['posts']
        posts = parsed_data['data']['content']['posts']
        post_hrefs = [i["href"] for i in posts]
        row_dict = {"Profile_link": url,"Username":username, "Post_count": post_count, "Followers": followers, "Following": following, "Profile_description": description}
        for i,index in zip(posts,range(1,13)):
            data_per_post_from_profile_call = {f'href_{index}': i["href"], f'description_{index}': i["description"], f'Hashtags_{index}': "", f'Visual_{index}': i["image"], f'Type_{index}': '', f'Likes_{index}': '', f'Comment_{index}': '', f'Engagement_rate_{index}': "", f'Date_{index}': '', f'Time_{index}': ''}
            row_dict.update(data_per_post_from_profile_call)
        return row_dict
    #JSONDecodeError
    except:
        pass




def prof_scrape(list_of_links):
    file_path = "profiles.csv"
   
    #urls = ["https://www.instagram.com/turingcollege/?hl=en","https://www.instagram.com/usykaa/?hl=en","https://www.instagram.com/bjj_world_/","https://www.instagram.com/bookingcom/","https://instagram.com/nathanielius?igshid=MzRlODBiNWFlZA==","https://www.instagram.com/turingcollege/?hl=en"]

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(get_the_profiles, list_of_links)
    for i in results:
        try:
            is_empty = os.stat(file_path).st_size == 0
            with open(file_path, mode="a", newline="") as file:
                writer = csv.writer(file)
                if is_empty:
                    writer.writerow(i.keys())
                writer.writerow(i.values())    
        except: 
            pass
    return(file_path)
   


if __name__ == "__main__":
    prof_scrape()


    