import numpy as np
import nltk
nltk.download('punkt')
import re

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import string

def sentence_split(paragraph):
    return nltk.sent_tokenize(paragraph)

def word_freq(data):
    w = []
    for sentence in data:
        for words in sentence:
            w.append(words)
    bag = list(set(w))
    res = {}
    for word in bag:
        res[word] = w.count(word)
    return res

def sentence_weight(data,wordfreq):
    weights = []
    for words in data:
        temp = 0
        for word in words:
            temp += wordfreq[word]
        weights.append(temp)
    return weights

news = """
Jagung menjadi salah satu komoditas pangan strategis setelah padi (beras). Sejak beberapa tahun terakhir produksi jagung mengalami surplus, sehingga berpeluang untuk ekspor.

Berbagai kalangan pelaku agribisnis jagung menilai peluang ekspor jagung cukup terbuka. Misalnya, Widyantoko dari PT Seger Agro Nusantara mengatakan, selama ini pihaknya menjadi pemasok jagung ke perusahaan pakan ternak. Namun jika serapan dalam negeri (pabrik pakan) jenuh karena penjualan pakan turun, maka pihaknya akan melepas jagung ke pasar ekspor.

“Jika pembelian jagung dari pabrik pakan turun, maka harga jagung di petani akan turun. Kondisi ini akan berdampak ke petani. Karena peluang di pasar internasional terbuka, sehingga dimungkinkan kami menjual ke luar negeri,” katanya saat diskusi PATAKA Prokontra Ekspor Jagung di Jakarta, Kamis (22/9).

Namun dalam mengekspor jagung, Widyantoko mengaku, pihaknya harus fleksibel dengan melihat juga penyaluran untuk dalam negeri. Jika melihat produksi jagung sejak tahun 2016, maka rata-rata ekspor jagung hanya 0,84 persen dari volume surplus. Untuk tahun ini hingga pertengahan Juli diperkirakan ekspor jagung hanya 350 ribu ton, sehingga masih cukup aman untuk ketersediaan dalam negeri.

“Jadi kegiatan ekspor itu tidak mempengaruhi stabilitas pasokan dan harga. Namun dari bulan ke bulan memang pasokan tidak merata. Kami sebagai pelaku akan melihat kondisi di lapangan dan selalu memantau neraca jagung,” katanya.

Menurut Widyantoko, data surplus jagung dari tahun ke tahun mengalami fluktuatif. Misalnya, tahun 2022 diperkirakan surplus 2,6 juta ton, tahun 2021 sebanyak 2,8 juta ton, tahun 2020 sekitar 6,2 juta ton dan tahun 2019 diperkirakan surplusnya 2,2 juta ton.

Namun rata-rata surplus dalam enam tahun terakhir sekitar 4,3 juta ton dan ekspor terjadi tiap tahun, paling tinggi tahun 2018 sebanyak 200 ribu ton. Di wilayah Gorontalo dan NTB, sebenarnya surplus sudah sejak lama.

Widyantoko mengungkapkan, kebutuhan jagung tiap bulan sepanjang tahun cukup merata. Namun di sisi lain, justru pasokan yang tidak kontinyu dan naik turun selama setahun. Misalnya, panen raya terjadi pada Maret-April. Jagung juga tidak ditanam di seluruh wilayah Indonesia. “Karena itu kami harus mengatur agar bisnis tetap berjalan,” katanya.

Jika melihat data harga yang cenderung turun sejak April-Agustus mencerminkan pasokan jagung cukup banyak. Untuk itu, pihaknya bersama pemerintah akan memantau pasokan agar jangan sampai turunnya harga jagung karena pasokan berlebih membuat petani tidak bertanam jagung pada musim tanam selanjutnya.

“Kami mendukung upaya pemerintah menjaga stabilitas harga dan pasokan. Apalagi tahun depan pemerintah telah mencanangkan swasembada jagung. Sebagai eksportir kita juga harus membuktikan bahwa ekspor jagung harus berkelanjutan,” tuturnya.

Hitung Neraca Jagung

Sementara itu Penggiat Jagung di NTB, Dean Novel mendukung rencana ekspor jagung karena jumlahnya hanya sekitar 100-200 ribu ton, bahkan hingga 500 ribu ron. “Ekspor jagung bisa kita lakukan. Kita bisa mengujicoba neraca komoditas yang kini sedang dirumuskan. Tahun ini ekspor saja, mungkin bisa sampai 500 ribu ton,” katanya.

Apalagi lanjut Dean, ekspor sebagian besar ke negara Asean seperti Filipina, Malaysia, Brunei Darussalam dan Timor Leste. “Sebenarnya ekspor jagung sudah biasa dan bukan hal yang baru. Tapi karean jadi isu ke ranah yang sensitif, ekspor jagung jadi hiruk pikuk, padahal sudah umum,” tuturnya.

Menurut Dean, ekspor juga akan mendorong sirkulasi stok jagung dalam negeri, karena gudang-gudang yang ada untuk menampung panen pada Okotober-Nopember mendatang. Umumnya atau hampir 60 persen, petani menanam jagung pada musim hujan, sehingga Maret-April akan ada panen raya. Namun pada musim selanjutnya hingga musim kemarau luas tanam akan turun, sehingga pasokan juga berkurang.

“Jika kita melihat, pola tanam jagung tidak berubah, dari dulu sama saja. Untuk itu dibutuhkan gudang-gudang di daerah sentra produksi untuk menampung panen saat 60 persen petani tanam jagung,” tuturnya.

Karena itu, Dean menilai, keberdaan KUD di era Presiden Soeharto yang bertujuan menampung hasil panen petani, termasuk jagung, cukup tepat. Cadangan pangan di daerah melalui stok-stok di gudang cukup strategis untuk menjaga stabilitas pasokan dan harga. “Saya juga berharap, Kementerian Pertanian bisa mengatur pola tanam jagung petani agar tidak terjadi penumpukan pasokan pada bulan-bulan tertentu,” katanya.

Sementara itu, Plt Dirjen Perdagangan Dalam Negeri, Syailendra mengatakan, hitungan tahunan, produksi jagung di dalam negeri memang surplus, tapi untuk produksi bulanan ada waktu waktu tertentu defisit. Saat pasokan berkurang, biasanya peternak unggas bereaksi.

“Kalau memang secara total, mungkin pasca panen yang perlu diperbaiki.  Surplus disimpan dalam silo. Jika stok ada dan dikuasai, maka kita bisa menjaga stabilitas harga dan jagung tersedia untuk peternak dengan harga yang terjangkau,” katanya.

Syailendra mengatakan, pihaknya mendukung langkah ekspor. Namun ia memberikan catatan agar perlu dilihat harga jagung dunia. Jika perbedaan harganya sedikit, maka ia menyarankan lebih baik stok yang ada untuk keperluan domestik. “Untuk kebutuhan dalam negeri harus diprioritaskan. Jangan sampai ekspor, tapi ketahanan pangan domestik, terutama kebutuhan peternak dalam negeri tidak terpenuhi,” katanya.
"""

def preprocess_text(text):
    # Remove symbols
    # text = re.sub(r'[^\w\s]', '', text)

    # Remove question words in Indonesian
    question_words = ['bagaimana', 'apa', 'dimana', 'siapa', 'kapan', 'berapa', 'mengapa','itu']
    text = ' '.join(word for word in text.split() if word.lower() not in question_words)

    # create stemmer
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    # stemming process
    text   = stemmer.stem(text)

    # case folding
    text = text.lower()

    # remove punctuation
    text = text.translate(str.maketrans("","",string.punctuation))

    # remove white space
    text = text.strip()

    return text

def sum(text):
    data = sentence_split(text)
    wordfreq = word_freq(data)
    rank = sentence_weight(data,wordfreq)
    print("aa",text)
    n = 2
    result = ''
    sort_list = np.argsort(rank)[::-1][:n]
    for i in range(n):
        result += '{} '.format(data[sort_list[i]])

    print(result)
    return result

print(preprocess_text("apa itu hama"))