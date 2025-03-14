from playwright.sync_api import Page, expect

def test_visit_menu_links(page:Page):
  #Abrir la URL de la pagina
  print("Given the user visit home page Accenture")
  page.goto("https://www.accenture.com/es-es")

  print("When the user aceppt the cookies")
  #Localizamos el elemento por texto
  page.get_by_text("Aceptar todas las Cookies").click()

  #Localizamos el elemento del enlace Servicio
  print("When Visit the service link")
  page.get_by_role("button", name="Servicios").click()

  #Accedemos al elemento dentro del enlace Servicio
  print("When Access the automation link")
  page.get_by_role("menuitem", name="Automation").click()

  #Acccedemos al enlace de quienes somos y entramos al apartado de Sostenibilidad
  print("When Visit the Who We Are link and access the Sustainability section")
  page.get_by_role("button", name="Quiénes Somos").click()
  page.locator("#linklistteaser-a707da989f").get_by_role("menuitem", name="Sostenibilidad").click()
  expect(page.get_by_role("link", name="Sostenibilidad", exact=True)).to_be_visible()

  #Accedemos al apartado de incorporate y accedemos al enlace de oferta
  print("When Visit the Join link and enter the Offer Finder link")
  page.get_by_role("button", name="Incorpórate").click()
  page.get_by_role("menuitem", name="Buscador de ofertas").click()


  





