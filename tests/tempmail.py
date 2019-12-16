import json
import hashlib
import random as r
import requests


def get_email_address():
    rand = r.randint(0, 1000)
    # 0: "@coreclip.com"
    # 1: "@vipepe.com"
    # 2: "@taphear.com"
    return "fortest" + str(rand) + "@tmailer.org"


def get_email_hash(em):
    return hashlib.md5(em.encode('utf-8')).hexdigest()


def get_emails(hs):
    url = "https://privatix-temp-mail-v1.p.rapidapi.com/request/mail/id/" + hs+"/"
    headers = {
        'x-rapidapi-host': "privatix-temp-mail-v1.p.rapidapi.com",
        'x-rapidapi-key': "3afd7c7147mshc4c1b2cb5adf888p17847djsn99f952bb2efd"
    }
    response = requests.request("GET", url, headers=headers)
    result = json.loads(response.text)
    return result


def check_mail(em):
    h = get_email_hash(em)
    url = "https://privatix-temp-mail-v1.p.rapidapi.com/request/mail/id/" + h
    headers = {
        'x-rapidapi-host': "privatix-temp-mail-v1.p.rapidapi.com",
        'x-rapidapi-key': "3afd7c7147mshc4c1b2cb5adf888p17847djsn99f952bb2efd"
    }
    response = requests.request("GET", url, headers=headers)
    result = json.loads(response.text)
    return result