# Created by Ferna at 12/1/2021
Feature: Registro de usuario
  Como un cliente de linda sonrisa deseo registrarme para tomar una hora con un dentista.

  Scenario: Registro de usuario nuevo
    Given Ingreso a lindasonrisa y me dirigo al registro
    And me llamo Felipe Villarroel, mi usuario sera felroel
    And mi contrasena sera adminminda, mi rut es 17.242.321-5
    And mi direccion es Brisas del Rio 2236, mi telefono es 945171370, mi correo es fernando@gmail.com
    When relleno con mis datos y presiono el boton de registro
    Then me registro exitosamente e inicio sesion en linda sonrisa, me llevan al home

  Scenario: Registro de usuario nuevo
    Given Ingreso a lindasonrisa y me dirigo al registro
    And me llamo Andres Soto, mi usuario sera andysoto
    And mi contrasena sera perand123, mi rut es 15.123.412-0
    And mi direccion es Avenida Los libertadores 234, mi telefono es 998202901, mi correo es andyperez@hotmail.com
    When relleno con mis datos y presiono el boton de registro
    Then me registro exitosamente e inicio sesion en linda sonrisa, me llevan al home

  Scenario: Registro de usuario nuevo
    Given Ingreso a lindasonrisa y me dirigo al registro
    And me llamo Karla Yañez, mi usuario sera yanezkarla
    And mi contrasena sera iamaraccoon, mi rut es 20.231.324-k
    And mi direccion es Antonio Varas 666, mi telefono es 920194123, mi correo es yanezkarla@protonmail.com
    When relleno con mis datos y presiono el boton de registro
    Then me registro exitosamente e inicio sesion en linda sonrisa, me llevan al home
