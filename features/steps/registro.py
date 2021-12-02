from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

use_step_matcher("parse")


@given("Ingreso a lindasonrisa y me dirigo al registro")
def step_impl(context):

    context.driver = webdriver.Chrome()
    context.driver.get('http://127.0.0.1:8000/')
    time.sleep(1)
    context.driver.find_element_by_id("registro").click()
    time.sleep(1)


@step(u"me llamo {first_name} {last_name}, mi usuario sera {username}")
def step_impl(context, first_name, last_name, username):
    context.first_name = first_name
    context.last_name = last_name
    context.username = username


@step("mi contrasena sera {password1}, mi rut es {rut}")
def step_impl(context, password1, rut):
    context.password1 = password1
    context.password2 = context.password1
    context.rut = rut


@step("mi direccion es {direccion}, mi telefono es {telefono}, mi correo es {email}")
def step_impl(context, direccion, telefono,email):
    context.direccion = direccion
    context.telefono = telefono
    context.email = email


@when("relleno con mid datos y presiono el boton de registro")
def step_impl(context):

    context.driver.find_element_by_id('id_username').send_keys(context.username)
    context.driver.find_element_by_id('id_email').send_keys(context.email)
    context.driver.find_element_by_id('id_rut').send_keys(context.rut)
    context.driver.find_element_by_id('id_direccion').send_keys(context.direccion)
    context.driver.find_element_by_id('id_telefono').send_keys(context.telefono)
    context.driver.find_element_by_id('id_password1').send_keys(context.password1)
    context.driver.find_element_by_id('id_password2').send_keys(context.password2)
    time.sleep(1)

    context.driver.find_element_by_id('botonsito').send_keys(Keys.ENTER)
    time.sleep(1)




@then("me registro exitosamente e inicio sesion en linda sonrisa, me llevan al home")
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_id('myaccount').click()
    time.sleep(1)
    context.driver.find_element_by_id('myusername').click()
    time.sleep(1)
    usuario = context.driver.find_element_by_id('myname').text
    time.sleep(1)
    assert context.username == usuario
    context.driver.close()
