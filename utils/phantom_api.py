"""
Utility module for interacting with the Phantombuster API.
Provides functions to launch agents, poll for completion, and extract result links.
"""
import time
import re
import requests

def launch_container(phantom_id, api_key):
    """
    Launch a Phantombuster agent (container) by ID.
    Args:
        phantom_id (str): The ID of the Phantombuster agent to launch.
        api_key (str): The Phantombuster API key.
    Returns:
        str: The container ID of the launched agent.
    """
    url = f"https://api.phantombuster.com/api/v1/agent/{phantom_id}/launch"
    headers = {"accept": "application/json", "X-Phantombuster-Key-1": api_key}
    resp = requests.post(url, headers=headers)
    resp.raise_for_status()
    return resp.json()["data"]["containerId"]

def get_output(phantom_id, api_key, container_id):
    """
    Get the output and status of a running Phantombuster container.
    Args:
        phantom_id (str): The ID of the Phantombuster agent.
        api_key (str): The Phantombuster API key.
        container_id (str): The container ID to check.
    Returns:
        tuple: (status, output) where status is a string and output is the result text.
    """
    url = f"https://api.phantombuster.com/api/v1/agent/{phantom_id}/output?containerId={container_id}"
    headers = {"accept": "application/json", "X-Phantombuster-Key-1": api_key}
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    data = resp.json()["data"]
    return data["agentStatus"], data["output"]

def wait_for_completion(phantom_id, api_key, container_id, interval=15):
    """
    Poll the Phantombuster container until it is no longer running.
    Args:
        phantom_id (str): The ID of the Phantombuster agent.
        api_key (str): The Phantombuster API key.
        container_id (str): The container ID to poll.
        interval (int): Seconds to wait between polls.
    Returns:
        str: The output text from the completed container.
    """
    status = "running"
    output = ""
    while status != "not running":
        status, output = get_output(phantom_id, api_key, container_id)
        time.sleep(interval)
    return output

def extract_result_links(output):
    """
    Extract CSV and JSON result links from the output text.
    Args:
        output (str): The output text containing result URLs.
    Returns:
        tuple: (csv_url, json_url) if found, otherwise None for missing links.
    """
    csv_match = re.search(r'https:\/\/phantombuster\.s3\.amazonaws\.com\/[^\s]+\.csv', output)
    json_match = re.search(r'https:\/\/phantombuster\.s3\.amazonaws\.com\/[^\s]+\.json', output)
    return (csv_match.group(0) if csv_match else None,
            json_match.group(0) if json_match else None)
