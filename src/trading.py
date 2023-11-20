import requests
import json

base_url = "https://demo-api.ig.com/gateway/deal/"

IG_API_KEY = "44ac979fa1a93690779469a62b5378c051993017"

headers = {
    "Content-Type": "application/json; charset=UTF-8",
    "Accept": "application/json; charset=UTF-8",
    "X-IG-API-KEY": "44ac979fa1a93690779469a62b5378c051993017",
    "CST": "",
    "X-SECURITY-TOKEN": "",
}

epics = {
    "BTCUSD": "CS.D.BITCOIN.CFD.IP",
    "ETHUSD": "CS.D.ETHUSD.CFD.IP",
    "DOGUSD": "CS.D.DOGUSD.CFD.IP",
    "BCHUSD": "CS.D.BCHUSD.CFD.IP",
    "EURJPY": "CS.D.EURJPY.CFD.IP",
    "EURUSD": "CS.D.EURUSD.CFD.IP",
    "USDJPY": "CS.D.USDJPY.CFD.IP",
    "GBPUSD": "CS.D.GBPUSD.CFD.IP",
    "AUDUSD": "CS.D.AUDUSD.CFD.IP",
    "USDTWD": "CS.D.USDTWD.CFD.IP",
}


def login(api_key):
    url = base_url + "session"
    payload = '{ \r\n"identifier": "hanknine", \r\n"password": "aA00000000" \r\n} '
    temp_headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "Accept": "application/json; charset=UTF-8",
        "VERSION": "2",
        "X-IG-API-KEY": api_key,
    }
    response = requests.request("POST", url, headers=temp_headers, data=payload)
    res_headers = response.headers

    global headers
    headers["CST"] = res_headers["CST"]
    headers["X-SECURITY-TOKEN"] = res_headers["X-SECURITY-TOKEN"]
    # print(headers)


def findAllEpics(id):
    url = base_url + "marketnavigation/" + id
    response = requests.request("GET", url, headers=headers)
    data = json.loads(response.text)
    if "nodes" in data:
        if data["nodes"] != None:
            for node in data["nodes"]:
                # print(node['id'], node['name'], sep=", ")
                # print(node['id'])
                findAllEpics(node["id"])
        else:
            # print(data["markets"])
            if len(data["markets"]) != 0:
                # print(data["markets"][0])
                for market in data["markets"]:
                    print(market["instrumentName"], market["epic"])


# findAllEpics("165333")


def get_market_info(epic):
    url = base_url + "markets/" + epic
    response = requests.request("GET", url, headers=headers)
    data = json.loads(response.text)
    snapshot = data["snapshot"]
    # Sample format:
    # "snapshot": {
    #             "marketStatus": "TRADEABLE",
    #             "netChange": 192.3,
    #             "percentageChange": 0.52,
    #             "updateTime": "13:20:02",
    #             "delayTime": 0,
    #             "bid": 37155.1,
    #             "offer": 37245.1,
    #             "high": 37564.2,
    #             "low": 36910.9,
    #             "binaryOdds": null,
    #             "decimalPlacesFactor": 1,
    #             "scalingFactor": 1,
    #             "controlledRiskExtraSpread": 300
    #         }

    return snapshot


login(IG_API_KEY)
for key, value in epics.items():
    print(key, get_market_info(value)["bid"])
