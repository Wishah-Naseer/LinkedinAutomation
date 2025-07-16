def run():
    import yaml
    import requests
    from utils.phantom_api import launch_container, wait_for_completion, extract_result_links
    from utils.google_sheet import GoogleSheetManager
    from utils.parser import parse_raw_response

    # Load Config
    with open("E:/Jobs/Workerbase/LinkedinAutomation/settings/config.yaml", "r") as f:
        config = yaml.safe_load(f)

    api_key = config["phantombuster"]["api_key"]
    phantom_id = config["phantombuster"]["phantoms"]["filter_likers_ai"]
    sheet_url = config["google_sheets"]["spreadsheet_url"]
    credentials_path = config["google_sheets"]["credentials_path"]

    print("🚀 Launching Phantom to filter likers...")
    container_id = launch_container(phantom_id, api_key)
    output = wait_for_completion(phantom_id, api_key, container_id)

    _, json_url = extract_result_links(output)
    print(f"✅ JSON Result: {json_url}")

    response = requests.get(json_url)
    data = response.json()
    raw_response = data[0].get("rawResponse", "")
    parsed_profiles = parse_raw_response(raw_response)

    # Upload to Google Sheets
    sheet_manager = GoogleSheetManager(credentials_path, sheet_url)
    headers = ["Profile URL", "Full Name", "Job Title", "Company", "Reason for Selection"]
    sheet_manager.update_sheet(config["google_sheets"]["sheets"]["filtered_likers"], headers, parsed_profiles)

