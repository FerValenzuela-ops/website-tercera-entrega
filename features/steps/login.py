from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


use_step_matcher("parse")


@given("Ingreso a lindasonrisa y me dirigo al login")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get('http://127.0.0.1:8000/')
    time.sleep(1)
    context.driver.find_element_by_id("mylogin").click()
    time.sleep(1)


@step(u"mi usuario es {username} y mi clave es {password}")
def step_impl(context,username,password):
    context.username = username
    context.password = password

@step(u"ingreso mis crendiciales y presiono el boton ingresar")
def step_impl(context):
    context.driver.find_element_by_id('id_username').send_keys(context.username)
    time.sleep(1)
    context.driver.find_element_by_id('id_password').send_keys(context.password)
    time.sleep(1)
    context.driver.find_element_by_id('botonsito').send_keys(Keys.ENTER)
    time.sleep(1)

@then("inicio sesion en linda sonrisa, me llevan al home, e ingreso a mi perfil")
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_id('myaccount').click()
    time.sleep(1)
    context.driver.find_element_by_id('myusername').click()
    time.sleep(1)
    usuario = context.driver.find_element_by_id('myname').text
    assert context.username == usuario