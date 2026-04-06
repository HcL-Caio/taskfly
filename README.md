# 🦅 TaskFly - Gerenciador de Tarefas Gamificado
![CI](https://github.com/HcL-Caio/taskfly/actions/workflows/ci.yml/badge.svg)

**Versão Atual:** 1.0.0

## 🎯 Descrição do Problema Real
Pessoas com TDAH (Transtorno do Déficit de Atenção com Hiperatividade) ou dificuldades crônicas de foco frequentemente lutam para manter rotinas diárias. A falta de estímulo imediato ao concluir tarefas simples do dia a dia gera desmotivação, procrastinação e desorganização.

## 💡 Proposta da Solução
O **TaskFly** é uma aplicação de linha de comando (CLI) que utiliza a gamificação para transformar obrigações diárias em "missões". Ao concluir tarefas, o sistema fornece recompensas virtuais imediatas, estimulando o engajamento contínuo e ajudando na manutenção da rotina de forma lúdica.

## 👥 Público-Alvo
Jovens e adultos com TDAH, estudantes, ou qualquer pessoa que tenha dificuldade em manter o foco e precise de um incentivo extra (sistema de recompensas) para completar suas tarefas diárias.

## ✨ Funcionalidades Principais
- **Sistema de Recompensas:** Ganhe pontos de experiência (XP) baseados na dificuldade da tarefa concluída (Fácil: 10, Médio: 20, Difícil: 50).
- **Progressão de Níveis:** A cada 100 XP acumulados, o usuário sobe de nível.
- **Conquistas e Medalhas:** Desbloqueio de medalhas automáticas ao atingir marcos específicos (ex: "Iniciante Alado" no Nível 2).
- **Persistência de Dados:** O progresso do usuário é salvo automaticamente em um arquivo `taskfly_data.json` local.
- **Interface CLI:** Menu interativo no terminal para gerenciar as tarefas e visualizar o status do jogador.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3.x
- **Persistência de Dados:** JSON (biblioteca nativa)
- **Testes Automatizados:** Pytest
- **Padronização e Linting:** Flake8 (Padrão PEP 8)
- **Integração Contínua (CI):** GitHub Actions

---

## 🚀 Instruções de Instalação

1. Clone este repositório para a sua máquina local:
   ```bash
   git clone [https://github.com/](https://github.com/)HcL-Caio/taskfly.git
