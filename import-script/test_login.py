# ~/Ubun_nitrate/import-script/test_login.py
from nitrate_utils.nitrate_helper import check_login_nitrate

NITRATE_URL = "http://127.0.0.1:8000/xmlrpc/"
NITRATE_USER = "admin"
NITRATE_PASS = "admin"

check_login_nitrate(NITRATE_URL, NITRATE_USER, NITRATE_PASS)
