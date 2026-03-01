# 🐢 Turtle Crossing Street

Um jogo de travessia inspirado no clássico Frogger, desenvolvido em Python utilizando a biblioteca gráfica **Turtle**. O objetivo é levar a tartaruga até o topo da tela desviando de um tráfego de carros que aumenta de velocidade e densidade a cada nível concluído.

## 🚀 Funcionalidades

* **Movimentação Fluida**: Sistema de *flags* que permite movimento contínuo ao segurar as teclas.
* **Dificuldade Dinâmica**: A cada nível, os carros aumentam a velocidade e a frequência de surgimento.
* **Gerenciamento de Colisão**: Detecção precisa baseada em distância entre objetos.
* **Interface de Usuário (UI)**: Placar em tempo real indicando o nível atual e tela de Game Over.

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**: Linguagem base.
* **Turtle Graphics**: Biblioteca nativa para interface gráfica e renderização.
* **Programação Orientada a Objetos (POO)**: Estrutura baseada em classes (`Player`, `CarManager`, `Scoreboard`).

## 📋 Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina. Não é necessário instalar bibliotecas externas, pois o `turtle` e o `time` já fazem parte da biblioteca padrão do Python.

## 🎮 Controles
* **Seta para Cima (Up):** Move a tartaruga para frente.

* **Seta para Baixo (Down):** Move a tartaruga para trás.

## 🏗️ Estrutura do Projeto
* **main.py:** O motor principal do jogo e controle do loop de execução.

* **player.py:** Define o comportamento e restrições do jogador.

* **car_manager.py:** Lógica de geração dinâmica e aceleração dos inimigos.

* **scoreboard.py:** Responsável por toda a comunicação visual com o usuário.

## 📝 Práticas de Mercado Aplicadas
* **Composição:** O main.py utiliza instâncias das classes para manter o código limpo.

* **Encapsulamento:** Lógicas específicas (como o aumento de velocidade) ficam restritas às suas respectivas classes.

* **Clean Code:** Variáveis constantes globais para fácil ajuste de equilíbrio (game design).

* **Documentação:** Código totalmente comentado e documentado com Docstrings.
