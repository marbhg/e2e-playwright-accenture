from playwright.sync_api import Page, expect

def test_visit_menu_links(page:Page):
  #Abrir la URL de la pagina
  print("Given the user visit home page Accenture")
  page.goto("https://www.accenture.com/es-es")

  print("When the user aceppt the cookies")
  #Localizamos el elemento por texto
  page.get_by_text("Aceptar todas las Cookies").click()

  





