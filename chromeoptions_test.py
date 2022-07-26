from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import  Service as ChromeService

def test_one():
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_argument("--start-maximized")
    chrome_option.add_argument("headless")
    chrome_option.add_argument("--ignore-certificate-errros")
    driver= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=chrome_option)
    driver.get("http://google.com")
    print(driver.title)



