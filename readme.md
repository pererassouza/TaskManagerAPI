
### Instruções de Uso

1. **Instalação**:
   - Certifique-se de ter Python e pip instalados em seu ambiente.
   - Crie um ambiente virtual para este projeto (opcional, mas recomendado).
   - Instale as dependências listadas no arquivo `requirements.txt` usando o comando `pip install -r requirements.txt`.

2. **Configuração do Banco de Dados**:
   - O banco de dados utilizado é o SQLite, e o arquivo padrão é `taskmanager.db`.
   - Se o arquivo `taskmanager.db` não existir, o aplicativo Flask criará automaticamente o banco de dados na pasta `instance` com as tabelas necessárias ao ser iniciado.

3. **Executando o Aplicativo**:
   - Para iniciar o servidor Flask, use o comando `flask run` ou rode o arquivo `run.py`.
   - O servidor estará disponível localmente em `http://localhost:5000`.

4. **Endpoints da API**:
   - **Listar Tarefas**:
     - **URL**: `/task`
     - **Método HTTP**: GET
     - **Descrição**: Retorna todas as tarefas cadastradas.

   - **Criar Nova Tarefa**:
     - **URL**: `/task`
     - **Método HTTP**: POST
     - **Descrição**: Cria uma nova tarefa com os dados fornecidos no corpo da requisição.
     - **Parâmetros do Corpo (JSON)**:
       - `titulo`: Título da tarefa (obrigatório)
       - `descricao`: Descrição da tarefa
       - `status`: Status da tarefa (default: "pendente")
       - `prioridade`: Prioridade da tarefa (default: "baixa")
       - `prazo`: Prazo da tarefa (formato: "YYYY-MM-DD HH:MM:SS")

5. **Estrutura do Projeto**:
   - `app/`: Contém os arquivos Python do aplicativo Flask.
     - `__init__.py`: Inicialização do aplicativo Flask e definição das rotas.
   - `instace` Contém o arquivo do db do SQLite
     - `taskmanager.db`: Arquivo do banco de dados SQLite.
   - `run.py` Contém o script para iniciar a API

6. **Tecnologias Utilizadas**:
   - **Flask**: Framework web para Python.
   - **SQLAlchemy**: ORM (Object-Relational Mapping) para Python.
   - **SQLite**: Banco de dados SQL embutido.

7. **Autor**:
   - Felipe.

---