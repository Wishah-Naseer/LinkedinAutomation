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

## Useful Links
  1. Loom videp explaining how the automation works: [click here.](https://www.loom.com/share/0f9140a3d0954f9888d3cf6e8189f9aa?sid=57eae115-6174-4549-9531-d8a35ead4d11)
  2. Google Sheet link where the data is dumped: [click here.](https://docs.google.com/spreadsheets/d/14FSsN9YNEeA8vGrOP0TyLwnfV4Qom4tRDhqiU6qxLfI/edit?gid=539116565#gid=539116565)