"""
Utility module for parsing raw AI-generated responses into structured profile data.
Used to extract LinkedIn profile details from unstructured text.
"""
import re

def parse_raw_response(raw_response):
    """
    Parse the raw response string from the AI filter into a list of profile details.
    Args:
        raw_response (str): The unstructured text containing profile information.
    Returns:
        list: List of lists, each containing profile details (URL, name, job, company, reason).
    """
    profiles = []
    # Split the raw response into chunks for each profile
    chunks = re.split(r"(?:\n\d+\.\s+\*\*|\n\*\*Full Name|\A\*\*Full Name)", raw_response)
    for chunk in chunks:
        chunk = chunk.strip()
        if not chunk:
            continue

        # Extract profile fields using regex
        full_name = re.search(r"Full Name\**:?\s*(.*?)\n", chunk)
        job_title = re.search(r"Job Title\**:?\s*(.*?)\n", chunk)
        company = re.search(r"Company\**:?\s*(.*?)\n", chunk)
        profile_url = re.search(r"\[.*?\]\((https?://[^\s)]+)\)", chunk)
        reason = re.search(r"Reason for Selection\**:?\s*(.*)", chunk)

        profiles.append([
            profile_url.group(1).strip() if profile_url else "",
            full_name.group(1).strip() if full_name else "",
            job_title.group(1).strip() if job_title else "",
            company.group(1).strip() if company else "",
            reason.group(1).strip() if reason else ""
        ])
    return profiles
