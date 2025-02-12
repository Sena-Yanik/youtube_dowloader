# YouTube Playlist Downloader

Bu proje, `yt-dlp` kütüphanesini kullanarak YouTube çalma listelerini indirmenizi sağlar.

## Özellikler
- YouTube çalma listelerini en iyi kalitede indirir.
- İndirilen videolar çalma listesi adına göre ayrı bir klasöre kaydedilir.

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
2. `download_playlist.py` dosyasını çalıştırın:

```bash
python download_playlist.py
```

3. İndirmek istediğiniz YouTube çalma listesi URL'sini girin.
4. Çalma listesi belirtilen dizine, klasör halinde indirilecektir.

## Kod Açıklaması

Python dosyasında aşağıdaki fonksiyon bulunmaktadır:

```python
def download_playlist(url, save_path="."):
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{save_path}/%(playlist)s/%(title)s.%(ext)s'
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Playlist download complete!")
    except Exception as e:
        print(f"Error: {e}")
```

- `download_playlist(url, save_path)`: Verilen YouTube çalma listesini indirir ve belirtilen dizinde çalma listesi adına sahip bir klasöre kaydeder.
- Hata durumunda kullanıcıya bilgi verir.

## Katkıda Bulunma
Projeye katkıda bulunmak isterseniz, pull request gönderebilir veya hata bildirebilirsiniz.

## Lisans
Bu proje MIT Lisansı ile lisanslanmıştır.

