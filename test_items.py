link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    assert browser.find_element_by_xpath("//button[@value='Añadir al carrito']")
