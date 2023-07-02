
# Execução 

É necessário possuir o Python versão 3.10 ou superior e o MySQL instalado.

* Recomenda-se criar um ambiente virtual ***venv***.

````
$ pip install -r requirements.txt
````

* Execute todas as querys do arquivo ```to_do_script_vfinal.sql``` no MySQL.

* Acesse o arquivo ```settings.py``` localizado em *```TPBD1/TPBD1/settings.py```* e modififique as linhas **81** e **82** para os respectivos **USER** e **PASSWORD** utilizados em seu MySQL.
    *  Recomendamos não acessar pelo usuário root do MySQL, crie um novo usuário e conceda-lhe os privilégio necessários.

* Entre no repositório ```/TPBD1``` e rode os comandos: 
````
$ python manage.py makemigrations
````

````
$ python manage.py migrate
````

* Agora rode a aplicação com o comando:
````
$ python manage.py runserver
````

* Abra o navegador e entre na url **```http://127.0.0.1:8000```**

# Descrição (Lista de Tarefas Compartilhada)
<p align="justify">
  Uma lista de tarefas é uma ferramenta poderosa e versátil que oferece uma variedade de funcionalidades para ajudar os usuários a gerenciar suas tarefas de forma eficiente. Dessa forma, você e seus colegas, decidiram utilizar uma lista de tarefas compartilhada para que, além de cada um poder organizar as suas próprias tarefas, vocês também pudessem editar listas de tarefas compartilhada entre vocês para se organizarem em relação a atividades em grupo, como tarefas na universidade e estágio.
</p>
<p align="justify">
  No entanto, ao pesquisarem por aplicações de listas de tarefas compartilhadas, vocês não encontraram nenhuma aplicação disponível que atendesse às suas necessidades e que fosse segura o suficiente para confiarem os seus dados.
</p>
<p align="justify">
  Como todos têm os conhecimentos necessários para o desenvolvimento de software, vocês decidiram criar uma aplicação própria de lista de tarefas compartilhada que, além de atender às necessidades do grupo, será disponibilizada para o público em geral que também buscam por uma ferramenta do tipo.
</p>
<p align="justify">
  Após discutirem sobre as funcionalidades que uma aplicação descente de lista de tarefas compartilhada deve oferecer, vocês elaboraram a uma lista descrevendo essas funcionalidades e que serão implementadas pela aplicação de vocês. Abaixo, essas funcionalidades são apresentadas e descritas:
</p>
<p>
 <ol>
   <li align="justify"><b>Cadastro e autenticação de usuários:</b> A aplicação permite que os usuários se cadastrem, fornecendo um nome de usuário e senha, além de informações como nome, telefone, e-mail. O cadastro é necessário para acessar todas as funcionalidades da aplicação. O acesso a aplicação será através do nome de usuário e senha.</li><br>
   <li align="justify"><b>Criação de listas de tarefas:</b> Após fazer acessar a aplicação, os usuários podem criar listas de tarefas para organizar suas atividades. Cada lista deve ter um nome descritivo para facilitar a identificação. Além disso, a aplicação deve ser capaz de apresentar a data e horário em que a lista foi criada e, também, a data e horário da última modificação na lista foi realizada (e o responsável pela modificação, no caso de listas compartilhadas).</li><br>
   <li align="justify"><b>Cadastro de tarefas:</b> Dentro de cada lista de tarefas, os usuários podem adicionar tarefas individuais. Cada tarefa deve conter uma descrição, data de cadastro, a data de vencimento da tarefa (opcional) e a indicação se a tarefa foi concluída ou não.</li><br>
   <li align="justify"><b>Compartilhamento de listas de tarefas:</b> Os usuários têm a opção de convidar outros usuários para participarem da edição suas listas de tarefas. Ao enviar um convite, o usuário convidado receberá uma notificação para aceitar ou recusar o acesso à lista de tarefas.</li><br>
   <li align="justify"><b>Aceitação ou recusa de convites:</b> Os usuários podem visualizar os convites recebidos para participar de listas de tarefas compartilhadas. Eles têm a opção de aceitar o convite, o que permite que eles visualizem e editem a lista compartilhada, ou recusar o convite, caso não estejam interessados em participar.</li><br> 
   <li align="justify"><b>Edição de listas compartilhadas:</b> Tanto o usuário criador da lista quanto os usuários convidados podem editar as listas compartilhadas. Eles podem adicionar, remover ou modificar tarefas, permitindo a colaboração e atualização em tempo real.</li><br>
   <li align="justify"><b>Exclusão de listas de tarefas:</b> Apenas o usuário criador da lista tem permissão para apagá-la. Essa funcionalidade garante que as listas compartilhadas não sejam excluídas acidentalmente por usuários
convidados.</li><br>
   <li align="justify"><b>Listagem de listas de tarefas:</b> A aplicação deve oferecer uma visão geral das listas de tarefas criadas pelo usuário, permitindo que ele as liste e selecione para visualização e edição.</li><br>
   <li align="justify"><b>Visualização e edição de listas de tarefas:</b> Os usuários podem visualizar suas listas de tarefas e as listas compartilhadas. Eles têm a opção de marcar tarefas como concluídas e editar detalhes das tarefas.</li>
 </ol>
</p>
<p align="justify">
  Essas funcionalidades essenciais garantem que os usuários tenham controle total sobre suas listas de tarefas e possam colaborar com outras pessoas quando necessário. A aplicação oferecerá uma experiência intuitiva e eficaz para o gerenciamento de tarefas, auxiliando na produtividade e organização pessoal.
</p>

# Tarefa 01.
<p align="justify">
  Dada a especificação da aplicação acima, realize a modelagem conceitual, gerando como resultado um Diagrama Entidade Relacionamento (DER).
</p>
<p align="center">
  <img src="imgs/DER.png">
</p>

# Tarefa 02.
<p align="justify">
  A partir do DER obtido na Tarefa 01, utilize as regras de mapeamento DER/Relacional para construção do modelo lógico relacional.
</p>
<p align="center">
  <img src="imgs/logico.png">
</p>

# Tarefa 03.
<p align="justify">
  A partir do modelo lógico relacional obtido na Tarefa 02, escreva um script SQL para construção do esquema do banco de dados. Considere que será utilizado o SGBD MySQL para implantação da aplicação.
</p>
<p align="justify">
  A implementação do esquema do banco está no arquivo: <b>to_do_script_vfinal.sql</b> 
</p>

# Tarefa 04.
<p align="justify">
  Implemente a aplicação especificada acima de forma que ela faça uso do banco de dados construído na Tarefa 03. Pode ser criada uma aplicação de terminal ou uma aplicação com interface gráfica (desktop ou Web). Essa escolha ficará a cargo do grupo de trabalho. A linguagem de programação também deve ser determinada pelo grupo.
</p>

# Tarefa 05.
<p align="justify">
  Escreva um script SQL com todas as consultas utilizadas na implementação da aplicação.
</p>
<p align="justify">
  As consultas utilizadas estão no arquivo: <b>to_do_script_funcoes_utilizadas.sql</b> 
</p>


