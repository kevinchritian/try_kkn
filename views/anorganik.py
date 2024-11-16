import streamlit as st
import streamlit as st
from PIL import Image
import base64
import io

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
st.set_page_config(layout='wide')
with open("style/anorganic.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Menyisipkan link Bootstrap 5 ke dalam aplikasi Streamlit
st.markdown("""
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
""", unsafe_allow_html=True)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

with open("images/sampah-2.jpg", "rb") as image_file:
    encoded_banner = base64.b64encode(image_file.read()).decode()


st.markdown(f"""
<style>
    .try {{
        background-image: linear-gradient(to left, white, rgba(255, 255, 255, 0.5) 20%,rgba(0, 0, 0, 0.7) 50%,rgba(255, 255, 255, 0.5) 80%,white), 
url('data:image/jpg;base64,{encoded_banner}');
        background-reapat: no-reapet;
        background-size: cover;
        background-position:center;
    }}
</style>
<div class="container-fluid banner try">
    <div class="container banner-content">
        <div class="sampah-organik">
            <h1 class="txt-banner fw-bold">
                Sampah Anorganik
            </h1>
            <hr class="garis-banner">
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


st.markdown("""
    <div class="container-fluid py-5">
        <div class="container col-8">
            <p class="p-organik">
                Sampah anorganik adalah jenis sampah yang berasal dari bahan non-biologis atau hasil olahan bahan sintetik tertentu. Materialnya tidak berasal dari alam, sehingga tidak mudah terurai secara alami (undegradable) dan membutuhkan waktu yang sangat lama untuk terdekomposisi di lingkungan. Sampah ini umumnya dihasilkan dari aktivitas manusia, terutama dari penggunaan bahan sintetis atau produk olahan.
            </p>
        </div>
    </div>
""", unsafe_allow_html=True)



# Conoth anorganik
with open("images/kaca.png", "rb") as image_file:
    encoded_kaca = base64.b64encode(image_file.read()).decode()

with open("images/kaleng.png", "rb") as image_file:
    encoded_kaleng = base64.b64encode(image_file.read()).decode()

with open("images/karet.png", "rb") as image_file:
    encoded_karet = base64.b64encode(image_file.read()).decode()

with open("images/kertas.png", "rb") as image_file:
    encoded_kertas = base64.b64encode(image_file.read()).decode()

with open("images/plastik.png", "rb") as image_file:
    encoded_plastik = base64.b64encode(image_file.read()).decode()



st.markdown(
    f"""
    <div class="container-fluid">
        <div class="container pb-5">
            <div class="text-center">
                <h1>
                    Contoh Sampah Anorganik
                </h1>
                <h2 class="text-center">5 Jenis sampah Anorganik berdasarkan sumbernya</h2>
            </div>
            <div class="row">
                <div class="col-lg-4">
                    <div class="text-center">
                        <img src="data:image/jpeg;base64,{encoded_plastik}" class="contoh">
                    </div>
                    <div class="text-center class="fw-bold"">
                        <h5 class="fw-bold">Sampah Plastik</h5>
                        <p>
                            Sampah plastik berasal dari material polimer sintetis yang diproduksi dari minyak bumi atau gas alam. Plastik memiliki sifat sulit terurai secara alami dan membutuhkan waktu hingga ratusan tahun untuk terdegradasi. Contoh sampah plastik meliputi botol minuman, kantong plastik, botol kosmetik, dan wadah makanan atau minuman.
                        </p>
                    </div>
                </div>
                <div class="col-lg-4">
                    <div class="text-center">
                        <img src="data:image/jpeg;base64,{encoded_kaleng}" class="contoh">
                    </div>
                    <div class="text-center">
                        <h5 class="fw-bold">Sampah Logam</h5>
                        <p>
                            Logam adalah material dengan sifat keras yang terbentuk dari unsur kimia seperti besi, tembaga, aluminium, atau seng. Sampah logam dapat berupa kaleng bekas minuman, besi tua, potongan kabel, paku bekas, dan sebagainya.
                        </p>
                    </div>
                </div>
                <div class="col-lg-4">
                    <div class="text-center">
                        <img src="data:image/jpeg;base64,{encoded_kertas}" class="contoh">
                    </div>
                    <div class="text-center">
                        <h5 class="fw-bold">Sampah Kertas</h5>
                        <p>
                            Kertas yang sudah tidak digunakan lagi termasuk dalam kategori sampah anorganik. Kertas terbuat dari serat kayu atau tanaman lain yang bisa didaur ulang menjadi produk baru. Jika tidak dikelola dengan baik, sampah kertas dapat mencemari lingkungan. Contohnya meliputi kertas bekas, koran, majalah, kardus, dan lainnya.
                        </p>
                    </div>
                </div>
                <div class="col-lg-4">
                    <div class="text-center">
                        <img src="data:image/jpeg;base64,{encoded_kaca}" class="contoh">
                    </div>
                    <div class="text-center">
                        <h5 class="fw-bold">Sampah Kaca</h5>
                        <p>
                            Kaca adalah material anorganik yang dibuat dari silika atau pasir dengan sifat keras dan sulit terurai. Contoh sampah kaca mencakup botol minuman, gelas, kaca jendela, dan pecahan piring.
                        </p>
                    </div>
                </div>
                <div class="col-lg-4">
                    <div class="text-center">
                        <img src="data:image/jpeg;base64,{encoded_karet}" class="contoh">
                    </div>
                    <div class="text-center">
                        <h5 class="fw-bold">Sampah Karet</h5>
                        <p>
                            Sampah karet terdiri dari material yang berasal dari getah pohon karet atau bahan sintetis. Contohnya meliputi ban bekas, sandal yang rusak, sepatu bekas, dan lainnya.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True
)



# Cara Mengelolah
with open("images/bank.jpg", "rb") as image_file:
    encoded_organik1 = base64.b64encode(image_file.read()).decode()

with open("images/reuse.jpg", "rb") as image_file:
    encoded_organik2 = base64.b64encode(image_file.read()).decode()




st.markdown(f"""
    <div class="container-fluid konten">
        <h2 class="text-center project pt-5 mb-5">Cara Mengolah Sampah Anorganik</h2>
        <div class="container pb-5 col-lg-8">
                <div class="col-lg-12">
                    <div class="card mb-5 equal-card shadow">
                        <div class="text-center mt-3">
                            <img src="data:image/jpeg;base64,{encoded_organik1}" class="mengelola">
                        </div>
                        <div class="card-body">
                            <h5 class="card-title text-center">Bank Sampah</h5>
                            <p class="card-text isi">Bank sampah adalah konsep pengumpulan dan pemilahan sampah kering yang dijalankan layaknya Bank dimana masyarakat dapat menabung sampah dan mendapatkan uang</p>
                        </div>
                    </div>
                </div>
                <div class="col-lg-12">
                    <div class="card mb-5 equal-card shadow">
                        <div class="text-center mt-3">
                            <img src="data:image/jpeg;base64,{encoded_organik2}" class="mengelola">
                        </div>
                        <div class="card-body">
                            <h5 class="card-title text-center">Reduce, Reuse, dan Recycle</h5>
                            <p class="card-text isi">Reduce merupakan kegiatan menekan dan mengurangi volume sampah.
                                Reuse adalah kegiatan menggunakan kembali barang-barang tanpa mengalami proses pengolahan.
                                Recycle adalah kegiatan memanfaatkan sampah dengan cara mendaur ulang.</p>
                        </div>
                    </div>
                </div>
        </div>
    </div> 
""", unsafe_allow_html=True)


st.markdown("""
    <style>
        .isi{
                text-align: justify;
            }
    </style>
""", unsafe_allow_html=True)




