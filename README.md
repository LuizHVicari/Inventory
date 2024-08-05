# Inventory

## Deploy

Antes de fazer o deploy, é necessário iniciar as variáveis de ambiente, configurando um arquivo .env de acordo com o [exemplo](.env.example). A maior parte das variáveis já está configurada para funcionar com o Docker, porém é necessário criar uma nova chave secreta (no exemplo há um tutorial mostrando como fazer), além disso, o nível de log e debug devem ser configurados para a produção.

Crie os containers pelo docker com:

```[sh]
docker-compose up -d --build
```

Agora, entre no terminal do Docker com:

```[sh]
docker exec -it students-room-inventory-web-1 sh
```

Entre na pasta src, faça as migrações e crie um super usuário

```[sh]
cd src
python manage.py migrate
python manage.py createsuperuser
```

Entre na [página de administrador](http://localhost:8000/admin) e faça login.

## Criando items

Na página do adminstrador, é possível criar items, guardando o local em que eles estão, sala e bloco, contudo, é necessário criar esses locais primeiro. A criação das outras entidades tamém é possível através do formulário de criação de itens, abrindo as páginas em cascata.

## Criando usuários

A criação de usuários por meio de formulário está desabilitada, assim, é possível apenas que os adminstradores do sistema criem novos usuários.

Para criar um usuário, deve ser utilizada a [página de criar usuários](http://localhost:8000/admin/auth/user/), após a criação deles, é necessário entrar na [página de emails](http://localhost:8000/admin/account/emailaddress/) e adicionar o email do usuário, marcando o como verificado e primário (em próximas atualizações será implementado essa etapa por meio de post save signals).

Por fim, caso o usuário seja um [aluno](http://localhost:8000/admin/users/student/) ou [professor](http://localhost:8000/admin/users/professor/), é necessário criar uma entidade para eles nos respectivos formulários. Para a criação desass entidades, também é necessário ser criado o curso e departamento, os quais podem ser criados nos formulários de alunos e professores em cascata.

## Chat

Foi implementado um chat experimental para permitir a comunicação entre os usuários e os administradores, a ideia é permitir que items sejam reservados com antecedência para agilizar o serviço.

Em próximas atualizações, será buscado criar uma página que mostre as notificações de conversas recentes.

Apenas o usuário e os adminstradores podem ver o chat. Além disso, os chats sempre são criados entre usuários normais e adminstradores, não sendo possível a interação entre dois usuários normais.

Foi implementado uma forma de limitar o envio de mensagens de forma experimental, buscando não sobrecarregar o banco de dados com muitas mensagens. O limite de mensagens pode ser configurado nas variávies de ambiente. Além disso, é criado um log toda vez que esse limite for excedido por um usuário.

## Reserva de itens

Para resevar um item, é necessário que o administrador registre-o no [formulário de reserva de estudantes](http://localhost:8000/admin/items/studentloan/) ou [de professor](http://localhost:8000/admin/items/professorloan/). A separação foi criada para facilitar a implementação de restições de itens, por exemplo, para que certos itens não possam ser emprestados por alunos.

### Devolução de itens

Para marcar um item como devolvido, basta editar o campo de data da devolução no empréstimo.

#### Nada consta

As entidades aluno e professor possuem um campo de nada consta, o usuário que tenha ele marcado como verdadeiro não pode mais fazer empréstimos no sistema.

O sistema não emite o certificado de nada consta, assim, a verificação e emissão são tarefas internas que devem ser realizadas pelos adminstradores do sistema.

Não foi implementada uma verificação se o usuário pode pedir o certificado, isso foi feito para que esse processo possa ser feito como a instituição desejar. Apesar disso, na página frontend o usuário pode ver quais itens ele tem reservados e se é possível pedir o certificado, baseado apenas em se todos os seus empréstimos foram devolvidos.

## Logging

Foram configurados 3 sistemas de logging, um para o terminal e dois em arquivo. O loggin em terminal está configurado para ser maias abrangente, enquanto isso, o primeiro logging em arquivo registra apenas mensagens de warning ou de maior prioridade, enquanto o segundo lista apenas as mensagens críticas (embora não foram utilizadas ainda no sistema), essa separação visa prover maior visibilidade quando houver acontecimentos críticos no sistema.

Para alterar essas configurações, basta editar o início do [arquivo de configurações](src/inventory/settings.py).

## Contribuições

O projeto aceita contribuíções, para encontrar ideias de como contribuir, basta procurar nesse arquivo as próximas _features_ a serem desenvolvidas ou contribuir nas seguintes:

- Melhorias no sistema de chat em geral;

- Adicionar sinais para o sistema de login com e-email, baseado no [django allauth](https://docs.allauth.org/en/latest/account/configuration.html);

- Melhorias em devops e integração com Docker;

Além disso, a correção de quaisquer bugs ou problemas de segurança que possam existir são bem vindas.
