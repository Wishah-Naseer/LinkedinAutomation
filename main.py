"""
Main entry point to run all LinkedIn automation scripts in sequence from the command line.
Useful for batch processing without the web interface.
"""
from scripts import extract_competitor_likers, extract_liker_details, filter_likers, send_message

# Run each script in order
extract_competitor_likers.run()
extract_liker_details.run()
filter_likers.run()
send_message.run()
