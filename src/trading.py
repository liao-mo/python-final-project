import requests
import json

# Base URL for IG API
base_url = "https://demo-api.ig.com/gateway/deal/"

# IG API Key
IG_API_KEY = "44ac979fa1a93690779469a62b5378c051993017"

# Common headers for API requests
headers = {
    "Content-Type": "application/json; charset=UTF-8",
    "Accept": "application/json; charset=UTF-8",
    "X-IG-API-KEY": IG_API_KEY,
    "CST": "",
    "X-SECURITY-TOKEN": "",
}

# Dictionary mapping instrument names to their corresponding EPIC codes
epics = {
    "BTCUSD": "CS.D.BITCOIN.CFD.IP",
    "ETHUSD": "CS.D.ETHUSD.CFD.IP",
    "DOGUSD": "CS.D.DOGUSD.CFD.IP",
    "BCHUSD": "CS.D.BCHUSD.CFD.IP",
    "AUDUSD": "CS.D.AUDUSD.CFD.IP",
    "EURCHF": "CS.D.EURCHF.CFD.IP",
    "EURJPY": "CS.D.EURJPY.CFD.IP",
    "EURGBP": "CS.D.EURGBP.CFD.IP",
    "EURUSD": "CS.D.EURUSD.CFD.IP",
    "GBPUSD": "CS.D.GBPUSD.CFD.IP",
    "GBPEUR": "CS.D.GBPEUR.CFD.IP",
    "USDCHF": "CS.D.USDCHF.CFD.IP",
    "USDCAD": "CS.D.USDCAD.CFD.IP",
    "USDJPY": "CS.D.USDJPY.CFD.IP",
    "USDTWD": "CS.D.USDTWD.CFD.IP",
    "GOLDUSD": "CS.D.CFDGOLD.CFDGC.IP",
}


def login(api_key):
    """
    Log in to the IG API and retrieve authentication tokens.

    Args:
        api_key (str): IG API Key.

    Returns:
        None
    """
    try:
        url = base_url + "session"
        payload = '{"identifier": "hanknine", "password": "aA00000000"}'
        temp_headers = {
            "Content-Type": "application/json; charset=UTF-8",
            "Accept": "application/json; charset=UTF-8",
            "VERSION": "2",
            "X-IG-API-KEY": api_key,
        }
        response = requests.post(url, headers=temp_headers, data=payload)
        if response.status_code == 200:
            print("Login to IG successfully")
        res_headers = response.headers

        global headers
        headers["CST"] = res_headers["CST"]
        headers["X-SECURITY-TOKEN"] = res_headers["X-SECURITY-TOKEN"]
    except Exception as e:
        print(f"Error: {e}")


def findAllEpics(id):
    """
    Recursively find all EPIC codes for a given market navigation ID.

    Args:
        id (str): Market navigation ID.

    Returns:
        None
    """
    try:
        url = base_url + "marketnavigation/" + id
        response = requests.get(url, headers=headers)
        data = json.loads(response.text)
        if "nodes" in data:
            if data["nodes"] is not None:
                for node in data["nodes"]:
                    findAllEpics(node["id"])
            else:
                if len(data["markets"]) != 0:
                    for market in data["markets"]:
                        print(
                            f'"{market["instrumentName"]}" : "{market["epic"]}"', end=", ")
    except Exception as e:
        print(f"Error: {e}")


def get_market_info(epic):
    """
    Get market information for a given EPIC code.

    Args:
        epic (str): EPIC code of the instrument.

    Returns:
        dict: Snapshot of market information.
    """
    try:
        url = base_url + "markets/" + epic
        response = requests.get(url, headers=headers)
        data = json.loads(response.text)
        snapshot = data["snapshot"]
        return snapshot
    except Exception as e:
        print(f"Error: {e}")


# Login to IG API
login(IG_API_KEY)

# Example: Retrieve and print market information for each instrument
# for key, value in epics.items():
#     print(key, get_market_info(value)["bid"])

# Example: Find all EPIC codes for a specific market navigation ID
# findAllEpics("165333")
