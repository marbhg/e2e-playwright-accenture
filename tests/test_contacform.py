from playwright.sync_api import Page, expect
 
#Arir la URL de la pagina
def test_visit_contactfomr(page:Page):

#Abrir la URL de la pagina 
  print("Given the user visit home page Accenture")
  page.goto("https://www.accenture.com/es-es/about/contact-us")

  #Acepta las Cookies
  print("When the user accept the cookies")
  page.get_by_role("button", name="Aceptar todas las Cookies.").click()

  print("When The user accesses the Jobseeker link")
  page.get_by_role("button", name="Jobseeker ").click()

  print("When the user fills in the name field")
  page.get_by_role("textbox", name="* First Name").clear()
  page.get_by_role("textbox", name="* First Name").fill("Maria")

  print("When the user fills in the last name field")
  page.get_by_role("textbox", name="* Last Name").clear()
  page.get_by_role("textbox", name="* Last Name").fill("Lopez")

  print("When the user selects the city Aruba")
  page.get_by_role("combobox", name="* Country/Region required").click()
  page.get_by_role("option", name="Aruba").click()

  print("When the user fills out the section How can we help you?")
  page.get_by_role("textbox", name="* How can we help you?").click()
  page.get_by_role("textbox", name="* How can we help you?").fill("Quiero informacion acerca de sus tecnologias")

  print("When the user accepts the privacy required")
  page.get_by_role("group", name="* Privacy required").locator("span").nth(3).click()

  print("When the user clicks the send button the from should display an error message")
  page.get_by_role("button", name="ENVIAR").click()
  expect(page.get_by_text("Email field is required and")).to_be_visible()




 

 



