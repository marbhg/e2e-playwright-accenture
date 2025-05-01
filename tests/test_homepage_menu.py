from playwright.sync_api import Page, expect
import utils
import re

def test_visit_menu_links(page:Page):
  #Abrir la URL de la pagina
  print("Given the user visit home page Accenture")
  page.goto("https://www.accenture.com/es-es")

 #Localizamos el elemento por texto
  print("When the user aceppt the cookies")
  page.get_by_role("button", name="Aceptar todas las Cookies.").click()
  #Comprobamos el ancho de la pantalla
  if(utils.is_mobile(page)):
    print("When the user click on menu")
    page.get_by_label("menu", exact=True).click()
    page.get_by_role("button", name="Servicios", exact=True).click()

  print("When the user click on services")
  page.get_by_role("button", name="Servicios").last.click()
  print("When the user click on automation, the expected page opens")
  page.get_by_role("link", name="Automation").click()
  expect(page).to_have_url(re.compile(".*automation.*"))

  page.goto("https://www.accenture.com/es-es")
  print("When the user click on Quienes somos")
  if(utils.is_mobile(page)):
    print("When the user click on menu")
    page.get_by_label("menu", exact=True).click()
    page.get_by_role("button", name="Quiénes somos", exact=True).click()
  page.get_by_role("button", name="Quiénes somos").last.click()

  print("When the user click on Sustainability, the expected page opens")
  page.locator("#globalnav-primarynavlinks-item1-5588bc7152").get_by_role("list").filter(has_text="Quiénes somos Equipo").get_by_label("Sostenibilidad").click()
  expect(page).to_have_url(re.compile(".*sustainability.*"))

  page.goto("https://www.accenture.com/es-es")
  print("When the user click on the Offer Finder")
  if(utils.is_mobile(page)):
    print("When the user click on menu")
    page.get_by_label("menu", exact=True).click()
    page.get_by_role("button", name="Incorpórate").click()

  if(utils.is_mobile(page)):
    page.get_by_role("button", name="Únete a nuestro equipo").click()
    

  