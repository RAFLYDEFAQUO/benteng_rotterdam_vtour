
<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>Tur Virtual Benteng Rotterdam</title>

  <!-- Pannellum -->
  <link
    rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/pannellum@2.5.7/build/pannellum.css"
  >
  <script src="https://cdn.jsdelivr.net/npm/pannellum@2.5.7/build/pannellum.js"></script>

  <style>
    * {
      box-sizing: border-box;
    }

    body {
      margin: 0;
      font-family: Arial, Helvetica, sans-serif;
      background: #0f172a;
      color: #ffffff;
    }

    header {
      padding: 16px 22px;
      background: #17243a;
    }

    h1 {
      margin: 0;
      font-size: 1.35rem;
    }

    .intro {
      margin: 7px 0 0;
      color: #d3e2f1;
      font-size: 0.95rem;
      line-height: 1.5;
    }

    /* AREA PANORAMA */
    #panorama {
      width: 100%;
      height: calc(100vh - 120px);
      min-height: 380px;
      background: #111827;
    }

    /* PANEL TOMBOL LOKASI */
    .nav-panel {
      margin: 16px;
      padding: 18px;
      background: #17243a;
      border: 1px solid #334155;
      border-radius: 12px;
    }

    .nav-heading {
      margin: 0 0 6px;
      font-size: 1.1rem;
    }

    .nav-help {
      margin: 0 0 15px;
      color: #cbd5e1;
      font-size: 0.9rem;
      line-height: 1.5;
    }

    /* SUSUNAN 10 TOMBOL */
    .location-buttons {
      display: grid;
      grid-template-columns: repeat(5, minmax(0, 1fr));
      gap: 10px;
    }

    .location-btn {
      display: flex;
      align-items: center;
      gap: 8px;
      min-height: 52px;
      padding: 10px;
      border: 1px solid #496078;
      border-radius: 9px;
      background: #26384e;
      color: #f8fafc;
      font-size: 0.85rem;
      line-height: 1.4;
      text-align: left;
      cursor: pointer;
      transition: background 0.2s, border-color 0.2s;
    }

    .location-btn:hover {
      background: #344b64;
      border-color: #7dd3fc;
    }

    .location-btn:focus-visible {
      outline: 3px solid #7dd3fc;
      outline-offset: 2px;
    }

    .location-btn.active {
      background: #0e7490;
      border-color: #67e8f9;
      color: #ffffff;
      box-shadow: 0 0 0 2px rgba(103, 232, 249, 0.15);
    }

    .location-number {
      display: inline-flex;
      flex-shrink: 0;
      width: 25px;
      height: 25px;
      align-items: center;
      justify-content: center;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.15);
      font-size: 0.8rem;
      font-weight: bold;
    }

    .current-location {
      margin: 14px 0 0;
      color: #bae6fd;
      font-size: 0.9rem;
    }

    footer {
      padding: 14px 22px;
      background: #17243a;
      color: #cbd5e1;
      font-size: 0.85rem;
      line-height: 1.5;
    }

    footer span {
      color: #9bd8f2;
      font-weight: bold;
    }

    /*
      GAYA KHUSUS HOTSPOT INFORMASI.
      Tidak mengubah tampilan hotspot panah type="scene".
    */
    #panorama .pnlm-hotspot.pnlm-info {
      border-radius: 50%;
      box-shadow: 0 0 0 4px rgba(34, 211, 238, 0.2);
    }

    #panorama .pnlm-hotspot.pnlm-info .pnlm-tooltip {
      width: max-content;
      max-width: min(340px, 72vw);
      padding: 10px 12px;
      border: 1px solid #67e8f9;
      border-radius: 10px;
      background: #f8fafc;
      color: #17243a;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25);
      font-size: 13px;
      line-height: 1.5;
      white-space: normal;
    }

    #panorama .pnlm-hotspot.pnlm-info .pnlm-tooltip span {
      white-space: normal;
    }

    /* RESPONSIF TABLET */
    @media (max-width: 900px) {
      .location-buttons {
        grid-template-columns: repeat(3, minmax(0, 1fr));
      }

      #panorama {
        height: 65vh;
      }
    }

    /* RESPONSIF HP */
    @media (max-width: 560px) {
      header {
        padding: 14px 16px;
      }

      h1 {
        font-size: 1.1rem;
      }

      #panorama {
        height: 55vh;
        min-height: 300px;
      }

      .nav-panel {
        margin: 10px;
        padding: 12px;
      }

      .location-buttons {
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 7px;
      }

      .location-btn {
        min-height: 48px;
        padding: 8px;
        font-size: 0.8rem;
      }
    }
  </style>
</head>

<body>

  <header>
    <h1>Benteng Rotterdam | Interactive Virtual Tour</h1>
    <p class="intro">
      Geser foto untuk melihat sekeliling. Gunakan panah di dalam foto
      atau pilih tombol lokasi di bawah untuk berpindah tempat.
    </p>
  </header>

  <main>
    <!-- PANORAMA 360 DERAJAT -->
    <div
      id="panorama"
      aria-label="Panorama 360 derajat Benteng Rotterdam"
    ></div>

    <!-- 10 TOMBOL NAVIGASI -->
    <section class="nav-panel">
      <h2 class="nav-heading">Jelajahi Titik Lokasi</h2>

      <p class="nav-help">
        Pilih salah satu lokasi untuk langsung membukanya.
        Tombol akan berubah warna sesuai lokasi yang sedang aktif.
      </p>

      <div class="location-buttons">

        <button class="location-btn active"
          type="button" data-scene="gerbang_masuk">
          <span class="location-number">1</span>
          <span>Gerbang Masuk</span>
        </button>

        <button class="location-btn"
          type="button" data-scene="jalan_dari_gerbang">
          <span class="location-number">2</span>
          <span>Jalan dari Gerbang</span>
        </button>

        <button class="location-btn"
          type="button" data-scene="bangunan_melengkung">
          <span class="location-number">3</span>
          <span>Bangunan Melengkung</span>
        </button>

        <button class="location-btn"
          type="button" data-scene="jalan_tengah_halaman">
          <span class="location-number">4</span>
          <span>Jalan Tengah Halaman</span>
        </button>

        <button class="location-btn"
          type="button" data-scene="sisi_bangunan">
          <span class="location-number">5</span>
          <span>Sisi Bangunan</span>
        </button>

        <button class="location-btn"
          type="button" data-scene="arkade_dan_taman_kecil">
          <span class="location-number">6</span>
          <span>Arkade dan Taman Kecil</span>
        </button>

        <button class="location-btn"
          type="button" data-scene="lapangan_rumput">
          <span class="location-number">7</span>
          <span>Lapangan Rumput</span>
        </button>

        <button class="location-btn"
          type="button" data-scene="arkade_bertiang">
          <span class="location-number">8</span>
          <span>Arkade Bertiang</span>
        </button>

        <button class="location-btn"
          type="button" data-scene="taman_melingkar">
          <span class="location-number">9</span>
          <span>Taman Melingkar</span>
        </button>

        <button class="location-btn"
          type="button" data-scene="lorong_antarbangunan">
          <span class="location-number">10</span>
          <span>Lorong Antarbangunan</span>
        </button>

      </div>

      <p class="current-location" id="currentLocation">
        Lokasi aktif: Gerbang Masuk
      </p>
    </section>
  </main>

  <footer>
    Tur virtual Benteng Rotterdam menggunakan
    <span>Pannellum</span>, dengan navigasi lokasi yang interaktif.
  </footer>

  <script>
    const sceneNames = {
      gerbang_masuk: "Gerbang Masuk",
      jalan_dari_gerbang: "Jalan dari Gerbang",
      bangunan_melengkung: "Bangunan Melengkung",
      jalan_tengah_halaman: "Jalan Tengah Halaman",
      sisi_bangunan: "Sisi Bangunan",
      arkade_dan_taman_kecil: "Arkade dan Taman Kecil",
      lapangan_rumput: "Lapangan Rumput",
      arkade_bertiang: "Arkade Bertiang",
      taman_melingkar: "Taman Melingkar",
      lorong_antarbangunan: "Lorong Antarbangunan",
      sisi_bangunan_timur: "Sisi Bangunan Timur"
    };

    const viewer = pannellum.viewer("panorama", {
      "default": {
        "firstScene": "gerbang_masuk",
        "sceneFadeDuration": 700,
        "autoLoad": true,
        "hfov": 110,
        "escapeHTML": true
      },

      "scenes": {
        "gerbang_masuk": {
          "title": "Gerbang Masuk",
          "type": "equirectangular",
          "panorama": "images/gerbang_masuk.jpg",
          "yaw": 0,
          "hotSpots": [
            {
              "pitch": 0,
              "yaw": 0,
              "type": "scene",
              "text": "Ke Jalan dari Gerbang",
              "sceneId": "jalan_dari_gerbang"
            },
            {
              "pitch": 10,
              "yaw": -50,
              "type": "info",
              "text": "Gerbang Masuk — Selamat datang di Benteng Rotterdam, salah satu situs bersejarah penting di Kota Makassar, Sulawesi Selatan. Benteng ini memiliki sejarah panjang yang berkaitan dengan Kerajaan Gowa dan masa kolonial Belanda. Melalui tur virtual ini, mari mengenal lebih dekat sejarah dan warisan budaya yang tersimpan di dalamnya."
            }
          ]
        },

        "jalan_dari_gerbang": {
          "title": "Jalan dari Gerbang",
          "type": "equirectangular",
          "panorama": "images/jalan_dari_gerbang.jpg",
          "yaw": 0,
          "hotSpots": [
            {
              "pitch": 0,
              "yaw": 0,
              "type": "scene",
              "text": "Ke Bangunan Melengkung",
              "sceneId": "bangunan_melengkung"
            },
            {
              "pitch": -6,
              "yaw": -110,
              "type": "scene",
              "text": "Kembali ke Gerbang Masuk",
              "sceneId": "gerbang_masuk"
            },
            {
              "pitch": 8,
              "yaw": 3,
              "type": "info",
              "text": "Jalan dari Gerbang — Area ini menjadi bagian awal perjalanan pengunjung setelah memasuki kompleks Benteng Rotterdam. Dari jalur ini, pengunjung dapat mulai mengamati suasana lingkungan dan bangunan bersejarah di sekitarnya. Mari mengenal kawasan ini dan memahami pentingnya menjaga peninggalan sejarah sebagai bagian dari warisan budaya."
            }
          ]
        },

        "bangunan_melengkung": {
          "title": "Bangunan Melengkung",
          "type": "equirectangular",
          "panorama": "images/bangunan_melengkung.jpg",
          "yaw": 0,
          "hotSpots": [
            {
              "pitch": 0,
              "yaw": 0,
              "type": "scene",
              "text": "Ke Jalan Tengah Halaman",
              "sceneId": "jalan_tengah_halaman"
            },
            {
              "pitch": -6,
              "yaw": -110,
              "type": "scene",
              "text": "Kembali ke Jalan dari Gerbang",
              "sceneId": "jalan_dari_gerbang"
            },
            {
              "pitch": 8,
              "yaw": 3,
              "type": "info",
              "text": "Bangunan Melengkung — Benteng Rotterdam memiliki kompleks bangunan dengan karakter arsitektur yang berkembang sepanjang sejarahnya. Bentuk, bahan, pintu, jendela, dan bagian-bagian bangunan menjadi petunjuk untuk memahami cara ruang di dalam benteng pernah digunakan. Amati bangunan ini dan perhatikan detail yang membedakannya dari bangunan di sekitarnya."
            }
          ]
        },

        "jalan_tengah_halaman": {
          "title": "Jalan Tengah Halaman",
          "type": "equirectangular",
          "panorama": "images/jalan_tengah_halaman.jpg",
          "yaw": 0,
          "hotSpots": [
            {
              "pitch": 0,
              "yaw": 0,
              "type": "scene",
              "text": "Ke Sisi Bangunan",
              "sceneId": "sisi_bangunan"
            },
            {
              "pitch": -6,
              "yaw": -110,
              "type": "scene",
              "text": "Kembali ke Bangunan Melengkung",
              "sceneId": "bangunan_melengkung"
            },
            {
              "pitch": 8,
              "yaw": 3,
              "type": "info",
              "text": "Jalan Tengah Halaman — Bagian tengah kompleks membantu pengunjung melihat keterhubungan berbagai bangunan di dalam benteng. Jalur dan halaman menjadi bagian dari pengalaman menjelajahi kawasan bersejarah ini. Saat melewati area ini, pengunjung dapat mengamati bagaimana bangunan, jalan, dan ruang terbuka membentuk satu kesatuan lingkungan."
            }
          ]
        },

        "sisi_bangunan": {
          "title": "Sisi Bangunan",
          "type": "equirectangular",
          "panorama": "images/sisi_bangunan.jpg",
          "yaw": 0,
          "hotSpots": [
            {
              "pitch": 0,
              "yaw": 0,
              "type": "scene",
              "text": "Ke Arkade dan Taman Kecil",
              "sceneId": "arkade_dan_taman_kecil"
            },
            {
              "pitch": -6,
              "yaw": -110,
              "type": "scene",
              "text": "Kembali ke Jalan Tengah Halaman",
              "sceneId": "jalan_tengah_halaman"
            },
            {
              "pitch": 8,
              "yaw": 3,
              "type": "info",
              "text": "Sisi Bangunan — Bagian ini menjadi kesempatan untuk mengamati lebih dekat kondisi fisik kompleks Benteng Rotterdam. Dinding, bukaan, dan bagian luar bangunan dapat membantu kita mengenali karakter bangunan bersejarah. Keberadaan kawasan ini juga mengingatkan kita akan pentingnya merawat peninggalan sejarah agar tetap dapat dipelajari oleh generasi berikutnya."
            }
          ]
        },

        "arkade_dan_taman_kecil": {
          "title": "Arkade dan Taman Kecil",
          "type": "equirectangular",
          "panorama": "images/arkade_dan_taman_kecil.jpg",
          "yaw": 0,
          "hotSpots": [
            {
              "pitch": 0,
              "yaw": 0,
              "type": "scene",
              "text": "Ke Lapangan Rumput",
              "sceneId": "lapangan_rumput"
            },
            {
              "pitch": -6,
              "yaw": -110,
              "type": "scene",
              "text": "Kembali ke Sisi Bangunan",
              "sceneId": "sisi_bangunan"
            },
            {
              "pitch": 8,
              "yaw": 3,
              "type": "info",
              "text": "Arkade dan Taman Kecil — Area ini memperlihatkan perpaduan bangunan dan ruang terbuka di dalam kompleks benteng. Bagian seperti ini dapat menjadi tempat pengunjung berhenti sejenak sambil menikmati suasana kawasan bersejarah. Kehadiran ruang terbuka juga mendukung pengalaman wisata yang tidak hanya berfokus pada bangunan, tetapi juga pada lingkungan sekitarnya."
            }
          ]
        },

        "lapangan_rumput": {
          "title": "Lapangan Rumput",
          "type": "equirectangular",
          "panorama": "images/lapangan_rumput.jpg",
          "yaw": 0,
          "hotSpots": [
            {
              "pitch": 0,
              "yaw": 0,
              "type": "scene",
              "text": "Ke Arkade Bertiang",
              "sceneId": "arkade_bertiang"
            },
            {
              "pitch": -6,
              "yaw": -110,
              "type": "scene",
              "text": "Kembali ke Arkade dan Taman Kecil",
              "sceneId": "arkade_dan_taman_kecil"
            },
            {
              "pitch": 8,
              "yaw": 3,
              "type": "info",
              "text": "Lapangan Rumput — Area terbuka di dalam kompleks benteng memberikan ruang untuk menikmati suasana dan melihat bangunan dari sudut pandang yang lebih luas. Benteng Rotterdam dikenal sebagai tujuan wisata sejarah dan budaya di Makassar. Kawasan bersejarah seperti ini juga dapat menjadi ruang untuk kegiatan edukasi dan pengenalan warisan budaya."
            }
          ]
        },

        "arkade_bertiang": {
          "title": "Arkade Bertiang",
          "type": "equirectangular",
          "panorama": "images/arkade_bertiang.jpg",
          "yaw": 0,
          "hotSpots": [
            {
              "pitch": 0,
              "yaw": 0,
              "type": "scene",
              "text": "Ke Taman Melingkar",
              "sceneId": "taman_melingkar"
            },
            {
              "pitch": -6,
              "yaw": -110,
              "type": "scene",
              "text": "Kembali ke Lapangan Rumput",
              "sceneId": "lapangan_rumput"
            },
            {
              "pitch": 8,
              "yaw": 3,
              "type": "info",
              "text": "Arkade Bertiang — Bagian berarkade dengan deretan tiang merupakan salah satu elemen yang dapat ditemukan pada bangunan di kompleks Benteng Rotterdam. Selain membentuk tampilan bangunan, selasar bertiang juga dapat menjadi area peralihan antara bagian luar dan bagian dalam. Perhatikan bagaimana susunan tiang, atap, dan jalur pejalan kaki membentuk karakter ruang tersebut."
            }
          ]
        },

        "taman_melingkar": {
          "title": "Taman Melingkar",
          "type": "equirectangular",
          "panorama": "images/taman_melingkar.jpg",
          "yaw": 0,
          "hotSpots": [
            {
              "pitch": 0,
              "yaw": 0,
              "type": "scene",
              "text": "Ke Lorong Antarbangunan",
              "sceneId": "lorong_antarbangunan"
            },
            {
              "pitch": -6,
              "yaw": -110,
              "type": "scene",
              "text": "Kembali ke Arkade Bertiang",
              "sceneId": "arkade_bertiang"
            },
            {
              "pitch": 8,
              "yaw": 3,
              "type": "info",
              "text": "Taman Melingkar — Area taman menjadi bagian dari pengalaman menikmati lingkungan Benteng Rotterdam. Selain menyimpan nilai sejarah, kawasan benteng juga memiliki daya tarik sebagai tempat untuk mengenal warisan budaya dan menikmati suasana kota. Saat menjelajahi area ini, pengunjung dapat melihat bagaimana ruang terbuka hadir berdampingan dengan bangunan bersejarah."
            }
          ]
        },

        "lorong_antarbangunan": {
          "title": "Lorong Antarbangunan",
          "type": "equirectangular",
          "panorama": "images/lorong_antarbangunan.jpg",
          "yaw": 0,
          "hotSpots": [
            {
              "pitch": 0,
              "yaw": 0,
              "type": "scene",
              "text": "Ke Sisi Bangunan Timur",
              "sceneId": "sisi_bangunan_timur"
            },
            {
              "pitch": -6,
              "yaw": -110,
              "type": "scene",
              "text": "Kembali ke Taman Melingkar",
              "sceneId": "taman_melingkar"
            },
            {
              "pitch": 8,
              "yaw": 3,
              "type": "info",
              "text": "Lorong Antarbangunan — Lorong menjadi bagian dari jalur pergerakan pengunjung di antara bangunan-bangunan dalam kompleks. Saat melewatinya, kita dapat melihat lebih dekat hubungan antarruang dan suasana di antara bangunan bersejarah. Lorong juga membantu pengunjung mengenali bahwa Benteng Rotterdam bukan hanya satu bangunan, melainkan kompleks yang memiliki berbagai bagian dengan karakter masing-masing."
            }
          ]
        },

        "sisi_bangunan_timur": {
          "title": "Sisi Bangunan Timur",
          "type": "equirectangular",
          "panorama": "images/sisi_bangunan_timur.jpg",
          "yaw": 0,
          "hotSpots": [
            {
              "pitch": 0,
              "yaw": 0,
              "type": "scene",
              "text": "Kembali ke Gerbang Masuk",
              "sceneId": "gerbang_masuk"
            },
            {
              "pitch": -7,
              "yaw": 100,
              "type": "scene",
              "text": "Kembali ke Lorong Antarbangunan",
              "sceneId": "lorong_antarbangunan"
            },
            {
              "pitch": 9,
              "yaw": 5,
              "type": "info",
              "text": "Sisi Bangunan Timur — Bagian ini menjadi salah satu titik akhir perjalanan virtual di Benteng Rotterdam. Setelah menjelajahi berbagai bagian kompleks, kita dapat melihat bahwa benteng ini menyimpan cerita tentang sejarah Makassar, perubahan kekuasaan, perkembangan arsitektur, dan pelestarian warisan budaya."
            }
          ]
        }
      }
    });

    const locationButtons = document.querySelectorAll(".location-btn");
    const currentLocation = document.getElementById("currentLocation");

    function updateActiveButton(sceneId) {
      locationButtons.forEach((button) => {
        const active = button.dataset.scene === sceneId;
        button.classList.toggle("active", active);
        button.setAttribute("aria-pressed", active ? "true" : "false");
      });

      currentLocation.textContent =
        "Lokasi aktif: " + (sceneNames[sceneId] || sceneId);
    }

    locationButtons.forEach((button) => {
      button.addEventListener("click", () => {
        const sceneId = button.dataset.scene;
        viewer.loadScene(sceneId);
        updateActiveButton(sceneId);
      });
    });

    viewer.on("scenechange", (sceneId) => {
      updateActiveButton(sceneId);
    });

    updateActiveButton("gerbang_masuk");
  </script>
</body>
</html>
