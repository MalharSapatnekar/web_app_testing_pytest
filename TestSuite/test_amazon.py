import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def driver():
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.metadata(requirement='REQ_21', testcase_id='TP005_TC001')
def test_amazon_title(driver):
    # Open Amazon.com
    driver.get("https://www.amazon.com")
    assert "Amazon.com" in driver.title

@pytest.mark.metadata(requirement='REQ_22', testcase_id='TP005_TC002')
def test_search_product(driver):
    # Open Amazon.com
    driver.get("https://www.amazon.com")

    # Find the search bar and enter a query
    search_box = driver.find_element_by_id("twotabsearchtextbox")
    search_box.send_keys("laptop")
    search_box.send_keys(Keys.RETURN)

    # Check if search results are displayed
    assert "laptop" in driver.page_source.lower()

@pytest.mark.metadata(requirement='REQ_23', testcase_id='TP005_TC003')
def test_add_to_cart(driver):
    # Open Amazon.com
    driver.get("https://www.amazon.com")

    # Find the search bar and enter a query
    search_box = driver.find_element_by_id("twotabsearchtextbox")
    search_box.send_keys("headphones")
    search_box.send_keys(Keys.RETURN)

    # Click on the first product
    product_link = driver.find_element_by_css_selector(".s-result-list .s-result-item a")
    product_link.click()

    # Find the 'Add to Cart' button and click it
    add_to_cart_button = driver.find_element_by_id("add-to-cart-button")
    add_to_cart_button.click()

    # Check if the cart count has increased
    cart_count = driver.find_element_by_id("nav-cart-count")
    assert cart_count.text == "1"
