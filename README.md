# LinkedIn Automation

This project automates several LinkedIn workflows, including extracting post likers, gathering their details, filtering them, and sending messages. It is built with Python and Flask, providing a simple web interface to run all automation scripts sequentially. Automation is done through APIs of PhantomBuster.

## Features
- **Extract Competitor Likers:** Scrape users who liked competitor posts.
- **Extract Liker Details:** Gather detailed information about each liker.
- **Filter Likers:** Filter likers based on custom criteria.
- **Send Message:** Send automated messages to filtered users.
- **Web Interface:** Run all scripts from a single web page.

## Project Structure
```
LinkedinAutomation/
  app.py                  # Flask web server
  main.py                 # (Entry point or additional logic)
  requirements.txt        # Python dependencies
  credentials/            # Store googlesheet credentials
  scripts/                # Automation scripts
    extract_competitor_likers.py
    extract_liker_details.py
    filter_likers.py
    send_message.py
  settings/
    config.yaml           # Configuration file
  static/
    images/
      logo.png            # Project logo
  templates/
    index.html            # Web UI template
  utils/                  # Utility modules
    google_sheet.py
    parser.py
    phantom_api.py
```

## Setup
1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd LinkedinAutomation
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure settings:**
   - Add your credentials to the `credentials/` directory.
   - Edit `settings/config.yaml` as needed.

## Usage
1. **Start the Flask server:**
   ```bash
   python app.py
   ```
2. **Open your browser and go to:**
   [http://localhost:5000](http://localhost:5000)
3. **Click the button to Perform Outreach, or visit `/run-all` endpoint.**
