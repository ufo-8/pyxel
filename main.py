import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120, title="Animated Character")
        pyxel.load("my_resource.pyxres")  # Pyxel Editorで作成したリソースファイルを読み込みます
        self.x = 72  # ドット絵の初期位置X座標
        self.y = 56  # ドット絵の初期位置Y座標
        self.vy = 0  # Y方向の速度
        self.gravity = 1.0  # 重力の強さ
        self.jump_strength = -6  # ジャンプの強さ
        self.is_jumping = False  # ジャンプ中かどうかのフラグ
        self.frame = 0  # アニメーションフレームのインデックス
        self.frame_count = 0  # フレームカウント
        pyxel.playm(0, loop=True)  # ミュージックを再生
        pyxel.run(self.update, self.draw)

    def update(self):
        # 左右の移動
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x = max(self.x - 2, 0)
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x = min(self.x + 2, pyxel.width - 16)

        # ジャンプの処理
        if pyxel.btnp(pyxel.KEY_SPACE) and not self.is_jumping:
            self.vy = self.jump_strength
            self.is_jumping = True

        # 重力の適用
        self.vy += self.gravity
        self.y += self.vy

        # 地面に着いたらジャンプをリセット
        if self.y > pyxel.height - 16:
            self.y = pyxel.height - 16
            self.vy = 0
            self.is_jumping = False

        # 天井にぶつかったら速度をリセット
        if self.y < 0:
            self.y = 0
            self.vy = 0

        # アニメーションフレームの更新
        self.frame_count += 1
        if self.frame_count % 10 == 0:  # 10フレームごとにアニメーションフレームを更新
            self.frame = (self.frame + 1) % 4  # フレーム数に応じて変更

    def draw(self):
        pyxel.cls(0)
        # 背景を描画
        pyxel.blt(0, 0, 1, 0, 0, 160, 120)
        # キャラクターを描画    
        pyxel.blt(self.x, self.y, 0, self.frame * 16, 0, 16, 16, 0)  # アニメーションフレームを描画

App()
