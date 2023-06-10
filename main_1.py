# Iniciar o shell do python
# -> Rodar o comando no terminar -> python manage.py shell

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


user = User.objects.get(pk=1)


token = Token.objects.create(user = user)
#Token: 25ad9a9e3c56d3dae0d487a582cf863a81b8e602>



# args são argumentos que são dinamicos
# e os kwargos são dicionarios dinamicos, voce cria e passa qualquer coisa e ele aceita qualquer coisa dinamica