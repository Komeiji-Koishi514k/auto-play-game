[app]
title = Auto Play Game
package.name = autoplaygame
package.domain = org.hykeegj
source.dir = android_app
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0
requirements = python3,kivy==2.3.0
orientation = portrait
fullscreen = 0

android.api = 35
android.minapi = 23
android.ndk = 27c
android.sdk = 35
android.archs = arm64-v8a
android.allow_backup = True
android.entrypoint = org.kivy.android.PythonActivity
android.accept_sdk_license = True

[buildozer]
warn_on_root = 1
log_level = 2
