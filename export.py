import re
from mechanize import Browser
import config

browser = Browser()
browser.set_handle_robots(False)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
browser.open("https://sodexo4you.be/nl")

browser.select_form(id="account-login")


browser.form['name'] = config.email
browser.form['pass'] = config.password


response = browser.submit()

browser.retrieve('https://sodexo4you.be/nl/mijn-sodexo-card-saldo?description=All&type=LUNCH&export=1','export.csv')
browser.close()
