import pygame
from pygame.locals import *
import sys
import numpy as np
import struct
import pyaudio
import wave

# 音名と周波数の対応付け（Hz）
do0 = 131
re0 = 147
mi0 = 165
fa0 = 175
so0 = 196
ra0 = 220
si0 = 247
do1 = 262 # ド 262 Hz
re1 = 294 # レ 294 Hz
mi1 = 330 # ミ 330 Hz
fa1 = 349 # ファ 349 Hz
so1 = 392 # ソ 392 Hz
ra1 = 440 # ラ 330 Hz
si1 = 494 # シ 494 Hz
do2 = 523 # ド 523 Hz
re2 = 587
mi2 = 659
fa2 = 698
so2 = 783
ra2 = 880
si2 = 988
res = 0 # 休符 0 Hz


# 正弦波を出力する関数
def makeSinWave(freq, sec, amp):

    if freq == "do0":
        freq = do0
    elif freq == "re0":
        freq = re0
    elif freq == "mi0":
        freq = mi0
    elif freq == "fa0":
        freq = fa0
    elif freq == "so0":
        freq = so0
    elif freq == "ra0":
        freq = ra0
    elif freq == "si0":
        freq = si0
    elif freq == "do1":
        freq = do1
    elif freq == "re1":
        freq = re1
    elif freq == "mi1":
        freq = mi1
    elif freq == "fa1":
        freq = fa1
    elif freq == "so1":
        freq = so1
    elif freq == "ra1":
        freq = ra1
    elif freq == "si1":
        freq = si1
    elif freq == "do2":
        freq = do2
    elif freq == "re2":
        freq = re2
    elif freq == "mi2":
        freq = mi2
    elif freq == "fa2":
        freq = fa2
    elif freq == "so2":
        freq = so2
    elif freq == "ra2":
        freq = ra2
    elif freq == "si2":
        freq = si2
    elif freq == "res":
        freq = res

    # 継続サンプル長の決定
    samplenum = int(fs*sec)
    # サンプル数と継続時間に対応したindex行列の作成
    x = np.arange(0, samplenum, 1.0)
    # sin信号の作成
    signal = amp * np.sin( 2 * np.pi * freq * x / fs)
    # signalをint16に変換
    signal16 = signal.astype(np.int16)

    # ここから再生
    binaryData = struct.pack("h" * len(signal16), *signal16)
    size = 1024
    current = 0
    buf = binaryData[current:current+size]

    print("playing " + str(freq) + " Hz, " + str(sec) + "sec.")
    while len(buf) != 0:
        stream.write(buf)
        current = current + size
        buf = binaryData[current:current+size]
    # ここまで再生
        
    return signal16
                    
                    
if __name__=="__main__":
    scale = []
    limitcount = 0
    limitlength = 0
    input_song = ""
    input_stop = ""
    pygame.init()    # Pygameを初期化
    screen = pygame.display.set_mode((1280, 720))    # 画面を作成
    pygame.display.set_caption("童謡作曲メーカー")    # タイトルを作成

    #フォントの用意  
    font = pygame.font.Font("TanukiMagic.ttf", 25)
    fonttitle = pygame.font.Font("TanukiMagic.ttf", 60)
    
    #テキストの設定

    doremi0 = ["ド/C3", "レ/D3", "ミ/E3", "ファ/F3", "ソ/G3", "ラ/A3", "シ/B3"]
    doremi1 = ["ド/C4", "レ/D4", "ミ/E4", "ファ/F4", "ソ/G4", "ラ/A4", "シ/B4"]
    doremi2 = ["ド/C5", "レ/D5", "ミ/E5", "ファ/F5", "ソ/G5", "ラ/A5", "シ/B5"]

    #図形の設定
    buttondo0 = pygame.Rect(55, 270, 120, 100)
    buttonre0 = pygame.Rect(230, 270, 120, 100)
    buttonmi0 = pygame.Rect(405, 270, 120, 100)
    buttonfa0 = pygame.Rect(580, 270, 120, 100)
    buttonso0 = pygame.Rect(755, 270, 120, 100)
    buttonra0 = pygame.Rect(930, 270, 120, 100)
    buttonsi0 = pygame.Rect(1105, 270, 120, 100)
    buttondo1 = pygame.Rect(55, 420, 120, 100)
    buttonre1 = pygame.Rect(230, 420, 120, 100)
    buttonmi1 = pygame.Rect(405, 420, 120, 100)
    buttonfa1 = pygame.Rect(580, 420, 120, 100)
    buttonso1 = pygame.Rect(755, 420, 120, 100)
    buttonra1 = pygame.Rect(930, 420, 120, 100)
    buttonsi1 = pygame.Rect(1105, 420, 120, 100)
    buttondo2 = pygame.Rect(55, 570, 120, 100)
    buttonre2 = pygame.Rect(230, 570, 120, 100)
    buttonmi2 = pygame.Rect(405, 570, 120, 100)
    buttonfa2 = pygame.Rect(580, 570, 120, 100)
    buttonso2 = pygame.Rect(755, 570, 120, 100)
    buttonra2 = pygame.Rect(930, 570, 120, 100)
    buttonsi2 = pygame.Rect(1105, 570, 120, 100)
    
    buttonkaeru = pygame.Rect(300, 270, 680, 100)
    buttonfurusato = pygame.Rect(300, 420, 680, 100)
    buttonfree = pygame.Rect(300, 570, 680, 100)
    buttonstop = pygame.Rect(15, 100, 120, 100)

    textdo0 = font.render(doremi0[0], True, (0,0,0))
    textre0 = font.render(doremi0[1], True, (0,0,0))
    textmi0 = font.render(doremi0[2], True, (0,0,0))
    textfa0 = font.render(doremi0[3], True, (0,0,0))
    textso0 = font.render(doremi0[4], True, (0,0,0))
    textra0 = font.render(doremi0[5], True, (0,0,0))
    textsi0 = font.render(doremi0[6], True, (0,0,0))
    textdo1 = font.render(doremi1[0], True, (0,0,0))
    textre1 = font.render(doremi1[1], True, (0,0,0))
    textmi1 = font.render(doremi1[2], True, (0,0,0))
    textfa1 = font.render(doremi1[3], True, (0,0,0))
    textso1 = font.render(doremi1[4], True, (0,0,0))
    textra1 = font.render(doremi1[5], True, (0,0,0))
    textsi1 = font.render(doremi1[6], True, (0,0,0))
    textdo2 = font.render(doremi2[0], True, (0,0,0))
    textre2 = font.render(doremi2[1], True, (0,0,0))
    textmi2 = font.render(doremi2[2], True, (0,0,0))
    textfa2 = font.render(doremi2[3], True, (0,0,0))
    textso2 = font.render(doremi2[4], True, (0,0,0))
    textra2 = font.render(doremi2[5], True, (0,0,0))
    textsi2 = font.render(doremi2[6], True, (0,0,0))

    textstop = font.render("完了", True, (0,0,0))
    textkaeru = font.render("かえるのうた", True, (0,0,0))
    textfurusato = font.render("　ふるさと　", True, (0,0,0))
    textfree = font.render("フリーモード", True, (0,0,0))
    texttitle = fonttitle.render("童謡作曲メーカー", True, (255,255,255))
    
    running = True
    #メインループ
    while running:
        screen.fill((0,0,0))  #画面を黒で塗りつぶす


        #描画
        screen.blit(texttitle, (10, 10))

        if input_song == "":
            pygame.draw.rect(screen, (255, 255, 255), buttonkaeru)
            pygame.draw.rect(screen, (255, 255, 255), buttonfurusato)
            pygame.draw.rect(screen, (255, 255, 255), buttonfree)

            screen.blit(textkaeru, (565, 310))
            screen.blit(textfurusato, (565, 460))
            screen.blit(textfree, (565, 610))

        elif input_song == "free" or (limitlength - len(scale) >= 0):
            pygame.draw.rect(screen, (255, 255, 255), buttondo0)
            pygame.draw.rect(screen, (255, 255, 255), buttonre0)
            pygame.draw.rect(screen, (255, 255, 255), buttonmi0)
            pygame.draw.rect(screen, (255, 255, 255), buttonfa0)
            pygame.draw.rect(screen, (255, 255, 255), buttonso0)
            pygame.draw.rect(screen, (255, 255, 255), buttonra0)
            pygame.draw.rect(screen, (255, 255, 255), buttonsi0)
            pygame.draw.rect(screen, (255, 255, 255), buttondo1)
            pygame.draw.rect(screen, (255, 255, 255), buttonre1)
            pygame.draw.rect(screen, (255, 255, 255), buttonmi1)
            pygame.draw.rect(screen, (255, 255, 255), buttonfa1)
            pygame.draw.rect(screen, (255, 255, 255), buttonso1)
            pygame.draw.rect(screen, (255, 255, 255), buttonra1)
            pygame.draw.rect(screen, (255, 255, 255), buttonsi1)
            pygame.draw.rect(screen, (255, 255, 255), buttondo2)
            pygame.draw.rect(screen, (255, 255, 255), buttonre2)
            pygame.draw.rect(screen, (255, 255, 255), buttonmi2)
            pygame.draw.rect(screen, (255, 255, 255), buttonfa2)
            pygame.draw.rect(screen, (255, 255, 255), buttonso2)
            pygame.draw.rect(screen, (255, 255, 255), buttonra2)
            pygame.draw.rect(screen, (255, 255, 255), buttonsi2)

            screen.blit(textdo0, (75, 310))
            screen.blit(textre0, (250, 310))
            screen.blit(textmi0, (425, 310))
            screen.blit(textfa0, (600, 310))
            screen.blit(textso0, (775, 310))
            screen.blit(textra0, (950, 310))
            screen.blit(textsi0, (1125, 310))
            screen.blit(textdo1, (75, 460))
            screen.blit(textre1, (250, 460))
            screen.blit(textmi1, (425, 460))
            screen.blit(textfa1, (600, 460))
            screen.blit(textso1, (775, 460))
            screen.blit(textra1, (950, 460))
            screen.blit(textsi1, (1125, 460))
            screen.blit(textdo2, (75, 610))
            screen.blit(textre2, (250, 610))
            screen.blit(textmi2, (425, 610))
            screen.blit(textfa2, (600, 610))
            screen.blit(textso2, (775, 610))
            screen.blit(textra2, (950, 610))
            screen.blit(textsi2, (1125, 610))

            pygame.draw.rect(screen, (255, 255, 255), buttonstop)
            screen.blit(textstop, (35, 140))

        pygame.display.update() #描画処理を実行
        for event in pygame.event.get():
            if event.type == QUIT:  # 終了イベント
                running = False
                pygame.quit()  #pygameのウィンドウを閉じる
                sys.exit() #システム終了
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttondo0.collidepoint(event.pos):
                    scale.append("do0")
                if buttonre0.collidepoint(event.pos):
                    scale.append("re0")
                if buttonmi0.collidepoint(event.pos):
                    scale.append("mi0")
                if buttonfa0.collidepoint(event.pos):
                    scale.append("fa0")
                if buttonso0.collidepoint(event.pos):
                    scale.append("so0")
                if buttonra0.collidepoint(event.pos):
                    scale.append("ra0")
                if buttonsi0.collidepoint(event.pos):
                    scale.append("si0")
                if buttondo1.collidepoint(event.pos):
                    scale.append("do1")
                if buttonre1.collidepoint(event.pos):
                    scale.append("re1")
                if buttonmi1.collidepoint(event.pos):
                    scale.append("mi1")
                if buttonfa1.collidepoint(event.pos):
                    scale.append("fa1")
                if buttonso1.collidepoint(event.pos):
                    scale.append("so1")
                if buttonra1.collidepoint(event.pos):
                    scale.append("ra1")
                if buttonsi1.collidepoint(event.pos):
                    scale.append("si1")
                if buttondo2.collidepoint(event.pos):
                    scale.append("do2")
                if buttonre2.collidepoint(event.pos):
                    scale.append("re2")
                if buttonmi2.collidepoint(event.pos):
                    scale.append("mi2")
                if buttonfa2.collidepoint(event.pos):
                    scale.append("fa2")
                if buttonso2.collidepoint(event.pos):
                    scale.append("so2")
                if buttonra2.collidepoint(event.pos):
                    scale.append("ra2")
                if buttonsi2.collidepoint(event.pos):
                    scale.append("si2")

                if buttonkaeru.collidepoint(event.pos):
                    input_song = "kaeru"
                    limitlength = 24
                    limitcount = limitlength
                if buttonfurusato.collidepoint(event.pos):
                    input_song = "furusato"
                    limitlength = 44
                    limitcount = limitlength
                if buttonfree.collidepoint(event.pos):
                    input_song = "free"
                if buttonstop.collidepoint(event.pos):
                    input_stop = "stop"

        if (((input_song == "kaeru") or (input_song == "furusato")) and (limitlength - len(scale) < 0)) or input_stop == "stop":

            running = False
            pygame.quit()  #pygameのウィンドウを閉じる

            # オーディオ再生の準備
            fs = 16000 # サンプリング周波数
            audio = pyaudio.PyAudio()
            stream = audio.open(format=pyaudio.paInt16, channels=1, rate=int(fs), output=True)

            output = [] # 初期化
            if input_song == "kaeru":
                output.extend(makeSinWave(str(scale[0]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[1]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[2]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[3]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[4]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[5]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[6]), 0.5, 2000))
                output.extend(makeSinWave(res, 0.5, 2000))
                output.extend(makeSinWave(str(scale[7]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[8]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[9]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[10]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[11]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[12]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[13]), 0.5, 2000))
                output.extend(makeSinWave(res, 0.5, 2000))
                output.extend(makeSinWave(str(scale[14]), 0.5, 2000))
                output.extend(makeSinWave(res, 0.5, 2000))
                output.extend(makeSinWave(str(scale[15]), 0.5, 2000))
                output.extend(makeSinWave(res, 0.5, 2000))
                output.extend(makeSinWave(str(scale[16]), 0.5, 2000))
                output.extend(makeSinWave(res, 0.5, 2000))
                output.extend(makeSinWave(str(scale[17]), 0.5, 2000))
                output.extend(makeSinWave(res, 0.5, 2000))
                output.extend(makeSinWave(str(scale[18]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[19]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[20]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[21]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[22]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[23]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[24]), 0.5, 2000))

            elif input_song == "furusato":
                output.extend(makeSinWave(str(scale[0]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[1]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[2]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[3]), 0.75, 2000))
                output.extend(makeSinWave(str(scale[4]), 0.25, 2000))
                output.extend(makeSinWave(str(scale[5]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[6]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[7]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[8]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[9]), 1.0, 2000))
                output.extend(makeSinWave(res, 0.5, 2000))
                output.extend(makeSinWave(str(scale[10]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[11]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[12]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[13]), 0.75, 2000))
                output.extend(makeSinWave(str(scale[14]), 0.25, 2000))
                output.extend(makeSinWave(str(scale[15]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[16]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[17]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[18]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[19]), 1.0, 2000))
                output.extend(makeSinWave(res, 0.5, 2000))
                output.extend(makeSinWave(str(scale[20]), 0.25, 2000))
                output.extend(makeSinWave(str(scale[21]), 0.25, 2000))
                output.extend(makeSinWave(str(scale[22]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[23]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[24]), 0.25, 2000))
                output.extend(makeSinWave(str(scale[25]), 0.25, 2000))
                output.extend(makeSinWave(str(scale[26]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[27]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[28]), 0.25, 2000))
                output.extend(makeSinWave(str(scale[29]), 0.25, 2000))
                output.extend(makeSinWave(str(scale[30]), 0.75, 2000))
                output.extend(makeSinWave(str(scale[31]), 0.25, 2000))
                output.extend(makeSinWave(str(scale[32]), 0.25, 2000))
                output.extend(makeSinWave(str(scale[33]), 0.25, 2000))
                output.extend(makeSinWave(str(scale[34]), 0.5, 2000))
                output.extend(makeSinWave(res, 0.5, 2000))
                output.extend(makeSinWave(str(scale[35]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[36]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[37]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[38]), 0.75, 2000))
                output.extend(makeSinWave(str(scale[39]), 0.25, 2000))
                output.extend(makeSinWave(str(scale[40]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[41]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[42]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[43]), 0.5, 2000))
                output.extend(makeSinWave(str(scale[44]), 1.0, 2000))
                output.extend(makeSinWave(res, 0.5, 2000))

            elif input_song == "free": 
                    for i in range(len(scale)):
                        output.extend(makeSinWave(str(scale[i]), 0.5, 2000))


            ####### wavファイルに保存
            binaryData = struct.pack("h" * len(output), *output)
            file_name = "newsong.wav"
            # WAV書き出し用オブジェクトの生成（ファイル名の決定）
            out = wave.Wave_write(file_name)
            # チャンネル数, 量子化ビット数（バイト）, サンプリング周波数, 長さ（バイト）, 圧縮有無, 圧縮形式
            param = (1, 2, fs, len(binaryData), 'NONE', 'not compressed')

            # ファイル出力
            out.setparams(param)
            out.writeframes(binaryData)
            out.close()

            sys.exit() #システム終了