
from playwright.sync_api import Page, expect

def test_changelanguage_chinesse(page:Page): 

  #Abrir la URL de la pagina
  print("Given the user visit home page Accenture")
  page.goto("https://www.accenture.com/es-es/about/contact-us") 

  print("When the user accept the cookies")
  page.get_by_role("button", name="Aceptar todas las Cookies.").click()
  
  print("When the user enters the language change link")
  page.get_by_role("button", name="Country and language selector").click()

  print("And the user changes the language to Chinese")
  page.get_by_role("menuitem", name="China/Mainland (Chinese)").click()



  