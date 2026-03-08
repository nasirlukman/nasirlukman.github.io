---
layout: post
title: "Pertambangan di Pulau-Pulau Kecil Indonesia"
date: 2026-03-07 20:36:10
description: Melacak aktivitas pertambangan di pulau kecil dengan analisa GIS dan citra satelit
tags: remote_sensing, monitoring, mining, security, GIS, environment
---

Beberapa bulan yang lalu, perbincangan publik ramai terkait aktivitas pertambangan nikel di Pulau Gag. Kasus ini mulai viral setelah aksi protes [Greenpeace Indonesia](https://www.greenpeace.org/indonesia/siaran-pers/63070/aktivis-greenpeace-aksi-di-konferensi-nikel-internasional/) di Konferensi Nikel Internasional di Jakarta pada Juni tahun lalu. Tentu, tudingan soal pelanggaran hukum dan kerusakan lingkungan membutuhkan investigasi mendalam dan data lapangan. da satu hal yang cukup mudah untuk diferivikasi: aktivitas pertambangan di pulau-pulau kecil.

Kegiatan pertambangan di pulau kecil memiliki potensi besar melanggar UU PWP3K No. 27/2007 juncto UU PWP3K No. 1/2014. Putusan MK No. 35/PUU-XXI/2023 mempertegas bahwa pertambangan di pulau kecil termasuk kegiatan berbahaya luar biasa *abnormally dangerous activity*, karena pulau-pulau kecil memiliki daya dukung terbatas, dan aktivitas tambang di sana dapat menimbulkan kerusakan permanen [1](https://www.tempo.co/politik/begini-aturan-penambangan-di-pulau-pulau-kecil-1673629)[2](https://apakabar.co.id/news/putusan-mk-nomor-35-puu-xxi-2023-koral-gkp-keliru-menafsirkan/).

Kegiatan pertambangan di pulau kecil seharusnya dapat terdeteksi dengan cukup akurat dan mudah dengan menggunakan citra penginderaan jauh dan analisis GIS. Di post kali ini, saya ingin membagikan sedikit hasil riset tipis-tipis saya mengenai topik ini.

# Pulau Kecil
Pertama kita butuh definisi tentang pulau kecil. Berdasarkan UU PWP3K No. 1/2014, pulau kecil merupakan pulau dengan luas ≤ 2,000 km². Indonesia, sebagai salah satu negara kepulauan terbesar di dunia, memiliki ribuan pulau. Berdasarkan data batas provinsi dari Badan Informasi Geospasial [(BIG)](https://geoportal.big.go.id/#/), terdapat setidaknya 19.249 pulau di Indonesia.

Jika kita menghapus pulau > 2.000 km² dan pulau < 1 km² (karena kemungkinan aktivitas tambang di pulau sangat kecil relatif rendah), tersisa 1.622 pulau kecil (Gambar 1). Jumlah ini masih cukup banyak, tetapi memungkinkan seabgai titik awal untuk analisis citra satelit lebih mendetail.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_15_small_islands.png" 
            class="img-fluid rounded" 
            alt="Pulau-pulau kecil di Indonesia yang ditampilan dengan latar google basemap."
        %}
    </div>
</div>
<div class="caption">
    Gambar 1. Pulau-pulau kecil ditandai dengan warna oranye. Peta dasar menggunakan Google Basemap.
</div>

# Aktivitas Pertambangan di Pulau-Pulau Kecil
Setelah batas pulau kecil ditentukan, citra satelit [LANDSAT](https://science.nasa.gov/mission/landsat/) dapat dianalisis untuk mendeteksi keberadaan tambang dan menghitung total area tambang dari tahun ke tahun (Gambar 2). Pada 2020, diperkirakan terdapat sekitar 16.800 hektar bukaan tambang di pulau kecil. Beberapa tambang masih aktif, sementara sebagian lain sudah tidak beroperasi dan tidak direklamasi. Status perizinan tambang juga bervariasi, ada yang resmi dan ada yang tanpa izin. Dalam analisis ini, perbedaan status tersebut tidak dibedakan dan semuanya dihitung sebagai bukaan tambang.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_15_total_area_per_year.png" 
            class="img-fluid rounded" 
            alt="Grafik yang menujukkan trend luasan bukaan tambang di pulau-pulau kecil di Indonesia selama 30 tahun. sejak tahun 1990 sampai 2020."
        %}
    </div>
</div>
<div class="caption">
    Gambar 2. Grafik yang menunjukkan total luas bukaan tambang di pulau-pulau kecil di Indonesia dari tahun 1990 hingga 2020.
</div>

Sebagian besar pertambangan di pulau kecil berkaitan dengan nikel, terutama di Sulawesi Tenggara, Maluku Utara, dan Papua Barat Daya, serta bauksit di Kepulauan Riau. Selain itu, terdapat pertambangan timah di Bangka Belitung, batubara di Kalimantan Utara, dan bijih besi di Kalimantan Selatan (Gambar 3).

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_15_example_per_commodity.png" 
            class="img-fluid rounded" 
            alt="Beberapa contoh citra satelit resolusi tinggi untuk pertambangan di pulau kecil. COntoh dari beberapa komoditas tambang yang berbeda seperti: bauksit, nikel, timah, batubara, bijih besi"
        %}
    </div>
</div>
<div class="caption">
    Gambar 3. Contoh citra satelit resolusi tinggi (Google Basemap Mosaic) yang menampilkan bukaan tambang di beberapa pulau kecil dengan berbagai komoditas: (1) Nikel – Pulau Gei, (2) Batubara – Pulau Bunyu, (3) Bijih Besi – Pulau Sebuku, (4) Timah – Pulau Lepar, (5) Bauksit – Pulau Kei.
</div>

Gambar 3 menunjukkan betapa parahnya imbas kegiatan pertambangan di beberapa pulau kecil di Indonesia. COntoh paling mencolok terlihat di Pulau Kas, di mana lebih dari 90% wilayah pulau telah menjadi bukaan tambang. Aktivitas pertambangan diperkirakan berhenti sejak 2014, namun tidak ada kegiatan reklamasi atau pemulihan pasca-tambang. Padahal sebelumnya, pulau ini merupakan kawasan hutan. [Ombudsman](https://ombudsman.go.id/perwakilan/news/r/pwkmedia--ombudsman-curigai-dana-pemulihan-lingkungan-hilang-tambang-bauksit-tinggalkan-luka-di-karimun) juga menduga dana pemulihan lingkungan yang seharusnya diberikan perusahaan kepada pemerintah hilang

Pertambangan bauksit di Kepulauan Riau secara umum telah berlangsung setidaknya sejak 1990-an. Provinsi ini unik karena seluruh daratannya termasuk pulau kecil, dan sejak lama dikenal sebagai penghasil bauksit, timah, dan granit. Sekitar 40% total bukaan tambang di pulau kecil Indonesia berada di wilayah ini. Artinya, sejak tahun 2007 seharusnya sudah dilakukan kajian khusus terkait aktivitas pertambangan di provinsi ini. Namun kenyataannya, luasan bukaan tambang di pulau-pulau kecil terus bertambah setidaknya hingga 2020.

Sementara itu, pertambangan nikel di pulau kecil Sulawesi Tenggara dan Maluku Utara relatif baru. Meski sudah ada tambang sejak awal 2000-an, ekspansi signifikan baru terjadi mulai 2018 di Sulawesi Tenggara dan 2020 di Maluku Utara.

Selain analisis untuk mendeteksi bukaan tambang dan menghitung luasnya tiap tahun, animasi perubahan bentang alam per tahun juga dapat dibuat menggunakan data LANDSAT. Ini membantu memahami bagaimana aktivitas tambang mengubah lanskap pulau-pulau kecil sejak 1990-an hingga saat ini. Gambar 4 dan 5 menunjukkan perubahan bentang alam Pulau Mala-Mala dan Pulau Pakal di Maluku Utara dari tahun 1995 hingga 2025, memperlihatkan seberapa cepat tambang dapat mengubah sebagian besar bentang alam pulau kecil.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_15_pulau_malamala.gif" 
            class="img-fluid rounded" 
            alt="Animasi citra satelit temporal LANDSAT di Pulau Malamala Maluku Utara yang menunjukkan perkembangan aktivitas pertambangan Nikel"
        %}
    </div>
</div>
<div class="caption">
    Gambar 4. Animasi perubahan bentang alam Pulau Malamala dari tahun 1995 hingga 2025.
</div>

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_15_pulau_pakal.gif" 
            class="img-fluid rounded" 
            alt="Animasi citra satelit temporal LANDSAT di Pulau Malamala Maluku Utara yang menunjukkan perkembangan aktivitas pertambangan Nikel"
        %}
    </div>
</div>
<div class="caption">
    Gambar 4. Animasi perubahan bentang alam Pulau Pakal dari tahun 1995 hingga 2025.
</div>

# Penutup
Setelah keributan di dunia maya terkait aktivitas penambangan di Pulau Gag, pemerintah mencabut izin beberapa perusahaan, namun PT. GAG dikecualikan dengan dalil yang kurang [jelas](https://www.tempo.co/politik/mengapa-pemerintah-tak-cabut-izin-pt-gag-nikel-di-raja-ampat--1673941). Di daerah lain, bisa jadi ada pengecualian serupa untuk meloloskan beberapa perusahaan tambang. Namun, pengecualian seperti ini tidak boleh menjadi norma. Sebagaimana dinyatakan Mahkamah Konstitusi, aktivitas pertambangan di pulau kecil termasuk abnormally dangerous activity. Pulau Kas menjadi contoh ekstrim, di mana lebih dari 90% luas pulau telah rusak akibat pertambangan dan bentang alamnya sudah sangat sulit untuk dikembalikan ke kondisi awal.

Analisis sederhana ini menunjukkan tren penting: luas bukaan tambang di pulau-pulau kecil terus meningkat, meski UU PWP3K 2007 melarang aktivitas tersebut, dan sebagian tambang yang ditinggalkan tidak direklamasi. Kecolongan di masa lalu karena sulitnya pengawasan pulau kecil yang luas dan terpencil seharusnya tidak lagi menjadi alasan. Dengan citra satelit yang semakin banyak dan mudah diakses, sistem pemantauan near-real-time seharusnya bisa diwujudkan. Yang terpenting kini adalah political will untuk menegakkan undang-undang dan memastikan pengelolaan pulau kecil berlangsung lebih bertanggung jawab.