# -*- coding: utf-8 -*-

# Emilio Devesa
# https://emiliodevesa.wordpress.com/

import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,GdkPixbuf

class DetailWindow(Gtk.Window):

    def __init__(self,name,pixbuf,description,biography):
        super().__init__(title=name)
        image=Gtk.Image()
        image.set_from_pixbuf(pixbuf)
        box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        box.pack_start(image, False, False, 0)
        box.pack_start(description, True, True, 0)
        box.pack_end(biography,True,True,0)
        self.add(box)
        