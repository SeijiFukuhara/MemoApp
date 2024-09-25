import tkinter as tk
import os

class StickyNoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("メモ帳")
        self.root.geometry("300x200+100+100")
        self.root.attributes('-topmost', True)  # 常に最前面に表示
        self.root.overrideredirect(True)  # 最小化・最大化・閉じるボタンなし

        # 内側のウィジェット用フレーム（ウィンドウ枠の内側に表示）
        self.inner_frame = tk.Frame(self.root, bg="white", bd=0, relief="solid")
        self.inner_frame.pack(expand=True, fill='both')

        # テキストウィジェット
        self.text_area = tk.Text(self.inner_frame, wrap='word')
        self.text_area.pack(expand=1, fill='both')

        # ボタンを追加するフレーム
        button_frame = tk.Frame(self.inner_frame)
        button_frame.pack(side='bottom', fill='x')

        # 所定の位置に戻すボタン
        self.reset_button = tk.Button(button_frame, text="元の位置に戻す", command=self.reset_position, width=15, height=2)
        self.reset_button.pack(side='left')

        # 表示・非表示を切り替えるボタン
        self.toggle_button = tk.Button(button_frame, text="メモの表示/非表示", command=self.toggle_visibility, width=15, height=2)
        self.toggle_button.pack(side='left')

        # 初期位置を記憶
        self.initial_position = (100, 100)

        # ウィンドウドラッグ用の変数
        self._offsetx = 0
        self._offsety = 0

        # マウスイベントのバインド
        self.root.bind("<Button-1>", self.click_window)
        self.root.bind("<B1-Motion>", self.drag_window)

        # メモ内容をファイルに保存・読み込み
        self.filename = "memo_content.txt"
        self.load_memo()

        # ウィンドウを閉じる前にメモ内容を保存
        self.root.protocol("WM_DELETE_WINDOW", self.save_and_close)

    def load_memo(self):
        """メモをファイルから読み込む"""
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as file:
                content = file.read()
                self.text_area.insert("1.0", content)

    def save_and_close(self):
        """メモ内容をファイルに保存してウィンドウを閉じる"""
        with open(self.filename, "w", encoding="utf-8") as file:
            content = self.text_area.get("1.0", tk.END)
            file.write(content)
        self.root.destroy()

    def click_window(self, event):
        """ウィンドウをドラッグするために、クリック位置を記録"""
        self._offsetx = event.x
        self._offsety = event.y

    def drag_window(self, event):
        """ウィンドウをドラッグして移動"""
        x = event.x_root - self._offsetx
        y = event.y_root - self._offsety
        self.root.geometry(f'+{x}+{y}')

    def reset_position(self):
        """ウィンドウを元の位置に戻す"""
        self.root.geometry(f'+{self.initial_position[0]}+{self.initial_position[1]}')
        self.root.attributes('-topmost', True)  # 常に最前面に表示

    def toggle_visibility(self):
        """メモ帳を表示/非表示に切り替える"""
        if self.root.winfo_viewable():
            self.root.withdraw()
        else:
            self.root.deiconify()
            self.root.attributes('-topmost', True)  # 常に最前面に表示

# Tkinterのメインウィンドウを設定
if __name__ == "__main__":
    root = tk.Tk()
    app = StickyNoteApp(root)
    root.mainloop()