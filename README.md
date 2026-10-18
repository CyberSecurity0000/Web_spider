<div align="center">

# 🕷️ Web Spider

### Um pequeno spider em Python para coletar links de páginas web

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Requests](https://img.shields.io/badge/HTTP-Requests-2E8B57)
![BeautifulSoup](https://img.shields.io/badge/HTML-BeautifulSoup4-2F6F44)
![Status](https://img.shields.io/badge/Projeto-Educacional-blue)

**Reconhecimento Web • Extração de Links • Python • Segurança**

[📂 Acessar Repositório](https://github.com/CyberSecurity0000/Web_spider)

</div>

---

## 📌 Sobre o Projeto

O **Web Spider** é um projeto desenvolvido em Python com o objetivo de praticar requisições HTTP, análise de HTML e extração automatizada de links.

A ferramenta acessa uma página web, analisa seu conteúdo HTML e identifica links encontrados nas tags `<a>`.

O projeto faz parte da minha jornada de estudos em programação, reconhecimento web e cibersegurança.

## ⚙️ Como Funciona

O funcionamento do programa pode ser dividido nas seguintes etapas:

1. 🌐 **Requisição HTTP:** acessa a página especificada.
2. 📡 **Resposta do servidor:** verifica o código de status HTTP.
3. 🧩 **Análise HTML:** utiliza BeautifulSoup para interpretar o conteúdo recebido.
4. 🔎 **Extração de links:** procura tags `<a>` e lê seus atributos `href`.
5. 🧹 **Organização:** filtra links HTTP/HTTPS e remove duplicatas.
6. 📋 **Exibição:** ordena os resultados e apresenta os links encontrados.

> **Observação:** a versão atual analisa os links encontrados na página consultada. Isso não significa que navegue automaticamente por todos os links encontrados.

## 🧰 Tecnologias Utilizadas

| Tecnologia | Finalidade |
|---|---|
| 🐍 Python 3 | Linguagem de programação |
| 🌐 Requests | Envio de requisições HTTP |
| 🧩 BeautifulSoup 4 | Análise e extração de informações do HTML |
| 📦 `set()` | Remoção de elementos duplicados |
| 🔤 `sorted()` | Ordenação dos resultados |

## 🚀 Instalação e Execução

### 1. Clonar o repositório

```bash
git clone https://github.com/CyberSecurity0000/Web_spider.git
```

### 2. Entrar no diretório

```bash
cd Web_spider
```

### 3. Criar um ambiente virtual

```bash
python3 -m venv .venv
```

### 4. Ativar o ambiente virtual no Linux

```bash
source .venv/bin/activate
```

### 5. Instalar as dependências

```bash
python -m pip install requests beautifulsoup4
```

### 6. Executar o programa

O script principal está localizado na pasta `Programs/`.

Substitua `<arquivo.py>` pelo nome real do script:

```bash
python3 Programs/<arquivo.py> https://example.com
```

**Nota:** esse exemplo pressupõe que o programa receba a URL como argumento. Caso a entrada seja configurada de outra maneira no código, ajuste o comando de acordo com a implementação.

## 🧪 Conceitos Praticados

Este projeto ajuda a desenvolver conhecimentos em:

- Requisições HTTP e códigos de status.
- Respostas de servidores web.
- Estrutura e análise de HTML.
- Tags HTML e atributos `href`.
- Listas, conjuntos e ordenação em Python.
- Bibliotecas externas e gerenciamento de dependências.
- Fundamentos de reconhecimento web.

## ⚠️ Limitações Conhecidas

- O programa analisa o HTML recebido na resposta inicial.
- Links criados dinamicamente por JavaScript podem não aparecer no HTML recebido.
- Links relativos, como `/about`, podem exigir tratamento adicional para serem convertidos em URLs completas.
- Encontrar um link não garante que ele esteja ativo ou acessível.
- A versão atual não representa um crawler recursivo completo nem um scanner de vulnerabilidades.

## 🔐 Uso Responsável

O Web Spider é destinado a estudos, experimentação e reconhecimento web em ambientes autorizados.

Utilize a ferramenta respeitando as regras dos serviços acessados, os limites de requisições e as autorizações aplicáveis.

Evite gerar tráfego excessivo e não utilize a ferramenta contra sistemas sem permissão.

## 🗺️ Melhorias Futuras

- [ ] Converter links relativos em URLs absolutas.
- [ ] Implementar tratamento de erros e timeouts.
- [ ] Salvar os resultados em arquivos.
- [ ] Adicionar filtros por domínio.
- [ ] Melhorar os argumentos de linha de comando.
- [ ] Implementar testes automatizados.
- [ ] Avaliar a possibilidade de rastreamento recursivo de links.

## 👨‍💻 Autor

**CyberSecurity0000**

Projeto pessoal de aprendizagem contínua em Python, reconhecimento web e cibersegurança.

📂 **GitHub:** [CyberSecurity0000/Web_spider](https://github.com/CyberSecurity0000/Web_spider)

---

<div align="center">

### 🧠 BRAIN

**Não aceite respostas; descubra como e por quê.**

</div>
