```python
# annotation.py
# Tool gán nhãn văn bản đơn giản bằng Python + Tkinter

import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

class AnnotationTool:
    def __init__(self, master):
        self.master = master
        master.title("Text Annotation Tool")

        self.texts = []
        self.labels = []
        self.current_index = 0
        self.file_path = ""

        # Vùng hiển thị câu
        self.text_display = tk.Label(master, text="", wraplength=400, font=("Arial", 14))
        self.text_display.pack(pady=20)

        # Nút gán nhãn
        self.button_frame = tk.Frame(master)
        self.button_frame.pack()

        self.positive_btn = tk.Button(self.button_frame, text="Positive", command=lambda: self.annotate("Positive"))
        self.positive_btn.grid(row=0, column=0, padx=10)

        self.negative_btn = tk.Button(self.button_frame, text="Negative", command=lambda: self.annotate("Negative"))
        self.negative_btn.grid(row=0, column=1, padx=10)

        self.neutral_btn = tk.Button(self.button_frame, text="Neutral", command=lambda: self.annotate("Neutral"))
        self.neutral_btn.grid(row=0, column=2, padx=10)

        # Nút load + save
        self.load_btn = tk.Button(master, text="Load Text File", command=self.load_file)
        self.load_btn.pack(pady=5)

        self.save_btn = tk.Button(master, text="Save Annotations", command=self.save_file)
        self.save_btn.pack(pady=5)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if not file_path:
            return
        self.file_path = file_path
        with open(file_path, "r", encoding="utf-8") as f:
            self.texts = [line.strip() for line in f if line.strip()]
        self.labels = [None] * len(self.texts)
        self.current_index = 0
        self.show_text()

    def show_text(self):
        if self.current_index < len(self.texts):
            self.text_display.config(text=self.texts[self.current_index])
        else:
            self.text_display.config(text="Hoàn thành gán nhãn!")

    def annotate(self, label):
        if self.current_index < len(self.texts):
            self.labels[self.current_index] = label
            self.current_index += 1
            self.show_text()

    def save_file(self):
        if not self.texts:
            messagebox.showwarning("Warning", "Chưa có dữ liệu để lưu!")
            return
        df = pd.DataFrame({"Text": self.texts, "Label": self.labels})
        save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if save_path:
            df.to_csv(save_path, index=False, encoding="utf-8")
            messagebox.showinfo("Success", f"Đã lưu annotation tại {save_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AnnotationTool(root)
    root.mainloop()
```
