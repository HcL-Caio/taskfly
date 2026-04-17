# 🦅 TaskFly - Gerenciador de Tarefas Gamificado
![CI](https://github.com/HcL-Caio/taskfly/actions/workflows/ci.yml/badge.svg)

**Versão Atual:** 1.0.0

---

## 🎯 Descrição do Problema Real
Pessoas com TDAH (Transtorno do Déficit de Atenção com Hiperatividade) ou dificuldades crônicas de foco frequentemente lutam para manter rotinas diárias. A falta de estímulo imediato ao concluir tarefas simples do dia a dia gera desmotivação, procrastinação e desorganização.

---

## 💡 Proposta da Solução
O **TaskFly** é uma aplicação de linha de comando (CLI) que utiliza a gamificação para transformar obrigações diárias em "missões". Ao concluir tarefas, o sistema fornece recompensas virtuais imediatas, estimulando o engajamento contínuo e ajudando na manutenção da rotina de forma lúdica.

Além disso, o sistema agora conta com **integração com API externa**, exibindo conselhos motivacionais dinâmicos ao usuário, reforçando o foco e a disciplina.

---

## 👥 Público-Alvo
Jovens e adultos com TDAH, estudantes, ou qualquer pessoa que tenha dificuldade em manter o foco e precise de um incentivo extra (sistema de recompensas) para completar suas tarefas diárias.

---

## ✨ Funcionalidades Principais
- 🎮 Sistema de recompensas (XP por tarefa)
- 📈 Progressão de níveis
- 🏆 Sistema de medalhas e conquistas
- 💾 Salvamento automático em JSON
- 🖥️ Interface CLI interativa
- 🌐 Integração com API de conselhos motivacionais
- 💡 Exibição de conselho do dia ao iniciar o sistema

---

## 🌐 API Utilizada
Este projeto utiliza a API pública **Advice Slip**:

👉 https://api.adviceslip.com/

A API fornece conselhos motivacionais aleatórios que são exibidos ao iniciar a aplicação, tornando a experiência mais dinâmica e engajadora.

---

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3.x
- **Persistência de Dados:** JSON (biblioteca nativa)
- **Consumo de API:** Requests
- **Testes Automatizados:** Pytest
- **Padronização e Linting:** Flake8 (PEP 8)
- **Integração Contínua (CI):** GitHub Actions

---

## ⚙️ Instalação e Execução

```bash
### 1. Clonar o repositório
- git clone https://github.com/HcL-Caio/taskfly.git
- cd taskfly

### 2. Instalar dependências
pip install -r requirements.txt

### 3. Executar o sistema
python src/main.py

### 4. Executar Testes
pytest

### 5. Executar Lint
flake8 . --max-line-length=100

### 6. Estrutura do Projeto
taskfly/
│── src/
│   ├── main.py
│   ├── core.py
│   └── api.py
│
│── tests/
│   └── test_api.py
│
│── .github/workflows/
│   └── ci.yml
│
│── requirements.txt
│── README.md

### 7. Integração Contínua (CI)

O projeto utiliza GitHub Actions para garantir qualidade automática do código:

- Instala dependências
- Executa lint (flake8)
- Executa testes automatizados (pytest)

Tudo isso roda automaticamente a cada push ou pull request.

### 8. Funcionalidade da Etapa Intermediária

Foi implementada a integração com uma API externa (Advice Slip), permitindo que o sistema exiba conselhos motivacionais em tempo real.

Essa funcionalidade adiciona valor ao projeto ao tornar a experiência mais interativa e incentivar o usuário a manter consistência nas tarefas.

### 9. Versionamento

Versão atual: 1.0.0

### 10. Autor

Caio Siqueira Amaral

### 11. Repositório

https://github.com/HcL-Caio/taskfly
