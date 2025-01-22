from flask import Flask, render_template, request, flash, redirect

app = Flask(__name__)

# Kunci rahasia untuk flash message
app.secret_key = "supersecretkey"

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
                            name = request.form.get('name')
                                    email = request.form.get('email')
                                            message = request.form.get('message')
                                                    
                                                            # Tampilkan pesan berhasil
                                                                    flash("Pesan Anda telah berhasil diterima. Terima kasih atas masukan Anda!")

                                                                            return redirect('/contact')  # Kembali ke halaman kontak

                                                                                return render_template('contact.html')

                                                                                if __name__ == '__main__':
                                                                                    app.run(debug=True)
                                                                                    