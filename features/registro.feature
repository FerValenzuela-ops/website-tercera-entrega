# Created by Ferna at 12/1/2021
Feature: Registro de usuario
  Como un cliente de linda sonrisa deseo registrarme para tomar una hora con un dentista.

  Scenario: Registro de usuario nuevo
    Given Ingreso a lindasonrisa y me dirigo al registro
    And me llamo Fernando Valenzuela, mi usuario sera fervp
    And mi contrasena sera adminminda, mi rut es 19.684.439-2
    And mi direccion es Brisas del Rio 2236, mi telefono es 945171370, mi correo es fernando@gmail.com
    When relleno con mis datos y presiono el boton de registro
    Then me registro exitosamente e inicio sesion en linda sonrisa, me llevan al home

