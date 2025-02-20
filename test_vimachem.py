from playwright.sync_api import Page
import pytest

def test_signup(page: Page):
     page.goto("https://thinking-tester-contact-list.herokuapp.com/addUser")
     page.fill("input[id='firstName']", "Katerina")
     page.fill("input[id='lastName']", "Papadopoulou")
     page.fill("input[id='email']", "test67abe14@gmail.com")
     page.fill("input[id='password']", "Test@1234")
     page.click("button[id='submit']")
     

def test_signin_addNewContact_validate(page: Page):
     # Login
     page.goto("https://thinking-tester-contact-list.herokuapp.com/login")
     page.fill("input[id='email']", "test67abe14@gmail.com")
     page.fill("input[id='password']", "Test@1234")
     page.click("button[id='submit']")
     

     # Add contact
     page.get_by_role("button", name="Add a New Contact").click()
     page.fill("input[id='firstName']", "Maria")
     page.fill("input[id='lastName']", "Papadopoulou")
     page.click("button[id='submit']")

     # Validate contact creation
     assert page.locator("text=Maria Papadopoulou").is_visible

def test_invalidDate_validateError(page: Page):
     # Login
     page.goto("https://thinking-tester-contact-list.herokuapp.com/login")
     page.fill("input[id='email']", "test67abe14@gmail.com")
     page.fill("input[id='password']", "Test@1234")
     page.click("button[id='submit']")

     # Add invalid birthdate in contact creation
     page.get_by_role("button", name="Add a New Contact").click()
     page.fill("input[id='firstName']", "John")
     page.fill("input[id='lastName']", "Doe")
     page.get_by_role("textbox", name="Date of Birth:").fill("1961-19-08")
     page.click("button[id='submit']")

     # Validate error message
     assert page.locator("text=Contact validation failed: birthdate: Birthdate is invalid").is_visible

def test_deleteContact(page: Page):
     # Login
     page.goto("https://thinking-tester-contact-list.herokuapp.com/login")
     page.fill("input[id='email']", "test67abe14@gmail.com")
     page.fill("input[id='password']", "Test@1234")
     page.click("button[id='submit']") 

     # Delete Contact
     page.click("text=Maria Papadopoulou")
     page.once("dialog", lambda dialog: dialog.accept())
     page.click("button[id='delete']")
     page.click("button:has-text('Ok')")

     # Validate contact deletion
     assert not page.locator("text=Maria Papadopoulou").is_visible

    

