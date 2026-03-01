from turtle import Turtle

# Configurações globais de estilo e posicionamento
ALIGNMENT = "left"               # Define a ancoragem do texto; 'left' mantém o placar fixo no canto superior
FONT = ("Courier", 20, "normal") # Estilo do nível; aumentar o tamanho pode sobrepor a área de jogo
FONT_GAME_OVER = ("Courier", 24, "bold") # Estilo de alerta; o negrito garante visibilidade sobre os carros

class Scoreboard(Turtle):
    """Gerencia a interface de usuário (UI), exibindo o progresso e o fim do jogo."""

    def __init__(self):
        """Inicializa o componente de texto herdando as capacidades gráficas da Turtle."""
        super().__init__()        # Herda métodos da Turtle para desenhar strings diretamente na tela
        self.color("black")       # Define a cor da fonte; preto é ideal para o fundo padrão branco
        self.penup()              # Garante que o objeto se mova para os cantos sem deixar rastros
        self.hideturtle()         # Oculta o cursor em forma de seta para exibir apenas o texto
        self.score = 1            # Contador de nível; dita a dificuldade atual no motor do jogo
        self.update_scoreboard()  # Realiza a primeira renderização do nível na tela

    def update_scoreboard(self):
        """Limpa o registro anterior e redesenha o nível atualizado na posição designada."""
        self.clear()              # Remove o texto anterior para evitar borrões e sobreposição
        self.goto(-280, 260)      # Posiciona o texto no canto superior esquerdo, fora da rota dos carros
        # Renderiza a string do nível usando as constantes de formatação definidas globalmente
        self.write(f"Level: {self.score}", align=ALIGNMENT, font=FONT)

    def total_score(self):
        """Soma um ponto ao nível e dispara a atualização visual após uma travessia bem-sucedida."""
        self.score += 1           # Incrementa o progresso do jogador
        self.update_scoreboard()  # Atualiza o visor para refletir a nova dificuldade

    def game_over(self):
        """Finaliza a interface exibindo a mensagem de encerramento no centro do visor."""
        
        self.goto(0, 0)           # Move o cursor para a origem central (0,0) para o anúncio final
        self.write("GAME OVER", align="center", font=FONT_GAME_OVER) # Exibe o aviso de derrota