import time
from selenium.webdriver import ActionChains, Keys

from selenium.webdriver.common.by import By



from pages import *

def test_explore_all_integrations(driver):
    home = HomePage(driver)

    # Step 1–3: Navigate & wait
    home.open()
    home.wait_for_dom_loaded()
    explore_element = home.scroll_to_explore_link()

    # Step 4: Right-click and open in new tab
    actions = ActionChains(driver)
    actions.context_click(explore_element).perform()
    # Workaround: Open link in new tab via CONTROL + click (or COMMAND on Mac)
    actions.key_down(Keys.CONTROL).click(explore_element).key_up(Keys.CONTROL).perform()

    time.sleep(3)

    # Step 5: Get window handles
    handles = driver.window_handles
    print(f"\nWindow handles: {handles}")
    assert len(handles) == 2, "Expected two browser windows to be open"

    # Step 6: Switch to new tab and verify URL
    driver.switch_to.window(handles[1])
    current_url = driver.current_url
    expected_url = "https://www.lambdatest.com/integrations"
    assert expected_url in current_url, f"URL mismatch! Got: {current_url}"

    # Step 7: Close current tab
    driver.close()
    # Optionally switch back to original tab
    driver.switch_to.window(handles[0])
