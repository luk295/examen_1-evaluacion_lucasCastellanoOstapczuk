# Github Actions

Repositorio de demostración de CI/CD con github actions

## Sesión 1

En esta sesión aprenderemos:
  - Github Actions: Qué son, para qué sirven y cómo configuralas.
  - Creación y configuración de ramas.
  - Gestión de Pull requests.
  - Introducción a Rulesets (Requerir pull-requests para merges sobre develop y main)

**Tarea 1:**

Crea un repositorio con tu cuenta Github que contenga el contenido de este, que puedes descargar como .zip desde la interfaz.

En ese repositorio, realiza la siguiente configuración:

 - Configura el repositorio para que no se pueda subir contenido directamente a develop y/o main.
 - Crea una nueva rama develop y súbela al repositorio.
 - Copia el contenido descargado previamente a dicha rama develop.

**Tarea 2:**

Crea un flujo de trabajo nuevo "Hola Mundo" que saque este mensaje en consola y muestre el contenido del repositorio con un pequeño script Bash.

 - Estando en la rama develop, crea una nueva rama, por ejemplo feature/nuevo-flujo-holamundo
 - Crea y edita el flujo en el directorio .github/workflows empleando la ayuda disponible en Github.
 - Sube el contenido de la nueva rama y activa el flujo creando una pull request de la rama sobre develop.
 - Verifica el funcionamiento del flujo.
 - Fin!

**Prerequisitos:**

  - Cuenta Github + creación de repositorios + uso básico (commit, push).
  - Ubuntu 20.04 con permisos de administrador.
  - Instalación de dependencias.

**Dependencias:**

Para las sesiones futuras, es conveniente ir instalando las utilidades detalladas en INSTALL.txt  

## Sesión 2

En esta sesión continuaremos creando un flujo de trabajo adicional, poniendo en práctica los conocimientos de python adquiridos.

Aprenderemos:
  - Integrar un script python en un Github Action.
  - Técnicas de análisis estático de código, verificación de fuga de secretos, etc.
  - Mecanismos de protección de ramas (Bloquear merges de PRs en base a resultados).

**Tarea 1:**

Crear una rama nueva (por ejemplo, feature/check-secrets) que permita detectar posibles fugas de secretos. 

Esta rama debe contener:
  - Script en python (a desarrollar) que analice un directorio en busca de una palabra clave.
  - Flujo de trabajo que utilice el script anterior para buscar, en el repositorio de código, cualquier archivo que pueda contener la palabra reservada **password** 
  - El script deberá terminar con error en caso de que se encuentre algún secreto.

Marketplace Github Actions: https://github.com/marketplace/actions

Tip! Códigos de salida: https://docs.github.com/en/actions/sharing-automations/creating-actions/setting-exit-codes-for-actions

**Tarea 2:**

¿Se han detectado passwords? Si es así, ¿Nos ha dejado realizar el merge igualmente?. Para evitarlo, debemos configurar Github para que no permita ejecutar las PR.

Una vez configurado, ¿Permite mezclar la PR? Eliminar el password, subir a la rama con commit + push y volver a probar.
