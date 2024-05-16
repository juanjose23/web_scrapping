from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

repetir =3

for _ in range(repetir):
   
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdp0nlvnMFzF_ukopN0nCpwjNA1MOuW6TGJYYk6tLiJc989Ag/viewform?usp=pp_url&entry.273385994=S%C3%AD&entry.1659275124=Auto+Master&entry.571926919=Cada+3+meses&entry.1148669254=Engrasamiento+de+motor&entry.1148669254=Alineamiento+y+balanceo&entry.1148669254=Inspecci%C3%B3n+y+diagn%C3%B3stico&entry.268280962=1400&entry.64076007=700&entry.1342197164=__other_option__&entry.1342197164.other_option_response=1300&entry.950564103=__other_option__&entry.950564103.other_option_response=100&entry.272570176=2100&entry.772078386=300&entry.596733151=Por+transferencia&entry.596733151=En+efectivo&entry.264910251=S%C3%AD&entry.563112947=Redes+Sociales&entry.2106355434=Distancia&entry.2106355434=Acceso&entry.1981179876=S%C3%AD&entry.242836106=De+7+meses+a+mas&entry.1525231337=Litro&entry.684656616=Distrito+VII&entry.1621456103=Descuentos+por+volumen&entry.1621456103=Promociones+de+temporadas&entry.1229227229=Redes+Sociales&entry.1229227229=Sitio+web&entry.1229227229=Carteles+publicitarios")

    # Esperar un breve momento para que la página se cargue completamente
    time.sleep(2)

    # Encontrar y hacer clic en el botón "Siguiente"
    boton_siguiente1 = driver.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    boton_siguiente1.click()
    time.sleep(2)
   
    boton_siguientes2 = driver.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')
    boton_siguientes2.click()
    time.sleep(2)

    btn_siguiente3=driver.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')
    btn_siguiente3.click()
    time.sleep(2)
   
    # Encontrar y hacer clic en el botón "Enviar"
    boton_enviar = driver.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')
    boton_enviar.click()

    # Esperar un breve momento para que la página se cargue después de hacer clic en "Enviar"
    time.sleep(2)

    # Cerrar el navegador
driver.quit()
