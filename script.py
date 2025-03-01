import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import csv
from datetime import datetime


def scrape_property_details(driver, url):
    try:
        print(f"\nNavigating to URL: {url}")
        driver.get(url)

        bolge = url.split('?')[0].split('/')[-1].split('-')[-1].capitalize()

        wait = WebDriverWait(driver, 10)

        property_rows = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "searchResultsItem")))
        results = []

        for row in property_rows:
            property_details = {}
            
            try:
                property_details['Bölge'] = bolge  

                brut = row.find_element(By.CSS_SELECTOR, "td.searchResultsAttributeValue").text.strip()
                property_details['m² (Brüt)'] = brut

                oda = row.find_elements(By.CSS_SELECTOR, "td.searchResultsAttributeValue")[1].text.strip()
                property_details['Oda Sayısı'] = oda

                fiyat = row.find_element(By.CSS_SELECTOR, "td.searchResultsPriceValue span").text.strip()
                property_details['Fiyat'] = fiyat

                mahalle = row.find_element(By.CSS_SELECTOR, "td.searchResultsLocationValue").text.strip()
                property_details['Mahalle'] = mahalle
                
                results.append(property_details)
                
            except Exception as e:
                print(f"Error extracting property details: {str(e)}")
                continue
                
        return results
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return None


def scrape_multiple_properties(urls):
    results = []
    driver = None
    
    try:
        options = uc.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--window-size=1920,1080')
        
        driver = uc.Chrome(options=options)

        for url in urls:
            try:
                result = scrape_property_details(driver, url)
                if result:
                    results.extend(result)
                time.sleep(10)
            except Exception as e:
                print(f"Error processing {url}: {str(e)}")
                continue
                
    except Exception as e:
        print(f"Error occurred: {str(e)}")
    finally:
        if driver:
            try:
                driver.close()
                driver.quit()
            except:
                pass
    
    return results

def save_to_csv(results):
    if not results:
        print("No results to save")
        return

    timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")
    filename = f"property_details_{timestamp}.csv"

    fieldnames = [
        'Bölge',
        'm² (Brüt)',
        'Oda Sayısı',
        'Fiyat',
        'Mahalle'
    ]

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(fieldnames)
        
        for result in results:
            row = [
                result.get('Bölge', ''),
                result.get('m² (Brüt)', ''),
                result.get('Oda Sayısı', ''),
                result.get('Fiyat', ''),
                result.get('Mahalle', '')
            ]
            writer.writerow(row)
    
    print(f"\nResults saved to {filename}")

if __name__ == "__main__":
    print("Starting the scraper...")

    urls = [
            "https://www.sahibinden.com/satilik-daire/istanbul-adalar?pagingSize=50",  
            "https://www.sahibinden.com/satilik-daire/istanbul-arnavutkoy?pagingSize=50",  
            "https://www.sahibinden.com/satilik-daire/istanbul-atasehir?pagingSize=50",    
            "https://www.sahibinden.com/satilik-daire/istanbul-avcilar?pagingSize=50",  
            "https://www.sahibinden.com/satilik-daire/istanbul-bagcilar?pagingSize=50",  
            "https://www.sahibinden.com/satilik-daire/istanbul-bahcelievler?pagingSize=50",  
            "https://www.sahibinden.com/satilik-daire/istanbul-bakirkoy?pagingSize=50",  
            "https://www.sahibinden.com/satilik-daire/istanbul-basaksehir?pagingSize=50",  
            "https://www.sahibinden.com/satilik-daire/istanbul-bayrampasa?pagingSize=50",  
            "https://www.sahibinden.com/satilik-daire/istanbul-besiktas?pagingSize=50",  
            "https://www.sahibinden.com/satilik-daire/istanbul-beykoz?pagingSize=50",  
            "https://www.sahibinden.com/satilik-daire/istanbul-beylikduzu?pagingSize=50",  
            "https://www.sahibinden.com/satilik-daire/istanbul-beyoglu?pagingSize=50",  
            "https://www.sahibinden.com/satilik-daire/istanbul-buyukcekmece?pagingSize=50",  
            "https://www.sahibinden.com/satilik-daire/istanbul-catalca?pagingSize=50",  
            "https://www.sahibinden.com/satilik-daire/istanbul-cekmekoy?pagingSize=50",  
            "https://www.sahibinden.com/satilik-daire/istanbul-esenler?pagingSize=50",  
            "https://www.sahibinden.com/satilik-daire/istanbul-esenyurt?pagingSize=50",  
            "https://www.sahibinden.com/satilik-daire/istanbul-eyupsultan?pagingSize=50",  
            "https://www.sahibinden.com/satilik-daire/istanbul-fatih?pagingSize=50",  
            "https://www.sahibinden.com/satilik-daire/istanbul-gaziosmanpasa?pagingSize=50",  
            "https://www.sahibinden.com/satilik-daire/istanbul-gungoren?pagingSize=50",  
            "https://www.sahibinden.com/satilik-daire/istanbul-kadikoy?pagingSize=50",  
            "https://www.sahibinden.com/satilik-daire/istanbul-kagithane?pagingSize=50",  
            "https://www.sahibinden.com/satilik-daire/istanbul-kartal?pagingSize=50",  
            "https://www.sahibinden.com/satilik-daire/istanbul-kucukcekmece?pagingSize=50",  
            "https://www.sahibinden.com/satilik-daire/istanbul-maltepe?pagingSize=50",  
            "https://www.sahibinden.com/satilik-daire/istanbul-pendik?pagingSize=50",  
            "https://www.sahibinden.com/satilik-daire/istanbul-sancaktepe?pagingSize=50",  
            "https://www.sahibinden.com/satilik-daire/istanbul-sariyer?pagingSize=50",  
            "https://www.sahibinden.com/satilik-daire/istanbul-silivri?pagingSize=50",  
            "https://www.sahibinden.com/satilik-daire/istanbul-sultanbeyli?pagingSize=50",  
            "https://www.sahibinden.com/satilik-daire/istanbul-sultangazi?pagingSize=50",  
            "https://www.sahibinden.com/satilik-daire/istanbul-sile?pagingSize=50",  
            "https://www.sahibinden.com/satilik-daire/istanbul-sisli?pagingSize=50",  
            "https://www.sahibinden.com/satilik-daire/istanbul-tuzla?pagingSize=50",  
            "https://www.sahibinden.com/satilik-daire/istanbul-umraniye?pagingSize=50",  
            "https://www.sahibinden.com/satilik-daire/istanbul-uskudar?pagingSize=50",  
            "https://www.sahibinden.com/satilik-daire/istanbul-zeytinburnu?pagingSize=50", 
    ]

    results = scrape_multiple_properties(urls)
    

    if results:
        print("\nExtracted Property Details:")
        for result in results:
            print("\nProperty:")
            for key, value in result.items():
                print(f"{key}: {value}")
            print("-" * 50)

    save_to_csv(results)
