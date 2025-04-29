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
  page.get_by_role("link", name="Automation").click()
  expect(page).to_have_url("automation")

  page.goto("https://www.accenture.com/es-es")
  print("When the user click on Quienes somos")
  page.get_by_role("button", name="Quiénes somos").click()
  expect(page).to_have_url("Quienes somos")
  print("When the user click on Sustainability, the expected page opens")
  page.locator("#globalnav-primarynavlinks-item1-5588bc7152").get_by_role("list").filter(has_text="Quiénes somos Equipo").get_by_label("Sostenibilidad").click()
  

  print("When the user click on the Offer Finder")
  page.get_by_role("button", name="Incorpórate").click()
  expect(page).to_have_url("Incorporate")
  print("When the user enters the offer search link and directs me to the corresponding page")
  page.get_by_role("link", name="Buscador de ofertas").click()
  page.goto("https://www.accenture.com/es-es/careers/jobsearch?jk=&vw=0&is_rj=0&pg=1")

  