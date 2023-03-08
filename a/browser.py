from selenium_profiles.utils.installer import install_chromedriver
from selenium_profiles.driver import driver as mydriver
from selenium_profiles.profiles import profiles
from selenium.webdriver.common.by import By
from selenium_profiles.utils.colab_utils import display, showscreen, show_html 
class Brows():
  def startup(self):
    install_chromedriver()
    self.mydriver = mydriver()
    self.display = display()
    self.display.start_display()
    self.driver = self.mydriver.start(profiles.Windows(), uc_driver=False)  # or .Android    
  def access(self,url):
    self.driver.get(url)
    showscreen(self.driver)
  def exit(self):
    self.driver.quit()
    self.display.stop_display()
  def search_ongoogle(self,word):
    self.access(f'https://google.com/search?q={word}')
