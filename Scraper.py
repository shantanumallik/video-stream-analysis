import csv
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# Configure WebDriver (example with Chrome)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

# Function to extract data from 'Stats for Nerds'
def extract_stats(driver):
    # Dictionary to hold the extracted data
    stats = {}

    # Define the labels of interest
    labels_of_interest = {
        "Connection Speed": "Connection Speed",
        "Network Activity": "Network Activity",
        "Buffer Health": "Buffer Health",
        "Current / Optimal Res": "Current / Optimal Res"
    }

    # Extract data for each label
    for label in labels_of_interest.values():
        try:
            label_element = driver.find_element(By.XPATH, f"//*[contains(text(), '{label}')]")
            if label_element:
                value_element = label_element.find_element(By.XPATH, "./following-sibling::span")
                if value_element:
                    value = value_element.text
                    if label == "Current / Optimal Res":
                        value = value.split(' / ')[0]
                    stats[label] = value
        except Exception as e:
            # Handle exception if element not found
            print(e)

    return stats

# CSV file setup
csv_file = open('youtube_stats_360p.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['timestamp', 'speed', 'network_activity', 'buffer_health', 'resolution'])

try:
    # Navigate to the YouTube video
    video_url = 'https://www.youtube.com/watch?v=P3-7b05uSkg'
    driver.get(video_url)

    # Wait for the video to load
    time.sleep(5)

    # Access 'Stats for Nerds' by right-clicking on the video and selecting the option
    video_element = driver.find_element(By.TAG_NAME, 'video')
    actions = ActionChains(driver)
    actions.context_click(video_element).perform()
    # You may need to add more actions to navigate the context menu and click 'Stats for Nerds'

    # Continuously scrape and write data to CSV
    for _ in range(999999999999999999999):  # Scrape 10 times as an example
        stats = extract_stats(driver)
        stats['Timestamp'] = time.strftime("%Y-%m-%d %H:%M:%S")
        csv_writer.writerow([stats.get('Timestamp'), stats.get('Connection Speed'), stats.get('Network Activity'), stats.get('Buffer Health'), stats.get('Current / Optimal Res')])
        time.sleep(1)  # Wait 1 second between each scrape

finally:
    csv_file.close()
    driver.quit()
