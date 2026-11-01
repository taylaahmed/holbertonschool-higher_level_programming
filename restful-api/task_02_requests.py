#!/usr/bin/python3

import csv
import requests

URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_and_print_posts():
    reponse = requests.get(URL)
    print("Status Code: {}".format(reponse.status_code))

    if reponse.status_code == 200:
        posts = reponse.json()
        for post in posts:
            print(post["title"])

def fetch_and_save_posts():
    reponse = requests.get(URL)

    if reponse.status_code == 200:
        posts = reponse.json()
        data = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]
        with open("posts.cvs", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data)
