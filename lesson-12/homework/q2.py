import requests
from bs4 import BeautifulSoup
import sqlite3
import csv


def scrape_jobs():
    url =  "https://realpython.github.io/fake-jobs"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    jobs =[]
    jobs_cards = soup.find_all("div", class_="card-content")
    for card in jobs_cards:
        title = card.find("div",class_="media-left")
        company=card.find("h3", class_="subtitle is-6 company")
        location=card.find("div", class_="content")
        description= card.find("a", class_="card-footer-item")["href"]
        apply_link=card.find("a", class_="card-footer-item")["href"]

import sqlite3
with sqlite3.connect("jobs.db") as conn:
  cursor = conn.cursor()
  cursor.execute("""
CREATE TABLE IF NOT EXISTS JOBS(
                 ID INT,
                 TITLE TEXT,
                 COMPANY TEXT,
                 LOCATION TEXT,
                 DESCRIPTION TEXT,
                 APPLY_LINK TEXT,
                 UNIQUE(TITLE, COMPANY, LOCATION)
                 
                 )""")
  conn.commit()

def insert_or_update_jobs(conn, jobs):
    cursor = conn.cursor()
    for job in jobs:
        cursor.execute("""
            SELECT id FROM jobs
            WHERE title = ? AND company = ? AND location = ?
        """, (job["title"], job["company"], job["location"]))

        result = cursor.fetchone()
    if result is None:
        cursor.execute("""
                INSERT INTO jobs (title, company, location, description, apply_link)
                VALUES (?, ?, ?, ?, ?)
            """, (job["title"], job["company"], job["location"], job["description"], job["apply_link"]))

    
    conn.commit()

    for job in jobs:
        cursor.execute("""
            INSERT OR REPLACE INTO jobs (title, company, location, description, apply_link)
            VALUES (?, ?, ?, ?, ?)
        """, (job["title"], job["company"], job["location"], job["description"], job["apply_link"]))

    conn.commit()
