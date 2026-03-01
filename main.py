import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Configurações iniciais da janela e motor gráfico
screen = Screen() # Cria a instância da janela principal
screen.setup(width=600, height=600) # Define dimensões; 600x600 equilibra área de jogo e tempo de travessia
screen.tracer(0) # Desativa animações automáticas; essencial para fluidez (FPS) e sincronia com screen.update()

# Inicialização dos objetos do jogo através de Composição
player = Player((0, -280)) # Instancia o jogador na posição inicial inferior
car_manager = CarManager() # Instancia o gerenciador de tráfego e dificuldade
scoreboard = Scoreboard() # Instancia o sistema de interface de usuário (UI) e placar

# Configuração de entradas do teclado
screen.listen() # Foca a janela para capturar comandos do teclado

# Mapeamento de movimentação: associa teclas às funções de controle de estado (flags)
screen.onkeypress(player.start_up, "Up") # Ativa movimento para cima ao pressionar
screen.onkeyrelease(player.stop_up, "Up") # Interrompe movimento para cima ao soltar
screen.onkeypress(player.start_down, "Down") # Ativa movimento para baixo ao pressionar
screen.onkeyrelease(player.stop_down, "Down") # Interrompe movimento para baixo ao soltar

# Controle de fluxo do jogo
game_is_on = True # Variável booleana que sustenta a execução do motor do jogo

# Loop de execução principal (Game Loop)
while game_is_on:
    time.sleep(0.05) # Define o FPS; valores menores (ex: 0.02) tornam o jogo mais rápido e fluido
    player.update_position() # Processa o deslocamento do jogador baseado nas teclas pressionadas
    screen.update() # Renderiza todas as mudanças de posição na tela simultaneamente

    # Gerenciamento de tráfego
    car_manager.create_car() # Tenta gerar um novo carro baseado na probabilidade atual
    car_manager.move_cars() # Atualiza a posição X de todos os carros ativos na lista

    # Verificação da condição de vitória (Travessia concluída)
    if player.player.ycor() > 240: # Checa se a tartaruga ultrapassou a linha de chegada superior
        player.go_to_start() # Reseta a posição física do jogador para o início
        car_manager.increase_speed() # Eleva a dificuldade (velocidade e densidade) para a próxima rodada
        scoreboard.total_score() # Incrementa o nível visual no placar
        print("Jogo finalizado. A tartaruga atravessou a rua em segurança!") # Feedback no console

    # Verificação da condição de derrota (Colisão)
    for car in car_manager.all_cars: # Itera sobre cada carro em movimento na tela
        if car.distance(player.player) < 20: # Checa proximidade; 20px é o limite do corpo da tartaruga
            game_is_on = False # Quebra o loop principal para interromper o jogo
            scoreboard.game_over() # Exibe a mensagem de derrota na tela
            print ("GAME OVER! Você foi atropelado.") # Feedback de encerramento no console

# Finalização
screen.exitonclick() # Mantém a janela ativa para visualização do placar final até o clique do usuário