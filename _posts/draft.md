---
layout: post
title: "Satellite Embeddings and Large Scale Model"
date: 2025-11-07 23:36:10
description: Brief note on my experience in upscaling my model using Google Satelite Embedings
tags: remote_sensing, machine_learning, image_analysis
---

Several months ago in Indoensia nickel mining activity in Gag Island becoming a [National headline](https://www.tempo.co/lingkungan/gimik-di-pulau-gag-2073920). THis time it was broguht to public attention through [Greenpeace Indonesia protest](https://www.greenpeace.org/indonesia/siaran-pers/63070/aktivis-greenpeace-aksi-di-konferensi-nikel-internasional/) in International Nickel Conference in Jakarta. Of course any accusation related with serious environemtal violation require further investagiation and hard data from the ground. But here is the easy one to verify: small island mining is inherently prohibited by law Thorugh UU PWP3K No. 1/2014. The prohibitative interpration also reinforced by the Constitutional Court Decision No. 35/PUU-XXI/2023 whish stated mining activity in small sialnd as abnormally dangerous activity [1](https://www.tempo.co/politik/begini-aturan-penambangan-di-pulau-pulau-kecil-1673629)[2](https://apakabar.co.id/news/putusan-mk-nomor-35-puu-xxi-2023-koral-gkp-keliru-menafsirkan/).
This is something easily detectible and analyzed using remote sensing and good old GIS. in this post ill share some quick look to the state of small island mining in Indonesia as can be seen by quick analysis wiht Remote Sensning and GIS.


# Small Islands
First, what is a small island? Based on UU PWP3K No. 1/2014, a small island have area lower than or equal to 2,000 km2. Indonesia is an archipelago with thousands of island where most of it are small islands. Using the 2023 Indonesia Provincial BOundary Layer from [BIG](https://geoportal.big.go.id/#/) we can see 19,249 island total in Indonesia. If we take all the island that is below 2,000 km2 we still left with tens of thousands of island. But most are very small(< 1km2), and quite unlikely that there are any mining activity in island that small. if we also ignore the very small one, we are left with 1,622 island with size between 1km2 to 200km2. I think this is a good start to look further with remote sensing about mining activities in these islands.

[Image]

# Small Islands Mining
Now we have the boundary of the small island, we can use satellite imaggery to spot mining activities in those islands. Almost all of small island mining in Indonesia are realted witih Nickel mining in Sualwesi Tenggara, Maluku Utara, and Papua Barat Daya, and Bauxite in Kepulauan Riau. There are also several other commodities such tin, coal, and iron (Image 2)

[Image 2]

Massive Bauxite mine in Kepulauan Riau can be observed to already occur since the 90s. Bauxite already been explotid in the islands as far as the Colonial era, and consnidered as one of the largest province thath produced bauxite in Indonesia. However, the entire Province of Kepulauan Riau are consist of small island according to UU PWP3K No. 1/2014. in some instances the footprint of  mining activities are so extreme it covers more than 90%  of the island (Image 2). Mining activitites in the Island have

Beberapa bulan yang lalu perckapan publik sempat dipenuhi dengan diskusi dan protes tentang aktivitas pertambangan nikel di Pulau Gag. Kalau tidak salah, kasus ini mulai viral setelah dipicu oleh aksi protes Greenpeace Indonesia di Konferensi Nikel  Internasional yang diselanggarakan di Jakarta di Bulan Juni tahun lalu. Tentu saja, segala tudingan tentang pelanggaran hukum dan perusakan lingkungan membutuhkan investigasi yang serius dan dukungan data yang dikumpulkan langsung di lokasi sekeitar tatmbang. tapi ada satu hal yang cukup mudah untuk diferivikasi: Aktivitas Pertambangan di Pulau-Pulau Kecil.
Kegiatan pertambangan di pulau-pulau kecil dapat dianggap melanggar peraturan Undang-Undang. Tepatnya UU PWP3K No. 1/2014, yang kemudian diperkuat dengan putusan MK No. 35/PUU-XXI/2023 yang mempertegas bahwa kegiatan pertamtbangan di pulau kecil dinyatakan sebagai abnormally dangerous activity karena pulau-pulau kecil dianggap memiliki daya dukung yang terbatas dan aktivitas tambang di kawasan tersebut dapat menimbulkan kerusakan yang tidak dapat diperbaiki.

Tambang di pulau kecil merupakan sesuatu yang seharusnya dapat dideteksi dengan cukup baik dan cepat menggunakan citra penginderaan jauh dan analisa GIS. Pada post kali ini saya akan menuliskan sedikit hasil riset tipis-tipis tentang topik ini yang saya lakukan dengan menggunakan analisa citra satelit dan GIS

# Pulau Kecil
Pertama kita butuh definisi tentang pulau kecil. Berdasarkan UU PWP3K No. 1/2014, pulau kecil merupakan pulau dengan luas lebih kecil atau sama dengan 2,000 km2. Indonesia, yang merupakan negara kepulauan memiliki ribuan pulau yang banyak diantaranya tergolong kedalam pulau kecil. Berdasark data batas provinsi Indonesia yang dikeularkan oleh BIG, tepatnya terdapat 19,249 pulau di indonesia yang dapat diperoleh dengan menghitung jumlah poligon yang tidak saling bersinggungan. Jika kita menghitungang luasan masing-masing pulau kemudian menghapus semua pulau dengan luasan diatas 2,000 km2, maka kita masih tersisa dengan puluhan ribu pulau.  Namun kebanyak dari pulau-pulau ini adalah pulau yang sangat kecil dengan luasan dibawah 1 km2, dan tampaknya kemunbgkinan untuk adanya aktivitas pertambangan di pulau sekecil itu cukup kecil (walaupun tidak mustahil!). Untuk mempermudah proses analisa, kita juga akan mengabaikan pulau dengan luasan dibawah 1 km2, sehingga hanya tersisa sebanya 1,622 pulau kecil. Jumlah yang masih cukup banyak, namun awal yang cukup untuk melihat dengan lebih detail dengan citra penginderaan jauh.

# Aktivitas Pertambangan di Pulau-Pulau Kecil
