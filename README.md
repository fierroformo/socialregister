## Descripción
socialregister es una aplicacion para autenticación de usuarios con facebook,
Twitter, Google+, Outlook, Github y Linkedin, hace uso del proyecto `python social auth`


######
## Prerequisites
+ [Oracle's VirtualBox](https://www.virtualbox.org/)
+ [Vagrant](http://www.vagrantup.com/)
+ [Python](http://www.python.org/)
+ [Fabric](http://www.fabfile.org/)
+ [fabutils](https://github.com/vinco/fabutils)


## Configuring your virtual environment
1. Clone repository

    ```bash
    $ git clone --recursive git@github.com:fierroformo/socialregister.git
    ```

2. Create the virtual machine

    ```bash
    $ cd socialregister
    $ vagrant up
    ```

3.  Development environment configuration for localhost to work in socialregister.local

    ```bash
    # /etc/hosts
    192.168.33.27       socialregister.local
    ```

4. Build the environment inside the virtual machine

    ```bash
    $ fab environment:vagrant bootstrap
    ```

5. Run the development server

    ```
    $ fab environment:vagrant runserver
    ```

6. Open your web browser and check the project at `redsep.local`


## Configuración social auth


| setting                                    | descripción                |
|--------------------------------------------|----------------------------|
| `SOCIAL_AUTH_LOGIN_REDIRECT_URL = '<url>'` | Redirige al usuario una vez terminado el proceso de autenticación |
| `SOCIAL_AUTH_LOGIN_ERROR_URL = '<url>'`    | Redirige al usuario en caso de error de autenticación |
| `SOCIAL_AUTH_LOGIN_URL = '<url>'`          | Se utiliza como una retrollamada para `LOGIN_ERROR_URL` |
| `AUTH_USER_MODEL = '<user_model>`          | Establece el modelo de usuario |
| `SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = <boolean>` | Define que el nombre de usuario sera el email |


## Configuración para autenticación con `Facebook` (oauth2)

* [Crea la aplicación](https://developers.facebook.com/quickstarts/?platform=web)
* Agregar `'social.backends.facebook.FacebookOAuth2'` a la tupla `AUTHENTICATION_BACKENDS`
* `SOCIAL_AUTH_FACEBOOK_KEY = '<key>'`
* `SOCIAL_AUTH_FACEBOOK_SECRET = '<secret>'`
* `SOCIAL_AUTH_FACEBOOK_SCOPE = [<scope>]`


## Configuracion para autenticación con `github` (oauth2)

* [Crea la aplicación](https://github.com/settings/applications)
* Agregar `'social.backends.github.GithubOAuth2'` a la tupla `AUTHENTICATION_BACKENDS`
* `SOCIAL_AUTH_GITHUB_KEY = '<key>'`
* `SOCIAL_AUTH_GITHUB_SECRET = '<secret>'`


## Configuración para autenticación con `google` (oauth2)

* [Crea la aplicación](https://console.developers.google.com/project)
* Agregar `'social.backends.google.GoogleOAuth2'` a la tupla `AUTHENTICATION_BACKENDS`
* `SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '<key>'`
* `SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '<secret>'`


## Configuración para autenticación con `Linkedin` (oauth2)

* [Crea la aplicación](https://www.linkedin.com/secure/developer)
* Activar los permisos `r_emailaddress` y `r_basicprofile` al crear la aplicación
* Agregar `'social.backends.linkedin.LinkedinOAuth2'` a la tupla `AUTHENTICATION_BACKENDS`
* `SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = '<key>'`
* `SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = '<secret>'`


## Configuración para autenticación con `Outlook` (oauth2)

* [Crea la aplicación](https://account.live.com/developers/applications/)
* Agregar `'social.backends.live.LiveOAuth2'` a la tupla `AUTHENTICATION_BACKENDS`
* `SOCIAL_AUTH_LIVE_KEY = '<key>'`
* `SOCIAL_AUTH_LIVE_SECRET = '<secret>'`


## Configuración para autenticación con `twitter` (oauth2)

* [Crea la aplicación](https://apps.twitter.com/)
* Agregar `'social.backends.twitter.TwitterOAuth'` a la tupla `AUTHENTICATION_BACKENDS`
* `SOCIAL_AUTH_TWITTER_KEY = '<key>'`
* `SOCIAL_AUTH_TWITTER_SECRET = '<secret>'`


## Otros

Al momento de proporcionar la redirect_uri en nuestra consola de aplicaciones (google, twitter, facebook...) debe
contener el siguiente formato `<protocol>://<domain>/social/complete/<backend>/`


## Problemas comunes

**Error:**
>ValueError: Only unicode objects are escapable. Got None of type <type 'NoneType'>.

**Causa**
No se agregaron las variables `SOCIAL_AUTH_<BACKEND>_KEY` o `SOCIAL_AUTH_<BACKEND>_SECRET`

**Solución**
Agregar dichas variables con su valor correcto.


**Error**
Al intentar conectarme con una red social la pantalla de queda en blanco.

**Causa**
El valor de `SOCIAL_AUTH_<BACKEND>_KEY` es incorrecto

**Solución**
Agregar el valor correcto


**Error**
Al intentar conectar con una red social
>HTTPError: 400 Client Error: Bad Request

**Causa**
El valor para `SOCIAL_AUTH_<BACKEND>_SECRET es incorrecto`

**Solución**
Agregar el valor correcto


**Error**
>Error: redirect_uri_mismatch

**Causa**
La URL de redireccion no es correcta.

**Solución**
Agregar la URL correcta en el administrador de aplicaciones correspondiente. El formato de la URL debe ser `<protocol>://<domain>/social/complete/<backend>/`


**Error**
Cuando intentamos conectar con Outlook
>No se puede completar la solicitud. La cuenta Microsoft está experimentando problemas técnicos. Inténtalo de nuevo más tarde.

**Causa**
Outlook no acepta peticiones a su api desde entornos de desarrollo (localhost)

**Solución**
Configuramos una URL en local(por ejemplo así [esto](http://stackoverflow.com/questions/8541182/apache-redirect-to-another-port/13089668#13089668)) para que coincida con la que agregamos en el centro de aplicaciones de Outlook
