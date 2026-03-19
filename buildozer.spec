[app]
# Основная информация
title = Helpy Assistant
package.name = helpyassistant
package.domain = com.helpy.pro
source.dir = .
source.include_exts = py,png,jpg,kv,json
version = 0.1

# Библиотеки (чтобы мозг работал)
requirements = python3,kivy,numpy

# Настройки экрана
orientation = portrait
fullscreen = 1

# Разрешения для Android (профессиональный уровень)
android.permissions = INTERNET, VIBRATE, USE_BIOMETRIC, USE_FINGERPRINT, WAKE_LOCK

# Хелпи как фоновый сервис
android.services = HelpyGuard:guardian.py

[buildozer]
log_level = 2
warn_on_root = 1