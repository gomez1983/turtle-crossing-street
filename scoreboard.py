from turtle import Turtle

# Configurações globais de estilo e posicionamento
ALIGNMENT = "left"               # Ancoragem do texto; 'left' fixa o início da frase no ponto de destino
FONT = ("Courier", 20, "normal") # Estilo do texto; aumentar o tamanho pode invadir a área de jogo dos carros
FONT_GAME_OVER = ("Courier", 24, "bold") # Fonte de destaque; o negrito garante leitura sobreposta ao tráfego

class Scoreboard(Turtle):
    """Gerencia a interface de usuário (UI), persistência de recorde em disco e estado do jogo."""

    def __init__(self):
        """Inicializa o sistema de placar, herdando de Turtle e carregando o arquivo de dados."""
        super().__init__()           # Ativa herança de Turtle para realizar desenhos e escritas na tela
        self.color("black")          # Define a cor da fonte; preto contrasta com o fundo padrão da Screen
        self.penup()                 # Levanta a caneta para evitar rastros durante o posicionamento do placar
        self.hideturtle()            # Oculta o ícone da tartaruga, deixando apenas o texto visível
        self.score = 1               # Atributo do nível atual; define a dificuldade progressiva
        
        # Leitura persistente: abre o arquivo TXT para recuperar o recorde salvo anteriormente
        with open("data.txt") as data:
            self.high_score = int(data.read()) # Converte o texto do arquivo em número inteiro
            
        self.update_scoreboard()     # Realiza a renderização visual inicial dos dados carregados

    def update_scoreboard(self):
        """Limpa o visor e redesenha o Nível e o High Score em posições distintas para evitar sobreposição."""
        self.clear()                 # Apaga a escrita anterior para evitar borrões de sobreposição de números
        
        # Posicionamento e escrita do Nível Atual no canto superior esquerdo
        self.goto(-280, 260)         # Coordenadas fixas fora da zona de movimentação dos carros
        self.write(f"Level: {self.score}", align=ALIGNMENT, font=FONT)
        
        # Posicionamento e escrita do Recorde (High Score) no topo central/direito
        self.goto(0, 260)            # Desloca o cursor horizontalmente para separar as informações
        self.write(f"High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        """Atualiza o recorde no sistema, sobrescreve o arquivo TXT e reinicia o contador de nível."""
        if self.score > self.high_score:    # Checa se o desempenho atual superou o recorde histórico
            self.high_score = self.score   # Atualiza o atributo em tempo de execução
            # Gravação em disco: o modo 'w' apaga o valor antigo e insere o novo recorde
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        
        self.score = 1                     # Reseta o progresso do jogador para o nível inicial
        self.update_scoreboard()           # Atualiza a tela com os novos valores (ou valores resetados)

    def total_score(self):
        """Soma um ponto ao nível e atualiza a interface após uma travessia concluída."""
        self.score += 1                    # Incrementa o nível de dificuldade
        self.update_scoreboard()           # Redesenha o placar com o novo nível

    def game_over(self):
        """Exibe a mensagem final de derrota no centro da tela ao detectar colisão."""
        
        self.goto(0, 0)                    # Move para a origem central para máxima visibilidade do aviso
        self.write("GAME OVER", align="center", font=FONT_GAME_OVER) # Anuncia o fim da partida