'''
Find the date, organization, total amount and currency from the ocr'ed text.

Hackathon 2019
Group 6
Derin Goulart Ulcay
'''
import re


with open(my_file, 'r') as f:
    lines = f.readlines()

#REGEX Patterns To Be Searched
date_pattern = re.compile(r"^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$")

total_amount_pattern = re.compile("")

currency_symbol_pattern = re.compile(u"[$¢£¤¥֏؋৲৳৻૱௹฿៛\u20a0-\u20bd\ua838\ufdfc\ufe69\uff04\uffe0\uffe1\uffe5\uffe6]")
currency_abbrev_pattern = re.compile(u"\b[A-Z]{3}\b")

#Find The Organization