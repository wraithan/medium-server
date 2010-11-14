from fabric.api import *

env.hosts = ['wraithan.net']

def local_install_requirements(upgrade=None):
    cmd = 'pip install -r requirements.txt'
    if upgrade:
        cmd = 'pip install --upgrade -r requirements.txt'
    local(cmd)

def install_requirements(upgrade=None):
    workon = 'workon medium-server && '
    cmd = 'pip install -r requirements.txt'
    if upgrade:
        cmd = 'pip install --upgrade -r requirements.txt'
    with cd('/srv/wsgi/medium-server/medium'):
        run(workon + cmd)

def deploy():
    with cd('/srv/wsgi/medium-server/medium'):
        run('git pull')
    install_requirements()
    touch()

def touch():
    with cd('/srv/wsgi/medium-server/medium'):
        sudo('kill -HUP `cat gunicorn.pid`')

