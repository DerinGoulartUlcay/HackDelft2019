"""
DeDucktible
Group 6
HackDelft 2019
"""
'''
Find the date, organization, total amount and currency from the ocr'ed text.

Hackathon 2019
Group 6
Derin Goulart Ulcay
'''
import re

import os
os.system('tesseract "TU Delft - 2019-05-12.jpeg" receipt dut')

def read_receipt(my_file):
    with open(my_file, 'r') as f:
        lines = f.readlines()
    return lines
#REGEX Patterns To Be Searched
date_pattern = re.compile(r"^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$")

total_amount_pattern = re.compile(r"\d*(\.|,)\d*")

currency_symbol_pattern = re.compile(u"[$¢£¤¥֏؋৲৳৻૱௹฿៛\u20a0-\u20bd\ua838\ufdfc\ufe69\uff04\uffe0\uffe1\uffe5\uffe6]")
currency_abbrev_pattern = re.compile(u"\b[A-Z]{3}\b")

#Find The Organization

from flask import Flask, render_template, request, redirect, url_for
import re
# import Controller.web_scraping as ws


app = Flask(__name__, template_folder="../View/templates", static_folder="../View/static")

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

receipt = read_receipt("receipt.txt")



file_name = "TU Delft - 2019-05-12.jpeg"
cost = "unknown"
for line in receipt:
    print(line)
    if "EUR" in line:
        currency = currency_abbrev_pattern.findall(line)
        price = total_amount_pattern.findall(line)
        print(currency, cost)
data = {'filename':file_name, 'breakfast': price}

@app.route('/', methods=['GET', 'POST'])
def index():
    """Renders a sample page."""
    if request.method == 'POST':
        pass
    else:
        return render_template("index.html", data = data)



if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
