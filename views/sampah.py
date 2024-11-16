import streamlit as st
import requests
import streamlit as st
from PIL import Image
import base64
import io
st.set_page_config(layout='wide')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
with open("style/style_sampah.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Menyisipkan link Bootstrap 5 ke dalam aplikasi Streamlit
st.markdown("""
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
""", unsafe_allow_html=True)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


with open("images/sampah.jpg", "rb") as image_file:
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
                Sampah
            </h1>
            <hr class="garis-banner">
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Pengertian sampah

st.markdown("""
    <div class="container-fluid pt-5">
        <div class="container col-8">
                <div class="">
                    <p class="pengetian-sampah">
                    	Menurut UU Nomor 8 Tahun 2008 tentang Pengelolaan Sampah, sampah adalah sisa kegiatan sehari-hari manusia atau proses 
                        alam yan berbentuk padat atau semi padat, berupa zat organik dan anorganik, dan bersifat dapat terurai atau tidak dapat terurai, 
                        yang dianggap sudah tidak berguna lagi dan dibuang ke lingkungan. Menurut World Health Organization (WHO), 
                        sampah adalah sesuatu yang tidak digunakan, tidak dipakai, tidak disenangi, 
                        atau sesuatu yang dibuang yang berasal dari kegiatan manusia dan tidak terjadi dengan sendirinya.
                    </p>
                </div>
        </div>
    </div>
""", unsafe_allow_html=True)

st.write("---")

# Jenis jenis sampah
with open("images/sampah-organik.jpg", "rb") as image_file:
    encoded_organik = base64.b64encode(image_file.read()).decode()

with open("images/sampah-anorganik.jpg", "rb") as image_file:
    encoded_anorganik = base64.b64encode(image_file.read()).decode()

with open("images/sampah-elektronik.jpg", "rb") as image_file:
    encoded_elektronik = base64.b64encode(image_file.read()).decode()

st.markdown(f"""
    <div class="container-fluid pt-5">
        <div class="container col-10">
            <h2 class="text-center">Klasifikasi Jenis Sampah</h2>
            <p class="text-center mb-5">Sampah dapat dibedakan menjadi beberapa jenis yaitu berdasarkan sifat, wujudnya, dan sumbernya.</p>
            <h3 class="text-center">Berdasarkan Sifat</h3>
            <div class="row">
                <div class="col-lg-4">
                    <div class="card mb-5 shadow">
                        <div class="text-center">
                            <img src="data:image/jpeg;base64,{encoded_organik}">
                        </div>
                        <div class="card-body">
                            <h5 class="card-title text-center">Organik</h5>
                        </div>
                    </div>
                </div>
                <div class="col-lg-4">
                    <div class="card mb-5 shadow">
                        <div class="text-center">
                            <img src="data:image/jpeg;base64,{encoded_anorganik}">
                        </div>
                        <div class="card-body">
                            <h5 class="card-title text-center">Anorganik</h5>
                        </div>
                    </div>
                </div>
                <div class="col-lg-4">
                    <div class="card mb-5 shadow">
                        <div class="text-center">
                            <img src="data:image/jpeg;base64,{encoded_elektronik}">
                        </div>
                        <div class="card-body">
                            <h5 class="card-title text-center">Limbah Berbahaya</h5>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
""",unsafe_allow_html=True)



# Berdasarkan Wujud

with open("images/limbah-cair.jpg", "rb") as image_file:
    encoded_cair = base64.b64encode(image_file.read()).decode()

with open("images/limbah-padat.jpg", "rb") as image_file:
    encoded_padat = base64.b64encode(image_file.read()).decode()

st.markdown(f"""
    <div class="container-fluid pt-5">
        <div class="container col-10">
            <h3 class="text-center">Berdasarkan Wujud</h3>
            <div class="row">
                <div class="col-lg-6">
                    <div class="card mb-5 shadow">
                        <div class="text-center">
                            <img src="data:image/jpeg;base64,{encoded_cair}">
                        </div>
                        <div class="card-body">
                            <h5 class="card-title text-center">Limbah Cair</h5>
                            <p>
                                Sampah padat adalah limbah berbentuk lunak sampai keras yang bisa berasal dari bahan organik maupun anorganik. Contohnya meliputi plastik, sayur-sayuran, sisa makanan, dan sebagainya. Meski demikian, tidak semua sampah padat dapat terurai secara alami.
                            </p>
                        </div>
                    </div>
                </div>
                <div class="col-lg-6">
                    <div class="card mb-5 shadow">
                        <div class="text-center">
                            <img src="data:image/jpeg;base64,{encoded_padat}">
                        </div>
                        <div class="card-body">
                            <h5 class="card-title text-center">Limbah Padat</h5>
                            <p>
                                Limbah cair merupakan sisa cairan tertentu yang sudah tidak diperlukan lagi. Contohnya yaitu air dari cucian, kamar mandi, cairan kimia dari industri, medis, dan lain-lain. Oleh karena itu, limbah cair biasanya memerlukan tempat khusus untuk pengolahannya.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
""",unsafe_allow_html=True)


# Berdasarkan Sumbernya

with open("images/alam.png", "rb") as image_file:
    encoded_alam = base64.b64encode(image_file.read()).decode()

with open("images/konsumsi.png", "rb") as image_file:
    encoded_konsumsi = base64.b64encode(image_file.read()).decode()

with open("images/industri.png", "rb") as image_file:
    encoded_industri = base64.b64encode(image_file.read()).decode()

with open("images/manusia2.png", "rb") as image_file:
    encoded_manusia2 = base64.b64encode(image_file.read()).decode()



st.markdown(
    f"""
    <div class="container-fluid">
        <div class="container">
            <div class="text-center">
                <h3 class="mt-5">
                    Berdasarkan Sumbernya
                </h3>
            </div>
            <div class="row">
                <div class="col-lg-6">
                    <div class="text-center gambar">
                        <img src="data:image/jpeg;base64,{encoded_alam}" class="contoh">
                    </div>
                    <div class="text-center class="fw-bold"">
                        <h5 class="fw-bold">Sampah Alam</h5>
                        <p>
                            Sumber sampah dihasilkan dari alami lingkungan. Contohnya berupa daun daunan yang gugur, ranting yang patah, buah yang jatuh ke pohon.
                        </p>
                    </div>
                </div>
                <div class="col-lg-6">
                    <div class="text-center gambar">
                        <img src="data:image/jpeg;base64,{encoded_konsumsi}" class="contoh">
                    </div>
                    <div class="text-center">
                        <h5 class="fw-bold">Sampah konsumsi</h5>
                        <p>
                            sampah ini berasal dari sisa konsumsi manusia. Contohnya adalah sampah rumah tangga seperti sisa makanan, kemasan plastik atau barang barang rumah tangga
                        </p>
                    </div>
                </div>
                <div class="col-lg-6">
                    <div class="text-center gambar">
                        <img src="data:image/jpeg;base64,{encoded_industri}" class="contoh">
                    </div>
                    <div class="text-center">
                        <h5 class="fw-bold">Sampah Industri</h5>
                        <p>
                            Sampah ini berasal dari kegiatan industri atau manufaktur. Contohnya sisa pangan hasil olahan, sampah industri kima dan bahan cairan kimia seperti oli, pelumas, minyak dan sampah elektronik.
                        </p>
                    </div>
                </div>
                <div class="col-lg-6">
                    <div class="text-center gambar">
                        <img src="data:image/jpeg;base64,{encoded_manusia2}" class="contoh">
                    </div>
                    <div class="text-center">
                        <h5 class="fw-bold">Sampah Manusia</h5>
                        <p>
                            sampah ini bersumber dari manusia atau yang disebut human waste. Contohnya seperti urin dan feses. Sampah dari sumber ini dapat membahayakan kesehatan jika dibuang sembarangan.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True
)


st.write("---")

# Dampak

with open("images/dampak.jpg", "rb") as image_file:
    encoded_alam = base64.b64encode(image_file.read()).decode()

st.markdown(f"""
    <div class="container-fluid">
    <h2 class="py-5 text-center">Dampak Negatif Sampah</h2>
    <div class="container col-8">
            <div>
                <div class="image-wrapper mb-5">
                    <img src="data:image/jpeg;base64,{encoded_alam}" class="contoh">
                </div>
            </div>
            <div>
                <p class="dampak">
                    Pemanfaatan sampah diperlukan untuk mencegahnya menjadi limbah yang tidak terkelola. Pengelolaan sampah yang 
                    bertanggung jawab dapat mengurangi risiko pencemaran lingkungan. Sampah yang tidak dikelola dengan baik menyebabkan
                    Tempat Pembuangan Akhir (TPA) menjadi over kapasitas, sementara gas metana dari sampah organik dapat memperparah
                    efek Gas Rumah Kaca yang memicu perubahan iklim. Sampah anorganik yang sulit terurai akan menjadi limbah abadi di
                    lingkungan.
                </p>
                <p class="dampak">
                    Selain mencemari lingkungan, sampah yang tidak terkelola juga berdampak buruk pada kesehatan makhluk hidup, termasuk 
                    manusia, tumbuhan, dan hewan. Pencemaran ini dapat masuk ke tubuh manusia melalui rantai makanan. Aktivitas manusia 
                    juga terganggu akibat pencemaran yang dihasilkan oleh sampah. Oleh karena itu, diperlukan penanganan sampah yang 
                    baik untuk mencegah kerugian yang lebih besar.
                </p>
            </div>
    </div>
</div>       
""", unsafe_allow_html=True)