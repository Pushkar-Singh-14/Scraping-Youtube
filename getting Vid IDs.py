from selenium import webdriver
import time 
from bs4 import BeautifulSoup as bs
import os
import pickle

cwd=os.getcwd()
parent_folder=os.path.join(cwd,'Data')
pickle_folder=os.path.join(parent_folder,"Pickle")

if not os.path.exists(parent_folder):
    os.makedirs(parent_folder)
    
if not os.path.exists(pickle_folder):
    os.makedirs(pickle_folder)

queries=['science and technology', 'food', 'manufacturing', 'history', 'art and music', 'travel blogs']

base="https://www.youtube.com/results?search_query="


for query in queries:
   
    query1=query.replace(" ","+")
    
    link=base+query1
    
    driver = webdriver.Firefox(executable_path=r'/Users/pushkarsingh/Downloads/geckodriver')
    driver.get(link)

    time.sleep(5)
    
    for i in range(0,100):
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(3)
        print(i)

    soup=bs(driver.page_source, 'lxml')
    vids = soup.findAll('a',{"class":"yt-simple-endpoint style-scope ytd-video-renderer"})
    print(query)
    
    save_ids=os.path.join(parent_folder,'IDs')
    if not os.path.exists(save_ids):
        os.makedirs(save_ids)
    
    name=query+".txt"
    save_ids_link=os.path.join(save_ids,name)
    
    f= open(save_ids_link,"a+")
    vid_id_list=[]

    for v in vids:
        d=str(v)
        vid_id=d[(d.find("href"))+15:(d.find("id="))-2]
        print(vid_id)
        if (vid_id.find("imple"))==-1:
            vid_id_list.append(vid_id)
            
            f.write(vid_id)
            f.write("\n")
    
    vid_id_dict.update({query:[ids for ids in vid_id_list ]})
    f.close()
vid_ids_dict_pickle_path=os.path.join("pickle_folder","vid_ids_dict.pickle")
pickle_in=open(vid_ids_dict_pickle_path,"wb")
pickle.dump(vid_id_dict,pickle_in)
pickle_in.close()

