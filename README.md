# Tool Convert image folder to webp with Python
# User guide in Vietnamese and English

# Hướng dẫn sử dụng

Công dụng:
Chuyển đổi toàn bộ ảnh trong thư mục sang định dạng WebP để giảm dung lượng, tối ưu tốc độ tải web.

Các bước sử dụng:
Cài đặt Python

Sau đó cài đặt thư viện pillow bằng lệnh: pip install pillow

Chạy file webp_converter_gui_VN.py bằng Python bằng lệnh: python webp_converter_gui_VN.py

Chọn thư mục ảnh: Nhấn Browse và chọn thư mục chứa ảnh.

Tùy chọn:

Quét cả thư mục con.

Xóa file gốc sau khi chuyển đổi.

Chọn chất lượng ảnh WebP (mặc định 85, khuyên dùng từ 70–90).

Chế độ lưu:

Ghi đè file .webp nếu đã tồn tại.

Tạo file mới, giữ nguyên file cũ.

Nhấn nút Convert để bắt đầu chuyển đổi.

Sau khi hoàn tất, chương trình sẽ báo số lượng ảnh đã chuyển đổi và bỏ qua.

# User guide

Purpose:
Convert all images in a folder to WebP format to reduce file size and improve website loading speed.

How to use:
Installer Python

Then install the pillow library using the command: pip install pillow

Launch webp_converter_gui_EN.py with Python using the command: python webp_converter_gui_EN.py

Select image folder: Click Browse and choose the folder containing your images.

Options:

Recursive (include subfolders): Scan all subfolders.

Delete original after convert: Remove original files after conversion.

Quality (0-100): Set WebP image quality (default 85, recommended 70–90).

Save mode:

Overwrite existing .webp: Replace existing .webp files.

Create new (_new.webp): Generate new files while keeping originals.

Click Convert to start the process.

When finished, the program will display the number of converted and skipped images.
