import openai
import requests
import json
import os
from github import Github

# Set up the GitHub API with authentication
access_token = os.environ["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"]  # replace with your own access token
g = Github(login_or_token=access_token)
repo = g.get_repo("imabutahersiddik/cdn")

# Scrape the latest earthquake data
url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
response = requests.get(url)
data = response.json()

# Extract the earthquake data
earthquake = data["features"][0]["properties"]
magnitude = earthquake["mag"]
place = earthquake["place"]
time = earthquake["time"]

# Generate a news article
prompt = f"Write a news article about a {magnitude} magnitude earthquake that occurred in {place} at {time}."
article = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac enim sed justo molestie elementum. Nullam vel odio auctor, cursus massa eu, ornare nibh. Sed euismod tellus eu nisl luctus, eu pulvinar elit eleifend. Sed semper, mauris eu consequat feugiat, lorem mauris tincidunt elit, eget volutpat lectus felis in risus. Donec euismod, enim vel euismod tincidunt, urna velit bibendum est, vitae vulputate sem metus vitae nulla. Sed ac enim sed justo molestie elementum. Nullam vel odio auctor, cursus massa eu, ornare nibh."

# Create a new GitHub issue with the news article
title = f"{magnitude} magnitude earthquake in {place}"
body = f"An earthquake with a magnitude of {magnitude} occurred in {place} at {time}. Here is the news article:\n\n{article}"
repo.create_issue(title=title, body=body)
