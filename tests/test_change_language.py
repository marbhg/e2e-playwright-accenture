import re
from playwright.sync_api import Page, expect
import utils

def test_change_language_chinese(page:Page):

  #Abrir la URL de la pagina
  print("Given the user visit home page Accenture")
  page.goto("https://www.accenture.com/es-es/about/contact-us") 

  print("When the user accept the cookies")
  page.get_by_role("button", name="Aceptar todas las cookies").click()
  if(utils.is_mobile(page)):
    print("When the user click on menu")
    page.get_by_label("menu", exact=True).click()
  
  print("When the user enters the language change link")
  page.get_by_role("button", name="Country and language selector").click()
  print("And the user changes the language to Chinese")
  page.get_by_role("menuitem", name="China/Mainland (Chinese)").click()
  expect(page).to_have_url(re.compile(".*cn-zh*."))


def test_change_language_french(page:Page):
  print("Given the user visit home page Accenture")
  page.goto("https://www.accenture.com/es-es/about/contact-us") 

  print("When the user accept the cookies")
  page.get_by_role("button", name="Aceptar todas las cookies").click()
  if(utils.is_mobile(page)):
    print("When the user click on menu")
    page.get_by_label("menu", exact=True).click()

  print("When the user the language link and change it to Canada")
  page.get_by_role("button", name="Country and language selector").click()
  page.get_by_role("menuitem", name="France (French)").click()
  expect(page).to_have_url(re.compile(".*fr-fr*."))




  
