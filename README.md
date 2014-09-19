## Descripción
socialregister es una aplicacion para autenticación de usuarios con facebook,
Twitter, Google+, Outlook, Github y Linkedin, hace uso del proyecto `python social auth`


## Configuración


### Instalar `python social auth`

* [Instalación](http://python-social-auth.readthedocs.org/en/latest/installing.html)


### Agregar los siguientes valores a settings.py


* Agregar `socialregister.users` a `INSTALLED_APPS`


* Definir la tupla `AUTHENTICATION_BACKENDS`, siempre debe incluir el backend `django.contrib.auth.backends.ModelBackend`

* Definir la tupla `SOCIAL_AUTH_PIPELINE`

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
* `SOCIAL_AUTH_GITHUB_KEY = '<key>'
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


### Otros

Al momento de proporcionar la redirect_uri en nuestra consola de aplicaciones (google, twitter, facebook...) debe
contener el siguiente formato `<protocol>://<domain>/social/complete/<backend>/`
