import pgzrun
from plataforma import *

# our plataforma constants
TILE_SIZE = 18
ROWS = 30
COLS = 20

# Pygame Constants
WIDTH = TILE_SIZE * ROWS
HEIGHT = TILE_SIZE * COLS
TITLE = "Raposa Invernal"

# Game states
MENU = 0
GAME = 1
GAME_OVER = 2
WIN = 3
current_state = MENU

# Menu options
menu_options = ["Jogar", "Sair"]
selected_option = 0

# bild world
plataformas = build("plataforma_plataformas.csv", TILE_SIZE)
obstaculos = build("plataforma_obstaculos.csv", TILE_SIZE)
cactos = build("plataforma_cactos.csv", TILE_SIZE)

#define Sprites
# Sprite("sprite_image.png", start, num_frames, color_key, refresh)
color_key = (0, 0, 0)
fox_stand = Sprite("fox.png", (0, 32, 32, 32), 14, color_key, 30)
fox_walk = Sprite("fox.png", (0, 64, 32, 32), 8, color_key, 5)
 
# define player Actor
player = SpriteActor(fox_stand)
player.bottomleft = (0, HEIGHT - TILE_SIZE)
# define Actor-specific variables
player.velocity_x = 3
player.velocity_y = 0
player.jumping = False
player.alive = True
player.scale = 1

# define global variables
gravity = 1
jump_velocity = -10
#over = False
#win = False

def reset_game():
    """Resets the game to its initial state."""
    global plataformas, obstaculos, cactos, player, over, win
    # Rebuild the world
    plataformas = build("plataforma_plataformas.csv", TILE_SIZE)
    obstaculos = build("plataforma_obstaculos.csv", TILE_SIZE)
    cactos = build("plataforma_cactos.csv", TILE_SIZE)
    
    # Reset player
    player.bottomleft = (0, HEIGHT - TILE_SIZE)
    player.velocity_x = 3
    player.velocity_y = 0
    player.jumping = False
    player.alive = True
    player.sprite = fox_stand
    player._flip_x = False
    
    over = False
    win = False

def draw():
    screen.clear()
    screen.fill("skyblue")

    if current_state == MENU:
        draw_menu()
    elif current_state == GAME:
        draw_game()
    elif current_state == GAME_OVER:
        draw_game_over()
    elif current_state == WIN:
        draw_win()

def draw_menu():
    screen.draw.text("Raposa Invernal", center=(WIDTH / 2, HEIGHT / 4), fontsize=60, color="white")
    for i, option in enumerate(menu_options):
        color = "white"
        if i == selected_option:
            color = "yellow"  # Highlight selected option
        screen.draw.text(option, center=(WIDTH / 2, HEIGHT / 2 + i * 30), fontsize=40, color=color)

def draw_game():
    # draw all plataformas
    for plataforma in plataformas:
        plataforma.draw()
    # draw all obstaculos
    for obstaculo in obstaculos:
        obstaculo.draw()
    # draw cactos
    for cacto in cactos:
        cacto.draw()

    # draw the player
    if player.alive:
        player.draw()

def draw_game_over():
    screen.draw.text("Game Over!", center=(WIDTH / 2, HEIGHT / 2), fontsize=60, color="red")
    screen.draw.text("Pressione ESPAÇO para voltar ao Menu", center=(WIDTH / 2, HEIGHT / 2 + 50), fontsize=30, color="white")

def draw_win():
    screen.draw.text("Você Ganhou!", center=(WIDTH / 2, HEIGHT / 2), fontsize=60, color="black")
    screen.draw.text("Pressione ESPAÇO para voltar ao Menu", center=(WIDTH / 2, HEIGHT / 2 + 50), fontsize=30, color="white")

def update():
    global current_state, over, win

    if current_state == GAME:
        update_game()

def update_game():
    global current_state, over, win
    # handle left movement
    if keyboard.LEFT and player.midleft[0] > 0:
        player.x -= player.velocity_x
        player.sprite = fox_walk
        player._flip_x = True
        # if the player collided with a plataforma
        if player.collidelist(plataformas) != -1:
            #get object that the player collided with
            object = plataformas[player.collidelist(plataformas)]
            player.x = object.x + (object.width / 2 + player.width / 2)

    # handle right movement
    elif keyboard.RIGHT and player.midright[0] < WIDTH:
        player.x += player.velocity_x
        player.sprite = fox_walk
        player._flip_x = False
        # if the player collided with a plataforma
        if player.collidelist(plataformas) != -1:
            #get object that the player collided with
            object = plataformas[player.collidelist(plataformas)]
            player.x = object.x - (object.width / 2 + player.width / 2)

    # handle gravity
    player.y += player.velocity_y
    player.velocity_y += gravity
    # if the player collided with a plataforma
    if player.collidelist(plataformas) != -1:
        #get object that the player collided with
        object = plataformas[player.collidelist(plataformas)]
        #moving down -> hit the ground
        if player.velocity_y >= 0:
            player.y = object.y - (object.height / 2 + player.height / 2)
            player.jumping = False
        #moving up -> hit their head
        else:
            player.y = object.y + (object.height / 2 + player.height / 2)
        player.velocity_y = 0

    #check collision with obstaculos
    if player.collidelist(obstaculos) != -1:
        player.alive = False
        current_state = GAME_OVER

    # check cacto collision
    for cacto in cactos:
        if player.colliderect(cacto):
            cactos.remove(cacto)

    if len(cactos) == 0:
        current_state = WIN

def on_key_down(key):
    global current_state, selected_option
    
    if current_state == MENU:
        if key == keys.UP:
            selected_option = (selected_option - 1) % len(menu_options)
        elif key == keys.DOWN:
            selected_option = (selected_option + 1) % len(menu_options)
        elif key == keys.RETURN:
            if selected_option == 0:  # "Jogar" selected
                current_state = GAME
                reset_game()
            elif selected_option == 1:  # "Sair" selected
                exit()
    elif current_state == GAME_OVER or current_state == WIN:
        if key == keys.SPACE:
            current_state = MENU

    elif current_state == GAME:
        if key == keys.UP and not player.jumping:
            player.velocity_y = jump_velocity
            player.jumping = True

def on_key_up(key):
    if current_state == GAME:
        if key == keys.LEFT or key == keys.RIGHT:
            player.sprite = fox_stand
    

pgzrun.go()