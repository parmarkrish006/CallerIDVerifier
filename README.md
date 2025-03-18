📞 CallerID - Python Project

CallerID is a Python-based tool that validates and retrieves details about phone numbers, including country, carrier, and line type.

✨ Features

1. Phone Number Validation – Check if a phone number is valid or not.
2. Detailed Information – Get country name, carrier, and line type.
3. Supports International Numbers – Works with numbers worldwide.
4. Lightweight & Fast – Efficient API-based lookup.

🖥️ Example Output

When you input a number, the program returns details in JSON format: (here the number was 919999999999 and it wasnt a working number so it showed false in "valid:")

{
  "valid": false,
  "number": "91919999999999",
  "local_format": "",
  "international_format": "",
  "country_prefix": "+91",
  "country_code": "IN",
  "country_name": "India",
  "location": "",
  "carrier": "",
  "line_type": null
}

🚀 Installation

🔹 Prerequisites

Ensure you have Python installed (3.7+ recommended). Install dependencies:

pip install requests

🔹 Running the Program

Clone the repository and navigate to the project folder:

git clone https://github.com/parmarkrish006/CallerIDVerifier.git

cd CallerIDVerifier

Run the script:

python callerid.py

⚙️ How It Works

The script takes a phone number as input.

It sends a request to a number validation API.

The API returns information about the number.

The program displays the details in JSON format.

🔧 Configuration

If using an API, update the API key in the script:

API_KEY = "your_api_key_here"

I have already used a free API called as numverify you can use different website APIs


