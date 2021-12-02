# Created by Ferna at 12/1/2021
Feature: Inicio de sesion
  Como un cliente de linda sonrisa deseo iniciar sesion para tomar una hora con un dentista.

  Scenario: Inicio de sesion como administrador
    Given Ingreso a lindasonrisa y me dirigo al login
    And mi usuario es admin y mi clave es admin
    And ingreso mis crendiciales y presiono el boton ingresar
    Then inicio sesion en linda sonrisa, me llevan al home, e ingreso a mi perfil

