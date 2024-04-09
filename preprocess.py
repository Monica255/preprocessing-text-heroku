import numpy as np
import nltk
nltk.download('punkt')

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

def preprocess_text(text):
    # Remove question words in Indonesian
    question_words = ['bagaimana', 'apa', 'dimana', 'siapa', 'kapan', 'berapa', 'mengapa','itu']
    text = ' '.join(word for word in text.split() if word.lower() not in question_words)

    # Create stemmer
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    # Stemming process
    text   = stemmer.stem(text)

    # Case folding
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans("","",string.punctuation))

    # Remove white space
    text = text.strip()

    return text

def sum(text):
    data = sentence_split(text)
    wordfreq = word_freq(data)
    rank = sentence_weight(data,wordfreq)
    # print("aa",text)
    n = 2
    result = ''
    sort_list = np.argsort(rank)[::-1][:n]
    for i in range(n):
        result += '{} '.format(data[sort_list[i]])

    # print(result)
    return result

print(sum("""Tanaman Jagung merupakan salah satu komoditas tanaman yang memiliki peran penting untuk pemenuhan kebutuhan pangan manusia, selain itu juga banyak dimanfaatkan sebagai bahan dasar pembuatan pakan ternak. Dengan kondisi tersebut menjadikan peluang bagi petani jagung untuk mengembangkan budidaya tanaman jagung agar produksi jagung meningkat.

Salah satu kendala yang dihadapi bertanam jagung adalah adanya organisme penganggu tumbuhan (OPT). Saat ini OPT yang mulai menganggu produktivitas jagung adalah ulat grayak (Spodoptera frugiperda). Hama tersebut merupakan hama asli daerah tropis dari Amerika Serikat hingga Argentina. Ulat FAW dapat menyerang lebih dari 80 spesies tanaman, termasuk jagung, padi, tebu, sayuran, dan kapas. FAW dapat mengakibatkan kehilangan hasil yang signifikan apabila tidak ditangani dengan baik. Di Indonesia sendiri hama ulat grayak telah ditemukan pada beberapa lokasi pertanaman jagung di Aceh, Sumatera Utara, Sumatera Barat, Lampung dan Sumatera Selatan.


Penyebaran hama ulat ‘FAW’ memang begitu cepat, hingga menimbulkan dampak serius yang sangat merugikan. Mengenalinya dengan lebih detail dan kemudian melakukan upaya pengendalian yang maksimal menjadi solusi yang baik untuk mengatasi masalah serangan hama yang sangat rakus tersebut.

Gejala serangan Ulat FAW
• Adanya bekas gerekan dari ulat
• Pada permukaan atas daun atau disekitar pucuk tanaman jagung, ditemukan serbuk kasar seperti serbuk gergaji.
• Ketika populasi ulat FAW ini sangat tinggi, maka bagian tongkol jagung juga akan diserang oleh hama ini.

Cara untuk menanggulangi ulat grayak

Rotasi tanaman untuk memutus daur hidup hama;
Pengolahan tanah yang baik (selama 1 bulan) untuk mengangkat kepompong hama dari dalam tanah agar mati terjemur oleh sinar matahari;
Pemasangan perangkap berferomon yaitu feromon Exi sebanyak 20 buah per hektar;
Pemasangan lampu perangkap sebanyak 30 buah per hektar;
Penyemprotan insektisida jika kerusakan daun telah mencapai 5%;
Penyemprotan insektisida jika populasi kelompok telur telah mencapai 1 kelompok atau 10 tanaman;
Selain itu pengendalian ulat grayak pada jagung juga dapat dilakukan dengan pembuatan pestisida nabati (botani).


Pestisdia nabati untuk ulat grayak

Bahan-bahan:

Bubuk cabai 1 sendok teh
Bawang putih 1 siung
Bawang merah 1 butir
Air 1 liter
Deterjen 1 sendok teh.
Cara pembuatan :

Bawang putih dan bawang merah dihancurkan;
Campur bubuk cabai dan air, aduk hingga rata, rendam 1 jam lalu saring, tambah deterjen aduk rata."""))