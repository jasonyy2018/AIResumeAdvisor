import tkinter as tk
from tkinter import filedialog, messagebox

def browse_file():
    file_path = filedialog.askopenfilename(
        title="Select a File",
        filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
    )
    if file_path:
        with open(file_path, 'r') as file:
            job_description_text.delete('1.0', tk.END)
            job_description_text.insert(tk.END, file.read())

def save_description():
    job_description = job_description_text.get("1.0", tk.END).strip()
    if job_description:
        # 在这里添加保存岗位描述的逻辑, 比如保存到数据库
        print("Job Description Saved:", job_description)
        messagebox.showinfo("Success", "Job Description saved successfully!")
        window.destroy()  # 关闭窗口
    else:
        messagebox.showwarning("Warning", "Job Description cannot be empty!")

def cancel():
    window.destroy()

# 创建主窗口
window = tk.Tk()
window.title("Import Job Description")
window.geometry("500x400")

# 创建文本框用于编辑岗位描述
job_description_text = tk.Text(window, wrap=tk.WORD, height=15)
job_description_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# 创建浏览按钮
browse_button = tk.Button(window, text="Browse", command=browse_file)
browse_button.pack(pady=5)

# 创建保存和取消按钮
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

save_button = tk.Button(button_frame, text="Save", command=save_description)
save_button.pack(side=tk.LEFT, padx=5)

cancel_button = tk.Button(button_frame, text="Cancel", command=cancel)
cancel_button.pack(side=tk.LEFT, padx=5)

# 运行主循环
window.mainloop()