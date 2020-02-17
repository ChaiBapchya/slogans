# slogans
Dataset for the slogans

# Pre-Requisites
Install requirements using the file `requirements.txt`
```
pip install -r requirements.txt
```

# 1. Slogan List (www.sloganlist.com)

Website that tracks list of slogans.
As of 15 Feb 2020, the website contains more than 1000 pairs of "company, slogan" spread across 10+ categories.

Leveraged requests, beautifulsoup (python packages) for scraping data off the sloganlist website.

### Run
```
python slogan_list_scrape.py
```
#### Note
In case of Status 403 (Forbidden Access), IP will be blocked due to high volume of GET requests. Only way out of it was to wait for a few hours.

##To Do
# 2. sloganspoint.com
# 3. thinkslogans.com
