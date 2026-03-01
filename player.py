from turtle import Turtle

# Constantes globais de configuração do jogador
STARTING_POSITION = (0, -280) # Ponto de partida; alterar o Y para valores menores desce a posição inicial
MOVE_DISTANCE = 10            # Passo de movimento; valores maiores tornam o jogador mais veloz e difícil de controlar
FINISH_LINE_Y = 280           # Linha de chegada; reduzir este valor encurta a distância da travessia e o tempo de jogo

class Player:
    """Gerencia a criação, movimentação e estado do jogador (Tartaruga)."""
    
    def __init__(self, position):
        """Inicializa os estados de movimento e a representação visual do jogador."""
        self.move_speed = 10          # Pixels deslocados por ciclo; define a agilidade de resposta do comando
        self.is_moving_up = False     # Flag para detecção de tecla 'seta para cima' pressionada
        self.is_moving_down = False   # Flag para detecção de tecla 'seta para baixo' pressionada
        self.create_player(position)  # Executa a montagem do objeto gráfico na tela

    # Métodos de controle de estado (Flags) para os eventos de teclado (onkeypress/onkeyrelease)
    def start_up(self): 
        """Sinaliza que o comando para subir foi ativado."""
        self.is_moving_up = True
        
    def stop_up(self): 
        """Sinaliza que o comando para subir foi interrompido."""
        self.is_moving_up = False
        
    def start_down(self): 
        """Sinaliza que o comando para descer foi ativado."""
        self.is_moving_down = True
        
    def stop_down(self): 
        """Sinaliza que o comando para descer foi interrompido."""
        self.is_moving_down = False

    def create_player(self, position):
        """Configura a instância física da Turtle que representa o jogador."""
        self.player = Turtle()         # Instancia o objeto Turtle via composição
        self.player.shape("turtle")    # Aplica o ícone visual de tartaruga ao jogador
        self.player.color("Black")     # Define a cor do preenchimento e contorno
        self.player.setheading(90)     # Rotaciona o ícone para apontar para o norte (topo da tela)
        self.player.penup()            # Desativa o rastro de desenho durante o deslocamento
        self.player.goto(position)     # Posiciona a tartaruga na coordenada inicial recebida

    def update_position(self):
        """Aplica o deslocamento nas coordenadas Y conforme as flags de movimento ativas."""
        # Processa subida respeitando a barreira superior de 250px
        if self.is_moving_up and self.player.ycor() < 250:
            new_y = self.player.ycor() + self.move_speed
            self.player.goto(self.player.xcor(), new_y)
            
        # Processa descida respeitando a barreira inferior de -250px
        if self.is_moving_down and self.player.ycor() > -250:
            new_y = self.player.ycor() - self.move_speed
            self.player.goto(self.player.xcor(), new_y)

    def go_to_start(self):
        """Reseta a posição do jogador para a base após uma vitória ou reinício."""
        self.player.goto(0, -280) # Teleporta a tartaruga para o eixo central inferior