# Depin Alliance AUTO

Depin Alliance Telegram Mini App Bot

For README in English: [![en](https://img.shields.io/badge/README-en-red.svg)](https://github.com/dzuhri-auto/depin-alliance/blob/master/README.md)

## Fitur

- Auto Claim Daily Check-in
- Auto Farming
- Auto Clear Mission / Tasks
- Auto Upgrade Skills
- Auto Open Cyber Box (deactivated by default)
- Auto Add New Device
- Auto Add Component Device

## .env Settings

| Name                    | Description                                     | Default |
| ----------------------- | ----------------------------------------------- | ------- |
| API_KEY                 | Custom API KEY                                  |         |
| API_ID / API_HASH       | API and API HASH from telegram account          |         |
| AUTO_OPEN_BOX           | Auto open box                                   | False   |
| RESERVE_POINT           | Minimum point hold                              | 1000000 |
| AUTO_UPGRADE_SKILL      | Auto upgrade skills                             | True    |
| USE_RANDOM_DELAY_IN_RUN | Activate delay before start the bot             | True    |
| RANDOM_DELAY_IN_RUN     | Randomize delay in seconds before start the bot | [5, 30] |
| USE_PROXY_FROM_FILE     | For using proxy                                 | False   |

## Persiapan

Pastikan kamu sudah menginstal:

- [Python](https://www.python.org/downloads/release/python-31014/) **versi 3.10**

Cara Mendapatkan API ID and API HASH:

1. Buka [my.telegram.org](https://my.telegram.org/) via browser, lalu login dengan akun telegram mu.
2. Pilih menu `API development tools` dan isi form nya untuk mendaftarkan aplikasi baru.
3. Simpan `API_ID` dan `API_HASH` yang diberikan setelah mendaftarkan aplikasi ke file .env.

### 🚨 Disclaimer 🚨

*Khusus untuk bot tipe login ini harap menggunakan akun telegram dengan awalan id dibawah `61xxxxx`, check `@userinfobot` untuk checking awalan id.
Jika pakai akun dengan awalan id diatas itu akan otomatis banned !!*

## Mendapatkan API KEY

Script ini menggunakan kustom API KEY, API KEY nya hanya tersedia untuk disewa.

Kamu bisa chat saya, [Irham](https://t.me/irhamdz) untuk menanyakan harga sewanya!

## Install

Clone ke PC / VPS kamu:

```shell
git clone https://github.com/dzuhri-auto/depin-alliance.git
```

Masuk ke folder:

```shell
cd depin-alliance
```

Kemudian gunakan perintah ini untuk instal otomatis:

**Windows** :

```shell
windows\install.bat
```

**Mac / Linux / VPS** :

```shell
sudo chmod +x ubuntu/install.sh ubuntu/run.sh ubuntu/update.sh
```

```shell
source ./ubuntu/install.sh
```

***note : Jangan lupa untuk mengedit file `.env`***

## Update API KEY

Setelah instalasi, kita bisa memperbarui menggunakan API KEY:

**Windows** :

```shell
$filePath = ".env"
$searchPattern = "^API_KEY="
$replacement = 'API_KEY="YOUR API KEY"'

(Get-Content $filePath) -replace $searchPattern + '.*', $replacement | Set-Content $filePath
```

**Mac / Linux / VPS** :

```shell
sed -i~ '/^API_KEY=/s/=.*/="YOUR API KEY"/' .env

# contoh jika API KEY kamu = "aisjiqiqssq"
# sed -i~ '/^API_KEY=/s/=.*/="aisjiqiqssq"/' .env
```

## Menjalankan Bot

Untuk menjalankan bot:

**Windows** :

```shell
windows\run.bat
```

**Mac / Linux / VPS** :

```shell
./ubuntu/run.sh
```
