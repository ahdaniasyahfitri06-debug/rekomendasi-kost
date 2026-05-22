from flask import Flask, render_template, abort

app = Flask(__name__)

# ==========================================
# DATA KOST
# ==========================================

kost_data = [

    {
        'id': 1,
        'nama': 'Kos Umi Lisya',
        'jenis': 'Khusus Putri',
        'alamat': 'Jln Qadr 7 No 10',
        'jarak': '0.8 km',
        'fasilitas': 'Wifi AC Lemari Kasur',
        'harga': 800000,
        'kapasitas': '2 Orang',
        'gambar': ['kost1.jpg', 'kost1_2.jpg'],

        # KOORDINAT KOST
        'lat': -6.224500,
        'lng': 106.651200
    },

    {
        'id': 2,
        'nama': 'Kos Sahakeelano',
        'jenis': 'Umum',
        'alamat': 'Jln Qadr 7 No 2',
        'jarak': '1 km',
        'fasilitas': 'Wifi Parkir Dapur',
        'harga': 900000,
        'kapasitas': '2 Orang',
        'gambar': ['kost2.jpg', 'kost2_2.jpg'],

        'lat': -6.223900,
        'lng': 106.652000
    }

]

# ==========================================
# ROUTE
# ==========================================

@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/cari')
def cari():
    return render_template(
        'index.html',
        hasil=kost_data
    )


@app.route('/tentang')
def tentang():
    return render_template('tentang.html')


@app.route('/detail/<int:kost_id>')
def detail(kost_id):

    kost = next(
        (k for k in kost_data if k['id'] == kost_id),
        None
    )

    if not kost:
        abort(404)

    return render_template(
        'detail.html',
        kost=kost
    )


# ==========================================
# MAIN
# ==========================================

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)