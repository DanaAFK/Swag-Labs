class LoginLocators:
    USERNAME_INPUT = 'xpath=//*[@id="user-name"]'
    PASSWORD_INPUT = 'xpath=//*[@id="password"]'
    LOGIN_BUTTON = 'xpath=//*[@id="login-button"]'
    INVENTORY_CONTAINER = '[data-test="inventory-container"]'
    INVALID_USERNAME = "invalid_user"
    INVALID_PASSWORD = "invalid_pass"
    ERROR_MESSAGE_TEXT = "Epic sadface: Username and password do not match any user in this service"
    ERROR_MESSAGE = "xpath=//*[@id='login_button_container']/div/form/div[3]"