from flask import Flask,render_template,request,redirect, url_for, session,flash
app = Flask(__name__)
app.secret_key = "Thay_chuoi_bi_mat_dai_va_kho_doan"
USERS ={
    "nhanvien": "nv123456",
    "quanly": "ql123456"
}
@app.route("/")
def index():
    if "user_login" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))
@app.route("/login", methods=["GET","POST"])
def login():
    if "user_login" in session:
        return redirect(url_for("dashboard"))
    if request.method == "POST":
        tai_khoan = request.form.get("tai_khoan", "").strip()
        mat_khau = request.form.get("mat_khau", "")

        if tai_khoan in USERS and USERS[tai_khoan] == mat_khau:
            session["user_login"]= tai_khoan
            flash("Đăng nhập thành công!", "success")
            return redirect(url_for("dashboard"))
        flash("Sai tài khoản hoặc mật khẩu!", "danger")
        return redirect(url_for("login"))
    return render_template("login.html")
#yêu cầu 4:bảo vệ trang và đăng xuất
@app.route("/dashboard")
def dashboard():
    if "user_login" not in session:
        flash("vui lòng đăng nhập trước!", "warning")
        return redirect(url_for("login"))

    return render_template("dashboard.html",tai_khoan=session["user_login"])

@app.route("/logout")
def logout():
    session.pop("user_login", None)
    flash("Bạn đã đăng xuất.","info")
    return redirect(url_for("login"))
#Yêu cầu 5:Lấy dữ liệu và kiểm trá kiểu số
@app.route("/hoa_don", methods=["GET", "POST"])
def hoa_don():
    if "user_login" not in session:
        flash("Vui lòng đăng nhập trước!", "warning")
        return redirect(url_for("login"))

    if request.method == "POST":
        ten_khach = request.form.get("ten_khach", "").strip()
        ten_san_pham = request.form.get("ten_san_pham", "").strip()
        try:
            don_gia = float(request.form.get("don_gia", ""))
            so_luong = int(request.form.get("so_luong", ""))
            vat = float(request.form.get("vat", ""))
            phi_van_chuyen = float(request.form.get("phi_van_chuyen", ""))
        except (ValueError,TypeError):
            flash("Vui lòng nhập số hợp lệ!", "danger")
            return redirect(url_for("hoa_don"))

        if not ten_khach or not ten_san_pham:
            flash("Vui lòng nhập tên khách và tên sản phẩm!", "warning")
            return redirect(url_for("hoa_don"))
        if don_gia <=0 or so_luong < 1 or vat <0 or phi_van_chuyen < 0:
            flash("ĐƠn giá lớn hơn 0,số lượng ít nhất là 1, VAT phí vận chuyển không được âm!", "warning")
            return redirect(url_for("hoa_don"))

        thanh_tien = don_gia * so_luong
        if so_luong >= 100:
            ty_le_chiet_khau = 12
        elif so_luong >= 50:
            ty_le_chiet_khau = 7
        elif so_luong >= 10:
            ty_le_chiet_khau = 3
        else:
            ty_le_chiet_khau = 0

        tien_chiet_khau = thanh_tien * ty_le_chiet_khau / 100
        tien_sau_chiet_khau = thanh_tien - tien_chiet_khau
        tien_vat = tien_sau_chiet_khau * vat /100
        tien_hang = tien_sau_chiet_khau + tien_vat
        tong_thanh_toan = tien_hang + phi_van_chuyen

        hoa_don_data = {
            "tai_khoan": session["user_login"],
            "ten_khach": ten_khach,
            "ten_san_pham": ten_san_pham,
            "don_gia": don_gia,
            "so_luong": so_luong,
            "vat": vat,
            "phi_van_chuyen":phi_van_chuyen,
            "thanh_tien": thanh_tien,
            "ty_le_chiet_khau": ty_le_chiet_khau,
            "tien_chiet_khau": tien_chiet_khau,
            "tien_sau_chiet_khau": tien_sau_chiet_khau,
            "tien_vat": tien_vat,
            "tien_hang": tien_hang,
            "tong_thanh_toan": tong_thanh_toan
        }
        return render_template("ket_qua.html",hoa_don=hoa_don_data)
    return render_template("form_hoa_don.html")

if __name__ == "__main__":
    app.run(debug=True)