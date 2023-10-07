# Importing required libraries

# pip install selenium

from selenium import webdriver
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Open the GitHub homepage
driver.get("https://github.com")
time.sleep(3)

# Navigate to the "Sign in" link
sign_in_link = driver.find_element("xpath", "/html/body/div[1]/div[1]/header/div/div[2]/div/div/div/a")
sign_in_link.click()
time.sleep(2)

# Enter GitHub username
username_field = driver.find_element("id", "login_field")
username_field.send_keys("varushivi106@gmail.com")
time.sleep(2)

# Enter GitHub password
password_field = driver.find_element("id", "password")
password_field.send_keys("Shivi@123@@")
time.sleep(2)

# Click the "Sign in" button
login_button = driver.find_element("xpath", "/html/body/div[1]/div[3]/main/div/div[4]/form/div/input[13]")
login_button.click()
time.sleep(3)

# # Click the user menu to open the dropdown
user_menu = driver.find_element("xpath", "/html/body/div[1]/div[1]/header/div/div[2]/div[3]/deferred-side-panel")
user_menu.click()
time.sleep(2)

# Hover on the "Sign out" button

hover_sign_out_button = driver.find_element("xpath",
                                            "/html/body/div[1]/div[1]/header/div/div[2]/div["
                                            "3]/deferred-side-panel/user-drawer-side-panel/div/modal-dialog/div["
                                            "2]/nav/nav-list/ul/li[22]")
hover_sign_out_button.click()
time.sleep(3)

# CLick the "Sign out" button
sign_out_button = driver.find_element("xpath", "/html/body/div[1]/div[6]/main/div/form/input[2]")
sign_out_button.click()
time.sleep(2)

# Closing the webdriver
driver.close()
