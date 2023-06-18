## Highlords Discord Bot
_( também conhecido como - O Narga do Giga )_

### Sobre o BOT
Este é um boilerplate para um bot de discord, com o único intuito de IMORTALIZAR as falas desse personagem ICÔNICO que atende pelo nome de Gigante.


### Configuração LOCAL
Primeiramente, o ambiente está em docker, utilizando do docker-composer.

#### Requerimentos
- docker
- docker.io
- docker-compose

#### .env
Substitua os valores no arquivo `./.env` pelos tokens de acesso do BOT e da base do AIRTABLE

#### Ligando o bot
```
docker-compose build
docker-compose up -d
```

#### Desligando o BOT
```
docker-compose down
```

### TODO
- separar os processos da camada comamands para a service
- adicionar logging
- adicionar linter
- adicionar pre-commit hooks para linter
- integrar a atualizacao da imagem na vm direto pela pipeline
