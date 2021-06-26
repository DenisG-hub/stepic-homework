def test_should_see_busket_button(browser):
    assert browser.find_element_by_css_selector("button.btn-add-to-basket")
