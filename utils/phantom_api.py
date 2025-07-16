import time
import re
import requests

def launch_container(phantom_id, api_key):
    url = f"https://api.phantombuster.com/api/v1/agent/{phantom_id}/launch"
    headers = {"accept": "application/json", "X-Phantombuster-Key-1": api_key}
    resp = requests.post(url, headers=headers)
    resp.raise_for_status()
    return resp.json()["data"]["containerId"]

def get_output(phantom_id, api_key, container_id):
    url = f"https://api.phantombuster.com/api/v1/agent/{phantom_id}/output?containerId={container_id}"
    headers = {"accept": "application/json", "X-Phantombuster-Key-1": api_key}
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    data = resp.json()["data"]
    return data["agentStatus"], data["output"]

def wait_for_completion(phantom_id, api_key, container_id, interval=15):
    status = "running"
    output = ""
    while status != "not running":
        status, output = get_output(phantom_id, api_key, container_id)
        time.sleep(interval)
    return output

def extract_result_links(output):
    csv_match = re.search(r'https:\/\/phantombuster\.s3\.amazonaws\.com\/[^\s]+\.csv', output)
    json_match = re.search(r'https:\/\/phantombuster\.s3\.amazonaws\.com\/[^\s]+\.json', output)
    return (csv_match.group(0) if csv_match else None,
            json_match.group(0) if json_match else None)
