import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from sga_login import SgaLogin
from sga_link import SgaLink
from view import View
from tkinter import filedialog
from selenium.webdriver.common.keys import Keys
import pandas as pd

global driver
global view
global file
global file_path


def open_interface():
    global view
    view = View()
    view.create_root("Academic Management")
    button_execute = view.create_button(text="Ejecutar", function=handler_data)
    button_execute.grid(row=4, column=1, padx=10, pady=10)
    button_file = view.create_button(text="Cargar", function=get_xls)
    button_file.grid(row=3, column=1, padx=10, pady=10)
    view.root.mainloop()


def init(url):
    global driver
    driver = webdriver.Chrome(executable_path=r"C:\\Program Files (x86)\\Driver Chrome\\chromedriver.exe")
    driver.get(url)


def login():
    sga_login = SgaLogin("1140849881", "soeariza1398", driver)
    sga_login.login()


def execute_link():
    sga_link_laboratory = SgaLink("Laboratorio", driver)
    sga_link_laboratory.execute_link_element()
    sga_link_management = SgaLink("Administrar deudas", driver)
    sga_link_management.execute_link_element()


def get_xls():
    global file_path
    file_path = filedialog.askopenfilename()


def get_data():
    global file
    file = pd.read_excel(file_path)
    return file.to_dict(orient="records")


def handler_data():
    data = get_data()
    init("https://funcionarios.portaloas.udistrital.edu.co/urano/")
    login()

    for student in data:
        time.sleep(1)
        execute_link()
        driver.switch_to.frame('bloqueC')
        time.sleep(2)
        set_search_value(student['CODIGO'])
        add_debt()
        set_select()
        set_material(student['SERIES'])
        set_year(student['YEAR'])
        set_period(student['PERIODO'])
        set_debt(student['DEUDA'])
        save_debt()
        time.sleep(3)
    driver.close()


def set_search_value(code):
    driver.find_element_by_id('valorConsulta').send_keys(code)
    driver.find_element_by_id('consultarUsuario').click()


def add_debt():
    time.sleep(2)
    driver.find_element_by_id('agregarFila').click()


def set_select():
    select = Select(driver.find_element_by_id('listadoLaboratorios'))
    select.select_by_value('9')


def set_material(material):
    driver.find_element_by_id('Material').send_keys(material)


def set_year(year):
    Select(driver.find_element_by_id('Anno')).select_by_value(str(year))


def set_period(period):
    Select(driver.find_element_by_id('Periodo')).select_by_value(str(period))


def set_debt(debt):
    driver.find_element_by_id('Multa').send_keys(debt)


def save_debt():
    driver.execute_script("window.open('');")
    driver.find_element_by_xpath('//*[@title="Guardar Deuda"]').click()
    driver.switch_to.window(driver.window_handles[0])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.get("https://funcionarios.portaloas.udistrital.edu.co/urano/index.php?data=vTFOZrbM4Dxc4pSke31YBsI5_IpCQ9HHTV3cbsU1b7Y")


open_interface()
