# YouTube Video Downloader

Bu proje, `yt-dlp` kütüphanesini kullanarak YouTube videolarını indirmenizi sağlar.

## Özellikler
- YouTube videolarını en iyi kalitede indirir.
- İndirilen videolar belirtilen dizine kaydedilir (varsayılan: mevcut dizin).

## Gereksinimler
Bu projeyi kullanabilmek için aşağıdaki gereksinimlere ihtiyacınız vardır:

- Python 3.x
- `yt-dlp` kütüphanesi

## Kurulum
Aşağıdaki komutu kullanarak `yt-dlp` kütüphanesini yükleyin:

```bash
pip install yt-dlp
```

## Kullanım

1. Terminali açın.
2. `download_video.py` dosyasını çalıştırın:

```bash
python download_video.py
```

3. İndirmek istediğiniz YouTube video URL'sini girin.
4. Video belirtilen dizine indirilecektir.

## Kod Açıklaması

Python dosyasında aşağıdaki fonksiyon bulunmaktadır:

```python
def download_video(url, save_path="."):
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{save_path}/%(title)s.%(ext)s'
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download complete!")
    except Exception as e:
        print(f"Error: {e}")
```

- `download_video(url, save_path)`: Verilen YouTube URL'sini indirir ve belirtilen dizine kaydeder.
- Hata durumunda kullanıcıya bilgi verir.

## Katkıda Bulunma
Projeye katkıda bulunmak isterseniz, pull request gönderebilir veya hata bildirebilirsiniz.

## Lisans
Bu proje MIT Lisansı ile lisanslanmıştır.

