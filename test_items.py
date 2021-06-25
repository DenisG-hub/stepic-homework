link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_switch_driver_lang(browser):
    browser.get(link)
    assert browser.find_element_by_xpath("//button[@value='Añadir al carrito']")
