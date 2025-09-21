from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import add

app = Flask(__name__)
app.secret_key = "isi_dengan_rahasia_kamu"  # ganti dengan secret key aman

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pemasukan", methods=["GET", "POST"])
def pemasukan():
    if request.method == "POST":
        try:
            jumlah = request.form["jumlah"]
            keterangan = request.form["keterangan"]
            tanggal = datetime.strptime(request.form["tanggal"], "%Y-%m-%d").date()

            add.inputPemasukan(jumlah, keterangan, tanggal)
            flash("✅ Data pemasukan berhasil disimpan!", "success")
        except Exception as e:
            flash(f"❌ Terjadi kesalahan: {e}", "error")
        return redirect(url_for("pemasukan"))

    # GET
    return render_template("pemasukan.html")

@app.route("/pengeluaran", methods=["GET", "POST"])
def pengeluaran():
    if request.method == "POST":
        try:
            jumlah = request.form["jumlah"]
            keterangan = request.form["keterangan"]
            tanggal = datetime.strptime(request.form["tanggal"], "%Y-%m-%d").date()

            add.inputPengeluaran(jumlah, keterangan, tanggal)
            flash("✅ Pengeluaran berhasil disimpan!", "success")
        except Exception as e:
            flash(f"❌ Terjadi kesalahan: {e}", "error")
        return redirect(url_for("pengeluaran"))

    return render_template("pengeluaran.html")

if __name__ == "__main__":
    app.run(debug=True)
