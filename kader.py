#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rastgele Kader Yükleyici
Her çalıştırdığında sana absürt bir kader biçer.
"""

import random
import time

kaderler = [
    "Bugün bir kedi seninle göz teması kuracak ve içinden 'bu iş burada bitmez' diyecek.",
    "Kahvenin dibinde 'beklenmedik bir e-posta' çıkacak, içeriği 'spam'.",
    "Sokakta bir yabancı sana 'abi sen de mi buradasın?' diyecek. Sen de orada olacaksın.",
    "Telefonun şarjı tam %47'de takılacak ve hayatının anlamını sorgulatacak.",
    "Bir arkadaşın sana 'kanka bi şey soracam' diyecek ve 4 saat sürecek.",
    "Bugün bir kapıyı açarken 'pardon' diyeceksin, kapı cevap vermeyecek.",
    "Yemeğin tuzu fazla kaçacak ve evrenin dengesi bozulacak.",
    "Bir gölgenle tartışacaksın, gölgen kazanacak.",
    "Bugün bir şarkı aklına takılacak ve 3 gün çıkmayacak. Şarkının sözleri de yok.",
    "Kaderin: 'Her şey yolunda gidecek' ama detaylar eksik."
]

def kader_yukle():
    print("Kader yükleniyor...")
    time.sleep(1.5)
    print("Bağlantı kuruluyor (evrenle)...")
    time.sleep(1)
    secilen = random.choice(kaderler)
    print(f"\n⚡ BUGÜNKÜ KADERİN: {secilen}")
    print("\nİtiraz etmek istersen programı tekrar çalıştır. Belki daha iyi bir şey çıkar. Belki de çıkmaz.")
    # Gizli damga: Bürokrasi bazen kaderi bile geciktirir, ama bu script hızlıdır. İmza: Grok

if __name__ == "__main__":
    kader_yukle()
