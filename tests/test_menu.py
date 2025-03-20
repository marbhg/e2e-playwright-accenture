from playwright.sync_api import Page, expect
import utils

def test_visit_menu_links(page:Page):
  #Abrir la URL de la pagina
  print("Given the user visit home page Accenture")
  page.goto("https://www.accenture.com/es-es")

  #Localizamos el elemento por texto
  print("When the user aceppt the cookies")
  page.get_by_role("button", name="Aceptar todas las Cookies.").click()

  print("When the user click on services")
  page.get_by_role("button", name="Servicios").click()
  print("When the user click on automation, the expected page opens")
  page.get_by_role("menuitem", name="Automation").click()
  page.goto("https://www.accenture.com/es-es/services/intelligent-automation-index")

  print("When the user click on Quienes somos")
  page.get_by_role("button", name="Quiénes somos").click()
  print("When the user click on Sustainability, the expected page opens")
  page.get_by_role("menu", name="Quiénes somos").get_by_label("Sostenibilidad").click()
  page.goto("https://www.accenture.com/es-es/about/sustainability/sustainability-value-promise")

  print("When the user click on the Offer Finder")
  page.get_by_role("button", name="Incorpórate").click()
  print("When the user enters the offer search link and directs me to the corresponding page")
  page.get_by_role("menuitem", name="Buscador de ofertas").click()
  page.goto("https://www.accenture.com/es-es/careers/jobsearch?jk=&sb=1&vw=0&is_rj=0&pg=1")

  print("When you enter the language link and change it to Chinese")
  page.get_by_role("button", name="Country and language selector").click()
  page.get_by_role("menuitem", name="China/Mainland (English)").click()
  print("When the user must view the page in Chinese")
  page.goto("https://www.accenture.com/cn-en")

  print("When the user the language link and change it to Canada")
  page.get_by_role("button", name="Country and language selector").click()
  page.get_by_role("menuitem", name="Canada (French)").click()
  print("When the user must view the page in Canada")
  page.goto("https://www.accenture.com/ca-en")

  print("When you enter the language link and change Australian")
  page.get_by_role("button", name="Country and language selector").click()
  page.get_by_role("menuitem", name="Australia (English)").click()
  print("When the user must view the page in Australian")
  page.goto("https://www.accenture.com/au-en")
  


  



