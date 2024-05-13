from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


desired_caps={
    "platformName":"Android",
    "deviceName": "2850bf41",
    "automationName":"uiautomator2",
    "appPackage":"com.safaricom.mpesa.lifestyle",
    "appActivity":"com.mpesa.splash.SplashActivity",
    "autoGrantPermissions":"true",
    # "skipDeviceInitialization":"true",
    # "skipServerInstallation":"true",
    "noReset":"true",
    "fullReset":"false",
    "newCommandTimeout":3600,
    "sessionId":None
    }
driver = webdriver.Remote(command_executor="http://localhost:4723",options=UiAutomator2Options().load_capabilities(caps=desired_caps))
driver.implicitly_wait(30)

#Enter m-pesa pin
driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id='com.safaricom.mpesa.lifestyle:id/' and @text='6']").click()
driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id='com.safaricom.mpesa.lifestyle:id/' and @text='5']").click()
driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id='com.safaricom.mpesa.lifestyle:id/' and @text='4']").click()
driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id='com.safaricom.mpesa.lifestyle:id/' and @text='4']").click()

#User clicks on the services section
driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id='com.safaricom.mpesa.lifestyle:id/' and @text='SERVICES']").click()

#User clicks on the search button
driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.ImageView[@resource-id='com.safaricom.mpesa.lifestyle:id/'])[1]").click()

#User enters the name of the app on the search button
driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@resource-id='com.safaricom.mpesa.lifestyle:id/']").send_keys("MDAKTARI")

#User navigates to the MINIAPP
driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id='com.safaricom.mpesa.lifestyle:id/title']").click()