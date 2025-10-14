# Formação Django — Repositório de Estudos

Este repositório organiza exercícios, projetos e anotações da "Formação Django" da Alura. A convenção principal é: cada branch corresponde a um curso diferente da formação. Assim você mantém o histórico e o material de cada curso separados, mas ainda dentro do mesmo repositório.

Link da formação na Alura:
https://cursos.alura.com.br/formacao-django

## Convenção de branches

- Branch principal: `main` — contém este README e material compartilhado (se houver).
- Cada curso deve ter sua própria branch nomeada com o padrão: `curso`

## Estrutura esperada por branch

Cada branch de curso pode seguir uma estrutura parecida com esta:

- `README.md` — explicação do curso, objetivo, links relevantes e resumo.
- `exercicios/` — exercícios resolvidos e não resolvidos.
- `requirements.txt` — dependências específicas do curso/projeto.

# Comandos do Django:
* `django-admin help` — lista todos os comandos disponíveis.
* `django-admin startproject {nome do projeto} .`: cria um novo projeto em django.
* `python manage.py runserver`: sobe o servidor com o reload.
* `python manage.py startapp {name app}`: cria uma aplicação para o projeto. a qual deve ser endereçada no setup para que o django interperte
* `python manage.py help`: mostra os comando referêntes a aplicação.
* `python manage.py collectstatic`: adiciona arquivos statics a pasta padrão.
