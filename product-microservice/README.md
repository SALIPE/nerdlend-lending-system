# Product Microservice

Este é o microserviço de gerenciamento de produtos, desenvolvido usando Django e Django REST Framework. Ele permite realizar operações CRUD para produtos e favoritos.

---

## **Requisitos**
- Python 3.10+
- PostgreSQL 14+
- Git
- Virtualenv (opcional, mas recomendado)

---

## **Passo a Passo para Configuração**

### 1. **Clone o Repositório**
```bash
git clone <URL_DO_REPOSITORIO>
cd product-microservice
```

### 2. **Crie um Ambiente Virtual**
(Recomendado para manter as dependências isoladas.)
```bash
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. **Instale as Dependências**
Certifique-se de estar no diretório `product-microservice` antes de rodar:
```bash
pip install -r requirements.txt
```

### 4. **Configure o Banco de Dados PostgreSQL**
1. Acesse o PostgreSQL:
   ```bash
   sudo -u postgres psql
   ```

2. Crie o banco de dados e o usuário:
   ```sql
   CREATE DATABASE product_db;
   CREATE USER product_user WITH PASSWORD 'secure_password';
   GRANT ALL PRIVILEGES ON DATABASE product_db TO product_user;
   ```

3. Atualize o arquivo `.env` com as credenciais do banco de dados:
   ```
   DATABASE_NAME=product_db
   DATABASE_USER=product_user
   DATABASE_PASSWORD=secure_password
   DATABASE_HOST=localhost
   DATABASE_PORT=5432
   SECRET_KEY=chave-secreta-segura
   DEBUG=True
   ALLOWED_HOSTS=127.0.0.1,localhost
   ```

4. Certifique-se de que o arquivo `.env` está no mesmo diretório que o `manage.py`.

### 5. **Aplique as Migrações**
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### 6. **Inicie o Servidor**
```bash
python3 manage.py runserver
```

O servidor estará disponível em `http://127.0.0.1:8000`.

---

## **Testando o Microservice**

### Endpoints Disponíveis
| Método | Endpoint         | Descrição                              |
|--------|------------------|----------------------------------------|
| GET    | `/products/`     | Lista todos os produtos.              |
| POST   | `/products/`     | Adiciona um novo produto.             |
| GET    | `/products/<id>/`| Detalhes de um produto específico.    |
| PUT    | `/products/<id>/`| Atualiza um produto existente.        |
| DELETE | `/products/<id>/`| Remove um produto.                    |

### Exemplo de Requisições

#### Adicionar um Produto
- **Endpoint:** `/products/`
- **Método:** `POST`
- **Corpo da Requisição:**
  ```json
  {
      "name": "Produto Teste",
      "description": "Descrição do Produto Teste",
      "price": 99.99,
      "stock": 10
  }
  ```

#### Listar Produtos
- **Endpoint:** `/products/`
- **Método:** `GET`

#### Atualizar um Produto
- **Endpoint:** `/products/<id>/`
- **Método:** `PUT`
- **Corpo da Requisição:**
  ```json
  {
      "name": "Produto Atualizado",
      "description": "Descrição Atualizada",
      "price": 109.99,
      "stock": 5
  }
  ```

#### Remover um Produto
- **Endpoint:** `/products/<id>/`
- **Método:** `DELETE`

---

## **Ferramentas para Teste**
Você pode testar os endpoints usando:
- **Postman** ou **Insomnia**.
- `cURL` no terminal.
- Interface web do Django REST Framework.

---



