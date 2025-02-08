import requests
import urllib.parse

# -------------------- Full Name Search --------------------
def check_full_name(full_name):
    print("\n🔍 Searching for Public Records and Social Media Profiles...")

    # Encode the name for URLs
    encoded_name = urllib.parse.quote(full_name)

    # List of OSINT search sites
    search_sites = {
        "PeekYou": f"https://www.peekyou.com/{encoded_name}",
        "WhitePages": f"https://www.whitepages.com/name/{encoded_name}",
        "Spokeo": f"https://www.spokeo.com/{encoded_name}",
        "FastPeopleSearch": f"https://www.fastpeoplesearch.com/name/{encoded_name}",
        "LinkedIn": f"https://www.linkedin.com/search/results/people/?keywords={encoded_name}",
        "Facebook": f"https://www.facebook.com/search/top?q={encoded_name}",
        "Twitter": f"https://twitter.com/search?q={encoded_name}",
        "Google Dork": f"https://www.google.com/search?q=%22{encoded_name}%22+site%3Alinkedin.com",
        "Google PDF Search": f"https://www.google.com/search?q=%22{encoded_name}%22+filetype%3Apdf"
    }

    for site, url in search_sites.items():
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"[✅] {site} Profile Found: {url}")
            else:
                print(f"[❌] {site} Not Found or Inaccessible")
        except requests.exceptions.RequestException:
            print(f"[⚠️] {site} Request Timed Out or Failed")

# -------------------- Social Media Lookup --------------------
def check_social(username):
    social_media_sites = {
        "Twitter": f"https://twitter.com/{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}",
        "LinkedIn": f"https://www.linkedin.com/in/{username}",
        "GitHub": f"https://github.com/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "YouTube": f"https://www.youtube.com/c/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}",
        "Snapchat": f"https://www.snapchat.com/add/{username}",
        "Tumblr": f"https://{username}.tumblr.com",
        "Flickr": f"https://www.flickr.com/photos/{username}",
        "Medium": f"https://medium.com/@{username}"
    }

    print("\n🔍 Checking Social Media Accounts...")
    for platform, url in social_media_sites.items():
        response = requests.get(url)
        if response.status_code == 200:
            print(f"[✅] {platform} Profile Found: {url}")
        else:
            print(f"[❌] {platform} Not Found")

# -------------------- Phone Number Lookup --------------------
def check_phone(phone_number, country_code):
    api_key = "API_KEY"  # Replace with your actual API key
    
    # Construct API request URL
    url = f"http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}&country_code={country_code}&format=1"

    print("\n🔍 Checking Phone Number Details...")

    try:
        response = requests.get(url)

        if response.status_code == 200:
            try:
                data = response.json()

                if data.get("valid"):
                    print(f"\n📞 Phone Number Lookup Result:")
                    print(f"   📌 Number: {data.get('international_format', phone_number)}")
                    print(f"   📌 Carrier: {data.get('carrier', 'Unknown')} - Location: {data.get('location', 'Unknown')}")
                    print(f"   📌 Country: {data.get('country_name', 'Unknown')} ({data.get('country_code', 'Unknown')})")
                    print(f"   📌 Line Type: {data.get('line_type', 'Unknown')}")
                else:
                    print(f"[❌] No information found for {phone_number}")
            except requests.exceptions.JSONDecodeError:
                print("❌ Error: API returned invalid JSON data")
        else:
            print(f"❌ Error: API request failed with status {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error: Could not reach the API ({e})")

# -------------------- GeoIP Lookup --------------------
def check_geoip(ip_address):
    url = f"http://ip-api.com/json/{ip_address}?fields=status,country,regionName,city,lat,lon,isp,query"
    
    print("\n🌍 🔍 Checking GeoIP Information...")

    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()

            if data["status"] == "success":
                print(f"\n🌎 GeoIP Lookup Result for {data['query']}:")
                print(f"   📌 Country: {data.get('country', 'Unknown')} ({data.get('regionName', 'Unknown')})")
                print(f"   📌 City: {data.get('city', 'Unknown')}")
                print(f"   📌 Latitude/Longitude: {data.get('lat', 'Unknown')}, {data.get('lon', 'Unknown')}")
                print(f"   📌 ISP: {data.get('isp', 'Unknown')}")
            else:
                print(f"[❌] No information found for {ip_address}")
        else:
            print(f"❌ Error: API request failed with status {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error: Could not reach the API ({e})")

# -------------------- Main OSINT Tool --------------------
def main():
    print("\n🔎 OSINT Finder: People Search, Phone Lookup & GeoIP Tool")
    print("1️⃣  Search by Full Name")
    print("2️⃣  Search Social Media by Username")
    print("3️⃣  Lookup Phone Number Details")
    print("4️⃣  Perform GeoIP Lookup on an IP Address")
    
    choice = input("\nEnter your choice (1/2/3/4): ").strip()

    if choice == "1":
        full_name = input("\nEnter the Full Name (First Last): ").strip()
        check_full_name(full_name)

    elif choice == "2":
        username = input("\nEnter the Username: ").strip()
        check_social(username)

    elif choice == "3":
        phone_number = input("\nEnter the Phone Number (without country code, e.g., 4168776497): ").strip()
        country_code = input("\nEnter the Country Code (e.g., US, CA, IN, UK): ").strip().upper()
        check_phone(phone_number, country_code)

    elif choice == "4":
        ip_address = input("\nEnter the IP Address: ").strip()
        check_geoip(ip_address)

    else:
        print("\n❌ Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
