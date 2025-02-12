# YouTube Audio Downloader

Bu proje, YouTube videolarından ses dosyalarını indirerek MP3 formatına dönüştüren basit bir Python betiğidir. `yt-dlp` kütüphanesini ve `ffmpeg` aracını kullanır.

## 🚀 Kurulum

### Gerekli Bağımlılıkları Yükleme

Projeyi kullanmadan önce aşağıdaki bağımlılıkları yükleyin:

```bash
pip install yt-dlp
```

Ayrıca, `ffmpeg` aracının sisteminizde kurulu olması gerekmektedir.
- Windows için: [FFmpeg Download](https://ffmpeg.org/download.html)
- Linux/Mac için:
  ```bash
  sudo apt install ffmpeg  # Debian/Ubuntu
  brew install ffmpeg      # macOS (Homebrew)
  ```

## 🔧 Kullanım

Python betiğini çalıştırarak YouTube videolarını MP3 formatında indirebilirsiniz:

```bash
python youtube_audio_downloader.py
```

Ardından, indirmek istediğiniz YouTube videosunun URL'sini girin.

## 📂 Dosya Yapısı

```
📁 Proje Klasörü
│── youtube_audio_downloader.py  # Ana Python betiği
│── README.md                    # Bu döküman
```

## ⚠️ Uyarılar

- Bu betik, yalnızca kişisel kullanım ve yasal içerikler için kullanılmalıdır. Telif hakkı kurallarına uymayı unutmayın.
- YouTube'un kullanım koşullarına uygun hareket ettiğinizden emin olun.

## 📜 Lisans

Bu proje MIT lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına göz atabilirsiniz.

---

Eğer bir hata ile karşılaşırsanız veya geliştirmeye katkıda bulunmak isterseniz, lütfen bir **issue** veya **pull request** açın! 😊

