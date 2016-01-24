# akademik-bilisim-crawler
Akademik Bilişim konferansındaki makale ve zaman çizelgesini çekip makale-zaman eşlemesini yapar.

```bash
pip install -r requirements.txt
scrapy crawl paperlist -o papers.json
scrapy crawl sessions -o sessions.json
python3 process.py
```

ile verileri json formatında çektikten sonra işlemden geçirir, HTML dosyaları üretir.

* AB2016 için özel oluşturulmuştur. 
* Çok sayıda quick workaroundlar içerdiğinden crappy durumda ama kullanıp üzerinden gitmek isteyen olursa örnek alabilir.
* Webdeki HTML dosyalarında syntax hatası olduğu için doğru parse edilemeyen cerceve.html lokale kaydedilmiştir.


