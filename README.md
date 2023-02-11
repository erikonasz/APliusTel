# APliusTel

--This script is a web scraping tool that collects phone numbers from the online marketplace "Autoplius" using the Python programming language and the Selenium and BeautifulSoup libraries.

--The script starts by asking the user to input a link to the Autoplius website, and then launches a Chrome web browser window to navigate to that page. It clicks on a button to accept the website's cookies and proceeds to scrape the phone numbers of a specified number of vehicles listed for sale on the website. The user is prompted to enter the number of vehicles they wish to scrape information from.

--The script uses Selenium to interact with the web page, clicking on individual vehicles to access their detailed pages, and BeautifulSoup to parse the HTML of each page and extract the phone numbers. The phone numbers are stored in a list and eventually saved to a CSV file. The script includes a function that adds random delays between actions to simulate human behavior and avoid raising suspicion from the website.

--This script is intended for educational or research purposes, and it is important to note that automated scraping of websites is often a violation of the website's terms of service and may result in the user's IP address being banned.
