# Historical Mapping and Verification Import

Imported on 12 September 2026 for UAIS-S3-CD1. This is an unchanged documentary baseline, not the revised runtime specification and not a test execution record. Apply only the explicitly declared deltas in UAIS_Section3_Final_Completion_Decisions.md to construct current expectations. Original case IDs, inputs and expected behavior remain preserved below.

Source: Recovered_Historical_Specifications.md, extracted from LAMPIRAN FINAL REVISI 2.docx. Original DOCX SHA-256: 18d603b150032591509e670e2e39277a61ab23420bee0a65da5e0b791997e9da.

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
