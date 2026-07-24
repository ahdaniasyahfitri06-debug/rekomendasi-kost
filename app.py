from flask import Flask, render_template, abort, request, redirect, url_for

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import json
import os

app = Flask(__name__)

# ==========================================
# DATA KOST
# ==========================================

kost_data = [

    {
        'id': 1,
        'nama': 'Kos Umi Lisya',
        'jenis': 'Putri',
        'alamat': 'Jln Qadr 7 No 10',
        'deskripsi': 'Kost putri yang nyaman dengan fasilitas lengkap, cocok untuk mahasiswa yang mengutamakan kenyamanan',
        'jarak': '0.8 km',
        'fasilitas': 'Wifi, AC, Lemari, Kasur',
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
        'deskripsi': 'Kost umum dengan suasana tenang serta dilengkapi area parkir dan dapur bersama',
        'jarak': '1 km',
        'fasilitas': 'Wifi, Parkir, Dapur',
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
        'deskripsi': 'Pilihan kost ekonomis dengan fasilitas dasar yang lengkap dan lingkungan yang nyaman',
        'jarak': '0.6',
        'fasilitas': 'Wifi, Listrik, Air, Kasur, Bantal, Set, Seprei, Lemari, Dapur, Umum, Kamar mandi luar, Parkir',
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
        'deskripsi': 'Kost putri dengan lingkungan yang bersih dan aman, cocok untuk mahasiswa maupun karyawan',
        'jarak': '0.7',
        'fasilitas': 'Kasur, Listrik, Air, Lemari, Mesin Cuci, Wifi, Kamar mandi luar, Parkir',
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
        'deskripsi': 'Kost putra dengan kamar luas dan fasilitas belajar yang mendukung aktivitas sehari-hari',
        'jarak': '1.35',
        'fasilitas': 'Kasur, Lemari, Karpet, Meja, Belajar, Kamar mandi dalam, Shower, Air, Listrik, Wifi, Parkir',
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
        'deskripsi': 'Menawarkan kamar ber-AC dengan harga yang sebanding dengan fasilitas yang tersedia',
        'jarak': '0.9',
        'fasilitas': 'Tempat Tidur, Lemari, AC, Kamar mandi luar, Air, Listrik, Dapur, Umum, Parkir',
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
        'deskripsi': 'Kost umum dengan fasilitas lengkap serta tersedia kulkas bersama untuk penghuni',
        'jarak': '1.9',
        'fasilitas': 'Kasur, Lemari, Meja, Belajar, Wifi, Air, Listrik, Kamar mandi dalam, Dapur, Umum, Kulkas, Umum, Bantal, Parkir',
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
        'deskripsi': 'Kost putri dengan fasilitas yang lengkap dan lingkungan yang nyaman untuk beristirahat',
        'jarak': '0.8',
        'fasilitas': 'Wifi, Kasur, Listrik, Air, Lemari, Kipas, Gorden, Kamar mandi dalam, Seprei, Bantal, Dapur, Umum, Kulkas, Umum, Tong Sampah, Gantungan Baju, Alas Kaki',
        'harga': 800000,
        'kapasitas': '1 Orang',
        'gambar': ['kost8.jpg', 'kost8_2.jpg'],
        'maps': 'https://maps.app.goo.gl/NR2eMEk533bYkmpU6'
    },
     {
        'id': 9,
        'nama': 'Kos Kara karawaci',
        'jenis': 'Umum',
        'alamat': 'Jl. Vila Permata No.1, Bencongan, Kecamatan Kelapa Dua, Kabupaten Tangerang, Banten 15810',
        'deskripsi': 'Kost premium dengan fasilitas modern, CCTV, dan lokasi yang strategis',
        'jarak': '2,3',
        'fasilitas': 'Wifi, Kasur, Listrik, Air, Lemari, Ac, Gorden, Kamar mandi dalam, Seprei, Bantal, Dapur, Umum, Kulkas, Umum, laundry, CCTV, Parkir',
        'harga': 2000000,
        'kapasitas': '2 Orang',
        'gambar': ['kost9.jpg', 'kost9_2.jpg'],
        'maps': 'https://maps.app.goo.gl/S6DH8aa2Cs1dR7QS6'
    },
      {
        'id': 10,
        'nama': 'Kos Sapona Sakti',
        'jenis': 'Umum',
        'alamat': 'Islamic Village, Jl. Islamic Raya Komp.Soponasakti. Blok C5 kav XIV, RT.002/RW.014, Klp. Dua, Kec. Karawaci, Kabupaten Tangerang, Banten 15810',
        'deskripsi': 'Kost nyaman di kawasan Islamic Village dengan akses yang mudah ke berbagai fasilitas umum',
        'jarak': '1,4',
        'fasilitas': 'Wifi, Kasur, Listrik, Air, Lemari, Ac, Kamar mandi dalam, Bantal, Dapur, Umum, Kulkas, Umum, Parkir',
        'harga': 1000000,
        'kapasitas': '1 Orang',
        'gambar': ['kost10.jpg', 'kost10_2.jpg'],
        'maps': 'https://maps.app.goo.gl/Rh7u4DFCsooiM3v48'
    },
      {
        'id': 11,
        'nama': 'Kos Putri Ibu Dewi',
        'jenis': 'Putri',
        'alamat': 'B3 No.1, Village, Jl. Zaitun I Jl. Islamic Raya, Kelapa Dua, Tangerang Regency, Banten 15810',
        'deskripsi': 'Kost putri dengan suasana kekeluargaan dan fasilitas yang mendukung aktivitas sehari-hari',
        'jarak': '0,8',
        'fasilitas': 'AC, kasur, ruang Tamu, Dapur, umum, Toilet luar, Meja, Lemari, Kasur, Parkir, Wifi',
        'harga': 1000000,
        'kapasitas': '1 Orang',
        'gambar': ['kost11.jpg', 'kost11_2.jpg'],
        'maps': 'https://maps.app.goo.gl/SA1NQcAck72Wyhar7'
    },
      {
        'id': 12,
        'nama': 'Kos Griya Mawaddah',
        'jenis': 'Umum',
        'alamat': 'Jl. Mawaddah Raya No.5, Klp. Dua, Kecamatan Kelapa Dua, Kabupaten Tangerang, Banten 15810',
        'deskripsi': 'Kost eksklusif dengan fasilitas lengkap, laundry, dispenser, dan penjaga kost',
        'jarak': '1,6',
        'fasilitas': 'AC, Meja, Kursi, Meja Rias, Kasur, TV, Lemari, Kamar mandi dalam, Dapur, umum, Parkir, Wifi, Laundry, Kulkas, Umum, Penjaga Kost, Dispenser, umum',
        'harga': 1900000,
        'kapasitas': '1 Orang',
        'gambar': ['kost12.jpg', 'kost12_2.jpg'],
        'maps': 'https://maps.app.goo.gl/ACT9VFe4kEof2Sv56'
    },
      {
        'id': 13,
        'nama': 'Kos H.yadi',
        'jenis': 'Umum',
        'alamat': 'jln besar legok gg h iman no 53',
        'deskripsi': 'Pilihan kost sederhana dengan kamar nyaman dan lokasi yang mudah dijangkau',
        'jarak': '1',
        'fasilitas': 'AC, kasur, Lemari, Kamar mandi dalam, Parkir',
        'harga': 1100000,
        'kapasitas': '1 Orang',
        'gambar': ['kost13.jpg', 'kost13_2.jpg'],
        'maps': 'https://maps.app.goo.gl/WobAkgq3qBxSKaXj7'
    },
      {
        'id': 14,
        'nama': 'Kost Murai Sawit Cibodas Tangerang',
        'jenis': 'Putra',
        'alamat': 'Jl. Murai Raya No.14, RT.003/RW.013, Panunggangan Bar., Kec. Cibodas, Kota Tangerang, Banten 15139',
        'deskripsi': 'Kost putra dengan fasilitas lengkap serta tersedia penjaga kost untuk meningkatkan keamanan',
        'jarak': '1',
        'fasilitas': 'AC, kasur, Lemari, Kamar mandi dalam, Parkir, Meja, Cermin, Kursi, Wastafel, Jemuran, WiFi, Penjaga Kost',
        'harga': 1150000,
        'kapasitas': '1 Orang',
        'gambar': ['kost14.jpg', 'kost14_2.jpg'],
        'maps': 'https://maps.app.goo.gl/tPcYzeg3aW7nD37t6'
    },
     {
        'id': 15,
        'nama': 'Kos griya kausar',
        'jenis': 'Umum',
        'alamat': 'Jl. Kelapa Dua Raya, Klp. Dua, Kecamatan Kelapa Dua, Kota Tangerang, Banten 15810',
        'deskripsi': 'Kost umum dengan suasana yang nyaman, cocok bagi mahasiswa maupun pekerja',
        'jarak': '1,5',
        'fasilitas': 'AC, kasur, Lemari, Kamar mandi dalam, Parkir, Meja, Kursi, Jemuran, WiFi, dapur umum',
        'harga': 1100000,
        'kapasitas': '1 Orang',
        'gambar': ['kost15.jpg', 'kost15_2.jpg'],
        'maps': 'https://maps.app.goo.gl/szL8dUWL82Vfg8fY9'
    },
     {
        'id': 16,
        'nama': 'reginaldcia kost',
        'jenis': 'Umum',
        'alamat': 'Jl. Sinai Raya No.22 blok k 1, Klp. Dua, Kecamatan Kelapa Dua, Kabupaten Tangerang, Banten 15810',
        'deskripsi': 'Menawarkan gazebo sebagai area bersantai serta dapur bersama yang nyaman digunakan',
        'jarak': '1,2',
        'fasilitas': 'AC, kasur, Lemari, Kamar mandi dalam, Parkir, Meja, Kursi, Jemuran, WiFi, gajebo, dapur umum',
        'harga': 1000000,
        'kapasitas': '1 Orang',
        'gambar': ['kost16.jpg', 'kost16_2.jpg'],
        'maps': 'https://maps.app.goo.gl/21hEUh4Fg1kRnTNF7'
    },
     {
        'id': 17,
        'nama': ' Kos putri adilla',
        'jenis': 'Putri',
        'alamat': ' Kecamatan kelapa dua,kabupaten tangerang RT/RW: 01/04,pertigaan kelapa dua, Jl. Kano Raya, arah, Kec. Legok, Kabupaten Tangerang, Banten 15810',
        'deskripsi': 'Kost putri dengan lingkungan yang tenang dan fasilitas yang menunjang kebutuhan penghuni',
        'jarak': '1',
        'fasilitas': 'kasur, Lemari, Kamar mandi dalam, Parkir, Meja, Kursi, Jemuran, WiFi, gajebo, dapur umum',
        'harga': 900000,
        'kapasitas': '1 Orang',
        'gambar': ['kost17.jpg', 'kost17_2.jpg'],
        'maps': 'https://maps.app.goo.gl/m1psYQ2wy89rcMPs9'
    },
      {
        'id': 18,
        'nama': 'Shafa kost putri',
        'jenis': 'Putri',
        'alamat': 'Jl. Mawaddah X No.11 Blok J8, Klp. Dua, Kecamatan Kelapa Dua, Kabupaten Tangerang, Banten 15810·5500',
        'deskripsi': 'Kost putri dengan lokasi strategis, fasilitas lengkap, dan suasana yang nyaman untuk belajar maupun beristirahat',
        'jarak': '2',
        'fasilitas': 'kasur, Lemari, Kamar mandi dalam, Parkir, Meja, Kursi, Jemuran, WiFi, gajebo, dapur umum',
        'harga': 900000,
        'kapasitas': '1 Orang',
        'gambar': ['kost18.jpg', 'kost18_2.jpg'],
        'maps': 'https://maps.app.goo.gl/Z8YTjNKQ4ua1RVRf9'
    },

]

# ==========================================
# RATING ASLI (disimpan di file JSON, BUKAN data karangan)
# Format: { "1": [5, 4, 5], "2": [4] , ... }  -> id_kost: daftar rating dari penghuni asli
# ==========================================

RATING_FILE = 'ratings.json'


def load_ratings():
    if os.path.exists(RATING_FILE):
        with open(RATING_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}


def simpan_rating(kost_id, rating):
    data = load_ratings()
    key = str(kost_id)
    data.setdefault(key, [])
    data[key].append(rating)
    with open(RATING_FILE, 'w') as f:
        json.dump(data, f, indent=2)


def hitung_content_score(preferensi):

    dokumen = [preferensi]

    for kost in kost_data:
        dokumen.append(
            kost['fasilitas'] + " " +
            kost['jenis']
        )

    tfidf = TfidfVectorizer()

    matrix = tfidf.fit_transform(dokumen)

    similarity = cosine_similarity(
        matrix[0:1],
        matrix[1:]
    )[0]

    return similarity


def hitung_collaborative_score():
    """
    Menghitung skor rata-rata rating ASLI per kost dari ratings.json.
    Kalau kost belum punya rating sama sekali, skornya 0 (dan akan
    ditandai 'Belum ada rating' di alasan rekomendasi).
    """
    data_rating = load_ratings()
    skor = {}

    for kost in kost_data:
        daftar_rating = data_rating.get(str(kost['id']), [])
        if daftar_rating:
            skor[kost['id']] = sum(daftar_rating) / len(daftar_rating)
        else:
            skor[kost['id']] = 0

    return skor


def jumlah_rating(kost_id):
    data_rating = load_ratings()
    return len(data_rating.get(str(kost_id), []))


# ==========================================
# ROUTE
# ==========================================

@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/cari')
def cari():

    jenis = request.args.get('jenis', '')
    budget = request.args.get('budget', '')
    kapasitas = request.args.get('kapasitas', '')
    fasilitas = request.args.getlist('fasilitas')

    ada_input = jenis or budget or kapasitas or fasilitas
    if not ada_input:
        return render_template('index.html', hasil=None)

    preferensi = (jenis + " " + " ".join(fasilitas)).strip()

    # Kalau user cuma isi budget/kapasitas tanpa jenis & fasilitas,
    # tidak ada teks yang bisa dibandingkan lewat TF-IDF -> content_score akan 0 untuk semua kost.
    # Tandai kondisi ini supaya kita bisa fallback ke rating & jarak, bukan urutan data mentah.
    preferensi_kosong = (preferensi == "")

    content_scores = hitung_content_score(preferensi) if not preferensi_kosong else [0] * len(kost_data)
    collab_scores = hitung_collaborative_score()

    hasil = []

    for i, kost in enumerate(kost_data):

        content_score = content_scores[i] * 100
        collaborative_score = (collab_scores[kost['id']] / 5) * 100
        n_rating = jumlah_rating(kost['id'])

        if preferensi_kosong:
            # Fallback: tidak ada preferensi teks -> urutkan dari rating asli
            # (kalau belum ada rating sama sekali, semua kost dianggap setara -> 50%)
            skor = collaborative_score if n_rating > 0 else 50
        elif n_rating == 0:
            # Belum ada rating sama sekali -> 100% pakai content-based
            skor = content_score
        else:
            skor = (content_score * 0.7) + (collaborative_score * 0.3)

        alasan = []

        if fasilitas:
            fasilitas_kost = kost['fasilitas'].lower()
            fasilitas_cocok = [f for f in fasilitas if f.lower() in fasilitas_kost]
            fasilitas_tidak = [f for f in fasilitas if f.lower() not in fasilitas_kost]

            if fasilitas_cocok:
                alasan.append(f"✅ Memiliki fasilitas yang kamu cari: {', '.join(fasilitas_cocok)}")
            if fasilitas_tidak:
                alasan.append(f"⚠️ Tidak memiliki: {', '.join(fasilitas_tidak)}")

        if jenis:
            if jenis.lower() in kost['jenis'].lower():
                alasan.append(f"✅ Jenis kost sesuai: {kost['jenis']}")
            else:
                alasan.append(f"⚠️ Jenis kost berbeda: kost ini adalah {kost['jenis']}")

        if budget:
            try:
                budget_int = int(budget)
                selisih = budget_int - kost['harga']
                if selisih >= 0:
                    alasan.append(f"✅ Harga Rp{kost['harga']:,} masih dalam budget (sisa Rp{selisih:,})")
                else:
                    alasan.append(f"⚠️ Harga Rp{kost['harga']:,} melebihi budget sebesar Rp{abs(selisih):,}")
            except:
                pass

        if kapasitas:
            if kost['kapasitas'] == kapasitas:
                alasan.append(f"✅ Kapasitas kamar {kost['kapasitas']} sesuai kebutuhan")
            else:
                alasan.append(f"⚠️ Kapasitas kamar berbeda: {kost['kapasitas']}")

        alasan.append(f"📍 Jarak dari kampus: {kost['jarak']} km")

        # Rating kolaboratif -- info status rating sudah ditampilkan lewat badge terpisah
        # di frontend, jadi di sini cukup tampilkan kalau memang tinggi (nilai tambah nyata)
        if n_rating > 0 and collaborative_score > 70:
            alasan.append(f"⭐ Rating tinggi dari {n_rating} penghuni ({round(collaborative_score, 1)}%)")

        # Skor akhir -- ditampilkan polos tanpa jargon metode (TF-IDF, dsb),
        # karena label itu untuk keperluan laporan/dokumentasi, bukan untuk end-user.
        # Metode yang dipakai: Content-Based Filtering (TF-IDF + Cosine Similarity),
        # digabung dengan Collaborative Filtering berbasis rating asli penghuni kalau tersedia.
        alasan.append(f"🎯 Tingkat kecocokan: {round(skor, 2)}%")

        if jenis:
            if jenis.lower() not in kost['jenis'].lower():
                continue

        if budget:
            try:
                if kost['harga'] > int(budget):
                    continue
            except:
                pass

        if kapasitas:
            if kost['kapasitas'] != kapasitas:
                continue

        kost_copy = kost.copy()
        kost_copy['skor'] = round(skor, 2)
        kost_copy['alasan'] = alasan
        kost_copy['jumlah_rating'] = n_rating
        kost_copy['rating_rata2'] = round(collab_scores[kost['id']], 2)
        hasil.append(kost_copy)

    hasil.sort(key=lambda x: x['skor'], reverse=True)

    for i, kost in enumerate(hasil):
        kost['ranking'] = i + 1

    return render_template('index.html', hasil=hasil)


@app.route('/detail/<int:kost_id>')
def detail(kost_id):

    kost = next(
        (k for k in kost_data if k['id'] == kost_id),
        None
    )

    if kost is None:
        abort(404)

    collab_scores = hitung_collaborative_score()
    kost = kost.copy()
    kost['rating_rata2'] = round(collab_scores[kost_id], 2)
    kost['jumlah_rating'] = jumlah_rating(kost_id)

    return render_template(
        'detail.html',
        kost=kost
    )


@app.route('/rate/<int:kost_id>', methods=['POST'])
def rate(kost_id):
    """
    Endpoint baru untuk menyimpan rating asli dari penghuni.
    Panggil dari form kecil di detail.html, misalnya:

    <form method="POST" action="{{ url_for('rate', kost_id=kost.id) }}">
        <select name="rating">
            <option value="5">5 - Sangat Puas</option>
            <option value="4">4 - Puas</option>
            <option value="3">3 - Cukup</option>
            <option value="2">2 - Kurang</option>
            <option value="1">1 - Tidak Puas</option>
        </select>
        <button type="submit">Kirim Rating</button>
    </form>
    """
    try:
        rating = int(request.form['rating'])
        if 1 <= rating <= 5:
            simpan_rating(kost_id, rating)
    except (KeyError, ValueError):
        pass

    return redirect(url_for('detail', kost_id=kost_id))


@app.route('/semua-kost')
def semua_kost():

    semua = []
    collab_scores = hitung_collaborative_score()

    for i, kost in enumerate(kost_data):

        kost_copy = kost.copy()
        kost_copy['ranking'] = i + 1
        kost_copy['rating_rata2'] = round(collab_scores[kost['id']], 2)
        kost_copy['jumlah_rating'] = jumlah_rating(kost['id'])

        semua.append(kost_copy)

    return render_template(
        'semua_kost.html',
        kost_list=semua
    )


@app.route('/tentang')
def tentang():
    return render_template('tentang.html')


# ==========================================
# MAIN
# ==========================================

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)