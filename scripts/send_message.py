"""
Script to send outreach messages to filtered LinkedIn users using Phantombuster API.
Prints confirmation after sending messages.
"""
def run():
    """
    Launches the Phantombuster 'send_message' agent, waits for completion, and confirms message delivery.
    """
    import yaml
    import requests
    from utils.phantom_api import launch_container, wait_for_completion, extract_result_links

    # Load configuration from YAML file
    with open("E:/Jobs/Workerbase/LinkedinAutomation/settings/config.yaml", "r") as f:
        config = yaml.safe_load(f)

    api_key = config["phantombuster"]["api_key"]
    phantom_id = config["phantombuster"]["phantoms"]["send_message"]

    print("🚀 Launching Phantom to Outreach Messages...")
    # Start the Phantombuster container
    container_id = launch_container(phantom_id, api_key)
    # Wait for the container to finish and get the output
    output = wait_for_completion(phantom_id, api_key, container_id)

    # Extract the JSON result link from the output
    _, json_url = extract_result_links(output)
    print(f"✅ JSON Result: {json_url}")
    
    # Print confirmation message
    print("Message sent to the Potential Fits for Workerbase")

