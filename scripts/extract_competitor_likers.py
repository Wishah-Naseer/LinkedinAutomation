def run():
    import yaml
    import requests
    from utils.phantom_api import launch_container, wait_for_completion, extract_result_links


    # Load Config
    with open("E:/Jobs/Workerbase/LinkedinAutomation/settings/config.yaml", "r") as f:
        config = yaml.safe_load(f)

    api_key = config["phantombuster"]["api_key"]
    phantom_id = config["phantombuster"]["phantoms"]["extract_likers"]
    print("🚀 Launching Phantom to Competitors likes...")
    container_id = launch_container(phantom_id, api_key)
    output = wait_for_completion(phantom_id, api_key, container_id)

    _, json_url = extract_result_links(output)
    print(f"✅ JSON Result: {json_url}")

    response = requests.get(json_url)
    data = response.json()
    

