import concurrent.futures
import pandas as pd
from post import Post
from engagement_rate import engagement_calculation
    
def get_the_post(url,n):
    #just to be sure that if one link is deffective or we will catch a instagrams defence system - they other links will still be worked on.
    try:
        current_post = Post(url)
        #just building the datapoints for the post
        post_data = {
            f"Hashtags_{n}": current_post.hashtags,
            f"Type_{n}": current_post.type,
            f"Likes_{n}": str(current_post.likes),
            f"Comment_{n}": str(current_post.comments),
            f"Engagement_rate_{n}": 0,
            f"Date_{n}": current_post.date,
            f"Time_{n}": current_post.time
        }
        return post_data
    except:
        pass
        


    

def post_enrichment(inial_file,final_file):
    #once we have the profile links - it's time to scrape the posts of those profiles. 
    # profiles.csv will be the inital file for this case
    with open (inial_file, "r") as file:
        df = pd.read_csv(file)
    #need to have all data-points numbered, so we can display the data on all posts in one row
    for index in range(1,13):
        links = df[f"href_{index}"]
        #multithreading in python - so now te are going to be sending up to 100 requests almost at the same time. 
        with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
            #all the outcomes are stored in results
            results = list(executor.map(get_the_post, links,[index] * len(links)))
        #building lists to push to our df
        types = [i[f"Type_{index}"] if i is not None else "" for i in results]
        likes = [i[f"Likes_{index}"] if i is not None else "" for i in results]
        comments = [i[f"Comment_{index}"] if i is not None else "" for i in results]
        dates = [i[f"Date_{index}"] if i is not None else "" for i in results]
        times = [i[f"Time_{index}"] if i is not None else "" for i in results]
        hashtags = [i[f"Hashtags_{index}"] if i is not None else "" for i in results]
        #print(types)
        #print(results)

        #pushing the lists to df
        df[f"Type_{index}"] = types
        df[f"Likes_{index}"] = likes
        df[f"Comment_{index}"] = comments
        df[f"Date_{index}"] = dates
        df[f"Time_{index}"] = times
        df[f"Hashtags_{index}"] = hashtags

    #print(df)
    df.to_csv("new_post.csv",index=False)
    engagement_calculation("new_post.csv",final_file)


#need to update the csv with this  daya 