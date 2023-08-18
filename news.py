import openai
import requests
import json
import os
from github import Github

repo = g.get_repo("cdn")

# Scrape the latest earthquake data
url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
response = requests.get(url)
data = response.json()

# Extract the earthquake data
earthquake = data["features"][0]["properties"]
magnitude = earthquake["mag"]
place = earthquake["place"]
time = earthquake["time"]

# Generate a news article using GPT-3
prompt = f"Write a news article about a {magnitude} magnitude earthquake that occurred in {place} at {time}."
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=2048,
    n=1,
    stop=None,
    temperature=0.5,
)
article = response.choices[0].text

# Create a new GitHub issue with the news article
title = f"{magnitude} magnitude earthquake in {place}"
body = f"An earthquake with a magnitude of {magnitude} occurred in {place} at {time}. Here is the news article:\n\n{article}"
repo.create_issue(title=title, body=body)
