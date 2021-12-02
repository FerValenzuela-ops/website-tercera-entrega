# Created by Ferna at 12/1/2021
Feature: Inicio de sesion
  Como un usuario registrador de linda sonrisa deseo iniciar sesion.

  Scenario: Inicio de sesion como administrador
    Given Ingreso a lindasonrisa y me dirigo al login
    And mi usuario es admin y mi clave es admin
    And ingreso mis crendiciales y presiono el boton ingresar
    Then inicio sesion en linda sonrisa, me llevan al home, e ingreso a mi perfil


  Scenario: Inicio de sesion como usuario
    Given Ingreso a lindasonrisa y me dirigo al login
    And mi usuario es felroel y mi clave es adminminda
    And ingreso mis crendiciales y presiono el boton ingresar
    Then inicio sesion en linda sonrisa, me llevan al home, e ingreso a mi perfil

  Scenario: Inicio de sesion como usuario
    Given Ingreso a lindasonrisa y me dirigo al login
    And mi usuario es andysoto y mi clave es perand123
    And ingreso mis crendiciales y presiono el boton ingresar
    Then inicio sesion en linda sonrisa, me llevan al home, e ingreso a mi perfil

  Scenario: Inicio de sesion como usuario
    Given Ingreso a lindasonrisa y me dirigo al login
    And mi usuario es yanezkarla y mi clave es adminminda
    And ingreso mis crendiciales y presiono el boton ingresar
    Then inicio sesion en linda sonrisa, me llevan al home, e ingreso a mi perfil
