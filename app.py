from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

repetir = 30

for _ in range(repetir):
   
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeqJTAoPqf0OIXIlQ11aKXPptesIwtK5vaPeinnfRjK14xhUg/viewform?usp=pp_url&entry.1166113517=Si&entry.1213387584=35+-+44+a%C3%B1os&entry.1112984907=Femenino&entry.686137596=$+501.00+-+$+800.00&entry.482809627=Educaci%C3%B3n+superior&entry.1169569517=Galer%C3%ADas+de+arte&entry.625206244=Anual&entry.1011249369=Pinturas&entry.1011249369=Dibujos&entry.1704813468=De+$101+a+$500&entry.1441004373=Efectivo&entry.1749443002=No&entry.187333772=Redes+Sociales&entry.1161620317=Desinteres&entry.1161620317=Acceso&entry.397647763=Si&entry.140909296=Pinturas&entry.1348238985=De+3+a+5+Obras&entry.166993211=Anual&entry.880253953=De+$500+a+Mas&entry.2055150023=Pagina+Web&entry.1942095088=Delivery+Gratis&entry.969761371=Redes+Sociales")

    # Esperar un breve momento para que la página se cargue completamente
    time.sleep(2)

    # Encontrar y hacer clic en el botón "Siguiente"
    boton_siguiente1 = driver.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    boton_siguiente1.click()

    # Esperar un breve momento para que la página se cargue después de hacer clic en "Siguiente"
    time.sleep(2)
    boton_siguientes2 = driver.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')
    boton_siguientes2.click()
    btn_siguiente3=driver.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')
    btn_siguiente3.click()
    
    btn_siguiente4=driver.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')
    btn_siguiente4.click()

    # Encontrar y hacer clic en el botón "Enviar"
    boton_enviar = driver.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')
    boton_enviar.click()

    # Esperar un breve momento para que la página se cargue después de hacer clic en "Enviar"
    time.sleep(2)

    # Cerrar el navegador
driver.quit()
