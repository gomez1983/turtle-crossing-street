from turtle import Turtle
import random

# Configurações de cores e movimentação
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"] # Lista de cores disponíveis; expandir a lista aumenta a variedade visual do tráfego
STARTING_MOVE_DISTANCE = 5 # Deslocamento inicial em pixels; valores altos tornam o primeiro nível muito veloz
MOVE_INCREMENT = 2         # Ganho de velocidade por nível; valores altos criam uma curva de dificuldade agressiva
CARS_QUANTITY = 5          # Divisor de spawn inicial; valores baixos geram uma densidade de carros maior desde o início

# Definição das faixas de tráfego (Eixo Y)
INFERIOR_LIMIT = -220 # Início da zona de tráfego; subir este valor libera espaço na parte inferior da tela
SUPERIOR_LIMIT = 250  # Fim da zona de tráfego; descer este valor cria uma área de segurança antes da linha de chegada
TOTAL_SPACE = 30      # Intervalo entre faixas; valores menores que 20 causam sobreposição visual dos carros
POSITIONS = [y for y in range(INFERIOR_LIMIT, SUPERIOR_LIMIT + 1, TOTAL_SPACE)] # Lista que mapeia todas as rotas fixas possíveis

class CarManager:
    """Gerencia a frota de veículos, sua criação, movimento e progressão de dificuldade."""

    def __init__(self):
        """Inicializa o gerenciador com listas de controle e parâmetros de nível."""
        self.all_cars = []                     # Repositório de objetos Turtle representando os carros ativos
        self.car_speed = STARTING_MOVE_DISTANCE # Armazena a velocidade atual que dita o ritmo do jogo
        self.car_probability = CARS_QUANTITY    # Atributo dinâmico que controla a frequência de surgimento de novos carros

    def create_car(self):
        """Gera um novo objeto de carro na borda direita baseado na probabilidade atual."""
        # Se o número sorteado for 1, um carro é criado; menores car_probability aumentam a chance de sucesso
        if random.randint(1, self.car_probability) == 1: 
            new_car = Turtle("square") # Cria a base geométrica do veículo
            new_car.shapesize(stretch_wid=1, stretch_len=2) # Modifica a escala para atingir o formato retangular
            new_car.penup() # Garante que o carro não risque a tela ao se deslocar
            new_car.color(random.choice(COLORS)) # Atribui uma cor aleatória para diversidade visual
            
            # Posicionamento inicial na 'entrada' da rua
            random_y = random.choice(POSITIONS) # Seleciona uma das faixas horizontais pré-definidas
            new_car.goto(300, random_y) # Teleporta o carro para a extremidade direita da tela
            self.all_cars.append(new_car) # Registra o carro na lista para processamento de movimento e colisão

    def move_cars(self):
        """Desloca todos os carros ativos para a esquerda conforme a velocidade do nível."""
        for car in self.all_cars: # Itera individualmente sobre cada veículo presente na lista
            car.backward(self.car_speed) # Move o carro no sentido contrário ao seu cabeçalho original (esquerda)

    def increase_speed(self):
        """Eleva o desafio aumentando a velocidade de movimento e a densidade do tráfego."""
        self.car_speed += MOVE_INCREMENT # Soma o incremento à velocidade para reduzir o tempo de reação do jogador
        # Mecanismo de densidade dinâmica: reduz o intervalo de spawn até o limite de segurança de 1 em 2
        if self.car_probability > 2: # Impede que a probabilidade chegue a 1 (que geraria uma parede intransponível)
            self.car_probability -= 1 # Reduz o divisor para tornar a execução do create_car mais frequente