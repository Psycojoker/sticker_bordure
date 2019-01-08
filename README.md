Introduction
============

Stickery is a GIMP plugin that puts a bordure arround the current layer to
"stickerify" it by putter a bordure arround it.

It's meant for creating Telegram stickers (and also an excuse to try to write a
plugin because fun.)

![before_after](./diff.png)

Usage
=====

The plug is located in Filter > Artistic > Stickerify

![menu](./menu.png)

And provide the following options:

![screenshot](./screenshot.png)

Installation
============

For gimp 2.8, haven't tested on other versions but it should work too.

```bash
sudo apt install gimp-python
wget https://raw.githubusercontent.com/Psycojoker/sticker_bordure/master/stickers_bordure.py
chmod +x stickers_bordure.py

# local install
mkdir -p ~/.gimp-2.8/plug-ins/
mv stickers_bordure.py ~/.gimp-2.8/plug-ins/

# global install
sudo mv stickers_bordure.py /usr/lib/gimp/2.8/plug-ins/
```

Licence
=======

wtfpl
