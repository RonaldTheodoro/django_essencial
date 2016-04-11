import os
import sys
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
from django.core.management import execute_from_command_line

DEBUG = os.environ.get('DEBUG', 'on') == 'on'
SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    'iax-97fqvo-jrf(z2r&b+g(x9%*0th%95^^74=7h@+w*vn9$@j'
)
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)


def index(request):
    return HttpResponse('Hello World')


urlpatterns = (
    url(r'^$', index),
)


application = get_wsgi_application()


if __name__ == '__main__':

    execute_from_command_line(sys.argv)