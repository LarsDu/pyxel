import math
import pyxel


class App:
    def __init__(self):
        pyxel.init(200, 150, caption='Pixel Sound API')

        pyxel.image(0).set(0, 0, [
            '00011000', '00010100', '00010010', '00010010', '00010100',
            '00010000', '01110000', '01100000'
        ])

        pyxel.sound(0).set(
            'e2e2c2g1 g1g1c2e2 d2d2d2g2 g2f2e2d2'
            'c2c2a1e1 e1e1a1c2 b1b1b1e2 e2d2c2b1', 'p', '6',
            'vffn fnff vffs fnff', 30)

        pyxel.sound(1).set(
            'r a1b1c2 b1b1c2d2 g2g2g2g2 c2c2d2e2'
            'f2f2f2f2 f2e2d2c2 d2d2d2d2 g2g2r r ', 'p', '6',
            'nnff vfff vvvv sfff svff vfff vvvv svnn', 30)

        pyxel.sound(2).set(
            'c1g1c1g1 c1g1c1g1 b0g1b0g1 b0g1b0g1'
            'a0e1a0e1 a0e1a0e1 g0d1g0d1 g0d1g0d1', 't', '7', 'n', 30)

        pyxel.sound(3).set(
            'f0c1f0c1 g0d1g0d1 c1g1c1g1 a0e1a0e1'
            'f0c1f0c1 f0c1f0c1 g0d1g0d1 g0d1g0d1', 't', '7', 'n', 30)

        pyxel.sound(4).set('f0ra4r f0ra4r f0ra4r f0f0a4r', 'n',
                           '6622 6622 6622 6422', 'f', 30)

        self.is_playing = [True] * 3

        self.play_music(True, True, True)

        pyxel.run(self.update, self.draw)

    def play_music(self, ch0, ch1, ch2):
        self.is_playing = (ch0, ch1, ch2)

        if ch0:
            pyxel.play(0, [0, 1], loop=True)
        else:
            pyxel.stop(0)

        if ch1:
            pyxel.play(1, [2, 3], loop=True)
        else:
            pyxel.stop(1)

        if ch2:
            pyxel.play(2, 4, loop=True)
        else:
            pyxel.stop(2)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_1):
            self.play_music(True, True, True)

        if pyxel.btnp(pyxel.KEY_2):
            self.play_music(True, False, False)

        if pyxel.btnp(pyxel.KEY_3):
            self.play_music(False, True, False)

        if pyxel.btnp(pyxel.KEY_4):
            self.play_music(False, False, True)

        if pyxel.btnp(pyxel.KEY_5):
            self.play_music(False, False, False)

    def draw(self):
        pyxel.cls(1)

        pyxel.text(6, 6, 'sound(no).set(note,tone,volume,effect,speed)', 7)
        pyxel.rect(12, 16, 188, 52, 2)
        pyxel.text(16, 20, 'note  :[CDEFGAB] + [ #-] + [0-4]', 9)
        pyxel.text(16, 28, 'tone  :[T]riangle [S]quare [P]ulse [N]oise', 9)
        pyxel.text(16, 36, 'volume:[0-7]', 9)
        pyxel.text(16, 44, 'effect:[N]one [S]lide [V]ibrato [F]adeOut', 9)

        pyxel.text(6, 62, 'play(ch,no,loop=False)', 7)
        pyxel.text(6, 76, 'stop(ch)', 7)

        pyxel.rectb(6, 97, 193, 143, 14)
        pyxel.rect(6, 91, 34, 97, 14)
        pyxel.text(7, 92, 'CONTROL', 1)

        pyxel.text(12, 102, '1: Play all channels', 14)
        pyxel.text(12, 110, '2: Play channel #0 (Melody)', 14)
        pyxel.text(12, 118, '3: Play channel #1 (Bass)', 14)
        pyxel.text(12, 126, '4: Play channel #2 (Drums)', 14)
        pyxel.text(12, 134, '5: Stop playing', 14)

        for i, v in enumerate(self.is_playing):
            pyxel.pal(1, v and 15 or 13)
            pyxel.blt(140 + i * 16,
                      116 + math.sin(pyxel.frame_count * 0.1 + i * 2.1) * 5, 0,
                      0, 0, 8, 8, 0)
        pyxel.pal()


App()
