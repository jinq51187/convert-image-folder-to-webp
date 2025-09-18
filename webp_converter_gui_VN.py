import os
from tkinter import Tk, filedialog, StringVar, IntVar, Label, Entry, Button, Checkbutton, Radiobutton, Frame, messagebox
from PIL import Image

def convert_images():
    folder = folder_path.get()
    if not folder or not os.path.isdir(folder):
        messagebox.showerror("Error", "Please select a valid folder.")
        return

    recursive = recursive_var.get()
    delete_original = delete_var.get()
    quality = int(quality_var.get())
    overwrite = save_mode.get() == 1

    converted, skipped = 0, 0

    for root, _, files in os.walk(folder):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
                input_path = os.path.join(root, file)
                output_path = os.path.splitext(input_path)[0] + ".webp"

                if not overwrite:
                    output_path = os.path.splitext(input_path)[0] + "_new.webp"

                if os.path.exists(output_path) and overwrite is False:
                    skipped += 1
                    continue

                try:
                    img = Image.open(input_path).convert("RGB")
                    img.save(output_path, "webp", quality=quality)
                    converted += 1
                    if delete_original:
                        os.remove(input_path)
                except Exception as e:
                    print(f"Error converting {input_path}: {e}")
                    skipped += 1

        if not recursive:
            break

    messagebox.showinfo("Done", f"Converted: {converted}, Skipped: {skipped}")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_path.set(folder_selected)

# GUI setup
root = Tk()
root.title("Image to WebP Converter")
root.geometry("500x360")

folder_path = StringVar()
recursive_var = IntVar(value=1)
delete_var = IntVar(value=0)
quality_var = StringVar(value="85")
save_mode = IntVar(value=1)

# Folder selection
Label(root, text="Chọn thư mục:", anchor="w").pack(fill="x", padx=10, pady=(10,0))
frame_folder = Frame(root)
frame_folder.pack(fill="x", padx=10)
Entry(frame_folder, textvariable=folder_path).pack(side="left", fill="x", expand=True)
Button(frame_folder, text="Browse", bg="#4CAF50", fg="white", command=browse_folder).pack(side="left", padx=5)

# Options
options_frame = Frame(root, relief="groove", borderwidth=2, padx=10, pady=10)
options_frame.pack(fill="x", padx=10, pady=10)

Checkbutton(options_frame, text="Quét cả thư mục con", variable=recursive_var).pack(anchor="w")
Checkbutton(options_frame, text="Xóa file gốc sau khi chuyển đổi", variable=delete_var).pack(anchor="w")

Label(options_frame, text="Chọn chất lượng ảnh WebP (mặc định 85, khuyên dùng từ 70–90):").pack(anchor="w", pady=(10,0))
Entry(options_frame, textvariable=quality_var, width=5).pack(anchor="w")

Label(options_frame, text="Tùy chọn:").pack(anchor="w", pady=(10,0))
Radiobutton(options_frame, text="Ghi đè file .webp nếu đã tồn tại", variable=save_mode, value=1).pack(anchor="w")
Radiobutton(options_frame, text="Tạo file mới (_new.webp), giữ nguyên file cũ", variable=save_mode, value=2).pack(anchor="w")

# Convert button
Button(root, text="Convert", bg="#4CAF50", fg="white", font=("Arial", 14, "bold"), command=convert_images).pack(pady=10)

root.mainloop()
