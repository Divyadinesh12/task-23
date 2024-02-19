"""
using python selenium automation and action chains do a drag and drop operation of the white rectangular box into the yellow rectangular box
"""



#Common
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep


# ActionChain
from selenium.webdriver import ActionChains




class DragAndDrop:


   def __init__(self, url):
       self.url = url
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
       self.action = ActionChains(self.driver)


   def boot(self):
       """
       This method open the url and maximize window
       """
       self.driver.get(self.url)
       self.driver.maximize_window()
       self.wait(5)


   def wait(self, secs):
       """
       This method stop the script at the given seconds
       :param secs:
       """
       sleep(secs)


   def findElementById(self, id):
       """
       This method find the element using its unique id
       :param id:
       :return: None
       """
       return self.driver.find_element(by=By.ID, value=id)

   def switchToIframe(self):
       """
       Switch to the iframe containing the draggable elements
       """
       iframe=self.driver.find_element(by=By.TAG_NAME, value="iframe")
       self.driver.switch_to.frame(iframe)


   def dragAndDrop(self):
       """
       This method locate the draggable and droppable elements and perform dra-and-drop operation using ActionChains
       :return:None
       """
       try:
           draggable_element = self.findElementById("draggable")
           droppable_element = self.findElementById("droppable")
           self.action.drag_and_drop(draggable_element,droppable_element).perform()
           self.wait(5)
           dropText = self.driver.find_element(by=By.XPATH, value="/html/body/div[2]/p").text
           if dropText == "Dropped!":
               print("Success: We dragged the element and dropped it in its place")
           else:
               print("Error: The action was not performed")
        # switch back to the default content
           self.driver.switch_to.default_content()


       except NoSuchElementException as e:
           #if element can not find from webpage then this block of code execute
           print("Element can not find from the webpage",e)

   def close(self):
       """
       This method close the browser
       :return:None
       """
       self.driver.quit()




url = "https://jqueryui.com/droppable/"
obj = DragAndDrop(url)
obj.boot()
obj.switchToIframe()
obj.dragAndDrop()

