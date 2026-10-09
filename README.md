# 🚀 InvoiceFlow - Quản Lý & Tính Toán Hóa Đơn Bán Hàng

Ứng dụng web hiện đại được phát triển bằng **Python (Flask)** giúp quản lý bán hàng, tự động tính chiết khấu theo bậc thang, tính thuế VAT, phí vận chuyển và xuất hóa đơn chi tiết, rõ ràng.

---

## ✨ Tính Năng Nổi Bật

- 🔐 **Hệ thống phân quyền & xác thực:** Hỗ trợ đăng nhập với các vai trò nhân viên và quản lý, bảo vệ an toàn các trang nghiệp vụ.
- 📊 **Bảng điều khiển (Dashboard):** Giao diện trực quan, hiển thị thông tin tài khoản và điều hướng thuận tiện.
- 📝 **Tạo hóa đơn & kiểm tra dữ liệu:** Form nhập thông tin khách hàng, sản phẩm, đơn giá, số lượng, thuế VAT và phí ship với cơ chế kiểm tra tính hợp lệ chặt chẽ.
- ⚡ **Tự động áp dụng chiết khấu bậc thang:**
  - Từ **100 sản phẩm** trở lên: Giảm **12%**
  - Từ **50 đến 99 sản phẩm**: Giảm **7%**
  - Từ **10 đến 49 sản phẩm**: Giảm **3%**
  - Dưới **10 sản phẩm**: Không áp dụng chiết khấu (0%)
- 🧾 **Xuất hóa đơn chi tiết:** Tự động tính thành tiền, chiết khấu, tiền sau chiết khấu, tiền VAT, phí vận chuyển và tổng tiền cần thanh toán.

---

## 🔑 Tài Khoản Demo

| Vai trò | Tên tài khoản | Mật khẩu |
| :--- | :--- | :--- |
| **Nhân viên** | `nhanvien` | `nv123456` |
| **Quản lý** | `quanly` | `ql123456` |

---

## 🛠️ Công Nghệ Sử Dụng

- **Backend:** Python 3.x, Flask
- **Frontend:** HTML5, CSS3, Jinja2 Template, Google Fonts (Be Vietnam Pro)

---

## 📥 Hướng Dẫn Cài Đặt & Chạy Thử

1. **Clone repository về máy:**
   ```bash
   git clone https://github.com/lequanganh612007-creator/Tuluyenpy2.git
   cd Tuluyenpy2
   ```

2. **Cài đặt thư viện phụ thuộc:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Khởi chạy ứng dụng:**
   ```bash
   python app.py
   ```

4. **Truy cập vào trình duyệt:**
   Mở trình duyệt và truy cập: [http://localhost:5000](http://localhost:5000)
