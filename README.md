# selenium tutorial


#### Basic Webdriver Methods:

* Creating a Webdriver object for chrome browser

        from selenium import webdriver
        driver = webdriver.Chrome(executable_path='/Users/garepall/Desktop//drivers/chromedriver')
        
* Open URL in new invoked browser

        driver.get('https://gopikrishna-a.github.io/')

* Get webpage title

        driver.title

* Get current webpage URL

        driver.current_url

* Maximize the browser window

        driver.maximize_window()

* Minimize the browser window

        driver.minimize_window()

* Go to previous webpage

    driver.back()

* Refresh the current webpage

        driver.refresh()
 
    or

        driver.get(driver.current_url)

* Close the invoked browser (only current window)

        driver.close()

* Close te invoked browser (all windows)
        driver.quit()


####  Webdriver Locator methods:


Below are methods to find a web element based on the locators in Selenium python bindings

1. find_element_by_id
2. find_element_by_name
3. find_element_by_xpath
4. find_element_by_link_text
5. find_element_by_partial_link_text
6. find_element_by_tag_name
7. find_element_by_class_name
8. find_element_by_css_selector

* ```find_element_by_id```

    - Use this when you know id attribute of an element. With this strategy, the first element with the id attribute value matching the location will be returned. If no element has a matching id attribute, a NoSuchElementException will be raised.

    - Element HTML code
    
            <input type="email" class="inputtext login_form_input_box" name="email" id="email" data-testid="royal_email">
    
    - Python selenium equivalent code to find the above element using element id i.e ```id="email"``` and send the given text
    
            from selenium import webdriver
            import time
            
            driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
            driver.get('https://www.facebook.com/')
            element = driver.find_element_by_id('email') # Find element
            element.send_keys('helloworld') # enter the given text in textbox
            time.sleep(10) # Sleep time to observe
            driver.quit() # Close browser


* ```find_element_by_name```

    - Use this when you know name attribute of an element. With this strategy, the first element with the name attribute value matching the location will be returned. If no element has a matching name attribute, a NoSuchElementException will be raised.

    - Element HTML code
    
            <input type="email" class="inputtext login_form_input_box" name="email" id="email" data-testid="royal_email">

    - Python selenium equivalent code to find the above element using element name i.e ```name="email"``` and send the given text
    
            from selenium import webdriver
            import time
            
            driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
            driver.get('https://www.facebook.com/')
            element = driver.find_element_by_name('email')
            element.send_keys('helloworld')
            time.sleep(10)# Sleep time to observe
            driver.quit()

* ```find_element_by_xpath```

    - XPath is the language used for locating nodes in an XML document. As HTML can be an implementation of XML (XHTML), Selenium users can leverage this powerful language to target elements in their web applications. XPath extends beyond (as well as supporting) the simple methods of locating by id or name attributes, and opens up all sorts of new possibilities such as locating the third checkbox on the page.

    - Element HTML code
    
            <input type="email" class="inputtext login_form_input_box" name="email" id="email" data-testid="royal_email">

    - Python selenium equivalent code to find the above element using element Xpath (using name attribute i.e ```name="email"```) and send the given text
    
            from selenium import webdriver
            import time
            
            driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
            driver.get('https://www.facebook.com/')
            element = driver.find_element_by_xpath('//input[@name="email"]')
            element.send_keys('helloworld')
            time.sleep(10)# Sleep time to observe
            driver.quit()

* ```find_element_by_link_text```

    - Use this when you know link text used within an anchor tag. With this strategy, the first element with the link text value matching the location will be returned. If no element has a matching link text attribute, a NoSuchElementException will be raised.
    - Element HTML code
    
            <a href="https://www.facebook.com/recover/initiate?lwv=110&amp;ars=royal_blue_bar">Forgotten account?</a>

    - Python selenium equivalent code to find the above link element using link text i.e ```Forgotten account?```) and click the link

            from selenium import webdriver
            import time
            
            driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
            driver.get('https://facebook.com')
            element = driver.find_element_by_link_text('Forgotten account?')
            element.click()
            time.sleep(10) # Sleep time to observe
            driver.quit()

* ```find_element_by_partial_link_text``` 

    - Element HTML code
    
            <a href="https://www.facebook.com/recover/initiate?lwv=110&amp;ars=royal_blue_bar">Forgotten account?</a>

    - Python selenium equivalent code to find the above link element using link text i.e ```Forgot```) and click the link

            from selenium import webdriver
            import time
            
            driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
            driver.get('https://facebook.com')
            element = driver.find_element_by_partial_link_text('Forgot')
            element.click()
            time.sleep(10) # Sleep time to observe
            driver.quit()

* ```find_element_by_tag_name```

    - Use this when you want to locate an element by tag name. With this strategy, the first element with the given tag name will be returned. If no element has a matching tag name, a NoSuchElementException will be raised.

    - Element HTML code
    
            <a href="https://www.facebook.com/recover/initiate?lwv=110&amp;ars=royal_blue_bar">Forgotten account?</a>

    - Python selenium equivalent code to find the above link element using link text i.e ```Forgot```) and click the link

            from selenium import webdriver
            import time
            
            driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
            driver.get('https://facebook.com')
            element = driver.find_element_by_partial_link_text('Forgot')
            element.click()
            time.sleep(10) # Sleep time to observe
            driver.quit()

* ```find_element_by_class_name```

    - Use this when you want to locate an element by class attribute name. With this strategy, the first element with the matching class attribute name will be returned. If no element has a matching class attribute name, a NoSuchElementException will be raised.
    - Element HTML code
    
            <a href="https://www.facebook.com/recover/initiate?lwv=110&amp;ars=royal_blue_bar">Forgotten account?</a>

    - Python selenium equivalent code to find the above link element using link text i.e ```Forgot```) and click the link

            from selenium import webdriver
            import time
            
            driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
            driver.get('https://facebook.com')
            element = driver.find_element_by_partial_link_text('Forgot')
            element.click()
            time.sleep(10) # Sleep time to observe
            driver.quit()
            

CSS --> Find element by CSS selector

driver.find_element_by_css_selector('input[name="name"]').send_keys('Gopikrishna')



Xpath Based  on Text (Faded)

driver.find_element_by_xpath('//span[text()="Faded"]').click()


Creating Xpath ans Css by traversing tags









