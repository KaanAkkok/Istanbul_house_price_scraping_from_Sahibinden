# Property Scraper for Sahibinden.com

A Python script that scrapes property listings from Sahibinden.com for all districts of Istanbul.

## Features
- Scrapes property details including:
  - District (Bölge)
  - Size (m² Brüt)
  - Number of Rooms (Oda Sayısı)
  - Price (Fiyat)
  - Neighborhood (Mahalle)
- Automatically handles multiple districts
- Saves results to a CSV file with timestamp
- Includes built-in delays to respect the website's rate limits

## Requirements
python
pip install undetected-chromedriver selenium

## Usage
1.Run the script:
python
python script.py

2. The script will:
   - Open a Chrome browser
   - Scrape property listings from all Istanbul districts
   - Save results to a CSV file named `property_details_YYYYMMDD_HHMMSS.csv`

## Output
The script generates a CSV file with semicolon (;) delimiter containing the following columns:
- Bölge (District)
- m² (Brüt) (Gross Area)
- Oda Sayısı (Number of Rooms)
- Fiyat (Price)
- Mahalle (Neighborhood)

## Note
- The script includes a 10-second delay between requests to avoid overwhelming the server
- Make sure you have Chrome browser installed on your system
- The script uses undetected-chromedriver to bypass potential anti-bot measures
