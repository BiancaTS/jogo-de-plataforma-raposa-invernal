# 🥚 Raposa Invernal

**Raposa Invernal** é um jogo de plataforma 2D desenvolvido em [PgZero](https://pygame-zero.readthedocs.io/) com arte em pixel retrô. O jogador controla uma raposa aventureira que precisa explorar uma terra congelada, evitar obstáculos perigosos e coletar todos os cactos espalhados pelo cenário para alcançar a vitória.

## 🎮 Gameplay

* **Gênero:** Plataforma 2D
* **Estilo Visual:** Pixel Art (estética retrô)
* **Objetivo:** Coletar todos os cactos e evitar os obstáculos para vencer
* **Plataformas:** Desktop (Python)

## 🔹 Controles

| Tecla      | Ação                                             |
| ---------- | ------------------------------------------------ |
| `←` ou `→` | Mover a raposa                                   |
| `↑`        | Pular                                            |
| `ENTER`    | Selecionar no menu                               |
| `↑` ou `↓` | Navegar no menu                                  |
| `ESPAÇO`   | Retornar ao menu principal (Game Over / Vitória) |

## 📆 Estrutura do Projeto

```
raposa-invernal/
├── plataforma.py                  # Sistema de sprites e tiles
├── raposa invernal.py            # Lógica principal do jogo
├── plataforma_cactos.csv         # Posição dos cactos
├── plataforma_obstaculos.csv     # Posição dos obstáculos
├── plataforma_plataformas.csv    # Mapa das plataformas
├── plataforma.tmx                # Mapa editável pelo Tiled
├── tilemap_packed.tsx            # Tileset XML do Tiled
└── images/
    └── sprites/
        └── fox.png               # Sprite da raposa
    └── tiles/
        └── tile_XXXX.png         # Imagens dos tiles do cenário
```

## 🛠️ Requisitos

* Python 3.8+
* Pygame Zero (`pgzero`)
* Pygame

### Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/raposa-invernal.git
   cd raposa-invernal
   ```

2. Instale as dependências:

   ```bash
   pip install pgzero pygame
   ```

3. Execute o jogo:

   ```bash
   pgzrun "raposa invernal.py"
   ```

## ❄️ Créditos

* **Desenvolvimento:** \[Bianca Bastos]
* **Sprites:** [Kenney.nl](https://kenney.nl/assets) (Tilemap)
* **Ferramentas:** [Tiled Map Editor](https://www.mapeditor.org/), Pygame Zero

## 📄 Licença

Este projeto é distribuído sob a [Licença MIT](LICENSE), permitindo modificação, uso e distribuição com atribuição adequada.
