# Guardian-API-Extractor
This script retrieves news articles related to Nigeria from The Guardian API, processes the data, and saves it to a CSV file
The Guardian API News Extractor
## Overview
This script retrieves news articles related to Nigeria from The Guardian API, processes the data, and saves it to a CSV file. The extracted information includes:

* Article type

* Section ID

* Publication date

* Web title

## Prerequisites
* Python 3.x

### Required Python libraries:

* requests

* pandas

## Installation
Clone this repository:
git clone https://github.com/yourusername/guardian-api-extractor.git

## Navigate into the project directory:
* cd guardian-api-extractor

## Install dependencies:
pip install -r requirements.txt
## Usage
* Update the API_KEY in the script with your Guardian API key.
* Modify the from_date and to_date variables if needed.

## Run the script:
python guardian_api_script.py
* The extracted data will be saved as a CSV file at the specified path.

## Output
A CSV file named The_GuardianFileUpdated.csv will be generated, containing the extracted article details.

## Troubleshooting
* Ensure your API key is valid.
* Confirm that the output directory exists.
* If the script fails, check for API request limits or network issues.

## License
This project is open-source and available under the MIT License.
