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
        'maps':'https://maps.app.goo.gl/4iT2zhgigMnuWfXGA'
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
        'maps':'https://maps.app.goo.gl/tHYViEcvkDC9v3NR6'
    },
    
    {

  'id': 3,
        'nama': 'Kos Zahira',
        'jenis': 'Putri',
        'alamat': 'Jln Zaitun 1 No 80 Isvil',
        'jarak': '0.6',
        'fasilitas': 'Wifi Listrik Air Kasur Bantal Set Seprei Lemari Dapur Umum Kamar mandi luar Parkir',
        'harga': 700000,
        'kapasitas': '2 Orang',
        'gambar': ['kost3.jpg', 'kost3_2.jpg'],
        'maps': 'https://maps.app.goo.gl/nqFU6YUqKMj3oP6R9'
    },

    {
        'id': 4,
        'nama': 'Syifa Kos',
        'jenis': 'Putri',
        'alamat': 'Jln Qadr 5 No 27',
        'jarak': '0.7',
        'fasilitas': 'Kasur Listrik Air Lemari Mesin Cuci Wifi Kamar mandi luar Parkir',
        'harga': 800000,
        'kapasitas': '2 Orang',
        'gambar': ['kost4.jpg', 'kost4_2.jpg'],
        'maps': 'https://maps.app.goo.gl/fNupGg7cSNEPhv7Q7'
    },

    {
        'id': 5,
        'nama': 'Kos Thin Karawaci',
        'jenis': 'Putra',
        'alamat': 'Jln Thin 8 No 15',
        'jarak': '1.35',
        'fasilitas': 'Kasur Lemari Karpet Meja Belajar Kamar mandi dalam Shower Air Listrik Wifi Parkir',
        'harga': 800000,
        'kapasitas': '1 Orang',
        'gambar': ['kost5.jpg', 'kost5_2.jpg'],
        'maps': 'https://maps.app.goo.gl/ZfrcP2avif17vg9F9'
    },

    {
        'id': 6,
        'nama': 'Kos Omah Rizki',
        'jenis': 'Putra',
        'alamat': 'Jln Qadr Raya No 33',
        'jarak': '0.9',
        'fasilitas': 'Tempat Tidur Lemari AC Kamar mandi luar Air Listrik Dapur Umum Parkir',
        'harga': 1200000,
        'kapasitas': '1 Orang',
        'gambar': ['kost6.jpg', 'kost6_2.jpg'],
        'maps': 'https://maps.app.goo.gl/1r1tyEc8s8i6EmS38'
    },

    {
        'id': 7,
        'nama': 'Kos Mafaza',
        'jenis': 'Umum',
        'alamat': 'Jln Buntu Danau Kelapa Dua',
        'jarak': '1.9',
        'fasilitas': 'Kasur Lemari Meja Belajar Wifi Air Listrik Kamar mandi dalam Dapur Umum Kulkas Umum Bantal Parkir',
        'harga': 1000000,
        'kapasitas': '2 Orang',
        'gambar': ['kost7.jpg', 'kost7_2.jpg'],
        'maps': 'https://maps.app.goo.gl/JeWYQNiUasq1KqBs9'
    },

    {
        'id': 8,
        'nama': 'Kos H Arizal Latif',
        'jenis': 'Putri',
        'alamat': 'Jln Zaitun 1 Blok B1 No 18',
        'jarak': '0.8',
        'fasilitas': 'Wifi Kasur Listrik Air Lemari Kipas Gorden Kamar mandi dalam Seprei Bantal Dapur Umum Kulkas Umum Tong Sampah Gantungan Baju Alas Kaki',
        'harga': 800000,
        'kapasitas': '1 Orang',
        'gambar': ['kost8.jpg', 'kost8_2.jpg'],
        'maps': 'https://maps.app.goo.gl/NR2eMEk533bYkmpU6'
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