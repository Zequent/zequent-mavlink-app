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

2. Hit command in root folder of zequent-mavlink-app <span style="color:red">(CAUTION!!! ONLY IF 'buildozer.spec' isn't in project-root folder!!!)</span>:
```shell
buildozer init
```

3. Now you created "buildozer.spec", you have to configure it if it isn't (Requirements-commaseperated [LIKE IN 'REQUIREMENTS.TXT'!!!], Version, Icon, Package,....)

4. To crate a ".apk" and run on VAD (Virtual Android Device):
```shell
buildozer android debug deploy run
```

5. If app crashes use this command in other terminal:

```shell
adb logcat
```

6. You'll find the ".apk" in project-root folder "bin"


# Troubleshooting - APK Creation

1. Cython OS und pip3 basierend installieren
```shell
pip3 install cython && sudo apt-get install  cython3
```


# TRYING KIVYMD 2.0.1DEV
```shell
pip install https://github.com/kivymd/KivyMD/archive/master.zip
```

# GOING BACK
```shell
pip install kivymd==1.2.0
```