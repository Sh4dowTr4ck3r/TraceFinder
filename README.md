# OSINT Finder

## Overview

**OSINT Finder** is a Python-based open-source intelligence (OSINT) tool designed for cyber investigations, digital forensics, and security operations. It automates the collection of publicly available data related to individuals, IP addresses, and phone numbers, assisting security analysts, digital forensics experts, and researchers in gathering critical information quickly.

## Features

- **Full Name Search**: Queries multiple OSINT databases (e.g., PeekYou, WhitePages, Spokeo, FastPeopleSearch, LinkedIn, Facebook, Twitter, Google Dork) for public records and social media profiles.
- **Social Media Lookup**: Checks usernames across various social media platforms (Twitter, Facebook, Instagram, LinkedIn, GitHub, TikTok, Reddit, YouTube, Pinterest, Snapchat, Tumblr, Flickr, Medium).
- **Phone Number Lookup**: Validates phone numbers and retrieves carrier, location, and line type information using the [apilayer Phone Validation API](https://apilayer.com/marketplace/phone_validation_api).
- **GeoIP Lookup**: Retrieves geolocation information (country, city, latitude/longitude, ISP) for a given IP address using the [ip-api](http://ip-api.com) service.

## Prerequisites

- Python 3.x
- Required Python packages:
  ```bash
  pip install requests
  ```

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Sh4dowTr4ck3r/TraceFinder.git
   ```
2. **Navigate to the Project Directory:**
   ```bash
   cd OSINT_Finder
   ```
3. **(Optional) Create a Virtual Environment and Activate It:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
4. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script using:

```bash
python OSINT_Finder.py
```

You will be presented with a menu to choose from the following options:

1. **Search by Full Name**: Enter a full name (e.g., "John Doe") to search multiple OSINT sources.
2. **Search Social Media by Username**: Input a username to check for profiles across social media platforms.
3. **Lookup Phone Number Details**: Enter a phone number and country code to retrieve relevant details.
4. **Perform GeoIP Lookup**: Enter an IP address to obtain geolocation details including the country, city, latitude/longitude, and ISP.

### Example Session

```
🔎 OSINT Finder: People Search, Phone Lookup & GeoIP Tool
1️⃣  Search by Full Name
2️⃣  Search Social Media by Username
3️⃣  Lookup Phone Number Details
4️⃣  Perform GeoIP Lookup on an IP Address

Enter your choice (1/2/3/4): 1

Enter the Full Name (First Last): Jane Doe

🔍 Searching for Public Records and Social Media Profiles...
[✅] PeekYou Profile Found: https://www.peekyou.com/Jane%20Doe
[❌] WhitePages Not Found or Inaccessible
[✅] LinkedIn Profile Found: https://www.linkedin.com/search/results/people/?keywords=Jane%20Doe
...
```

## API Key Setup for Phone Lookup

For the phone number lookup feature, you need an API key from [apilayer](https://apilayer.com/marketplace/phone_validation_api). Replace the placeholder API key in the `check_phone` function:

```python
api_key = "YOUR_API_KEY_HERE"
```

## Future Enhancements

- **Enhanced Error Handling and Logging:** Use Python’s `logging` module to track errors and API failures.
- **Command-Line Arguments:** Implement `argparse` for non-interactive searches.
- **Asynchronous Requests:** Improve performance using `asyncio` and `aiohttp`.
- **Dockerization:** Package the tool into a Docker container for easy deployment.
- **Unit Testing:** Implement `pytest` tests to validate script functionality.
- **Integration with Additional Threat Feeds:** Expand lookup capabilities with VirusTotal, MISP, and AbuseIPDB.

## Contributing

Contributions are welcome! If you have ideas for improvements, bug fixes, or new features, please fork the repository and submit a pull request.


