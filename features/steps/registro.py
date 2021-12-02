from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

use_step_matcher("parse")


@given(u"Ingreso a lindasonrisa y me dirigo al registro")
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


@step(u"mi contrasena sera {password1}, mi rut es {rut}")
def step_impl(context, password1, rut):
    context.password1 = password1

    context.rut = rut


@step(u"mi direccion es {direccion}, mi telefono es {telefono}, mi correo es {email}")
def step_impl(context, direccion, telefono,email):
    context.direccion = direccion
    context.telefono = telefono
    context.email = email

@when("relleno con mis datos y presiono el boton de registro")
def step_impl(context):
    context.driver.find_element_by_id('id_username').send_keys(context.username)
    time.sleep(1)
    context.driver.find_element_by_id('id_email').send_keys(context.email)
    time.sleep(1)
    context.driver.find_element_by_id('id_rut').send_keys(context.rut)
    time.sleep(1)
    context.driver.find_element_by_id('id_direccion').send_keys(context.direccion)
    time.sleep(1)
    context.driver.find_element_by_id('id_telefono').send_keys(context.telefono)
    time.sleep(1)
    context.driver.find_element_by_id('id_password1').send_keys(context.password1)
    time.sleep(1)
    context.driver.find_element_by_id('id_password2').send_keys(context.password1)
    time.sleep(1)

    context.driver.find_element_by_id('botonsito').send_keys(Keys.ENTER)
    time.sleep(1)







@then(u"me registro exitosamente e inicio sesion en linda sonrisa, me llevan al home")
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_id('myaccount').click()
    time.sleep(1)
    context.driver.find_element_by_id('myusername').click()
    time.sleep(1)
    usuario = context.driver.find_element_by_id('myname').text
    assert context.username == usuario


