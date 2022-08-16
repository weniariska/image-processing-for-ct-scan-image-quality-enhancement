<div id="deskripsi">
  <hr>
  <h3>Deskripsi Project</h3>
  Program sederhana dengan menggunakan Bahasa Pemrograman Python dan library Open-CV untuk membantu tenaga medis dalam mendeteksi seseorang terkena penyakit covid-19 atau tidak. Program sibuat untuk meningkatkan kualitas citra input menjadi lebih baik dengan meningkatkan kontras dan mengurangi noise, serta tenaga medis juga dapat fokus pada bagian citra yang ingin ditelitinya, yaitu fokus hanya pada paru-parunya saja.
</div>

<div id="tahapan">
  <hr>
  <ul>
    <li>
    Baca data <br>
    Data berupa citra CT-Scan dada pasien dengan kualitas citra yang kurang baik serta belum fokus ke paru-paru sebagai berikut <br>
    <img width="40%" alt="image" src="https://user-images.githubusercontent.com/96558726/184844388-d1439e7f-3192-47fd-99e8-aa27579e6131.png">
    </li>
    <li>
    Operasi Bitwise <br>
    Dilakukan untuk mendapatkan gambar yang berfokus pada paru paru, berikut hasil operasi bitwise : <br>
    <img width="40%" alt="image" src="https://user-images.githubusercontent.com/96558726/184844789-d07916ee-c8af-4a53-bac7-56daa2e5818f.jpg">
    </li>
    <li>
    Noise Removal <br>
    Dilakukan untuk mendapatkan menghilangkan noise pada citra, berikut hasilnya : <br>
    <img width="40%" alt="image" src="https://user-images.githubusercontent.com/96558726/184845072-4ee5b75f-34ad-4643-8179-9786d160c394.jpg">
    </li>
    <li>
    Plotting histogram <br>
    <img width="40%" alt="image" src="https://user-images.githubusercontent.com/96558726/184845837-b864895d-3f47-4f83-9648-185a4241bfb5.png">
    </li>
    <li>
    Perbaiki kontran citra <br>
    <img width="40%" alt="image" src="https://user-images.githubusercontent.com/96558726/184846008-803e4f91-a7ab-49d1-b83e-a1272813350f.jpg"> <br>
    Plotting histogram setelah kualitas diperbaiki <br>
    <img width="40%" alt="image" src="https://user-images.githubusercontent.com/96558726/184846790-5750ffa0-235d-4d33-87cc-b1c197cf00da.png">
    </li>
    <li>
    Thresholding <br>
    <img width="40%" alt="image" src="https://user-images.githubusercontent.com/96558726/184846202-c7ceaeb0-6b56-4549-aaf5-901e3346f786.jpg">
    </li>
  </ul>
</div>
