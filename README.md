# Sprint4

This in an MVP of social media scraper program that transforms json output into CSV providing user of Smartproxy social media API with an easy way of getting data without any coding. 
To use it you will need to have an active subscription for Smartproxy SM API. 

Expected usage of requests: on each profile link with at least 12 public posts - you should expect 13 API calls. 

#How to use it?
0. Install Python from here https://www.python.org/downloads/
1. You will need to download the files in this repository 
2. Open the Terminal. You would want to navigate to the needed folder using “cd”-change directory until you are in the right one. Read this, if unsure how to do it - https://gomakethings.com/navigating-the-file-system-with-terminal/. 
3. You will need to run “$pip install -r requirements.txt”
4. Then run main.py
5. Input the needed credentials 
6. Click “Start Scraping”
Here is a Video on how to do it: https://www.loom.com/share/ecd4c247763e445d88ecff892d6984aa 

Right now you can only scrape profiles with all the public posts (12). The input should be only links of the profiles (see the video). As the output you will get enriched profiles + their enriched 12 posts.  

The next step will be to add functionality of scraping just profiles or Just posts by their links. 
Later users will be able to scrape TikTok as well. 

