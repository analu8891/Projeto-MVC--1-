from app.models import categoria
from app.models import produto
from app.models import usuarios

#Gerer a migration

#python -m alembic revision --autogenerate -m "Criando tabela categorias e produtos"

#Aplicar a migration
# python -m alembic upgrade head