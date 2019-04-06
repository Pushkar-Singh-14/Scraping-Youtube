from bs4 import BeautifulSoup as bs
import requests
import pickle
import os
import csv

cwd=os.getcwd()
parent_folder=os.path.join(cwd,'Data')
pickle_out=open("/Users/pushkarsingh/Data/Pickle/vid_ids_dict.pickle","rb")
vid_id_dict=pickle.load(pickle_out)

dataset_folder=os.path.join(parent_folder,"Dataset")
if not os.path.exists(dataset_folder):
    os.makedirs(dataset_folder)



csv_file_path= os.path.join(parent_folder,'main.csv')


    
    
base = "https://www.youtube.com/watch?v="
for key, values in vid_id_dict.items():
    if key=="travel blogs":
        query_dataset_folder=os.path.join(dataset_folder,key)

        if not os.path.exists(query_dataset_folder):
            os.makedirs(query_dataset_folder)

        for link in values:


            r = requests.get(base+link)
            soup = bs(r.text)
            name=link+".txt"
            save_description_link=os.path.join(query_dataset_folder,name)

            f= open(save_description_link,"a+")

            for title in soup.findAll('p', attrs={'id': 'eow-description'}):
                description=title.text.strip()
                f.write(description)
            f.close()

            for title in soup.findAll('span', attrs={"class": 'watch-title'}):
                vid_title= title.text.strip()

            with open(csv_file_path, 'a+') as csvfile:
                fieldnames = ['Video id', 'Title','Description','Category']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({'Video id': link, 'Title': vid_title, 'Description':description,'Category':key})
