# Recovered historical specification evidence

Recovered on 12 September 2026. This is a documentary extract, not a newly adopted UAIS specification. The source has six actions per family, C1.3 Normal/AssistanceNeeded/Recovering/Unknown, and PR1–PR4. These differ from current UAIS instructions; do not import those conflicting definitions automatically. No verification was executed for this audit.

Source: C:\Users\X\Documents\Codex\2026-09-08\files-mentioned-by-the-user-lampiran\outputs\LAMPIRAN FINAL REVISI 2.docx
SHA-256: 18d603b150032591509e670e2e39277a61ab23420bee0a65da5e0b791997e9da

## Source prose

C.2.2 Keterampilan Interaksi Digital

ISS-20 mencakup empat dimensi dengan masing-masing lima item: operational, information navigation, social, dan creative. Instrumen merupakan laporan diri. Gunakan terjemahan kerja berikut secara konsisten; kesetaraan psikometrik versi bahasa Indonesia ini tidak diasumsikan telah terbukti. Pemeriksaan pada pilot terbatas pada keterpahaman prosedur dan redaksi, tanpa membentuk kategori kemampuan baru (van Deursen et al., 2016; van Deursen, 2020).

Petunjuk: Nilai seberapa sesuai setiap pernyataan dengan diri Anda, dari 1 = sama sekali tidak sesuai sampai 5 = sepenuhnya sesuai; 2, 3, dan 4 menunjukkan tingkat kesesuaian di antaranya. Jika belum pernah melakukan kegiatan tersebut, bayangkan kemampuan Anda bila diminta melakukannya. Gunakan pilihan T = tidak memahami pernyataan bila maknanya tidak dipahami; jangan menggantinya dengan skor 1.

ISS-20 Operational

ISS-20 Information navigation

ISS-20 Social

ISS-20 Creative

Penskoran: item 1–5, 11–15, dan 16–20 mengikuti nilai respons. Item 6–10 dibalik dengan 6 − respons. Hitung rerata lima item setiap dimensi hanya bila kelimanya lengkap; jika tidak, skor dimensi tersebut missing. Simpan vector [operational, information navigation, social, creative] dan 20 respons beserta kelengkapan masing-masing. Tidak ada imputasi nol, skor total untuk klasifikasi, atau cut-off rendah/sedang/tinggi. Dimensi yang lengkap tetap disimpan ketika dimensi lain missing. Aturan kelengkapan ini merupakan keputusan pengelolaan data penelitian.

Lampiran F Spesifikasi Teknis Model Adaptive UI

Lampiran ini merupakan acuan operasional C→N→R→U. Kamus, matriks, Action Catalogue, resolver, oracle, dan log menggunakan istilah yang sama dengan BAB IV. Hasil inferensi N menjadi satu-satunya dasar pencalonan R; tidak terdapat jalur langsung C→R. Metadata ketidakpastian dipisahkan dari nilai kategori agar tidak menambah kategori kemampuan atau risiko yang tidak ditetapkan.

F.1 Kamus Parameter C1–C4

Reference-Based Context Classification Specification v1.0 (FROZEN)

Semua klasifikasi, representasi, dan aturan transisi pada F.1 berlaku tetap. Rujukan memberi dasar teoritis atau batas pengujian; definisi event, penggabungan status, serta penanganan ketidaklengkapan dinyatakan sebagai keputusan operasional penelitian. Baseline hanya mengisi data pada skema ini. Pilot memeriksa keterlaksanaan prosedur, task, dan logging, tanpa kalibrasi threshold.

F.1.1 C1 User Context

Tabel F.1.1 Parameter Pengguna

Untuk C1.1, rentang 12 bulan dihitung mundur dari tanggal sesi secara kalender; penggunaan tepat pada tanggal batas termasuk Recent Experience. Jika peserta pernah menggunakan layanan tetapi hanya lebih dari 12 bulan sebelumnya, kedua definisi kategori substantif tidak mencakup riwayat tersebut. Rekam riwayat mentah, biarkan nilai kategori tidak terisi, dan gunakan uncertainty_status=Unknown dengan reason=outside_defined_recency_categories. Penanganan ini mempertahankan definisi No Recent Experience sebagai belum pernah, tanpa membuat kategori baru atau memaksakan riwayat lama menjadi tidak berpengalaman.

C1.2 digunakan sebagai representasi kontinu dan evidence pendukung kebutuhan, bukan penentu N berdasarkan ambang tersembunyi. Skor yang lengkap maupun tinggi tidak dengan sendirinya mengaktifkan N. Kondisi C→N menggunakan relevansi kebutuhan yang dinyatakan pengguna atau struktur tugas sebagaimana F.2; skor tetap disimpan untuk deskripsi dan penjelasan konteks. Skor ISS tidak diperbarui menggunakan performa peserta selama evaluasi.

Tabel F.1.2 Transisi C1.3

F.1.2 C2 Device Context

Tabel F.1.3 Parameter Perangkat

Constraint 320 CSS px berasal dari WCAG 2.2 SC 1.4.10 untuk konten dengan arah gulir vertikal. Lebar viewport semata tidak menetapkan Constrained: yang diperiksa adalah hilangnya informasi/fungsi atau kebutuhan gulir dua arah, dengan pengecualian komponen yang memang memerlukan tata letak dua dimensi. Hasil pengujian pada 320 CSS px dan hasil runtime pada viewport aktual dicatat terpisah. Tidak ada aturan viewport <320→R; kebutuhan harus melalui F.2.

F.1.3 C3 Connectivity Context

Tabel F.1.4 Parameter Konektivitas

Response time dinyatakan dalam detik tanpa pembulatan sebelum klasifikasi. Timeout diperlakukan sebagai event terminal yang dilaporkan request; poor sudah dapat diketahui ketika durasi teramati mencapai 4 detik, sehingga model tidak memerlukan ambang timeout tambahan. Kegagalan yang tidak menghasilkan durasi tetap menjadi evidence Unstable, sedangkan C3.1 Unknown bila tidak ada pengukuran/timeout yang dapat digunakan. HTTP validation error akibat isian peserta dicatat sebagai error layanan, bukan kegagalan konektivitas. Pengamatan berasal dari jalur aplikasi; navigator.onLine saja tidak cukup.

Batas Preferred dan Acceptable diadaptasi dari ITU-T G.1010 Tabel I.2 untuk respons web/layanan transaksi. Penelitian menggunakan interval eksklusif agar hasil dapat diuji pada 2 dan 4 detik. Nama Poor, Unknown, penetapan rangkaian observasi berbasis event, dan aturan risiko merupakan spesifikasi operasional penelitian. Tidak digunakan persentase retry, jendela waktu numerik tambahan, atau kalibrasi berbasis baseline/pilot.

Tabel F.1.5 Penurunan Risiko Gangguan C3.3

Jika gangguan muncul kembali selama Recovering, gunakan pasangan baru untuk kembali ke AtRisk atau Disrupted sesuai tabel. Urutan event memberi kestabilan transisi tanpa menambah threshold numerik. Status Recovering pada C3.3 berbeda dari C1.3: yang pertama menjelaskan pemulihan konektivitas, sedangkan yang kedua menjelaskan pengguna yang kembali ke tugas setelah bantuan.

F.1.4 C4 Service Context

Tabel F.1.6 Vector Layanan

C4 dibaca saat layanan dipilih dan ketika versi SOP/formulir berubah. Perubahan nilai vector karena pemilihan layanan menggunakan skema yang sama dan tidak berarti mengkalibrasi klasifikasi. Penarikan kebutuhan dilakukan dari keberadaan struktur yang relevan, seperti dependensi lintas langkah atau pilihan bersyarat, bukan dari skor kompleksitas agregat. Jumlah langkah, persyaratan, dan field tetap dipertahankan sebagai atribut yang diminta.

F.2 Mapping C→N

N1 Pemahaman informasi; N2 Mengikuti proses; N3 Orientasi atau navigasi; N4 Dukungan memori; N5 Dukungan keputusan; N6 Pencegahan atau pemulihan kesalahan; N7 Keberlanjutan proses atau progres. N menyatakan kebutuhan interaksi. Tanda ✓ berarti hubungan utama, ○ hubungan kondisional, dan – tidak ada hubungan langsung. Pola 84 sel dipertahankan. Tanda ✓ tetap memerlukan kondisi aktivasi yang relevan; keberadaan nilai C saja tidak cukup.

Tabel F.2.1 Matriks Konseptual C→N

Evaluasi menggunakan logika true/false/unknown. Pada ✓, N aktif jika kondisi dasar pada Tabel F.2.2 true. Pada ○, kondisi dasar dan evidence tambahan harus true. Jika false atau unknown, edge tidak mengaktifkan N; alasannya dicatat. Aktivasi satu N merupakan gabungan evidence dari edge yang sah, sehingga gagalnya satu edge tidak menonaktifkan N yang didukung edge lain. Seluruh edge C2.1 tetap – dan tidak mengaktifkan kebutuhan.

Tabel F.2.2 Kondisi Aktivasi Seluruh Edge Non-Dash C→N

Kondisi struktur tugas atau pernyataan pengguna yang mendukung C1.2 dicatat sebagai observation reference tambahan; parameter C1.2 tetap vector ISS dan tidak berubah menjadi kategori bantuan. Nilai missing tidak diisi dari demografi, jenis perangkat, atau dugaan observer. Bukti runtime dipakai untuk keputusan antarmuka sesuai fungsi model; outcome agregat studi tidak digunakan untuk mengubah klasifikasi atau edge selama evaluasi.

F.3 Mapping N→R

R1 Guided Interaction Support; R2 Interface Simplification; R3 Interaction Resilience & Continuity; R4 Step-by-Step Task Structure. R1–R4 adalah keluarga respons adaptasi dalam satu model dan satu layout. Matriks 28 sel berikut mempertahankan hubungan many-to-many: satu N dapat mencalonkan beberapa R dan satu R dapat memperoleh dukungan dari beberapa N.

Tabel F.3.1 Matriks Konseptual N→R

Tabel F.3.2 Kondisi Edge Non-Dash N→R

Untuk semua edge, N harus aktif terlebih dahulu. Relasi ✓ mencalonkan R saat N aktif; ○ mencalonkan R hanya bila kondisi tambahannya true. Kondisi false/unknown dicatat dan tidak mencalonkan R dari edge tersebut. Candidate R diturunkan menjadi action yang relevan, kemudian resolver memeriksa kelayakan komposisi. Relasi ini tidak menyatakan bahwa semua action dalam suatu R harus diterapkan bersamaan.

F.4 Action Catalogue

Action Catalogue v1.0 berisi 24 candidate UI actions. Candidate UI Actions bukan halaman UI yang berbeda: action merupakan konfigurasi perilaku antarmuka yang dapat dikombinasikan dalam satu layout Vue. ID R1.A1–R4.A4 mempertahankan properti pada katalog sumber; A5 dan A6 tiap keluarga merinci fungsi bantuan, penyajian, pemulihan, dan alur yang telah tercakup dalam prototipe. Tidak ada penambahan domain layanan atau metode adaptasi.

Kolom default merupakan konfigurasi Non-Adaptive UI dan nilai awal Adaptive UI. Kolom target menunjukkan nilai saat action relevan dan guard terpenuhi. Event dasar layanan, seperti menampilkan error/recovery ketika terjadi gangguan, tetap tersedia pada kedua kondisi. Reversible berarti pengaturan dapat dikembalikan pada safe point dengan state tetap utuh; tidak berarti membatalkan transaksi yang sudah terjadi. Guard false menggugurkan target; guard unknown menunda perubahan yang bergantung pada evidence tersebut.

Tabel F.4.1 Candidate UI Actions R1

Tabel F.4.2 Candidate UI Actions R2

Tabel F.4.3 Candidate UI Actions R3

Tabel F.4.4 Candidate UI Actions R4

Tanda “/” pada daftar N berarti sekurang-kurangnya satu N yang disebut aktif dan mendukung keluarga R tersebut melalui F.3. Objek action juga harus relevan pada langkah aktif: contoh hanya ditawarkan jika contoh tersedia, error explanation hanya saat error terkait ada, dan review hanya jika data dapat diringkas. Keluarga R yang aktif tanpa action relevan pada langkah saat ini dapat tidak mengubah U. Resolver tetap mencatat alasan sehingga candidate R tidak disamakan dengan halaman atau mode antarmuka baru.

R3.A1 default on berlaku bila penyimpanan didukung dan sesuai persetujuan; bila guard tidak terpenuhi, nilai efektif off serta status keterbatasan dicatat pada kedua kondisi. R3.A4 dapat visible pada kedua kondisi jika ada error/pending state yang memerlukan penjelasan keselamatan. Pencegahan submit ganda dan validasi server selalu aktif, terlepas dari nilai action. R3.A2 tidak mengulang submit yang hasilnya belum diketahui tanpa kunci idempotensi dan pemeriksaan status yang sah.

F.5 Resolver

Resolver membentuk U(t) dari candidate actions dengan memeriksa guard, kompatibilitas, komposisi, konflik yang nyata, dan safe point. Kandidat beberapa R secara bersamaan tidak dengan sendirinya merupakan konflik. PR1–PR4 tidak mengaktifkan R dan tidak memberi bobot numerik pada konteks. Prioritas hanya digunakan ketika tujuan action yang sama-sama relevan tidak dapat dipenuhi dalam bentuk awalnya.

Tabel F.5.1 Istilah Komposisi Respons

Tabel F.5.2 Prioritas Resolver

Tabel F.5.3 Operasi Resolver

Urutan keputusan: (1) pilih action dari N→R dengan objek relevan; (2) periksa nilai legal dan guard; (3) KEEP action yang dapat berdiri bersama dan COMBINE respons yang dapat disatukan; (4) untuk potential conflict, periksa tumpang tindih properti, informasi, atau dampak state; (5) bila konflik terbukti, gunakan TRANSFORM yang mempertahankan tujuan, atau SUPPRESS target berprioritas lebih rendah; (6) DEFER bila perubahan belum aman pada state saat ini. Penggabungan dapat berupa COMBINE untuk sekumpulan action dengan keputusan KEEP pada action individual.

Jika masih terdapat beberapa U yang sama-sama valid setelah PR1–PR4 diterapkan, pilih konfigurasi dengan perubahan properti paling sedikit dari U saat ini. Jika jumlah perubahannya sama, gunakan urutan ID action leksikografis dan urutan nilai legal sebagaimana tercantum di F.4. Aturan tersebut hanya tie-break deterministik, bukan skor konteks atau ukuran kualitas pengguna. Tidak ada pemilihan prioritas berdasarkan hasil evaluasi pengguna.

Tabel F.5.4 Kombinasi R dan Pemeriksaan Komposisi

Tabel F.5.5 Kasus Pemeriksaan dan Resolusi

Tabel kasus bukan daftar konflik yang selalu terjadi. Jika pemeriksaan menunjukkan kompatibilitas, action dipertahankan atau dikombinasikan. TRANSFORM hanya menggunakan nilai legal pada F.4 atau komposisi komponen yang memenuhi tujuan dan guard yang sama. Misalnya, panduan penuh (nilai on) dapat menjadi contextual/on-demand, contoh media menjadi teks ekuivalen, dan cue/progress disatukan. Informasi yang tidak mempunyai pengganti setara tidak boleh dihapus untuk menghemat data.

F.5.1 Penerapan State dan Penanganan Tanpa Konfigurasi Layak

Safe point adalah keadaan setelah edit field tersimpan dan tidak terdapat mutasi kirim/unggah yang statusnya belum jelas untuk bagian yang akan berubah. Sebelum reconfiguration, sistem menyimpan reference snapshot field, current_step, pilihan, validation state, dan progres. Jika semuanya dapat dipetakan, perubahan diterapkan dan hasil diperiksa; jika gagal, rollback memulihkan snapshot. Jika target sama dengan U saat ini, tidak ada mutasi layout. Adaptasi tertunda dievaluasi kembali saat safe point atau evidence relevan berubah.

Bila tidak ada konfigurasi feasible, sistem mempertahankan U valid terakhir dan snapshot, menahan operasi yang berisiko, menampilkan status yang dapat dipahami, serta mencatat alasan. Pada awal sesi ketika U valid belum tersedia, gunakan default yang memenuhi guard dan blok tindakan esensial yang belum aman sampai keadaan dapat dipastikan. Preserve, block, notify, dan log adalah empat tindakan keselamatan eksekusi; tindakan tersebut tidak menambah atau menggantikan lima operasi resolver. Permintaan yang hasil kirimnya belum jelas diperiksa statusnya sebelum pengguna dapat mencoba kembali.

F.6 Test Oracle

Verifikasi dilakukan oleh peneliti menggunakan V1 Decision Verification, V2 Resolver Verification, dan V3 Safety Verification. Klasifikasi, keputusan, resolver, transisi state, dan invariant seluruhnya tercakup dalam tiga kelompok ini. Expected behavior diturunkan dari v1.0 sebelum eksekusi actual. Kasus bertanda beberapa kondisi diuraikan menjadi subkasus terpisah saat dijalankan; respons yang belum diuji tidak diberi status lulus.

Tabel F.6.1 Kasus Verifikasi V1–V3

Kasus end-to-end menggunakan tiga rangkaian yang sudah tercakup: (a) struktur C4 menghasilkan N lalu panduan dan tahap; (b) penurunan/pemulihan C3 menghasilkan respons kontinuitas; (c) evidence unknown disertai beberapa kandidat R. Peneliti menelusuri V1, V2, dan V3 pada rangkaian yang sama. Ini menghindari pengulangan kelompok oracle tanpa menghilangkan pengujian seluruh rantai.

Tabel F.6.2 Rekaman Eksekusi Uji

Cakupan dilaporkan pada semua kategori/vector, batas 2 dan 4 detik, reflow 320 CSS px, 84 sel C→N, 28 sel N→R, 24 action, lima operasi resolver, kombinasi R yang sah, dan invariant V3. Setiap edge kondisional diuji dengan evidence true, false, dan unknown; setiap action diuji dengan guard relevan. Seluruh kegagalan kritis diselesaikan sebelum evaluasi pengguna; kasus yang belum dieksekusi tidak diakui sebagai bukti kelulusan.

F.7 Logging dan Traceability

Tiga rekaman terhubung melalui observation_id, decision_id, dan execution_id. Log menyimpan evidence yang diperlukan untuk menjelaskan keputusan dengan meminimalkan data pribadi. Isi field sensitif dan dokumen peserta tidak disalin ke log ketika reference, event type, ukuran, atau status telah memadai. Runtime C1.3 bersumber dari event permintaan bantuan, sedangkan error dan time evaluasi dicatat dengan tujuan analisisnya sendiri.

Tabel F.7.1 Observation Log

Tabel F.7.2 Decision Log

Tabel F.7.3 Execution Log

Versi lengkap dapat disimpan sekali pada manifest sesi dan ditautkan dari setiap log, sehingga integritas delapan ID versi tetap terjaga tanpa pengulangan isi. Data evaluasi menambahkan participant_id pseudonim, kondisi, periode, paket/task_id, waktu mulai/akhir, task completion, error pengguna, bantuan eksternal, kejadian teknis, dan respons instrumen. Penyimpanan identitas langsung dipisahkan dari data analisis. Akses, retensi, ekspor, dan penghapusan mengikuti persetujuan etik serta rencana pengelolaan data.

## ISS instrument source table 4

| No | Pernyataan | 1 | 2 | 3 | 4 | 5 | T |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Saya dapat membuka file unduhan. |  |  |  |  |  |  |
| 2 | Saya dapat menyimpan foto dari internet. |  |  |  |  |  |  |
| 3 | Saya dapat memakai pintasan tombol, seperti salin atau simpan. |  |  |  |  |  |  |
| 4 | Saya dapat membuka tab baru pada peramban. |  |  |  |  |  |  |
| 5 | Saya dapat menandai situs sebagai bookmark. |  |  |  |  |  |  |

## ISS instrument source table 5

| No | Pernyataan | 1 | 2 | 3 | 4 | 5 | T |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 6 | Saya sulit menentukan kata kunci pencarian. |  |  |  |  |  |  |
| 7 | Saya sulit menemukan kembali situs yang pernah dikunjungi. |  |  |  |  |  |  |
| 8 | Saya merasa lelah ketika mencari informasi daring. |  |  |  |  |  |  |
| 9 | Saya kadang tidak tahu bagaimana sampai ke suatu situs. |  |  |  |  |  |  |
| 10 | Tata letak banyak situs membingungkan saya. |  |  |  |  |  |  |

## ISS instrument source table 6

| No | Pernyataan | 1 | 2 | 3 | 4 | 5 | T |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 11 | Saya mengetahui informasi yang pantas dibagikan daring. |  |  |  |  |  |  |
| 12 | Saya mengetahui waktu yang tepat untuk berbagi informasi daring. |  |  |  |  |  |  |
| 13 | Komentar dan perilaku daring saya sesuai situasi. |  |  |  |  |  |  |
| 14 | Saya dapat mengatur siapa yang menerima konten saya. |  |  |  |  |  |  |
| 15 | Saya dapat menghapus orang dari daftar kontak. |  |  |  |  |  |  |

## ISS instrument source table 7

| No | Pernyataan | 1 | 2 | 3 | 4 | 5 | T |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 16 | Saya dapat mengolah gambar, musik, atau video daring menjadi karya baru. |  |  |  |  |  |  |
| 17 | Saya dapat membuat perubahan sederhana pada konten orang lain. |  |  |  |  |  |  |
| 18 | Saya dapat merancang situs web. |  |  |  |  |  |  |
| 19 | Saya mengetahui jenis lisensi konten daring. |  |  |  |  |  |  |
| 20 | Saya percaya diri mengunggah video buatan sendiri. |  |  |  |  |  |  |

## F.1.1 User context

| Kode dan konstruk | Evidence dan perolehan | Klasifikasi atau vector | Missing dan evaluasi ulang |
| --- | --- | --- | --- |
| C1.1 Digital Experience | Deklarasi faktual pernah/tidak pernah menggunakan layanan digital sejenis, nama/jenis layanan, dan bulan/tanggal terakhir. Sumber: pertanyaan pada C.2.1. | Recent Experience: pernah menggunakan layanan digital sejenis dalam 12 bulan terakhir. No Recent Experience: belum pernah menggunakan layanan digital sejenis. Unknown: informasi tidak tersedia. | Awal sesi atau koreksi riwayat. Simpan evidence dan alasan unknown; tidak menggunakan usia/pendidikan sebagai proksi. |
| C1.2 Digital Interaction Skills | 20 respons ISS pada C.2.2; lima item untuk setiap dimensi operational, information navigation, social, dan creative. | ISS-20 score vector empat rerata dimensi kontinu (1–5). Item information navigation dibalik. Tidak ada kategori rendah/sedang/tinggi atau cut-off arbitrer. | Satu kali sebelum evaluasi; tetap selama tugas. Dimensi tidak lengkap diberi missing, tanpa imputasi. Respons dan kelengkapan disimpan. |
| C1.3 Runtime Assistance Indication | Permintaan bantuan eksplisit, jenis bantuan, event bantuan selesai, dan konfirmasi melanjutkan tugas. | Normal: tidak ada permintaan aktif dan observasi tersedia. AssistanceNeeded: ada permintaan aktif. Recovering: bantuan selesai dan pengguna kembali ke tugas. Unknown: status tidak dapat dikonfirmasi. | Saat sesi dimulai, permintaan bantuan berubah, bantuan selesai, atau pengguna melanjutkan. Error/time tidak menjadi trigger otomatis. |

## F.1.2 C1.3 transitions

| State asal | Event | State hasil | Ketentuan |
| --- | --- | --- | --- |
| Unknown | Status bantuan dikonfirmasi tanpa permintaan aktif | Normal | Kekurangan data tidak ditafsirkan sebagai kebutuhan bantuan. |
| Normal / Recovering / Unknown | Pengguna meminta bantuan dan jenisnya tercatat | AssistanceNeeded | Pertahankan jenis bantuan sebagai evidence edge kondisional. |
| AssistanceNeeded | Pengguna mengonfirmasi bantuan selesai | Recovering | Dukungan yang relevan dipertahankan sampai aman untuk kembali ke tugas. |
| Recovering | Pengguna melanjutkan pada safe point tanpa permintaan baru | Normal | Perubahan UI tetap menjaga fokus, nilai, dan progres. |
| State apa pun | Event atau konfirmasi tidak dapat dipercaya | Unknown | Simpan state valid terakhir sebagai riwayat, bukan evidence pasti saat ini. |

## F.1.3 Device context

| Kode dan konstruk | Evidence dan perolehan | Klasifikasi | Missing dan evaluasi ulang |
| --- | --- | --- | --- |
| C2.1 Device/Form Factor | Descriptor kelas perangkat berdasarkan informasi perangkat dan konfirmasi bila perlu. Input touch/keyboard/pointer dicatat terpisah. | Mobile; Tablet; Desktop. Descriptor tidak mengaktifkan N atau R. | Deteksi tidak pasti: nilai descriptor kosong dan uncertainty_status=Unknown. Periksa pada awal sesi/perubahan perangkat. |
| C2.2 Available Display Space | Viewport dalam CSS px, zoom/orientasi, hasil pemeriksaan reflow dan akses terhadap informasi/kontrol. | ReflowOK: informasi dan fungsi dapat diakses tanpa gulir dua arah pada konten yang wajib reflow. Constrained: pemeriksaan menemukan keterbatasan tersebut. Unknown: hasil tidak tersedia. | Periksa pada awal tampilan dan perubahan viewport yang memengaruhi susunan konten. Uji constraint 320 CSS px dicatat bersama viewport aktual. |
| C2.3 Required Feature Availability | Feature test terhadap fitur wajib layanan pada perangkat/peramban: penyimpanan draf, unggahan, dan API yang benar-benar dipakai. | Supported: seluruh fitur wajib didukung. Limited: sedikitnya satu fitur wajib terbukti tidak didukung/gagal. Unknown: pengujian belum cukup untuk memastikan dan tidak ada kegagalan yang terbukti. | Simpan hasil per fitur. Periksa pada awal sesi, layanan berubah, atau kegagalan fitur. Unknown tidak dianggap Limited. |

## F.1.4 Connectivity

| Kode | Evidence dan pengamatan | Klasifikasi tetap | Evaluasi ulang |
| --- | --- | --- | --- |
| C3.1 Connection Quality | Response time request ringan aplikasi pada endpoint dan payload pembanding yang tetap per versi; waktu dari dispatch sampai respons lengkap diterima. Bukan total waktu unggahan dokumen. | Preferred: <2 detik. Acceptable: 2–<4 detik. Poor: ≥4 detik atau timeout. Unknown: waktu/hasil pengamatan tidak tersedia. | Pada hasil request pembanding yang relevan, sebelum operasi jaringan penting, dan setelah gangguan. |
| C3.2 Connection Stability | Rangkaian satu request logis beserta seluruh percobaan ulangnya. Event retry/failure/timeout diperiksa pada rangkaian yang sama dengan C3.1. | Stable: rangkaian teramati dan tidak ada retry/failure/timeout. Unstable: terjadi salah satu event tersebut. Unknown: observasi tidak cukup, misalnya belum ada hasil/event yang dapat dinilai. | Per event gangguan dan penutupan rangkaian. Rangkaian baru dievaluasi tersendiri; riwayat tetap tersimpan. |
| C3.3 Derived Disruption Risk | Pasangan C3.1 dan C3.2 yang selaras waktunya serta urutan pasangan sebelumnya. | Normal; AtRisk; Disrupted; Recovering menurut F.1.5. Tidak ada skor atau bobot risiko. | Ketika salah satu status sumber berubah dan saat pemulihan menghasilkan observasi baru. |

## F.1.5 Derived risk

| C3.1 | C3.2 | C3.3 | Urutan atau kondisi tambahan |
| --- | --- | --- | --- |
| Preferred / Acceptable | Stable | Normal | Awal rangkaian tanpa state risiko sebelumnya; atau observasi baik berikutnya setelah Recovering. |
| Poor | Stable | AtRisk | Respons lambat, tanpa retry/failure/timeout yang tercatat pada rangkaian ini. |
| Preferred / Acceptable | Unstable | AtRisk | Respons sudah diterima, tetapi rangkaian mengandung retry/failure/timeout. |
| Poor | Unstable | Disrupted | Kualitas buruk bersamaan dengan evidence ketidakstabilan. |
| Preferred / Acceptable | Stable | Recovering | Observasi baik pertama setelah AtRisk atau Disrupted. |
| Unknown atau data tidak selaras | Status apa pun | Tidak menetapkan state baru | Nilai turunan kosong dengan uncertainty_status=Unknown; pertahankan konfigurasi aman terakhir. |
| Status apa pun | Unknown atau data tidak selaras | Tidak menetapkan state baru | Aturan ketidakpastian didahulukan. Tidak menambah kategori risiko kelima. |

## F.1.6 Service vectors

| Kode | Komponen vector | Sumber | Penggunaan dan missing |
| --- | --- | --- | --- |
| C4.1 Process Length | number of steps; branching; dependency; rollback point. | Graf langkah dari SOP layanan berversi. | Simpan jumlah langkah, identitas cabang/dependensi, dan titik kembali. Atribut yang tidak relevan berupa himpunan kosong; yang belum diketahui berupa null dengan alasan. |
| C4.2 Requirement Load | requirement count; requirement type; dependency; format. | Daftar persyaratan, tipe dokumen/data, relasi prasyarat, dan format yang diterima. | Simpan nilai/daftar faktual. Tidak menjumlahkan skor, memberikan bobot, atau melabeli kompleksitas rendah/sedang/tinggi. |
| C4.3 Form Interaction Complexity | field count; conditional field; validation; upload; review. | Skema formulir berversi, kondisi field, aturan validasi, unggahan, dan mekanisme tinjau ulang. | Simpan struktur aktual berikut hubungan antar komponen. Metadata ambigu/tidak tersedia dicatat pada atribut terkait. |

## F.2.1 C to N matrix

| C | N1 | N2 | N3 | N4 | N5 | N6 | N7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C1.1 | ○ | ✓ | ✓ | ○ | ○ | ○ | – |
| C1.2 | ✓ | ✓ | ○ | – | ✓ | ○ | – |
| C1.3 | ○ | ○ | ○ | ○ | ○ | ○ | – |
| C2.1 | – | – | – | – | – | – | – |
| C2.2 | ○ | – | ✓ | ○ | ○ | – | – |
| C2.3 | – | – | – | – | – | ○ | ○ |
| C3.1 | – | – | – | ○ | – | ✓ | ✓ |
| C3.2 | – | – | – | ○ | – | ✓ | ✓ |
| C3.3 | – | – | – | ○ | – | ○ | ✓ |
| C4.1 | – | ✓ | ✓ | ✓ | ○ | ○ | ○ |
| C4.2 | ✓ | ✓ | – | ○ | ✓ | ○ | ○ |
| C4.3 | ○ | ✓ | ○ | ✓ | ✓ | ✓ | ○ |

## F.2.2 C to N conditions

| Edge | Tipe | Kondisi dasar | Kondisi relevan atau evidence tambahan | N |
| --- | --- | --- | --- | --- |
| C1.1→N1 | ○ | Kategori diketahui; untuk edge utama gunakan No Recent Experience. Edge kondisional menilai riwayat relevan secara eksplisit. | Riwayat faktual menunjukkan kesulitan memahami informasi layanan sejenis, bukan sekadar frekuensi penggunaan rendah. | N1 |
| C1.1→N2 | ✓ | Kategori diketahui; untuk edge utama gunakan No Recent Experience. Edge kondisional menilai riwayat relevan secara eksplisit. | Belum pernah menggunakan layanan sejenis; dibutuhkan panduan mengikuti proses. | N2 |
| C1.1→N3 | ✓ | Kategori diketahui; untuk edge utama gunakan No Recent Experience. Edge kondisional menilai riwayat relevan secara eksplisit. | Belum pernah menggunakan layanan sejenis; dibutuhkan penanda posisi/navigasi. | N3 |
| C1.1→N4 | ○ | Kategori diketahui; untuk edge utama gunakan No Recent Experience. Edge kondisional menilai riwayat relevan secara eksplisit. | Tugas menuntut pengingatan lintas langkah dan pengguna menunjukkan keterbatasan paparan sebelumnya yang relevan. | N4 |
| C1.1→N5 | ○ | Kategori diketahui; untuk edge utama gunakan No Recent Experience. Edge kondisional menilai riwayat relevan secara eksplisit. | Pilihan layanan belum dikenal dan ada bukti keraguan atau kebutuhan membandingkan alternatif. | N5 |
| C1.1→N6 | ○ | Kategori diketahui; untuk edge utama gunakan No Recent Experience. Edge kondisional menilai riwayat relevan secara eksplisit. | Ada riwayat kesalahan atau kesulitan pemulihan pada layanan sejenis. | N6 |
| C1.2→N1 | ✓ | Vector/dimensi ISS tersedia sebagai konteks pendukung; kebutuhan relevan dikonfirmasi pengguna atau tuntutan struktur tugas. Skor saja tidak mengaktifkan N. | Ada pernyataan kebutuhan penjelasan informasi atau instruksi/istilah tugas yang perlu dijelaskan; ISS menjadi konteks pendukung kontinu. | N1 |
| C1.2→N2 | ✓ | Vector/dimensi ISS tersedia sebagai konteks pendukung; kebutuhan relevan dikonfirmasi pengguna atau tuntutan struktur tugas. Skor saja tidak mengaktifkan N. | Ada pernyataan kebutuhan panduan atau urutan/dependensi tindakan yang harus diikuti; ISS menjadi konteks pendukung kontinu. | N2 |
| C1.2→N3 | ○ | Vector/dimensi ISS tersedia sebagai konteks pendukung; kebutuhan relevan dikonfirmasi pengguna atau tuntutan struktur tugas. Skor saja tidak mengaktifkan N. | Pengguna menyatakan kebutuhan orientasi/navigasi atau struktur tugas memerlukan penanda posisi; vector ISS saja tidak cukup. | N3 |
| C1.2→N5 | ✓ | Vector/dimensi ISS tersedia sebagai konteks pendukung; kebutuhan relevan dikonfirmasi pengguna atau tuntutan struktur tugas. Skor saja tidak mengaktifkan N. | Ada pernyataan kebutuhan memilih atau alternatif/prasyarat layanan yang perlu dibandingkan; ISS menjadi konteks pendukung kontinu. | N5 |
| C1.2→N6 | ○ | Vector/dimensi ISS tersedia sebagai konteks pendukung; kebutuhan relevan dikonfirmasi pengguna atau tuntutan struktur tugas. Skor saja tidak mengaktifkan N. | Pengguna menyatakan kebutuhan koreksi/pemulihan atau tugas memiliki validasi yang relevan; skor ISS bukan cut-off. | N6 |
| C1.3→N1 | ○ | AssistanceNeeded, atau Recovering selama dukungan masih diperlukan untuk kembali ke tugas; jenis bantuan tercatat. | Pengguna secara eksplisit meminta klarifikasi istilah atau informasi. | N1 |
| C1.3→N2 | ○ | AssistanceNeeded, atau Recovering selama dukungan masih diperlukan untuk kembali ke tugas; jenis bantuan tercatat. | Pengguna secara eksplisit meminta instruksi langkah atau panduan tindakan berikutnya. | N2 |
| C1.3→N3 | ○ | AssistanceNeeded, atau Recovering selama dukungan masih diperlukan untuk kembali ke tugas; jenis bantuan tercatat. | Pengguna secara eksplisit meminta bantuan mengenai posisi, tahap, atau navigasi. | N3 |
| C1.3→N4 | ○ | AssistanceNeeded, atau Recovering selama dukungan masih diperlukan untuk kembali ke tugas; jenis bantuan tercatat. | Pengguna secara eksplisit meminta pengingat atau penyajian kembali informasi yang perlu dipertahankan. | N4 |
| C1.3→N5 | ○ | AssistanceNeeded, atau Recovering selama dukungan masih diperlukan untuk kembali ke tugas; jenis bantuan tercatat. | Pengguna secara eksplisit meminta dukungan untuk membandingkan pilihan atau mengambil keputusan. | N5 |
| C1.3→N6 | ○ | AssistanceNeeded, atau Recovering selama dukungan masih diperlukan untuk kembali ke tugas; jenis bantuan tercatat. | Pengguna secara eksplisit meminta bantuan koreksi atau pemulihan kesalahan. | N6 |
| C2.2→N1 | ○ | Constrained terbukti pada tampilan aktif; bukan hanya nilai lebar viewport. | Reflow/zoom memecah atau menyembunyikan informasi sehingga pemahaman terhambat. | N1 |
| C2.2→N3 | ✓ | Constrained terbukti pada tampilan aktif; bukan hanya nilai lebar viewport. | Keterbatasan reflow mengganggu akses terhadap posisi/kontrol navigasi. | N3 |
| C2.2→N4 | ○ | Constrained terbukti pada tampilan aktif; bukan hanya nilai lebar viewport. | Nilai atau instruksi acuan tidak dapat dipertahankan terlihat dan beban mengingat lintas fragmen meningkat. | N4 |
| C2.2→N5 | ○ | Constrained terbukti pada tampilan aktif; bukan hanya nilai lebar viewport. | Alternatif pilihan terfragmentasi sehingga perbandingan atau keputusan menjadi ambigu. | N5 |
| C2.3→N6 | ○ | Limited pada fitur wajib yang sedang diperlukan. | Fitur wajib tidak didukung atau gagal dan menimbulkan kebutuhan pencegahan/pemulihan kesalahan. | N6 |
| C2.3→N7 | ○ | Limited pada fitur wajib yang sedang diperlukan. | Keterbatasan kapabilitas mengancam kontinuitas draf, unggahan, atau progres. | N7 |
| C3.1→N4 | ○ | Poor; nilai Preferred/Acceptable tanpa evidence lain tidak mengaktifkan edge ini. | Latensi/ketidakpastian respons meningkatkan kebutuhan mengingat status tertunda atau posisi retry. | N4 |
| C3.1→N6 | ✓ | Poor; nilai Preferred/Acceptable tanpa evidence lain tidak mengaktifkan edge ini. | Respons Poor menuntut pencegahan pengulangan tindakan atau penjelasan status. | N6 |
| C3.1→N7 | ✓ | Poor; nilai Preferred/Acceptable tanpa evidence lain tidak mengaktifkan edge ini. | Respons Poor mengancam kelanjutan operasi atau progres. | N7 |
| C3.2→N4 | ○ | Unstable pada rangkaian request teramati. | Fluktuasi koneksi memutus tugas dan menambah beban mengingat keadaan sebelumnya. | N4 |
| C3.2→N6 | ✓ | Unstable pada rangkaian request teramati. | Retry/failure/timeout menuntut pencegahan kesalahan atau recovery. | N6 |
| C3.2→N7 | ✓ | Unstable pada rangkaian request teramati. | Retry/failure/timeout menuntut perlindungan progres dan kelanjutan tugas. | N7 |
| C3.3→N4 | ○ | AtRisk, Disrupted, atau Recovering pada rangkaian yang relevan. | Risiko gangguan disertai status tertunda atau beban kembali ke tugas yang belum terselesaikan. | N4 |
| C3.3→N6 | ○ | AtRisk, Disrupted, atau Recovering pada rangkaian yang relevan. | Ada kegagalan kirim/unggah atau status pengiriman ambigu yang memerlukan pemulihan. | N6 |
| C3.3→N7 | ✓ | AtRisk, Disrupted, atau Recovering pada rangkaian yang relevan. | Risiko/gangguan/pemulihan menuntut kontinuitas hingga keadaan tugas dapat dilanjutkan. | N7 |
| C4.1→N2 | ✓ | Vector proses tersedia dan struktur yang disebut pada kondisi edge ada. | Ada urutan atau dependensi tindakan yang perlu diikuti. | N2 |
| C4.1→N3 | ✓ | Vector proses tersedia dan struktur yang disebut pada kondisi edge ada. | Ada perpindahan antarlangkah atau percabangan yang memerlukan orientasi. | N3 |
| C4.1→N4 | ✓ | Vector proses tersedia dan struktur yang disebut pada kondisi edge ada. | Ada informasi/hasil langkah yang harus dirujuk pada langkah lain. | N4 |
| C4.1→N5 | ○ | Vector proses tersedia dan struktur yang disebut pada kondisi edge ada. | Tahap memuat percabangan atau titik keputusan; jumlah tahap saja tidak cukup. | N5 |
| C4.1→N6 | ○ | Vector proses tersedia dan struktur yang disebut pada kondisi edge ada. | Dependensi/validasi lintas tahap menimbulkan risiko kesalahan atau pemulihan. | N6 |
| C4.1→N7 | ○ | Vector proses tersedia dan struktur yang disebut pada kondisi edge ada. | Dependensi multi-tahap menuntut persistensi progres atau kemampuan melanjutkan. | N7 |
| C4.2→N1 | ✓ | Vector persyaratan tersedia dan struktur yang disebut pada kondisi edge ada. | Jenis, istilah, atau format persyaratan memerlukan informasi penjelas. | N1 |
| C4.2→N2 | ✓ | Vector persyaratan tersedia dan struktur yang disebut pada kondisi edge ada. | Persyaratan memiliki urutan persiapan atau dependensi. | N2 |
| C4.2→N4 | ○ | Vector persyaratan tersedia dan struktur yang disebut pada kondisi edge ada. | Persyaratan perlu dipertahankan, dibandingkan, atau dirujuk lintas langkah. | N4 |
| C4.2→N5 | ✓ | Vector persyaratan tersedia dan struktur yang disebut pada kondisi edge ada. | Ada pilihan persyaratan atau keputusan pemenuhan prasyarat. | N5 |
| C4.2→N6 | ○ | Vector persyaratan tersedia dan struktur yang disebut pada kondisi edge ada. | Prasyarat, format, atau dependensi dokumen menimbulkan risiko kesalahan/pemulihan. | N6 |
| C4.2→N7 | ○ | Vector persyaratan tersedia dan struktur yang disebut pada kondisi edge ada. | Persiapan/unggah persyaratan harus bertahan terhadap jeda atau gangguan. | N7 |
| C4.3→N1 | ○ | Vector formulir tersedia dan struktur yang disebut pada kondisi edge ada. | Label, instruksi, atau pesan validasi menimbulkan beban pemahaman yang teramati. | N1 |
| C4.3→N2 | ✓ | Vector formulir tersedia dan struktur yang disebut pada kondisi edge ada. | Isian/validasi memiliki urutan tindakan atau dependensi. | N2 |
| C4.3→N3 | ○ | Vector formulir tersedia dan struktur yang disebut pada kondisi edge ada. | Percabangan atau dependensi isian menimbulkan risiko kehilangan orientasi. | N3 |
| C4.3→N4 | ✓ | Vector formulir tersedia dan struktur yang disebut pada kondisi edge ada. | Nilai/acuan perlu dipertahankan lintas field, langkah, atau review. | N4 |
| C4.3→N5 | ✓ | Vector formulir tersedia dan struktur yang disebut pada kondisi edge ada. | Ada field pilihan atau conditional field yang menuntut keputusan. | N5 |
| C4.3→N6 | ✓ | Vector formulir tersedia dan struktur yang disebut pada kondisi edge ada. | Ada validasi atau unggahan yang menuntut pencegahan/koreksi kesalahan. | N6 |
| C4.3→N7 | ○ | Vector formulir tersedia dan struktur yang disebut pada kondisi edge ada. | Formulir panjang/dependen atau unggahan menuntut persistensi keadaan. | N7 |

## F.3.1 N to R matrix

| N | R1 | R2 | R3 | R4 |
| --- | --- | --- | --- | --- |
| N1 | ✓ | ○ | – | – |
| N2 | ✓ | – | – | ✓ |
| N3 | ○ | ✓ | – | ✓ |
| N4 | – | ○ | ○ | ○ |
| N5 | ✓ | ✓ | – | ○ |
| N6 | ✓ | – | ✓ | ✓ |
| N7 | – | – | ✓ | ○ |

## F.3.2 N to R conditions

| Edge | Tipe | Evidence setelah N aktif | Keputusan | R |
| --- | --- | --- | --- | --- |
| N1→R1 | ✓ | Tidak diperlukan; N aktif menghasilkan R sebagai kandidat. | N aktif→candidate R | R1 |
| N1→R2 | ○ | Kepadatan/elemen opsional dapat dikurangi tanpa menghapus informasi esensial. | true→candidate R; false/unknown→R tidak dicalonkan dari edge ini | R2 |
| N2→R1 | ✓ | Tidak diperlukan; N aktif menghasilkan R sebagai kandidat. | N aktif→candidate R | R1 |
| N2→R4 | ✓ | Tidak diperlukan; N aktif menghasilkan R sebagai kandidat. | N aktif→candidate R | R4 |
| N3→R1 | ○ | Isyarat langkah/panduan memang diperlukan dan tidak menambah overload. | true→candidate R; false/unknown→R tidak dicalonkan dari edge ini | R1 |
| N3→R2 | ✓ | Tidak diperlukan; N aktif menghasilkan R sebagai kandidat. | N aktif→candidate R | R2 |
| N3→R4 | ✓ | Tidak diperlukan; N aktif menghasilkan R sebagai kandidat. | N aktif→candidate R | R4 |
| N4→R2 | ○ | Penyederhanaan mengurangi rujukan lintas layar sambil mempertahankan acuan penting. | true→candidate R; false/unknown→R tidak dicalonkan dari edge ini | R2 |
| N4→R3 | ○ | Gangguan/ketidakpastian mengancam ingatan terhadap keadaan tugas sehingga dukungan persistensi diperlukan. | true→candidate R; false/unknown→R tidak dicalonkan dari edge ini | R3 |
| N4→R4 | ○ | Penahapan mempertahankan nilai, ringkasan, pilihan sebelumnya, serta akses kembali/review. | true→candidate R; false/unknown→R tidak dicalonkan dari edge ini | R4 |
| N5→R1 | ✓ | Tidak diperlukan; N aktif menghasilkan R sebagai kandidat. | N aktif→candidate R | R1 |
| N5→R2 | ✓ | Tidak diperlukan; N aktif menghasilkan R sebagai kandidat. | N aktif→candidate R | R2 |
| N5→R4 | ○ | Titik keputusan selaras dengan tahap dan informasi perbandingan tetap tersedia. | true→candidate R; false/unknown→R tidak dicalonkan dari edge ini | R4 |
| N6→R1 | ✓ | Tidak diperlukan; N aktif menghasilkan R sebagai kandidat. | N aktif→candidate R | R1 |
| N6→R3 | ✓ | Tidak diperlukan; N aktif menghasilkan R sebagai kandidat. | N aktif→candidate R | R3 |
| N6→R4 | ✓ | Tidak diperlukan; N aktif menghasilkan R sebagai kandidat. | N aktif→candidate R | R4 |
| N7→R3 | ✓ | Tidak diperlukan; N aktif menghasilkan R sebagai kandidat. | N aktif→candidate R | R3 |
| N7→R4 | ○ | Progres/keadaan dipersistenkan dan alur dapat dilanjutkan setelah jeda. | true→candidate R; false/unknown→R tidak dicalonkan dari edge ini | R4 |

## F.4.1 R1 actions

| Action | Property | Nilai legal | Default | Target adaptasi | Relevansi dan guard | State |
| --- | --- | --- | --- | --- | --- | --- |
| R1.A1 | guidance.visibility | off/on/contextual | off | contextual | N: N1/N2. N aktif dan ruang tersedia | Tidak mengubah nilai isian; reversible: Ya |
| R1.A2 | term.explanation | hidden/on-demand/inline | on-demand | inline; on-demand bila ruang terbatas | N: N1. Istilah memiliki referensi | Tidak mengubah alur; reversible: Ya |
| R1.A3 | step.cue | compact/full | compact | full | N: N2/N3. Cue dapat digabungkan dengan progress; satu informasi alur yang konsisten | Tidak mengubah current_step; reversible: Ya |
| R1.A4 | example.visibility | hidden/on-demand | hidden | on-demand | N: N1/N5/N6. Contoh valid untuk service version | Tidak mengubah data; reversible: Ya |
| R1.A5 | help.access | standard/contextual | standard | contextual | N: N1/N2/N3/N5. Permintaan bantuan relevan; kontrol bantuan tetap tersedia | Preserve focus dan nilai; reversible: Ya |
| R1.A6 | error.explanation | standard/contextual | standard | contextual | N: N6. Pesan error relevan dan sumber koreksi jelas | Preserve error dan nilai; reversible: Ya |

## F.4.2 R2 actions

| Action | Property | Nilai legal | Default | Target adaptasi | Relevansi dan guard | State |
| --- | --- | --- | --- | --- | --- | --- |
| R2.A1 | layout.density | standard/reduced | standard | reduced | N: N1/N3. Informasi esensial tetap ada | Preserve focus dan reading order; reversible: Ya |
| R2.A2 | optional.elements | shown/collapsed | shown | collapsed | N: N1/N3. Hanya elemen opsional | Tidak menyembunyikan error/status; reversible: Ya |
| R2.A3 | grouping.mode | standard/semantic | standard | semantic | N: N3/N4. Urutan logis tetap | Preserve field values; reversible: Ya |
| R2.A4 | primary.control.emphasis | standard/emphasized | standard | emphasized | N: N3/N5. Satu primary action valid | Tidak mengubah action semantics; reversible: Ya |
| R2.A5 | requirements.view | full/checklist | full | checklist | N: N4/N5. Seluruh persyaratan dan status tetap terlihat/terakses | Preserve status pemenuhan; reversible: Ya |
| R2.A6 | secondary.navigation | full/collapsed | full | collapsed | N: N3. Hanya navigasi sekunder; akses fungsi esensial tetap | Preserve lokasi dan urutan baca; reversible: Ya |

## F.4.3 R3 actions

| Action | Property | Nilai legal | Default | Target adaptasi | Relevansi dan guard | State |
| --- | --- | --- | --- | --- | --- | --- |
| R3.A1 | draft.autosave | off/on | on | on | N: N4/N6/N7. Storage supported; consent policy | Snapshot draf; reversible: Ya |
| R3.A2 | network.retry | manual/guarded-auto | manual | guarded-auto | N: N6/N7. Operasi idempotent | No duplicate submit; reversible: Ya |
| R3.A3 | asset.profile | standard/low-bandwidth | standard | low-bandwidth | N: N7. Konten esensial setara | Tidak menghapus informasi; reversible: Ya |
| R3.A4 | recovery.panel | hidden/visible | hidden | visible | N: N6/N7. Pending/error state ada | Tampilkan status dan pilihan aman; reversible: Ya |
| R3.A5 | submission.feedback | standard/explicit | standard | explicit | N: N6/N7. Status server/request dapat dibedakan: pending/success/failed | Tidak mengirim ulang; status eksplisit; reversible: Ya |
| R3.A6 | draft.resume | manual/guided | manual | guided | N: N4/N7. Draf/snapshot valid, pengguna menyetujui melanjutkan | Restore draf dan progres; reversible: Ya |

## F.4.4 R4 actions

| Action | Property | Nilai legal | Default | Target adaptasi | Relevansi dan guard | State |
| --- | --- | --- | --- | --- | --- | --- |
| R4.A1 | flow.mode | single-page/staged | single-page | staged | N: N2/N3/N4. Step dependencies valid | Preserve fields/current step; reversible: Ya |
| R4.A2 | progress.indicator | off/on | off | on | N: N2/N3/N7. Stage model tersedia | Tidak mengubah progres; reversible: Ya |
| R4.A3 | validation.timing | submit/step | submit | step | N: N6. Validasi tidak destruktif | Preserve error/value state; reversible: Ya |
| R4.A4 | review.summary | off/on | off | on | N: N4/N5/N6. Summary setara dengan data | Back/review tersedia; reversible: Ya |
| R4.A5 | stage.navigation | basic/back-review | basic | back-review | N: N2/N3/N4. Tahap sebelumnya dapat diakses sesuai SOP | Preserve dependensi dan hasil validasi; reversible: Ya |
| R4.A6 | dependency.cue | hidden/visible | hidden | visible | N: N2/N5/N6. Prasyarat tahap/isian berasal dari metadata layanan | Tidak mengubah persyaratan; reversible: Ya |

## F.5.1 Composition terms

| Istilah | Makna | Contoh |
| --- | --- | --- |
| Compatible combination | Action dapat diterapkan bersama tanpa perubahan semantik atau perebutan properti. | R1.A2 penjelasan istilah dan R3.A1 autosave. |
| Composable response | Tujuan action dapat disatukan menjadi komponen/perilaku konsisten. | R1.A3 cue langkah dan R4.A2 indikator progres menjadi satu komponen. |
| Potential conflict | Ada kemungkinan tumpang tindih yang masih harus diperiksa pada state/layout aktual. | Panduan dengan reduced density; tidak selalu saling mengganggu. |
| Conflict requiring resolution | Pemeriksaan membuktikan action tidak dapat dipenuhi bersama dalam bentuk awal. | Pengulangan submit saat status belum jelas; atau perubahan alur yang kehilangan state. |

## F.5.2 Resolver priorities

| Kode | Tujuan yang dilindungi | Penerapan |
| --- | --- | --- |
| PR1 | Perlindungan data dan progres | Menahan perubahan atau pengulangan operasi yang mengancam state/transaksi. |
| PR2 | Fungsi esensial dan keberhasilan tugas | Menjaga akses persyaratan, validasi, submit aman, dan status. |
| PR3 | Pemahaman dan pencegahan kesalahan | Mempertahankan penjelasan, cue, serta koreksi yang relevan. |
| PR4 | Presentasi dan elemen sekunder | Mengatur kepadatan dan komponen opsional setelah tujuan lain terjaga. |

## F.5.3 Resolver operations

| Operasi | Kondisi Penggunaan | Hasil | Batas |
| --- | --- | --- | --- |
| KEEP | Action legal, guard terpenuhi, dan tidak berkonflik. | Action dipertahankan. | Tidak boleh menghilangkan tujuan terlindungi. |
| COMBINE | Dua atau lebih action kompatibel atau dapat disatukan. | Konfigurasi gabungan. | Tidak menimbulkan duplikasi atau inkonsistensi. |
| TRANSFORM | Tujuan action tetap diperlukan tetapi bentuk implementasinya berkonflik. | Action diganti dengan bentuk ekuivalen. | Informasi, fungsi, dan state tetap setara. |
| SUPPRESS | Action berprioritas lebih rendah mengganggu tujuan yang lebih tinggi. | Action ditahan dari konfigurasi. | Alasan dan protected objective dicatat. |
| DEFER | Adaptasi belum aman diterapkan pada state interaksi saat ini. | Perubahan ditunda sampai safe point. | Konfigurasi valid terakhir dipertahankan. |

## F.5.4 Rule combinations

| Kandidat R | Perlakuan awal | Pemeriksaan kritis | Hasil yang diharapkan |
| --- | --- | --- | --- |
| Tidak ada R | Pertahankan default atau U aman yang masih diperlukan | Tidak mengaktifkan R melalui resolver | Kembalikan action yang tidak diperlukan pada safe point; invariant tetap berlaku |
| R1 | KEEP | Guard panduan/ruang | Tindakan R1 legal |
| R2 | KEEP | Informasi dan fungsi esensial | Tindakan R2 legal |
| R3 | KEEP | Storage, idempotency, recovery | Tindakan R3 aman |
| R4 | KEEP | Dependensi tahap dan state mapping | Tindakan R4 aman |
| R1+R2 | Periksa compatible/composable; konflik hanya bila terbukti | Panduan tidak meniadakan penyederhanaan | Panduan contextual/on-demand bila perlu |
| R1+R3 | Periksa compatible/composable; konflik hanya bila terbukti | Media bantuan vs profil hemat data | Panduan setara tanpa mengorbankan kontinuitas |
| R1+R4 | Periksa compatible/composable; konflik hanya bila terbukti | Cue langkah vs indikator progres | Satu isyarat alur konsisten |
| R2+R3 | Periksa compatible/composable; konflik hanya bila terbukti | Elemen opsional vs recovery/bandwidth | Ringkas dengan state aman |
| R2+R4 | Periksa compatible/composable; konflik hanya bila terbukti | Grouping vs batas tahap | Grouping di dalam tahap |
| R3+R4 | Periksa compatible/composable; konflik hanya bila terbukti | Flow change harus state-map-able | Alur bertahap dengan persistensi; defer bila unsafe |
| R1+R2+R3 | Periksa compatible/composable; konflik hanya bila terbukti | Panduan, density, kontinuitas | U valid dengan PR1–PR4 bila konflik; perubahan minimum |
| R1+R2+R4 | Periksa compatible/composable; konflik hanya bila terbukti | Panduan, density, struktur tahap | Transform redundansi; fungsi esensial terjaga |
| R1+R3+R4 | Periksa compatible/composable; konflik hanya bila terbukti | Panduan, recovery, state/tahap | PR1–PR4 bila konflik; defer bila state belum aman |
| R2+R3+R4 | Periksa compatible/composable; konflik hanya bila terbukti | Density, recovery, state/tahap | Kontinuitas diproteksi; elemen sekunder dapat ditahan |
| R1+R2+R3+R4 | Periksa compatible/composable; konflik hanya bila terbukti | Guard→compatibility→PR→tie-break | U valid/deterministik atau no-feasible handling |

## F.5.5 Resolution cases

| Kandidat dan kondisi | Prioritas | Pemeriksaan | Operasi bila diperlukan | Hasil |
| --- | --- | --- | --- | --- |
| R1.A3 step cue + R4.A2 progress indicator | PR3 sebelum PR4 | Apakah dua indikator memberi informasi yang sama? | COMBINE/TRANSFORM | Satu komponen progres dengan cue langkah yang konsisten. |
| R2.A1 reduced density + R1.A1 guidance.visibility=on | PR3 sebelum PR4 | Apakah panduan penuh meningkatkan kepadatan dan mengganggu pemahaman? | TRANSFORM/DEFER | Panduan contextual atau on-demand; defer bila ruang belum aman. |
| R2.A2 collapsed optional elements + R1.A4 example | PR3 sebelum PR4 | Apakah contoh dibutuhkan untuk memahami field aktif? | TRANSFORM | Contoh tetap tersedia secara on-demand. |
| R2.A3 semantic grouping + R4.A1 staged flow | PR2 dan PR3 | Apakah grouping melintasi dependensi tahap? | COMBINE/TRANSFORM | Grouping diterapkan di dalam tahap; transform bila pengelompokan awal melintasi batas tahap. |
| R3.A2 guarded auto retry + submit | PR1 sebelum PR2 | Apakah operasi idempotent dan status transaksi jelas? | SUPPRESS/DEFER | Auto retry ditahan atau ditunda; tidak ada submit ganda. |
| R3.A3 low-bandwidth + R1.A4 contoh yang memuat media | PR2 dan PR3 | Apakah media esensial dan tersedia bentuk setara? | TRANSFORM | Contoh teks setara menggantikan media berat. |
| R3.A4 recovery panel + R4.A4 review summary | PR1 sebelum PR3 | Apakah status error dan data review dapat dibedakan? | COMBINE | Recovery dan review tampil bersama tanpa status ambigu. |
| R4.A1 staged flow + state snapshot tidak dapat dipetakan | PR1 | Apakah seluruh field, step, dan validation state dapat dipertahankan? | DEFER | Konfigurasi saat ini dipertahankan sampai state aman. |
| Tidak ada konfigurasi feasible | PR1–PR4 | Apakah ada fallback yang telah dipraspesifikasi dan aman? | DEFER/SUPPRESS | Pertahankan state aman, blok operasi berisiko, beri informasi, dan log; tidak mengarang fallback. |

## F.6.1 Original 35 principal cases

| ID | Uji | Objek | Input atau rangkaian | Expected behavior |
| --- | --- | --- | --- | --- |
| V1-01 | V1 | C1.1 | Riwayat dalam 12 bulan; tepat batas; belum pernah; data kosong; riwayat hanya >12 bulan. | Recent; Recent; No Recent; Unknown; kategori kosong dengan uncertainty Unknown serta alasan cakupan. Tidak ada inferensi kemampuan. |
| V1-02 | V1 | C1.2 | 20 item lengkap; item 6–10 bernilai 1/5; satu item kosong. | Vector empat dimensi; pembalikan menghasilkan 5/1; dimensi tidak lengkap missing. Tidak ada cut-off atau label kemampuan. |
| V1-03 | V1 | C1.3 | Permintaan→bantuan selesai→lanjut aman; lalu error tanpa permintaan. | AssistanceNeeded→Recovering→Normal. Error sendiri tidak mengubah C1.3; event tak tersedia menghasilkan Unknown. |
| V1-04 | V1 | C2.1 | Mobile, Tablet, Desktop, deteksi tidak pasti. | Descriptor dicatat; deteksi tidak pasti metadata Unknown. Tidak ada N dari semua tujuh edge C2.1. |
| V1-05 | V1 | C2.2 | Konten pada 320 CSS px: reflow baik; kehilangan fungsi; hasil tak tersedia. Ulang pada viewport aktual. | ReflowOK; Constrained; Unknown. Lebar saja tidak mengaktifkan R; exception dua dimensi dicatat. |
| V1-06 | V1 | C2.3 | Semua fitur wajib didukung; satu gagal; sebagian belum teruji tanpa kegagalan terbukti. | Supported; Limited; Unknown. Hasil per fitur dan alasan tersimpan. |
| V1-07 | V1 | C3.1 | Response time 1,999; 2,000; 2,001; 3,999; 4,000; 4,001 detik. | Preferred; Acceptable; Acceptable; Acceptable; Poor; Poor. Tidak membulatkan sebelum klasifikasi. |
| V1-08 | V1 | C3.1 | Timeout; tidak ada waktu/hasil; validation error pada input. | Timeout→Poor; data tak tersedia→Unknown; validation error tidak otomatis menjadi gangguan konektivitas. |
| V1-09 | V1 | C3.2 | Rangkaian tanpa retry/failure/timeout; retry; failure; timeout; belum cukup observasi. | Stable; Unstable; Unstable; Unstable; Unknown. Tidak menggunakan persentase kejadian. |
| V1-10 | V1 | C3.3 | Poor+Stable; Acceptable+Unstable; Poor+Unstable. | AtRisk; AtRisk; Disrupted dengan pasangan observasi selaras. |
| V1-11 | V1 | Pemulihan C3 | Disrupted→Preferred+Stable→Acceptable+Stable pada rangkaian berikutnya. | Recovering→Normal. Unknown di salah satu sumber tidak menciptakan Normal baru. |
| V1-12 | V1 | C4 | Vector layanan lengkap; himpunan kosong yang sah; atribut tidak tersedia. | Seluruh komponen tetap vector; kosong dibedakan dari null; tidak ada skor agregat/kategori kompleksitas. |
| V1-13 | V1 | C→N | Semua 84 sel dan 51 edge non-dash; kondisi relevan true/false/unknown. | Matriks sama dengan F.2; ✓ memakai kondisi relevan, ○ membutuhkan evidence tambahan, – tidak aktif. Gabungan evidence menghasilkan N. |
| V1-14 | V1 | ISS dan descriptor | Ubah skor ISS tanpa evidence kebutuhan lain; ubah descriptor perangkat saja. | Skor kontinu/descriptor tersimpan; tidak terjadi aktivasi N atau R hanya karena angka atau kelas perangkat. |
| V1-15 | V1 | N→R | Semua 28 sel dan 18 edge non-dash; N aktif/tidak aktif; kondisi ○ true/false/unknown. | ✓ mencalonkan R hanya dari N aktif; ○ memerlukan kondisi true; – tidak aktif. Tidak ada C→R. |
| V2-01 | V2 | Katalog | Masing-masing dari 24 action dengan nilai legal dan guard true/false/unknown. | Target legal hanya untuk action relevan; default/penundaan sesuai guard. Satu layout Vue; state terjaga. |
| V2-02 | V2 | Compatible combination | R1.A2 dan R3.A1; guard terpenuhi; tidak ada properti bertabrakan. | KEEP pada action, COMBINE pada U. Tidak dicatat sebagai conflict requiring resolution. |
| V2-03 | V2 | Composable response | R1.A3 dan R4.A2 memberi cue/progress sama. | Satu komponen konsisten melalui COMBINE/TRANSFORM; tidak ada indikator redundan. |
| V2-04 | V2 | Potential conflict | R2.A1 reduced + R1.A1 on; uji kondisi ruang cukup dan tidak cukup. | Ruang cukup: COMBINE. Bila panduan membuat density tidak layak: TRANSFORM menjadi contextual; DEFER hanya bila perubahan belum aman. |
| V2-05 | V2 | Grouping dan tahap | R2.A3 semantic melintasi batas R4.A1 staged. | TRANSFORM grouping ke dalam tahap; COMBINE dengan alur; dependensi dan field tetap. |
| V2-06 | V2 | Media dan bandwidth | R3.A3 low-bandwidth + R1.A4 contoh bermedia dengan teks ekuivalen. | TRANSFORM ke contoh teks setara; bantuan dan informasi esensial tetap dapat diakses. |
| V2-07 | V2 | PR1 dan retry | R3.A2 guarded-auto; status submit belum jelas atau guard idempotensi gagal. | SUPPRESS/DEFER retry. Periksa status transaksi; tidak mengirim ulang sampai aman. |
| V2-08 | V2 | Fungsi esensial | R2.A2/R2.A6 akan menutup error/status/kontrol wajib. | SUPPRESS target yang menghilangkan fungsi; PR1/PR2/PR3 mengatasi PR4. Elemen sekunder boleh diringkas. |
| V2-09 | V2 | Recovery dan review | R3.A4 dan R4.A4 sama-sama relevan. | COMBINE panel dan ringkasan dengan status terpisah, bukan menganggap kombinasi sebagai konflik otomatis. |
| V2-10 | V2 | Seluruh kombinasi R | 15 kombinasi nonkosong dan keadaan tanpa R pada F.5.4; gunakan guard legal. | Setiap kombinasi menghasilkan U sesuai pemeriksaan; kombinasi R tidak menjadi indeks halaman Vue. |
| V2-11 | V2 | Tie-break | Beberapa U memenuhi PR1–PR4; input, U asal, dan versi identik. | Pilih perubahan properti paling sedikit; jika sama gunakan urutan ID/nilai legal. U identik pada pengulangan. |
| V2-12 | V2 | No feasible | Tidak ada kandidat target yang memenuhi guard. | DEFER/SUPPRESS sesuai alasan; pertahankan state aman, blok operasi berisiko, tampilkan status, dan log. |
| V3-01 | V3 | Tidak kehilangan data | Perubahan guidance/density/staged saat field telah terisi dan validasi ada. | Snapshot dan state setelah penerapan berisi nilai, current_step, pilihan, serta progres yang setara. |
| V3-02 | V3 | Duplicate submission | Kirim simulatif diikuti timeout, retry, klik ulang, dan recovery. | Satu hasil transaksi per kunci idempotensi; status diperiksa sebelum pengiriman ulang. |
| V3-03 | V3 | State continuity | Target material pada safe point; target sama; target saat edit/kirim belum aman. | Safe: snapshot/apply/commit. Target sama: tidak mutasi. Unsafe: DEFER dan U terakhir dipertahankan. |
| V3-04 | V3 | Rollback | Kesalahan penerapan konfigurasi setelah snapshot. | Rollback memulihkan nilai, fokus yang sesuai, tahap, dan validation state; kegagalan pemulihan ditandai kritis. |
| V3-05 | V3 | Recovery | C3 memburuk lalu Recovering dan Normal; draf tersedia. | State tetap kontinu; pemulihan memakai draf yang benar; perubahan hanya pada safe point. |
| V3-06 | V3 | Traceability | Satu keputusan dan eksekusi end-to-end, termasuk edge unknown/deferred. | Observation→C→edge C→N→N→edge N→R→R→action→resolver→U→execution dapat ditelusuri. |
| V3-07 | V3 | Integritas versi | Eksekusi berulang dengan paket spesifikasi/build yang sama. | Semua ID versi F.7 tercatat; actual dapat dibandingkan dengan oracle yang benar; hasil deterministik. |
| V3-08 | V3 | Invariant kedua kondisi | Adaptive UI dan Non-Adaptive UI pada task sama dan guard dasar sama. | Konten, validasi, aksesibilitas dasar, penyimpanan minimum, dan pencegahan submit ganda tetap setara. |

## F.6.2 Execution record

| Field | Isi yang wajib dicatat |
| --- | --- |
| Identitas | case_id/subcase_id, peneliti, waktu, versi spesifikasi/oracle, scenario, dan build. |
| Input dan prasyarat | Raw evidence, C awal, U awal, state snapshot reference, guard, dan langkah uji. |
| Expected | Klasifikasi/vector, N, R, action/operasi, U target, dan invariant sesuai kelompok kasus. |
| Actual | Hasil eksekusi aktual dan reference log, termasuk status yang unknown/deferred. |
| Keputusan | Pass / fail / not run; alasan mismatch; defect_id bila ada; hasil pengujian ulang. |

## F.7.1 Observation log

| Field | Isi | Wajib | Fungsi |
| --- | --- | --- | --- |
| observation_id | Identitas unik observasi. | Ya | Menghubungkan evidence dengan keputusan. |
| pseudonymous_session_id | Identitas sesi tanpa identifier langsung. | Ya | Mengelompokkan event dalam satu sesi. |
| timestamp | Waktu observasi dengan zona waktu. | Ya | Menetapkan urutan dan jendela observasi. |
| source | Pengguna, feature check, probe, metadata layanan, atau event. | Ya | Menjelaskan asal evidence. |
| evidence_reference/value_class | Referensi atau kelas nilai yang diminimalkan. | Ya | Mendukung audit tanpa merekam isi sensitif. |
| quality_flag | Valid, incomplete, suspect, atau unavailable. | Ya | Menilai mutu evidence. |
| C_code | C1.1-C4.3. | Ya | Menetapkan parameter yang diproses. |
| classification/vector | Kategori legal, descriptor, atau vector; nilai kosong bila tidak dapat ditetapkan. | Ya | Merekam hasil klasifikasi. |
| uncertainty_status | Known, missing, atau unknown. | Ya | Mencegah inferensi diam-diam. |
| ParameterSetVersion | Versi aturan klasifikasi. | Ya | Menjamin reproduksibilitas. |
| unknown_reason | Alasan missing/unknown atau kategori tidak mencakup riwayat. | Bila unknown | Membedakan tidak tersedia dari nilai yang tidak tercakup. |
| request_chain_id/service_version | ID rangkaian request atau versi SOP/formulir. | Bila relevan | Menyelaraskan observasi dan metadata. |

## F.7.2 Decision log

| Field | Isi | Wajib | Fungsi |
| --- | --- | --- | --- |
| decision_id | Identitas unik keputusan. | Ya | Menjadi kunci trace keputusan. |
| observation_ids | Daftar observasi yang digunakan. | Ya | Menelusuri evidence asal. |
| active_C | Parameter dan nilai konteks aktif. | Ya | Merekam input terklasifikasi. |
| CN_edge_ids/conditions | Edge C→N serta hasil TRUE, FALSE, atau UNKNOWN. | Ya | Menjelaskan pembentukan N. |
| active_N | N1-N7 yang aktif. | Ya | Merekam kebutuhan yang disimpulkan. |
| NR_edge_ids/conditions | Edge N→R dan kondisi yang digunakan. | Ya | Menjelaskan kandidat R. |
| candidate_R | R1-R4 yang menjadi kandidat. | Ya | Merekam keluarga respons. |
| candidate_action_ids | Action R1.A1 dan seterusnya. | Ya | Merekam tindakan kandidat. |
| guard_result | Hasil pemeriksaan guard setiap action. | Ya | Menjelaskan action yang gugur atau ditunda. |
| compatibility_result | Compatible combination, composable response, potential conflict, atau conflict requiring resolution. | Ya | Mencegah semua multi-R diberi label konflik. |
| conflict_set | Action yang setelah pemeriksaan terbukti memerlukan resolusi konflik. | Bila ada | Menetapkan ruang kerja resolver. |
| PR_judgment | PR1-PR4 yang relevan dan protected objective. | Bila ada | Menjelaskan prioritas semantik. |
| resolver_operation | KEEP, COMBINE, TRANSFORM, SUPPRESS, atau DEFER. | Ya | Merekam hasil resolusi. |
| target_U | Target konfigurasi resolver; bukan pengganti expected output oracle yang disusun sebelum uji. | Ya | Menjadi target penerapan dan oracle. |
| version_ids | ModelVersion, ParameterSetVersion, RuleSetVersion, ActionCatalogueVersion, ResolverVersion, OracleVersion, ScenarioVersion, PrototypeBuildVersion. | Ya | Menjamin trace terhadap spesifikasi. |

## F.7.3 Execution log

| Field | Isi | Wajib | Fungsi |
| --- | --- | --- | --- |
| execution_id | Identitas unik eksekusi. | Ya | Menelusuri penerapan keputusan. |
| decision_id | Referensi keputusan sumber. | Ya | Menghubungkan decision dan execution log. |
| U_before / U_target | Konfigurasi sebelum dan target. | Ya | Merekam perubahan yang direncanakan. |
| safe_point_status | Safe, unsafe, atau deferred. | Ya | Menentukan waktu penerapan. |
| state_snapshot_reference | Referensi snapshot field, step, validation, pilihan, dan progres. | Bila berubah | Mendukung rollback dan recovery. |
| operation | Apply, defer, rollback, restore, preserve, atau block. | Ya | Merekam tindakan eksekusi. |
| apply_result | Success, failed, atau not attempted. | Ya | Menilai hasil penerapan. |
| U_after | Konfigurasi setelah operasi. | Ya | Membuktikan keadaan akhir. |
| rollback_result | Not required, success, atau failed. | Bila gagal | Membuktikan pemulihan. |
| error_code | Kode error tanpa isi sensitif. | Bila ada | Mengklasifikasi defect. |
| reevaluation_trigger | Evidence atau event pemicu evaluasi ulang. | Bila ada | Menjelaskan perubahan keputusan. |
| execution_timestamp | Waktu eksekusi. | Ya | Menetapkan urutan aktual. |
| PrototypeBuildVersion | Versi build yang menjalankan keputusan. | Ya | Menjamin reproduksibilitas teknis. |

## G.1 Context provenance

| Komponen Model | Spesifikasi Frozen | Dasar Literatur atau Sumber | Sintesis Penelitian |
| --- | --- | --- | --- |
| C1.1 Digital Experience | Recent Experience: penggunaan layanan sejenis dalam 12 bulan terakhir; No Recent Experience: belum pernah; Unknown: informasi tidak tersedia. | Dey, A. K. (2001). Understanding and Using Context. Personal and Ubiquitous Computing, 5, 4-7. DOI: 10.1007/s007790170019. https://doi.org/10.1007/s007790170019 | Riwayat penggunaan diperlakukan sebagai konteks pengguna yang relevan bagi interaksi. Jendela 12 bulan dan tiga nilai legal merupakan keputusan operasional penelitian; sumber tidak diklaim menetapkan jendela tersebut. |
| C1.2 Digital Interaction Skills | ISS-20 score vector empat dimensi yang kontinu, tanpa kategori kemampuan atau cut-off. | van Deursen, A. J. A. M., Helsper, E. J., & Eynon, R. (2016). Development and Validation of the Internet Skills Scale (ISS). Information, Communication & Society, 19(6), 804-823. DOI: 10.1080/1369118X.2015.1078834. https://doi.org/10.1080/1369118X.2015.1078834 van Deursen, A. (2020). Internet Skills Scale (NL): Hoe meet ik digitale vaardigheden? Centrum voor Digitale Inclusie, Universiteit Twente. https://www.utwente.nl/nl/centrumdigitaleinclusie/Blog/05-Hoe_meet_ik_digitale_vaardigheden/ | ISS memberi representasi keterampilan internet yang berdimensi. Penelitian menyimpan empat skor dimensi dan respons item sebagai evidence kontinu; skor tidak menjadi diagnosis atau pemicu adaptasi tunggal. |
| C1.3 Runtime Assistance Indication | Normal; AssistanceNeeded; Recovering; Unknown. | W3C. (2021). Making Content Usable for People with Cognitive and Learning Disabilities. W3C Working Group Note, 29 April 2021. https://www.w3.org/TR/coga-usable/ Dey, A. K. (2001). Understanding and Using Context. Personal and Ubiquitous Computing, 5, 4-7. DOI: 10.1007/s007790170019. https://doi.org/10.1007/s007790170019 | Kebutuhan bantuan dan kendali pengguna diperlakukan sebagai konteks runtime. Nama state dan transisi berbasis event permintaan serta penyelesaian bantuan merupakan operasionalisasi penelitian. |
| C2.1 Device/Form Factor | Mobile; Tablet; Desktop sebagai descriptor. | Dey, A. K. (2001). Understanding and Using Context. Personal and Ubiquitous Computing, 5, 4-7. DOI: 10.1007/s007790170019. https://doi.org/10.1007/s007790170019 Alegre, U., Augusto, J. C., & Clark, T. (2016). Engineering Context-Aware Systems and Applications: A Survey. Journal of Systems and Software, 117, 55-83. DOI: 10.1016/j.jss.2016.02.010. https://doi.org/10.1016/j.jss.2016.02.010 | Perangkat merupakan bagian situasi interaksi yang dapat dicatat sistem. Penelitian membatasinya sebagai descriptor dan tidak menggunakannya sebagai proksi kemampuan atau jalur langsung menuju kebutuhan. |
| C2.2 Available Display Space | ReflowOK; Constrained; Unknown; 320 CSS px sebagai constraint pengujian reflow. | W3C. (2024). Web Content Accessibility Guidelines (WCAG) 2.2, Success Criterion 1.4.10 Reflow. W3C Recommendation, 12 December 2024. https://www.w3.org/TR/2024/REC-WCAG22-20241212/#reflow | WCAG 2.2 SC 1.4.10 menjadi dasar pemeriksaan reflow pada 320 CSS px untuk konten yang relevan. Penelitian mengklasifikasikan hasil observasi reflow; 320 CSS px tidak dijadikan breakpoint desain otomatis. |
| C2.3 Required Feature Availability | Supported; Limited; Unknown. | Dey, A. K. (2001). Understanding and Using Context. Personal and Ubiquitous Computing, 5, 4-7. DOI: 10.1007/s007790170019. https://doi.org/10.1007/s007790170019 Alegre, U., Augusto, J. C., & Clark, T. (2016). Engineering Context-Aware Systems and Applications: A Survey. Journal of Systems and Software, 117, 55-83. DOI: 10.1016/j.jss.2016.02.010. https://doi.org/10.1016/j.jss.2016.02.010 | Kapabilitas yang dibutuhkan layanan diperlakukan sebagai evidence situasional dari feature test. Nilai legal dan aturan bahwa unknown tidak sama dengan gagal merupakan keputusan operasional penelitian. |
| C3.1 Connection Quality | Preferred <2 detik; Acceptable 2–<4 detik; Poor ≥4 detik atau timeout; Unknown. | ITU-T. (2001). Recommendation G.1010: End-user Multimedia QoS Categories, Table I.2. https://www.itu.int/rec/T-REC-G.1010-200111-I/en | Rentang waktu respons diadaptasi dari kategori pengalaman waktu tunggu pada ITU-T G.1010 Tabel I.2. Penelitian menerapkannya secara eksklusif pada request aplikasi dan menambahkan penanganan timeout serta unknown. |
| C3.2 Connection Stability | Stable: tanpa retry/failure/timeout; Unstable: terdapat salah satu event tersebut; Unknown: observasi tidak cukup. | Dey, A. K. (2001). Understanding and Using Context. Personal and Ubiquitous Computing, 5, 4-7. DOI: 10.1007/s007790170019. https://doi.org/10.1007/s007790170019 Alegre, U., Augusto, J. C., & Clark, T. (2016). Engineering Context-Aware Systems and Applications: A Survey. Journal of Systems and Software, 117, 55-83. DOI: 10.1016/j.jss.2016.02.010. https://doi.org/10.1016/j.jss.2016.02.010 | Perubahan lingkungan dan event runtime merupakan evidence konteks dinamis. Penelitian memilih retry, failure, dan timeout sebagai indikator yang dapat dicatat tanpa membentuk threshold persentase baru. |
| C3.3 Derived Disruption Risk | Normal; AtRisk; Disrupted; Recovering, diturunkan dari C3.1 dan C3.2. | ITU-T. (2001). Recommendation G.1010: End-user Multimedia QoS Categories, Table I.2. https://www.itu.int/rec/T-REC-G.1010-200111-I/en Alegre, U., Augusto, J. C., & Clark, T. (2016). Engineering Context-Aware Systems and Applications: A Survey. Journal of Systems and Software, 117, 55-83. DOI: 10.1016/j.jss.2016.02.010. https://doi.org/10.1016/j.jss.2016.02.010 | State merangkum kualitas, stabilitas, dan urutan pemulihan untuk kebutuhan keputusan antarmuka. Keempat nama state serta tabel turunannya merupakan sintesis operasional penelitian, bukan taksonomi yang diklaim berasal langsung dari satu sumber. |
| C4.1 Process Length | Vector: number of steps; branching; dependency; rollback point. | Dey, A. K. (2001). Understanding and Using Context. Personal and Ubiquitous Computing, 5, 4-7. DOI: 10.1007/s007790170019. https://doi.org/10.1007/s007790170019 W3C. (2021). Making Content Usable for People with Cognitive and Learning Disabilities. W3C Working Group Note, 29 April 2021. https://www.w3.org/TR/coga-usable/ Dokumen SOP layanan berversi. | Struktur tugas merupakan bagian konteks layanan. Penelitian merepresentasikan urutan, cabang, dependensi, dan titik kembali sebagai atribut faktual tanpa skor kompleksitas agregat. |
| C4.2 Requirement Load | Vector: requirement count; requirement type; dependency; format. | W3C. (2021). Making Content Usable for People with Cognitive and Learning Disabilities. W3C Working Group Note, 29 April 2021. https://www.w3.org/TR/coga-usable/ Dokumen persyaratan layanan berversi. | Kejelasan persyaratan dan dukungan penyelesaian tugas disintesis menjadi vector persyaratan. Jumlah, jenis, dependensi, dan format disimpan terpisah tanpa bobot atau kategori rendah/sedang/tinggi. |
| C4.3 Form Interaction Complexity | Vector: field count; conditional field; validation; upload; review. | W3C. (2021). Making Content Usable for People with Cognitive and Learning Disabilities. W3C Working Group Note, 29 April 2021. https://www.w3.org/TR/coga-usable/ Skema formulir dan aturan validasi layanan berversi. | Pola penyelesaian, pemeriksaan, serta koreksi tugas disintesis menjadi vector struktur formulir. Atribut merekam keadaan layanan aktual dan tidak dijumlahkan menjadi skor numerik. |
