# -*- coding:utf-8 -*-
from pprint import pprint

import requests

HOST = "http://127.0.0.1:8000"

trendOfTurnoverChart = '/dashboard/trendOfTurnoverChart'

assetAndCashFlowChart = '/dashboard/assetAndCashFlowChart'

# Asset and Cash
a = {
    "code": 200,
    "message": "success",
    "data": {
        "latestData": {
            "inceptionDate": "20250305",
            "netAssetValue": 32.0,
            "cashAndCashEquivalent": 54.0
        },
        "totalInterestReceived": 1311075.75,
        "chartData": {
            "expectedInterest": [
                {
                    "date": "2020",
                    "value": 253515.0
                },
                {
                    "date": "2021",
                    "value": 231102.46
                },
                {
                    "date": "2022",
                    "value": 337209.34
                },
                {
                    "date": "2023",
                    "value": 1119183.8
                },
                {
                    "date": "2024",
                    "value": 2160192.45
                },
                {
                    "date": "2025",
                    "value": 511885.27
                }
            ],
            "actualInterestReceived": [
                {
                    "date": "2020",
                    "value": 3665.62
                },
                {
                    "date": "2021",
                    "value": 2688.11
                },
                {
                    "date": "2022",
                    "value": 27410.09
                },
                {
                    "date": "2023",
                    "value": 167511.89
                },
                {
                    "date": "2024",
                    "value": 337941.46
                },
                {
                    "date": "2025",
                    "value": 18935.4
                }
            ]
        }
    }
}


def req_get(url, params=None):
    # response = requests.get(url, params=params)
    # res = response.json()
    res = a
    return res
