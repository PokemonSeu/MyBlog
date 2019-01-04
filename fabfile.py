
from fabric.api import env,run
from fabric.operations import sudo

GIT_REPO = "https://github.com/PokemonSeu/MyBlog.git"

env.user = 'pythonman'
env.password = ' '


env.hosts = ['www.pythonman.cn']


env.port = '22'


def deploy():
    source_folder = '/home/pythonman/sites/www.pythonman.cn/MyBlog'

    run('cd %s && git pull' % source_folder)
    run("""
        cd {} &&
        ../env/bin/pip install -r requirements.txt &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py migrate
        """.format(source_folder))
    sudo('restart gunicorn-www.pythonman.cn')
    sudo('service nginx reload')
