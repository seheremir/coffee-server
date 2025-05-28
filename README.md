# Coffee API Server ☕

AlexFlipnote Coffee API'sini kullanan kapsamlı FastAPI sunucusu.

## Özellikler

- **Ana Endpoints:**
  - `GET /random` - Rastgele kahve fotoğrafı (JSON)
  - `GET /random/image` - Rastgele kahve fotoğrafına yönlendirme
  - `GET /coffee` - Rastgele kahve fotoğrafı (alias)
  - `GET /coffee/image` - Rastgele kahve fotoğrafına yönlendirme (alias)

- **Özel Endpoints:**
  - `GET /random/info` - Rastgele kahve fotoğrafı + kahve bilgisi
  - `GET /daily` - Günlük özel kahve fotoğrafı
  - `POST /batch` - Toplu rastgele kahve fotoğrafları (1-20 adet)
  - `GET /stats` - API istatistikleri

## Kurulum

### Docker ile Çalıştırma

```bash
# Docker image oluştur
docker build -t coffee-server .

# Konteyner çalıştır
docker run -p 8080:8080 coffee-server
```

### Manuel Kurulum

```bash
# Bağımlılıkları yükle
pip install -r requirements.txt

# Sunucuyu başlat
python server.py
```

## API Kullanımı

Sunucu çalıştıktan sonra `http://localhost:8080` adresinden erişebilirsiniz.

### Örnek Kullanımlar

#### 1. Rastgele Kahve Fotoğrafı (JSON)

```bash
curl http://localhost:8080/random
```

Response:
```json
{
  "success": true,
  "file": "https://coffee.alexflipnote.dev/random_image.jpg",
  "timestamp": "2025-05-28T10:30:00.000Z",
  "source": "coffee.alexflipnote.dev"
}
```

#### 2. Rastgele Kahve Fotoğrafına Yönlendirme

```bash
curl -L http://localhost:8080/random/image
# Doğrudan kahve fotoğrafına yönlendirir
```

#### 3. Toplu Kahve Fotoğrafları

```bash
curl -X POST "http://localhost:8080/batch?count=3"
```

#### 4. Bilgili Kahve Fotoğrafı

```bash
curl http://localhost:8080/random/info
```

Response:
```json
{
  "success": true,
  "file": "https://coffee.alexflipnote.dev/random_image.jpg",
  "info": {
    "fact": "Kahve dünyanın en çok tüketilen ikinci içecektir",
    "source": "coffee.alexflipnote.dev",
    "total_images_in_api": 1257
  },
  "timestamp": "2025-05-28T10:30:00.000Z"
}
```

#### 5. Günlük Özel Kahve

```bash
curl http://localhost:8080/daily
```

## API Dokümantasyonu

Sunucu çalışırken aşağıdaki adreslerde interaktif API dokümantasyonuna erişebilirsiniz:

- **Swagger UI:** http://localhost:8080/docs
- **ReDoc:** http://localhost:8080/redoc

## Özellikler

### Rate Limiting
- IP başına dakikada 100 istek sınırı
- Aşıldığında 429 status kodu döner

### CORS Desteği
- Tüm origin'lere izin verilir
- Frontend uygulamalar için uygun

### Hata Yönetimi
- Kapsamlı hata yakalama
- Anlamlı hata mesajları
- API durumu kontrolü

### Endpoint Çeşitliliği
- JSON ve yönlendirme formatları
- Toplu istek desteği
- Günlük özel fotoğraf
- Kahve bilgileri ile zenginleştirilmiş yanıtlar

## Hata Kodları

- `200` - Başarılı
- `400` - Geçersiz parametreler
- `404` - Endpoint bulunamadı
- `408` - İstek zaman aşımı
- `429` - Rate limit aşıldı
- `500` - Sunucu hatası

## Teknik Detaylar

- **Framework:** FastAPI
- **HTTP Client:** httpx (async)
- **Veri Validasyonu:** Pydantic
- **CORS:** Tüm origin'lere açık
- **Rate Limiting:** IP bazlı (100 req/dakika)
- **Timeout:** 30 saniye
- **Source API:** coffee.alexflipnote.dev

## Lisans

MIT License

---

☕ **Coffee API Server** - Gününüzü güzel kahve fotoğraflarıyla başlatın!