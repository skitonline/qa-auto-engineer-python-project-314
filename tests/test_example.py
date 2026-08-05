def test_open_main_page(browser):
    browser.get("https://example.com")
    assert "Example Domain" in browser.title