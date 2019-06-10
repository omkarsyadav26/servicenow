#Need to install requests package for python
#easy_install requests
import requests
from log import logging
import time

def calling():

    time.sleep(10)
    # Set the request parameters
    logging.info("expense allocation rest call")
    url = 'https://dev67363.service-now.com/api/323921/budget_use_case_exp_alloc'
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    response = requests.request('POST', url, headers=headers, allow_redirects=False,
                                auth=('admin', 'K3w1sTVeDtZl'))
    print(response.text)

    time.sleep(10)
    logging.info("expense allocation rest call")
    url = 'https://dev67363.service-now.com/api/323921/budget_use_case_budget_calc'
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    response = requests.request('POST', url, headers=headers, allow_redirects=False,
                                auth=('admin', 'K3w1sTVeDtZl'))
    print(response.text)