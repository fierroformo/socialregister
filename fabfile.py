# encoding: utf-8
import os

from fabric.api import env, local, run, cd, task, require, settings, prefix
from fabric.contrib.project import rsync_project
from fabric.colors import green, red


#
# Environments
#
@task
def vagrant():
    """
    Ambiente local de desarrollo (máquina virtual Vagrant).
    """
    # Usuario "vagrant"
    env.user = "vagrant"
    # Se conecta al ssh local
    env.hosts = ["127.0.0.1:2222"]

    # Llave ssh creada por Vagrant
    result = local("vagrant ssh-config | grep IdentityFile", capture=True)
    env.key_filename = result.split()[1]

    # Directorio del sitio Django
    env.site_dir = "/home/vagrant/app"


#
# Tasks
#
@task
def bootstrap():
    """
    A partir de un sistema "vacío", con todas las dependencias instaladas,
    prepara el ambiente para correr la aplicación en modo desarrollo.
    """
    require("site_dir")
    with cd(env.site_dir):
        # Crea la base de datos
        run('touch db/database.db')
    # Sincroniza la base de datos
    syncdb()


@task
def resetdb():
    require("site_dir")
    with cd(env.site_dir):
        run('rm db/database.db')
        run('touch db/database.db')

    syncdb()


#
# manage.py
#
@task
def syncdb():
    require("site_dir")
    with cd(env.site_dir):
        run("python manage.py syncdb --noinput")
        run("python manage.py migrate")


@task
def schemamigration(app):
    require("site_dir")
    with cd(env.site_dir):
        with settings(warn_only=True):
            run("python manage.py schemamigration --auto %s" % app)


@task
def runserver():
    require("site_dir")
    with cd(env.site_dir):
        run("python manage.py runserver_plus 0.0.0.0:8000")
