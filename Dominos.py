from selenium import webdriver
from time import sleep
from vAss import talk,rec_audio

def pizza():
    driver = webdriver.Chrom(r"D:\Users\Admin\Desktop\chromedriver.exe")

    driver.maximize_window()
    talk("Opening Dominos")

    driver.get('https://www.dominos.co.in/')
    sleep(5)

    talk("getting ready to order")
    driver.find_element_by_link_text("ORDER ONLINE NOW").click()
    sleep(1)

    talk("getting ready to order")
    driver.find_element_by_class_name('srch-cnt-srch-inpt').click()
    sleep(1)

    location = "shahibaug"

    talk("Entering your location")
    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div/div[3]/div/div[1]/div[2]/div/div[1]/input'
    ).send_keys(location)
    sleep(1)

    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div/div[3]/div/div[1]/div[2]/div[2]/div/ul/li[1]'
    ).click()
    sleep(1)

    try:
        driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[1]/div[2]'
        ).click()
        sleep(1)

    except:
        talk("Your location could not be found. Please try again later")
        exit()

    talk("Logging in")
    phone_num = "1234567899"
    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div//div[2]/div/form/div[1]/div[2]/input'
    ).send_keys(phone_num)
    sleep(1)

    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div//div[2]/div/form/div[2]/input'
    ).click()
    sleep(1)

    talk("what is your OTP")
    sleep(3)

    otp_log = rec_audio()

    driver.find_element_by_xpath(
         '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div//div[2]/div/div/div/div[1]/input'
    ).send_keys(otp_log)
    sleep(2)

    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div//div[2]/div/div/div/div[2]/div[2]/button/span'
    ).click()
    sleep(2)

    talk("Do you want me to order from your favorites?")
    query_fev = rec_audio()

    if "yse" in query_fev:
        try:
            driver.find_element_by_xpath(
                '//*[@id="mn-lft"]/div[6]/div/div[6]/div/div/div[2]/div[3]/div/button/span'
            ).click()
            sleep(1)
        except:
            talk("The entered OTP is incorrect.")
            exit()

        talk("Adding your favorites to cart")

        talk("Do you want to add extra cheese for your pizza?")
        ex_cheese = rec_audio()
        if "yes" in ex_cheese:
            talk("Extra cheese added")
            driver.find_element_by_xpath(
                '//*[@id="mn-lft"]/div[6]/div/div[1]/div/div/div[2]/div[3]/div[2]/button'
            ).click()

        elif "no" in ex_cheese:
            driver.find_element_by_xpath(
                '//*[@id="mn-lft"]/div[6]/div/div[1]/div/div/div[2]/div[3]/div[1]/button/span'
            ).click()
        else:
            talk("I don't know that")
            driver.find_element_by_xpath(
                '//*[@id="mn-lft"]/div[6]/div/div[1]/div/div/div[2]/div[3]/div[1]/button/span'
            ).click()

        driver.find_element_by_xpath(
            '//*[@id="mn-lft"]/div[16]/div/div[1]/div/div/div[2]/div[2]/div/button'
        ).click()
        sleep(1)

        talk("Would you like to increase the quantity?")
        qty = rec_audio()
        qty_pizza = 0
        qty_pepsi = 0
        if "yes" in qty:
            talk("Would you like to increase the quantity of pizza?")
            wh_qty = rec_audio()
            if "yes" in wh_qty:
                talk("How many more pizza would you like to add?")
                try:
                    qty_pizza = rec_audio()
                    qty_pizza = int(qty_pizza)
                    if qty_pizza > 0:
                        talk_piz = f"Adding {qty_pizza} more pizzas"
                        talk(talk_piz)
                        for i in range(qty_pizza):
                            driver.find_element_by_xpath(
                                '//*[@id="__next"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div/div/div[2]'
                            ).click()

                except:
                    talk("I don't know that")
            else:
                pass

            talk("Would you like to increase the quantity of pepsi?")
            pep_qty = rec_audio()
            if "yes" in pep_qty:
                talk("Hom many more pepsi do you like to add?")
                try:
                    qty_pepsi = rec_audio()
                    qty_pepsi = int(qty_pepsi)
                    if qty_pepsi > 0:
                        talk_pep = f"Adding {qty_pepsi} more pepsis"
                        talk(talk_pep)
                        for i in range(qty_pepsi):
                            driver.find_element_by_xpath(
                                '//*[@id="__next"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[2]'
                            ).click()

                except:
                    talk("I don't know that")
            else:
                pass
        elif "no" in qty:
            pass

        total_pizza = qty_pizza + 1
        total_pepsi = qty_pepsi + 1
        tell_num = f"This is your list of orders. {total_pizza} Pizzas and {total_pepsi} Pepsis. Do you want to checkout"
        talk(tell_num)
        check_order = rec_audio()

        if "yes" in check_order:
            talk("Checking out")
            driver.find_element_by_xpath(
                '//*[@id="__next"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button'
            ).click()
            sleep(1)
            driver.find_element_by_xpath(
                '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[6]/div/div//div[6]/span[2]/span'
            )
            total_price = f'Total price is {total.text}'
            talk(total_price)
            sleep(1)

        else:
            exit()

        talk("Placing your order")
        driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[6]/div/div/div[8]/button'
        ).click()
        sleep(2)
        try:
            talk("Saving your location")
            driver.find_element_by_xpath(
                '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/div[3]/div/div/input'
            ).click()
            sleep(2)
        except:
            talk("The store is currently offline.")

        talk("Do you want to confirm your order?")
        confirm = rec_audio()
        if "yes" in confirm:
            talk("Placing your order")
            driver.find_element_by_xpath(
                '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div/div[2]/button'
            ).click()
            sleep(2)
            talk("Your order is placed successfully. Wait for dominos to delivery your order. Enjoy day!")
        else:
            exit()

    else:
        exit()

pizza()