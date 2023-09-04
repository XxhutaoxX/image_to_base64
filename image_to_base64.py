import tkinter as tk
from tkinter import filedialog
import base64


def encode_and_save_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.gif")])
    if file_path:
        with open(file_path, 'rb') as image_file:
            base64_encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

        # 提示用户选择保存位置
        save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])

        if save_path:
            with open(save_path, 'w') as file:
                file.write(base64_encoded_image)

            result_label.config(text=f"已保存到文件：{save_path}")


# 创建主窗口
root = tk.Tk()
root.title("图片转换工具")

# 设置窗口大小
root.geometry("400x300")

# 创建标签
info_label = tk.Label(root, text="请选择要转换的图片文件：")
info_label.pack(pady=10)

# 创建按钮
convert_button = tk.Button(root, text="选择图片并转换", command=encode_and_save_image)
convert_button.pack()

# 创建结果标签
result_label = tk.Label(root, text="")
result_label.pack()

# 运行主循环
root.mainloop()
