"""
Script to filter LinkedIn likers using an AI-powered Phantombuster agent.
Parses the raw response and uploads filtered profiles to a Google Sheet.
"""
def run():
    """
    Launches the Phantombuster 'filter_likers_ai' agent, waits for completion, parses the raw response,
    and uploads the filtered profiles to a specified Google Sheet.
    """
    import yaml
    import requests
    from utils.phantom_api import launch_container, wait_for_completion, extract_result_links
    from utils.google_sheet import GoogleSheetManager
    from utils.parser import parse_raw_response

    # Load configuration from YAML file
    with open("E:/Jobs/Workerbase/LinkedinAutomation/settings/config.yaml", "r") as f:
        config = yaml.safe_load(f)

    api_key = config["phantombuster"]["api_key"]
    phantom_id = config["phantombuster"]["phantoms"]["filter_likers_ai"]
    sheet_url = config["google_sheets"]["spreadsheet_url"]
    credentials_path = config["google_sheets"]["credentials_path"]

    print("🚀 Launching Phantom to filter likers...")
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
    # Parse the raw response to extract filtered profiles
    raw_response = data[0].get("rawResponse", "")
    parsed_profiles = parse_raw_response(raw_response)

    # Upload the filtered profiles to Google Sheets
    sheet_manager = GoogleSheetManager(credentials_path, sheet_url)
    headers = ["Profile URL", "Full Name", "Job Title", "Company", "Reason for Selection"]
    sheet_manager.update_sheet(config["google_sheets"]["sheets"]["filtered_likers"], headers, parsed_profiles)

