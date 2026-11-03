# 🏦 PyBank

Um sistema bancário desenvolvido em **Python**, utilizando **Programação Orientada a Objetos (POO)** e **Flask** para criar uma interface web.

O projeto foi desenvolvido como forma de praticar conceitos de programação, desenvolvimento web, organização de projetos e integração entre backend e frontend.

## 🌐 Demonstração

Você pode acessar o PyBank online:

👉 **https://pybank-6qrp.onrender.com**

## 📌 Sobre o projeto

O PyBank simula um sistema bancário simples onde é possível cadastrar duas contas e realizar diferentes operações financeiras.

O projeto começou como uma aplicação executada diretamente pelo terminal e posteriormente evoluiu para uma aplicação web utilizando Flask.

A principal ideia foi transformar conceitos de **Python e POO** em uma aplicação prática e acessível pelo navegador.

## ⚙️ Funcionalidades

- 👤 Cadastro de duas contas bancárias
- 💰 Definição de saldo inicial
- ➕ Depósito
- ➖ Saque
- 🏦 Guardar dinheiro
- 💸 Resgatar dinheiro guardado
- 📊 Visualização dos saldos
- 📜 Histórico de movimentações
- 🔄 Reinício da sessão
- 🌐 Interface web
- 🚀 Aplicação hospedada online

## 🧠 Conceitos praticados

Durante o desenvolvimento foram trabalhados conceitos como:

- Variáveis e tipos de dados
- Condicionais
- Funções
- Listas
- Métodos
- Classes e objetos
- Construtores (`__init__`)
- Atributos de objetos
- Encapsulamento básico
- Programação Orientada a Objetos
- Manipulação de formulários
- Rotas com Flask
- Templates HTML
- CSS
- Git e GitHub
- Deploy de aplicações web

## 🛠️ Tecnologias utilizadas

### Backend

- **Python**
- **Flask**
- **Gunicorn**

### Frontend

- **HTML5**
- **CSS3**
- **Jinja2**

### Ferramentas

- **Visual Studio Code**
- **Git**
- **GitHub**
- **Render**

## 📁 Estrutura do projeto

```text
PyBank/
│
├── app.py
├── banco.py
├── requirements.txt
├── .gitignore
│
├── templates/
│   ├── cadastro.html
│   └── index.html
│
└── static/
    └── style.css
```

### `app.py`

Responsável pela aplicação Flask, pelas rotas, formulários e comunicação entre o frontend e as classes do sistema bancário.

### `banco.py`

Contém a classe `Conta`, responsável pelas informações e operações de cada conta bancária.

### `templates/`

Contém as páginas HTML utilizadas pela aplicação.

### `static/`

Contém os arquivos estáticos, como o CSS responsável pelo visual da aplicação.

### `requirements.txt`

Lista as bibliotecas necessárias para executar o projeto.

## 🚀 Como executar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/src-Yur1/PYbank.git
```

### 2. Entre na pasta

```bash
cd PYbank
```

### 3. Crie um ambiente virtual

```bash
python -m venv .venv
```

### 4. Ative o ambiente virtual

No Windows:

```bash
.venv\Scripts\activate
```

### 5. Instale as dependências

```bash
pip install -r requirements.txt
```

### 6. Execute a aplicação

```bash
python app.py
```

Depois, abra no navegador:

```text
http://127.0.0.1:5000
```

## 🌍 Deploy

O PyBank está hospedado utilizando o **Render**.

O projeto utiliza o **Gunicorn** como servidor para executar a aplicação Flask em produção.

### Comando utilizado no deploy

```bash
gunicorn app:app
```

## ⚠️ Observação

Atualmente, os dados das contas são armazenados apenas na memória da aplicação.

Isso significa que as contas cadastradas podem ser perdidas caso o servidor seja reiniciado.

Essa limitação faz parte da versão atual do projeto e abre espaço para futuras melhorias, como a implementação de um banco de dados.

## 🔮 Próximos passos

Algumas melhorias planejadas para versões futuras:

- [ ] Implementar banco de dados
- [ ] Utilizar SQLite
- [ ] Criar sistema de login
- [ ] Permitir cadastro de mais contas
- [ ] Melhorar validações dos formulários
- [ ] Adicionar autenticação de usuários
- [ ] Criar uma área individual para cada cliente
- [ ] Melhorar o histórico de transações
- [ ] Adicionar gráficos financeiros
- [ ] Melhorar a segurança da aplicação

## 📚 Objetivo acadêmico

O PyBank foi desenvolvido como projeto prático durante minha formação em **Ciência da Computação**, com o objetivo de aplicar conhecimentos de programação em uma aplicação real.

O projeto também representa minha evolução no aprendizado de **Python, Programação Orientada a Objetos, desenvolvimento web e ferramentas utilizadas no desenvolvimento de software**.

---

## 👨‍💻 Autor

**Yuri Gabriel**

Estudante de Ciência da Computação.

### 🔗 Projeto

**GitHub:**  
https://github.com/src-Yur1/PYbank

**Aplicação online:**  
https://pybank-6qrp.onrender.com

---

⭐ Se este projeto foi útil ou interessante, considere deixar uma estrela no repositório!
