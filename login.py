import mechanize
from bs4 import BeautifulSoup
from getpass import getpass

browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
browser.set_handle_refresh(False)

url = 'http://www.facebook.com/login.php'
browser.open(url)
browser.select_form(nr = 0)       #This is login-password form -> nr = number = 0
browser.form['email'] = "patel.ayush08@gmail.com"
browser.form['pass'] = getpass("Enter pasword : ")
resp_ = browser.submit().geturl()
resp = browser.open(resp_)
response = browser.response()
x=response.read()

soup=BeautifulSoup(x.encode('UTF-8'),"html.parser")
print(soup.prettify())
