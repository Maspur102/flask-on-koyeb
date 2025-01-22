from flask import Flask, render_template, request, flash, redirect
from flask_mail import Mail, Message

app = Flask(__name__)

# Kunci rahasia untuk flash message
app.secret_key = "supersecretkey"

# Konfigurasi Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'maspur15022005@gmail.com'  # Ganti dengan email Anda
app.config['MAIL_PASSWORD'] = 'your-email-pa'       # Ganti dengan password email Anda
app.config['MAIL_DEBUG'] = True  # Debugging untuk email

# Inisialisasi Flask-Mail
mail = Mail(app)

# Route untuk halaman utama
@app.route('/')
def home():
    return render_template('index.html')

    # Route untuk halaman "Tentang Kami"
    @app.route('/about')
    def about():
        return render_template('about.html')

        # Route untuk halaman "Layanan/Produk"
        @app.route('/services')
        def services():
            return render_template('services.html')

            # Route untuk halaman "Testimoni"
            @app.route('/testimonials')
            def testimonials():
                return render_template('testimonials.html')

                # Route untuk halaman "Kontak"
                @app.route('/contact', methods=['GET', 'POST'])
                def contact():
                    if request.method == 'POST':
                            name = request.form['name']
                                    email = request.form['email']
                                            message = request.form['message']
                                                    
                                                            # Kirim email
                                                                    try:
                                                                                msg = Message(
                                                                                                subject="Pesan Baru dari Website Anda",
                                                                                                                sender=app.config['MAIL_USERNAME'],
                                                                                                                                recipients=['maspur15022005@gmail.com'],  # Ganti dengan email tujuan
                                                                                                                                                body=f"Nama: {name}\nEmail: {email}\nPesan: {message}"
                                                                                                                                                            )
                                                                                                                                                                        mail.send(msg)
                                                                                                                                                                                    
                                                                                                                                                                                                # Tampilkan pesan berhasil
                                                                                                                                                                                                            flash("Pesan Anda telah berhasil dikirim. Terima kasih!")
                                                                                                                                                                                                                    except Exception as e:
                                                                                                                                                                                                                                print(f"Error: {e}")
                                                                                                                                                                                                                                            flash("Terjadi kesalahan. Pesan tidak dapat dikirim.")

                                                                                                                                                                                                                                                    return redirect('/contact')  # Kembali ke halaman kontak

                                                                                                                                                                                                                                                        return render_template('contact.html')

                                                                                                                                                                                                                                                        if __name__ == '__main__':
                                                                                                                                                                                                                                                            app.run(debug=True)
                                                                                                                                                                                                                                                            