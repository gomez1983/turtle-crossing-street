import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Configurações iniciais da janela e motor gráfico
screen = Screen() # Cria a instância da janela principal do jogo
screen.setup(width=600, height=600) # Define dimensões; 600x600 equilibra a área de tráfego e o tempo de reação
screen.tracer(0) # Desativa animações automáticas para permitir o controle manual via screen.update()

# Inicialização dos objetos do jogo através de Composição
player = Player((0, -280)) # Instancia o jogador na base da tela (eixo Y negativo)
car_manager = CarManager() # Instancia o controlador de frota, velocidade e densidade de carros
scoreboard = Scoreboard()  # Instancia a interface de placar e carregamento de recorde (High Score)

# Configuração de entradas do teclado
screen.listen() # Habilita o foco da janela para capturar eventos de teclas do usuário

# Mapeamento de movimentação: associa teclas às funções de controle de estado (flags)
screen.onkeypress(player.start_up, "Up")     # Inicia o movimento ascendente ao segurar a tecla
screen.onkeyrelease(player.stop_up, "Up")    # Interrompe o movimento ascendente ao soltar a tecla
screen.onkeypress(player.start_down, "Down") # Inicia o movimento descendente ao segurar a tecla
screen.onkeyrelease(player.stop_down, "Down") # Interrompe o movimento descendente ao soltar a tecla

# Controle de fluxo do jogo
game_is_on = True # Variável booleana que mantém o loop principal em execução

# Loop de execução principal (Game Loop)

while game_is_on:
    time.sleep(0.05)         # Sincronização de frames; valores menores (ex: 0.02) aumentam o FPS e a fluidez
    player.update_position() # Aplica o deslocamento do jogador baseado nas teclas ativas
    screen.update()          # Renderiza todas as mudanças de posição de uma só vez para evitar cintilação

    # Gerenciamento de tráfego
    car_manager.create_car() # Executa a tentativa de spawn de um novo carro conforme a probabilidade do nível
    car_manager.move_cars()   # Desloca todos os carros ativos para a esquerda

    # Verificação da condição de vitória (Travessia concluída com sucesso)
    if player.player.ycor() > 240: # Checa se a tartaruga atingiu a zona de segurança superior
        player.go_to_start()       # Retorna o jogador para a base sem reiniciar o jogo
        car_manager.increase_speed() # Incrementa a dificuldade (velocidade/spawn) para o próximo nível
        scoreboard.total_score()   # Atualiza o nível visual no placar
        print(f"A tartaruga atravessou a rua em segurança! Você foi para o level {scoreboard.score}")

    # Verificação da condição de derrota (Colisão detectada)
    for car in car_manager.all_cars: # Percorre a lista de carros para checar distâncias individuais
        if car.distance(player.player) < 20: # Limite de proximidade física entre a tartaruga e o veículo
            scoreboard.reset_score() # Compara o nível atual com o recorde e salva no arquivo data.txt
            game_is_on = False       # Interrompe a execução do loop principal
            scoreboard.game_over()   # Renderiza a mensagem de fim de jogo no centro da tela
            print("GAME OVER! Você foi atropelado.") # Log final no console

# Finalização do ambiente
screen.exitonclick() # Mantém a janela aberta após o término para análise do placar final