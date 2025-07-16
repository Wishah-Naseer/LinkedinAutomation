def run():
    import yaml
    import requests
    from utils.phantom_api import launch_container, wait_for_completion, extract_result_links
    from utils.google_sheet import GoogleSheetManager

    # Load Config
    with open("E:/Jobs/Workerbase/LinkedinAutomation/settings/config.yaml", "r") as f:
        config = yaml.safe_load(f)

    api_key = config["phantombuster"]["api_key"]
    phantom_id = config["phantombuster"]["phantoms"]["extract_liker_details"]
    sheet_url = config["google_sheets"]["spreadsheet_url"]
    credentials_path = config["google_sheets"]["credentials_path"]

    print("🚀 Launching Phantom to likers details...")
    # container_id = launch_container(phantom_id, api_key)
    container_id = 6589948122593180
    output = wait_for_completion(phantom_id, api_key, container_id)

    _, json_url = extract_result_links(output)
    print(f"✅ JSON Result: {json_url}")

    response = requests.get(json_url)
    json_data = response.json()
        
    headers = ["First Name","Last Name", "Linkedin Headline", "Linedin Job Title", "Company Name", "Company Tagline", "Profile URL"]  # Header row
    rows = []
    for item in json_data:
        first_name = item.get("firstName", "")
        last_name = item.get("lastName", "")
        headline = item.get("linkedinHeadline", "")
        role = item.get("linkedinJobTitle", "") or headline
        company = item.get("companyName", "")
        company_tagline = item.get("linkedinCompanyTagline", "")
        profile_url = item.get("profileUrl", "")

        rows.append([first_name,last_name,headline, role, company, company_tagline, profile_url])

    # Upload to Google Sheets
    sheet_manager = GoogleSheetManager(credentials_path, sheet_url)
    sheet_manager.update_sheet(config["google_sheets"]["sheets"]["liker_details"], headers, rows)
