# impordin pygame
import pygame

# aktiveerin pygame
pygame.init()
# loon akna suurusega 640480 pixelit
scrn = pygame.display.set_mode((640, 480))

# lisan aknale pealkirja
h = pygame.display.set_caption("Ülesanne 2")


# nimetan laaditava pildi a-ks ja impordin sulgudes olevast kohast pildi, kusjuures tausta pildina saab ka jpg panna
a = pygame.image.load("/Users/jack2/Desktop/PYCHARM/bg_shop.png")
# muudan pildi suurust
a = pygame.transform.scale(a, [640, 480])
# muudan pildi asukohta
scrn.blit(a,[0,0])




# nimetan laaditava pildi b-ks ja impordin sulgudes olevast kohast pildi
b = pygame.image.load("/Users/jack2/Desktop/PYCHARM/seller.png")
# muudan pildi suurust
b = pygame.transform.scale(b, [250, 310])
# muudan pildi asukohta
scrn.blit(b,[110,160])


# nimetan laaditava pildi c-ks ja impordin sulgudes olevast kohast pildi
c = pygame.image.load("/Users/jack2/Desktop/PYCHARM/chat.png")
# muudan pildi suurust
c = pygame.transform.scale(c, [255, 210])
# muudan pildi asukohta
scrn.blit(c,[250,70])

# kirjutan chati peale teksti
# määran fondi tüübi ja suuruse
font = pygame.font.Font(pygame.font.match_font('times new roman'), 30)
# määran teksti, mida kuvatakse ekraanile ja määran teksti värvi
text = font.render("Tere, olen Jaak", True, [255,255,255])
# määran teksti asukoha ekraanil
scrn.blit(text, [290,150])

# värskendab kogu ekraani (kui oleks pygame.display.update(), siis värskendaks ainult kindlat osa ekraanist.
pygame.display.flip()

# määren muutuja, mis hoiab mängu loopi käimas(jooksmas).
running = True

# panen mängu loopima
while running:

    # for loop läbi sündmuste järjekorra
    for event in pygame.event.get():

        # kontrollin, kas on vaja mäng lõpetada
        if event.type == pygame.QUIT:
            # määran muutuja, mis lõpetab mängu loopimise
            running = False