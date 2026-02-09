Feeding System - Backend Integration
Este projeto é um sistema de gerenciamento de usuários desenvolvido em Python, focado na integração robusta com o banco de dados relacional PostgreSQL. O objetivo principal foi migrar uma estrutura de dados volátil (listas em memória) para uma solução de persistência real e segura.

 O que foi implementado
Persistência de Dados: Integração total com PostgreSQL utilizando o driver psycopg2.

Arquitetura Modular: Divisão do código em módulos de conexão (database.py), validação (validacoes.py) e lógica de negócio (banco.py).

Segurança e Integridade:
# feeding

Uso de Constraints SQL (UNIQUE) para garantir que nomes de usuários não se dupliquem diretamente no banco.

Prevenção contra SQL Injection através de consultas parametrizadas.

Tratamento de exceções com blocos try/except/finally para gestão de erros de conexão e integridade.

Gestão de Recursos: Implementação de fechamento automático de conexões e cursores para evitar vazamento de memória.

Versionamento Seguro: Configuração estratégica de .gitignore para proteção de ambientes virtuais (venv), caches e variáveis de ambiente sensíveis.

Tecnologias Utilizadas:
Linguagem: Python 3

Banco de Dados: PostgreSQL

Driver de Conexão: Psycopg2-binary

Ambiente: Linux (Ubuntu)

Ferramenta de Gestão DB: DBeaver

Práticas de Segurança Aplicadas:
Isolamento de Credenciais: Preparado para uso de .env.

Robustez de Transações: Uso de commit e rollback para garantir que o banco nunca fique em estado inconsistente após um erro.

Validação em Duas Camadas: Verificação lógica via código e restrição física via Schema do Banco de Dados.
