from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.safari.webdriver import WebDriver as SafariWebDriver

def home_view(request):

    return render(request, "portfolio/home.html", {})
"""
def get_div_content(url, div_id):

    driver = SafariWebDriver()

    try:
        driver.get(url)
        div_content = driver.find_element(By.ID, div_id).get_attribute('outerHTML')

        return div_content
    finally:
        driver.quit()
"""