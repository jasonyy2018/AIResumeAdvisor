import tkinter as tk
from tkinter import filedialog, messagebox

class SimpleSubmitResumeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Submit Resume")
        self.root.geometry("400x300")

        # Create a Frame for the Textbox and File Upload
        frame = tk.Frame(self.root)
        frame.pack(padx=20, pady=20)

        self.label_name = tk.Label(frame, text="Name:")
        self.label_name.pack(anchor="w")

        self.entry_name = tk.Entry(frame, width=40)
        self.entry_name.pack(pady=5)

        self.label_upload = tk.Label(frame, text="Upload Resume File:")
        self.label_upload.pack(anchor="w", pady=(20, 0))

        self.uploaded_file = None
        self.file_button = tk.Button(frame, text="Choose File", command=self.upload_file)
        self.file_button.pack(pady=5)

        self.file_label = tk.Label(frame, text="")
        self.file_label.pack(pady=5)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_info)
        self.submit_button.pack(side="left", padx=20, pady=20)

        self.cancel_button = tk.Button(self.root, text="Cancel", command=self.root.destroy)
        self.cancel_button.pack(side="right", padx=20, pady=20)

    def upload_file(self):
        self.uploaded_file = filedialog.askopenfilename()
        if self.uploaded_file:
            self.file_label.config(text=self.uploaded_file)

    def submit_info(self):
        name = self.entry_name.get().strip()

        if name and self.uploaded_file:
            # 在这里添加保存个人信息的逻辑，例如保存到数据库或进一步处理
            print("Name:", name)
            print("Uploaded File:", self.uploaded_file)
            messagebox.showinfo("Success", "Resume submitted successfully!")
            self.root.destroy()  # 关闭窗口
        else:
            messagebox.showwarning("Warning", "Please enter your name and choose a file to upload.")

# 运行主循环
if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleSubmitResumeApp(root)
    root.mainloop()