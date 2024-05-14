import tkinter as tk
from tkinter import messagebox
import pygame
import sys
from game import Game
from colors import Colors

# Fungsi login
def login():
    # Cek apakah username sesuai
    if entry_username.get() == " ":
        messagebox.showinfo("Login", "Berhasil masuk")
        # Jalankan game setelah login berhasil
        run_game()
    else:
        messagebox.showinfo("Login", "Berhasil masuk")
        run_game()

# Fungsi menjalankan game Tetris
def run_game():
    pygame.init()

    title_font = pygame.font.Font(None, 40)
    score_surface = title_font.render("Score", True, Colors.white)
    next_surface = title_font.render("Next", True, Colors.white)
    game_over_surface = title_font.render("GAME OVER", True, Colors.white)

    score_rect = pygame.Rect(320, 55, 170, 60)
    next_rect = pygame.Rect(320, 215, 170, 180)

    screen = pygame.display.set_mode((500, 620))
    pygame.display.set_caption("Python Tetris")

    clock = pygame.time.Clock()

    game = Game()

    GAME_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(GAME_UPDATE, 200)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if game.game_over == True:
                    game.game_over = False
                    game.reset()
                if event.key == pygame.K_LEFT and game.game_over == False:
                    game.move_left()
                if event.key == pygame.K_RIGHT and game.game_over == False:
                    game.move_right()
                if event.key == pygame.K_DOWN and game.game_over == False:
                    game.move_down()
                    game.update_score(0, 1)
                if event.key == pygame.K_UP and game.game_over == False:
                    game.rotate()
            if event.type == GAME_UPDATE and game.game_over == False:
                game.move_down()

        #Drawing
        score_value_surface = title_font.render(str(game.score), True, Colors.white)

        screen.fill(Colors.pink)
        screen.blit(score_surface, (365, 20, 50, 50))
        screen.blit(next_surface, (375, 180, 50, 50))

        if game.game_over == True:
            screen.blit(game_over_surface, (320, 450, 50, 50))

        pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
        screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx,
            centery = score_rect.centery))
        pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
        game.draw(screen)

        pygame.display.update()
        clock.tick(60)

# Membuat jendela login
root = tk.Tk()
root.title("Ayoo masuk")
root.configure(bg="Blue")

# Membuat frame untuk elemen-elemen form
frame = tk.Frame(root, bg="blue")  # Mengubah latar belakang frame menjadi biru
frame.pack(padx=20, pady=20)

# Membuat label dan entry untuk username
label_username = tk.Label(frame, text="Name:", bg="blue", fg="white")  # Mengubah warna teks label menjadi putih
label_username.grid(row=0, column=0, sticky="w")
entry_username = tk.Entry(frame)
entry_username.grid(row=0, column=1)

# Membuat tombol untuk login
btn_login = tk.Button(frame, text="Login", command=login, bg="blue", fg="white")  # Mengubah warna tombol menjadi biru dan teks menjadi putih
btn_login.grid(row=1, columnspan=2, pady=10)

# Menjalankan loop utama
root.mainloop()
