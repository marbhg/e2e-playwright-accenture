from playwright.sync_api import Page, expect
 
#Arir la URL de la pagina
def test_contac_form_invalid_email(page:Page):

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


  def Fill_out_the_form_with_the_email_section_empty(page:Page):
    print("Given the user visit home page Accenture")
    page.goto("https://www.accenture.com/es-es")

    print("When the user accept the cookies")
    page.get_by_role("button", name="Aceptar todas las Cookies.").click()

    print("When I enter the form section")
    page.get_by_role("link", name="Contacto").click()
    page.get_by_role("button", name="Jobseeker ").click()
    
    print("When I fill out all the fields")
    page.get_by_role("textbox", name="* First Name").click()
    page.get_by_role("textbox", name="* First Name").fill("Maria")
    page.get_by_role("textbox", name="* First Name").press("Tab")
    page.get_by_role("textbox", name="* Last Name").press("CapsLock")
    page.get_by_role("textbox", name="* Last Name").fill("Lopez")
    page.get_by_role("textbox", name="* Last Name").press("Tab")
    page.get_by_role("textbox", name="* E-mail Address").press("Tab")
    page.get_by_role("combobox").click()
    page.get_by_role("option", name="Andorra").click()
    page.get_by_role("textbox", name="* How can we help you?").click()
    page.get_by_role("textbox", name="* How can we help you?").fill("kajskhsa")

    print("When I accept the Accenture private statement and accept the Captch") 
    page.get_by_role("group", name="* Privacy required").locator("span").nth(3).click()
    page.locator("iframe[name=\"a-7xrl8zdyng0n\"]").content_frame.get_by_role("checkbox", name="No soy un robot").click()
    page.locator("iframe[name=\"c-7xrl8zdyng0n\"]").content_frame.locator("tr:nth-child(3) > td:nth-child(2)").click()
    page.locator("iframe[name=\"c-7xrl8zdyng0n\"]").content_frame.locator("tr:nth-child(4) > td:nth-child(3)").click()
    page.locator("iframe[name=\"c-7xrl8zdyng0n\"]").content_frame.locator("tr:nth-child(4) > td:nth-child(2)").click()
    page.locator("iframe[name=\"c-7xrl8zdyng0n\"]").content_frame.locator("tr:nth-child(3) > td:nth-child(3)").click()
    page.locator("iframe[name=\"c-7xrl8zdyng0n\"]").content_frame.get_by_role("button", name="Siguiente").click()
    page.locator("iframe[name=\"c-7xrl8zdyng0n\"]").content_frame.locator("tr:nth-child(3) > td:nth-child(2)").click()
    page.locator("iframe[name=\"c-7xrl8zdyng0n\"]").content_frame.locator("tr:nth-child(2) > td:nth-child(4)").click()
    page.locator("iframe[name=\"c-7xrl8zdyng0n\"]").content_frame.locator("tr:nth-child(3) > td:nth-child(3)").click()
    page.locator("iframe[name=\"c-7xrl8zdyng0n\"]").content_frame.locator("tr:nth-child(3) > td:nth-child(4)").click()

    print("And the form should not be submitted and display an error message")
    page.locator("iframe[name=\"c-7xrl8zdyng0n\"]").content_frame.get_by_role("button", name="Verificar").click()
    page.get_by_text("Email field is required and").click()
    expect(page.get_by_text("Email field is required and")).to_be_visible()


    


