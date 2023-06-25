import pandas as pd

def engagement_calculation(old_file,new_file):
    with open (old_file, "r") as file:
        df = pd.read_csv(file)

    followers = df["Followers"]
    # a for loop to conduct the calculation of the engagement rate for all columns 
    for index in range(1,13):
        # private profiles will have no info on the posts, so not to screw up - all NaNs are converted to zeros
        likes = df[f"Likes_{index}"].fillna(0)
        comments = df[f"Comment_{index}"].fillna(0)

    #adding likes and comments,
        sums = [int(i.replace(",", "")) + int(j) if isinstance(i,str) else i + int(j) for i,j in zip(likes,comments)]
    #executing the formula for the engagement rate per post 
        
        list_of_engagement = ["{0:.2f}%".format((i/float(str(j).replace(",","")))*100) for i,j in zip(sums,followers)]
    
        df[f"Engagement_rate_{index}"] = list_of_engagement


    #writing the fully updated df to the csv
    df.to_csv(new_file, index = False)

if __name__ == "__main__":
    engagement_calculation(old_file="new_post.csv", new_file="newf.csv")

