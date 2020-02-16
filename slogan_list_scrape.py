import requests
import csv
import sys
import time

from bs4 import BeautifulSoup

# categories in sloganlist.com website as of 15 Feb 2020
category_list=['drinking', 'food', 'restaurant', 'car', 'apparel', 'technology', 'business', 'company', 'cosmetic', 'household', 'tours', 'airlines', 'financial', 'health-medicine', 'education']
# max number of pages per category as of 15 Feb 2020
max_page_count = 20
# name of the output file
output_file = 'sloganlist.csv'


def get_data(url):
	# In case of Status 403 (Forbidden), wait for some time (maybe hours) before retrying
	headers = {
	"Connection": "keep-alive",
	"Upgrade-Insecure-Requests": "1",
	"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36",
	"Sec-Fetch-Dest": "document",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"Sec-Fetch-Site": "none",
	"Sec-Fetch-Mode": "navigate",
	"Sec-Fetch-User": "?1",
	"Accept-Encoding": "gzip, deflate, br",
	"Accept-Language": "en-US,en;q=0.9"
	}

	try:
		return requests.get(url, headers=headers).text
	except Exception:
		time.sleep(1)
		return requests.get(url, headers=headers).text
	print(requests.get(url).status_code)

def collect_data(category_list=None, max_page_count=0):
	# a. scrape data from the link
	# b. parse it
	# c. final result stored as a list of rows
	rows=[]
	print(max_page_count)
	print(category_list)
	for category in category_list:
		print('Category:'+category)
		base_url = "https://www.sloganlist.com/"+str(category)+"-slogans/"
		for page in range(max_page_count):
			print("Page Number:"+str(page))
			url = base_url
			if(page > 0):
				url = base_url + "index_"+str(page)+".html"
			data = get_data(url)			
			soup = BeautifulSoup(data,'html.parser')
			org_names = soup.findAll('h5',{'class':'list-group-item-heading'})
			org_slogans = soup.findAll('p',{'class':'list-group-item-text'})
			# if(len(org_names) == 0):
			# 	break
			# 	# no more company slogans found
			# 	# break out of inner for loop
			# 	# continue with the next category
			# 	print('yes')
			# 	break
			for i in range(0,len(org_slogans)):
				try:
				    row = [org_names[i].contents[1].strip(), org_slogans[i].contents[0].strip()]
				    rows.append(row)
				    # print(row)
				except AttributeError:
				    pass
	return rows

def write_data(data, output_file):
	# write data to the output file
	with open(output_file, 'w', newline='') as file:
		writer = csv.writer(file)
		# header of the csv
		writer.writerow(['Company', 'Slogan'])
		# contents
		writer.writerows(data)
	pass

def main():
	data = collect_data(category_list, max_page_count)
	write_data(data, output_file)
	return 0

if __name__ == '__main__':
    sys.exit(main())