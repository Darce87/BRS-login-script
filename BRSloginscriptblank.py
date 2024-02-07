from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Set the login credentials
username = ""
password = ""

# Set the login URL
login_url = "https://members.brsgolf.com/---/login"
logged_in_url = "https://members.brsgolf.com/---"

# Create a Chrome webdriver
driver = webdriver.Chrome()

# Navigate to the login page
driver.get(login_url)

# Find the username and password fields, and submit the form
username_field = driver.find_element(By.ID, 'login_form_username')
password_field = driver.find_element(By.ID, 'login_form_password')

username_field.send_keys(username)
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)

# Wait for a few seconds to ensure the login process is complete
time.sleep(5)

# Print the current URL for debugging
print("Current URL:", driver.current_url)

# Check if the redirection to the logged-in page was successful
if logged_in_url in driver.current_url:
    print("Successfully logged in!")
else:
    print("Login failed. Please check your credentials.")

# Keep the browser window open
# driver.quit()
