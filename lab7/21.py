import pygame

pygame.init()

pygame.display.set_mode((400, 100), pygame.RESIZABLE)
pygame.display.set_caption('music')

player = pygame.image.load("C:/Users/77785/Desktop/pp2-Ayazhan/lab7/play.jpeg")
new_player = pygame.transform.scale(player, (400, 100))

songs = [
    r"C:/Users/77785/Desktop/pp2-Ayazhan/lab7/blackpink/BLACKPINK-Hard-to-Love-(HiphopKit.com).mp3",
    r"C:/Users/77785/Desktop/pp2-Ayazhan/lab7/blackpink/BLACKPINK-Pink-Venom-1-(HiphopKit.com).mp3",
    r"C:/Users/77785/Desktop/pp2-Ayazhan/lab7/blackpink/BLACKPINK-Ready-For-Love-Ft-PUBG-MOBILE-(HiphopKit.com).mp3"
]

for song in songs:
    pygame.mixer.music.load(song)

current_song_index = 0

ok = True
while ok:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ok = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pygame.mixer.music.play()
            elif event.key == pygame.K_DOWN:
                pygame.mixer.music.stop()
            elif event.key == pygame.K_LEFT:
                current_song_index = (current_song_index - 1) % len(songs)
                pygame.mixer.music.load(songs[current_song_index])
            elif event.key == pygame.K_RIGHT:
                current_song_index = (current_song_index + 1) % len(songs)
                pygame.mixer.music.load(songs[current_song_index])

    pygame.display.update()

pygame.quit()