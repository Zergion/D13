from django.apps import AppConfig
import redis


class NewappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newapp'


    def ready(self):
        import newapp.signals

red = redis.Redis(
    host='redis-10332.c273.us-east-1-2.ec2.cloud.redislabs.com',
    port=10332,
    password='3AhbR1HWfwmnKftX15RqkoPH7SzcLPmI'
)

