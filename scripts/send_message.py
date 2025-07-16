def run():
    import yaml
    import requests
    from utils.phantom_api import launch_container, wait_for_completion, extract_result_links


    # Load Config
    with open("E:/Jobs/Workerbase/LinkedinAutomation/settings/config.yaml", "r") as f:
        config = yaml.safe_load(f)

    api_key = config["phantombuster"]["api_key"]
    phantom_id = config["phantombuster"]["phantoms"]["send_message"]


    print("🚀 Launching Phantom to Outreach Messages...")
    container_id = launch_container(phantom_id, api_key)
    output = wait_for_completion(phantom_id, api_key, container_id)

    _, json_url = extract_result_links(output)
    print(f"✅ JSON Result: {json_url}")
    
    print("Message sent to the Potential Fits fot Workerbase")

