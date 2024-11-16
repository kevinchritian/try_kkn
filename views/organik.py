import streamlit as st
import streamlit as st
from PIL import Image
import base64
import io

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
st.set_page_config(layout='wide')
with open("style/organik.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Menyisipkan link Bootstrap 5 ke dalam aplikasi Streamlit
st.markdown("""
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
""", unsafe_allow_html=True)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

with open("images/banner-organik.jpg", "rb") as image_file:
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
                Sampah Organik
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
                Sampah Organik adalah sampah yang dapat terurai secara alamiah di alam. Sampah Organik biasanya berasal 
                dari sisa sisa mahkluk hidup, seperti hewan, tanaman, maupun manusia. Sampah organik juga bisa disebut 
                sebagai sampah ramah lingkungan. Ciri sampah organik yaitu mudah membusuk, memiliki kandungan air, 
                basah atau kering. 
                Sampah organik bisa dibedakan lebih detail lagi, yaitu sampah organik kering atau sampah organik basah.
                Sampah oraganik kering memiliki kandungan air dibandingkan dengan sasmpah organik basah. Sehingga sampah
                basah lebih cepat membusuk dan hancur terlebih dahulu.
            </p>
        </div>
    </div>
""", unsafe_allow_html=True)



# Conoth anorganik
with open("images/organik.png", "rb") as image_file:
    encoded_judul = base64.b64encode(image_file.read()).decode()

with open("images/hewan.png", "rb") as image_file:
    encoded_hewan = base64.b64encode(image_file.read()).decode()

with open("images/kebun.png", "rb") as image_file:
    encoded_kebun = base64.b64encode(image_file.read()).decode()

with open("images/pertanian.png", "rb") as image_file:
    encoded_pertanian = base64.b64encode(image_file.read()).decode()

with open("images/manusia.png", "rb") as image_file:
    encoded_manusia = base64.b64encode(image_file.read()).decode()



st.markdown(
    f"""
    <div class="container-fluid">
        <div class="container pb-5">
            <div class="text-center">
                <h1>
                    Contoh Sampah Organik
                </h1>
                <h2 class="text-center">5 Jenis sampah organik berdasarkan sumbernya</h2>
            </div>
            <div class="row">
                <div class="col-lg-4">
                    <div class="text-center">
                        <img src="data:image/jpeg;base64,{encoded_judul}" class="contoh">
                    </div>
                    <div class="text-center class="fw-bold"">
                        <h5 class="fw-bold">Sampah Sisa Makanan</h5>
                        <p>
                            komposisi sampah sisa makanan mencakup segala jenis makanan seperti sayur, buah cangkang telur, kulit buah, sayuran, serta
                            material lain yang tidak dikonsumsi lagi
                        </p>
                    </div>
                </div>
                <div class="col-lg-4">
                    <div class="text-center">
                        <img src="data:image/jpeg;base64,{encoded_kebun}" class="contoh">
                    </div>
                    <div class="text-center">
                        <h5 class="fw-bold">Sampah Kebun</h5>
                        <p>
                            Sampah kebun sumber nya dapat dihasilkan melaui taman atau perkarangan seperti
                            dedaunan, pohon, ranting, serta rerumputan sisa pemangkasan. Sampah ini juga dikenal sebagai sampah kering dan sering dijadikan pupuk kompos
                        </p>
                    </div>
                </div>
                <div class="col-lg-4">
                    <div class="text-center">
                        <img src="data:image/jpeg;base64,{encoded_pertanian}" class="contoh">
                    </div>
                    <div class="text-center">
                        <h5 class="fw-bold">Sampah Pertanian</h5>
                        <p>
                            Sampah pertanian merupakan sampah dari hasil pemrosesan tanaman seperti sekam padi, batang jagung, dan dedaunan.
                            Biasanya sampah ini dikelola menjadi sampah kompos.
                        </p>
                    </div>
                </div>
                <div class="col-lg-4">
                    <div class="text-center">
                        <img src="data:image/jpeg;base64,{encoded_hewan}" class="contoh">
                    </div>
                    <div class="text-center">
                        <h5 class="fw-bold">Sampah Sisa Hewan Ternak</h5>
                        <p>
                            Sampah dari hewan ternak, seperti kotoran sapi dan kambing termasuk kedalam kategori sampah jenis organik. Sampah ini
                            biasanya juga akan dipakai untuk dijadikan pupuk atau biogas sebagai bahan bakar.
                        </p>
                    </div>
                </div>
                <div class="col-lg-4">
                    <div class="text-center">
                        <img src="data:image/jpeg;base64,{encoded_manusia}" class="contoh">
                    </div>
                    <div class="text-center">
                        <h5 class="fw-bold">Sampah dari Bagian Tubuh</h5>
                        <p>
                            Sampah ini yang dimaksud adalah potongan kuku dan rambut manusia yang rontok. Helai rambut yang rontok dan potongan kuku
                            bisa dijadikan sebagai bahan komposter.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True
)



# Cara Mengelolah
with open("images/organik1.jpg", "rb") as image_file:
    encoded_organik1 = base64.b64encode(image_file.read()).decode()

with open("images/organik2.jpg", "rb") as image_file:
    encoded_organik2 = base64.b64encode(image_file.read()).decode()

with open("images/organik3.jpg", "rb") as image_file:
    encoded_organik3 = base64.b64encode(image_file.read()).decode()

with open("images/organik4.jpg", "rb") as image_file:
    encoded_organik4 = base64.b64encode(image_file.read()).decode()



st.markdown(f"""
    <div class="container-fluid konten">
        <h2 class="text-center project pt-5 mb-5">Cara Mengolah Sampah Organik</h2>
        <div class="container pb-5 col-lg-8">
                <div class="col-lg-12">
                    <div class="card mb-5 equal-card shadow">
                        <div class="text-center mt-3">
                            <img src="data:image/jpeg;base64,{encoded_organik2}" class="mengelola">
                        </div>
                        <div class="card-body">
                            <h5 class="card-title text-center">Dapat diolah menjadi kompos dan pupuk sederhana</h5>
                            <p class="card-text isi">Sampah organik dapat diolah menjadi kompos untuk pertanian dengan tahapan yang telaten dan benar. Jika kurang telaten, sampah organik bisa dijadikan pupuk sederhana dengan membuat lubang pembuangan di tanah dan membiarkannya membusuk hingga menyerupai tanah. Unsur hara yang dihasilkan bermanfaat untuk menyuburkan tanaman.</p>
                        </div>
                    </div>
                </div>
                <div class="col-lg-12">
                    <div class="card mb-5 equal-card shadow">
                        <div class="text-center mt-3">
                            <img src="data:image/jpeg;base64,{encoded_organik3}" class="mengelola">
                        </div>
                        <div class="card-body">
                            <h5 class="card-title text-center">Tambahan Pakan Ternak</h5>
                            <p class="card-text isi">Dedaunan dari sampah organik dapat dimanfaatkan sebagai pakan ternak seperti kambing dan sapi. Selain itu, sampah organik juga dapat diolah menjadi pelet untuk makanan ayam dan ikan, sehingga berguna untuk kebutuhan peternakan.</p>
                        </div>
                    </div>
                </div>
                <div class="col-lg-12">
                    <div class="card mb-5 equal-card shadow">
                        <div class="text-center mt-3">
                            <img src="data:image/jpeg;base64,{encoded_organik1}" class="mengelola">
                        </div>
                        <div class="card-body">
                            <h5 class="card-title text-center">Kerajinan Tangan</h5>
                            <p class="card-text isi">Sampah organik seperti enceng gondok yang dikeringkan dan dibakar dapat diolah menjadi tas dan barang bernilai jual. Batok kelapa, selain digunakan sebagai bahan bakar, juga bisa dijadikan produk seperti centong, cangkir, atau peralatan masak lainnya.</p>
                        </div>
                    </div>
                </div>
                <div class="col-lg-12">
                    <div class="card mb-5 equal-card shadow">
                        <div class="text-center mt-3">
                            <img src="data:image/jpeg;base64,{encoded_organik4}" class="mengelola">
                        </div>
                        <div class="card-body">
                            <h5 class="card-title text-center">Biogas dan Listrik</h5>
                            <p class="card-text isi">Sampah organik dari tahu, tempe, dan kotoran hewan dapat dimanfaatkan sebagai bahan pembuatan biogas. Dengan menggunakan wadah tertutup, ditambahkan air, dan diaduk, proses fermentasi bisa dipercepat. Decomposer juga dapat digunakan untuk mempersingkat waktu pembuatan biogas, yang umumnya membutuhkan lebih dari dua minggu jika hanya menggunakan air.</p>
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




