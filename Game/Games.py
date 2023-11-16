import pygame
import sys
import random
import time

# Pygame'ı başlat
pygame.init()

# Ekran boyutları
ekran_genislik = 800
ekran_yukseklik = 600

# Ekran oluştur
ekran = pygame.display.set_mode((ekran_genislik, ekran_yukseklik))
pygame.display.set_caption("Tek Nesne Oyunu")

# Renkler
siyah = (0, 0, 0)
beyaz = (255, 255, 255)

# Skor
skor = 0

# Oyun süresi (saniye)
oyun_suresi = 60
baslangic_zamani = time.time()

# Nesne özellikleri
nesne_renk = beyaz
nesne_genislik = 50
nesne_yukseklik = 50

# Nesne başlangıç konumu
nesne_x = random.randint(0, ekran_genislik - nesne_genislik)
nesne_y = random.randint(0, ekran_yukseklik - nesne_yukseklik)

# Zaman damgası
son_hareket_zamani = time.time()

# Oyun döngüsü
clock = pygame.time.Clock()
while time.time() - baslangic_zamani < oyun_suresi:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            t_x, t_y = event.pos
            # Eğer fare ile nesne yakalanırsa
            if nesne_x < t_x < nesne_x + nesne_genislik and nesne_y < t_y < nesne_y + nesne_yukseklik:
                skor += 1
                nesne_x = random.randint(0, ekran_genislik - nesne_genislik)
                nesne_y = random.randint(0, ekran_yukseklik - nesne_yukseklik)

    # Ekranı temizle
    ekran.fill(siyah)

    # Nesneyi ekrana çiz
    pygame.draw.rect(ekran, nesne_renk, (nesne_x, nesne_y, nesne_genislik, nesne_yukseklik))

    # Skoru ekrana yazdır
    font = pygame.font.Font(None, 36)
    skor_yazi = font.render("Skor: {}".format(skor), True, beyaz)
    ekran.blit(skor_yazi, (10, 10))

    # Oyun süresini ekrana yazdır
    kalan_sure = int(oyun_suresi - (time.time() - baslangic_zamani))
    sure_yazi = font.render("Kalan Süre: {} saniye".format(kalan_sure), True, beyaz)
    ekran.blit(sure_yazi, (ekran_genislik - 200, 10))

    # Ekranı güncelle
    pygame.display.update()

    # Zorluk: Nesneyi yarım saniyede bir hareket ettir
    if time.time() - son_hareket_zamani >= 0.5:
        nesne_x = random.randint(0, ekran_genislik - nesne_genislik)
        nesne_y = random.randint(0, ekran_yukseklik - nesne_yukseklik)
        son_hareket_zamani = time.time()

    # FPS ayarı
    clock.tick(60)  # 60 FPS

# Oyun süresi bittiğinde skoru ekrana yazdır
ekran.fill(siyah)
son_skor_yazi = font.render("Oyun Bitti! Skorunuz: {}".format(skor), True, beyaz)
ekran.blit(son_skor_yazi, (ekran_genislik // 2 - 200, ekran_yukseklik // 2 - 50))
pygame.display.update()

# Biraz bekleyip sonra kapat
time.sleep(2)
pygame.quit()
sys.exit()
