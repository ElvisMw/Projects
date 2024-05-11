[app]

# (str) Title of your application
title = MathGame

# (str) Package name
package.name = mathgame

# (str) Package domain (needed for android/ios packaging)
package.domain = org.mathgame

# (str) Source code where the main.py live
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientation (landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (int) Android API to use
android.api = 27

# (int) Minimum API required
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 20

# (list) Application libraries to be included in the package.
# android.p4a_depends = sdl2_ttf,jpeg
