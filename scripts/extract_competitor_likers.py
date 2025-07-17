"""
Script to extract the list of users who liked competitor posts on LinkedIn using Phantombuster API.
Downloads the result as JSON for further processing.
"""
def run():
    """
    Launches the Phantombuster 'extract_likers' agent, waits for completion, and downloads the JSON result.
    """
    import yaml
    import requests
    from utils.phantom_api import launch_container, wait_for_completion, extract_result_links

    # Load configuration from YAML file
    with open("E:/Jobs/Workerbase/LinkedinAutomation/settings/config.yaml", "r") as f:
        config = yaml.safe_load(f)

    api_key = config["phantombuster"]["api_key"]
    phantom_id = config["phantombuster"]["phantoms"]["extract_likers"]
    print("🚀 Launching Phantom to Competitors likes...")
    # Start the Phantombuster container
    container_id = launch_container(phantom_id, api_key)
    # Wait for the container to finish and get the output
    output = wait_for_completion(phantom_id, api_key, container_id)

    # Extract the JSON result link from the output
    _, json_url = extract_result_links(output)
    print(f"✅ JSON Result: {json_url}")

    # Download the JSON data
    response = requests.get(json_url)
    data = response.json()
    # Data is now available for further processing or saving
    

