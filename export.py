import re
from mechanize import Browser
import config

browser = Browser()
browser.open("https://sodexo4you.be/nl")

browser.select_form(id="account-login")


browser.form['name'] = config.email
browser.form['pass'] = config.password


response = browser.submit()

browser.retrieve('https://sodexo4you.be/nl/mijn-sodexo-card-saldo?description=All&type=LUNCH&export=1','export.csv')
browser.close()
