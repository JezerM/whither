# whither
### Universal Linux Application SDK - Create once. Run everywhere.

Whither is a simple SDK to create web applications, such as [LightDM Web Greeter][web-greeter]

## Dependencies
|                   |     Arch     |     Ubuntu      |     fedora     |      openSUSE     | 
|-------------------|--------------|-----------------|----------------|-------------------|
|**pyqt5**          |python-pyqt5  |python3-pyqt5    |python3-qt5     |python3-qt5        |
|**qt5-webengine**  |qt5-webengine |libqt5webengine5 |qt5-qtwebengine |libqt5-qtwebengine |

### PIP
You can install the dependencies with **pip**
```sh
pip install PyQt5 PyQtWebEngine ruamel.yaml
```

## Download & Install
```sh
git clone https://github.com/JezerM/whither.git
cd whither
sudo python setup.py install
```
Either, you could use `sudo pip install .` in the project directory.

If you have problems when using it in not-root, you should also install it in user directory.

Also, you can download and install the latest release.

[web-greeter]: https://github.com/JezerM/web-greeter "web-greeter"
