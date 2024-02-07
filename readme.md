Moinsen.
# INIT PROJECT

1. Change Authorization of "init_packages.sh"
```shell
chmod 777 ./init_packages.sh
```

2. Startup
```shell
./init_packages.sh
```

# APK Creation

1. Buildozer installieren:
```shell
pip3 install buildozer
```

2. Im Root Folder des projektes folgendes eingeben:
```shell
buildozer init
```

3. Jetzt wurde eine buildozer.spec erstellt, die dementsprechend angepasst werden MUSS! (Requirements-Kommasepariert[WIE IN DER REQUIREMENTS.TXT!!!], Version, Icon, Package,....)

4. Um eine APK zu erstellen und laufen zu lassen (Android studio mit laufenden Virtual Android Device):
```shell
buildozer android debug deploy run
```
5. Die APK befindet sich im Python-Root Ordner "bin"


# Troubleshooting - APK Creation

1. Cython OS und pip3 basierend installieren
```shell
pip3 install cython && sudo apt-get install  cython3
```