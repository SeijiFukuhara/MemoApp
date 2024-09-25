import tkinter as tk
import os

# メモを保存するファイル名
MEMO_FILE = "memo.txt"

# メインウィンドウの初期位置とサイズ
INITIAL_POSITION = (100, 100)
INITIAL_SIZE = (400, 360)

# ウィンドウを元の位置とサイズに戻す関数
def reset_position():
    window.geometry(f"{INITIAL_SIZE[0]}x{INITIAL_SIZE[1]}+{INITIAL_POSITION[0]}+{INITIAL_POSITION[1]}")

# テキストをファイルに保存する関数
def save_text():
    with open(MEMO_FILE, "w", encoding="utf-8") as file:
        file.write(text.get("1.0", tk.END))  # テキストエリアの内容をファイルに書き込む

# テキストをファイルから読み込む関数
def load_text():
    if os.path.exists(MEMO_FILE):  # メモファイルが存在するかチェック
        with open(MEMO_FILE, "r", encoding="utf-8") as file:
            text.insert(tk.END, file.read())  # ファイルから内容を読み込んでテキストエリアに表示する

# メインウィンドウの作成
window = tk.Tk()
window.title("Memo")  # ウィンドウのタイトルを設定

# ウィンドウの幅と高さを指定（初期設定）
window.geometry(f"{INITIAL_SIZE[0]}x{INITIAL_SIZE[1]}+{INITIAL_POSITION[0]}+{INITIAL_POSITION[1]}")

# 常に最前面に表示
window.attributes('-topmost', True)

# 最大化ボタンの無効化（サイズ変更禁止）
window.resizable(False, False)

# フレーム1の作成（テキスト入力エリアの上にスペースを空けるため）
frame1 = tk.Frame(window)
frame1.pack(pady=10)

# テキスト入力エリアの作成
text = tk.Text(frame1, height=20, width=50)
text.pack()

# テキスト内容をファイルから読み込む
load_text()

# ボタンフレームの作成
button_frame = tk.Frame(window)
button_frame.pack()

# 「元の位置に戻す」ボタンの作成
reset_button = tk.Button(button_frame, text="元の位置に戻す", command=reset_position)
reset_button.pack(side="left", padx=5, pady=20)

# ウィンドウを閉じる際にテキスト内容を保存する
window.protocol("WM_DELETE_WINDOW", lambda: [save_text(), window.destroy()])

# メインループの開始
window.mainloop()
