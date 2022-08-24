# -*- coding: utf-8 -*-

# Emilio Devesa
# https://emiliodevesa.wordpress.com/

import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk, GdkPixbuf

class Cell(Gtk.EventBox):
    name=None
    pixbuf=None
    description=None
    biography=None
    
    def __init__(self,name,image,description,biography):
        super().__init__()
        self.name=name
        self.pixbuf=image
        self.description=description
        self.biography=biography
        imagen=Gtk.Image()
        imagen.set_from_pixbuf(self.pixbuf)
        box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        box.pack_start(Gtk.Label(label=name), False, False, 0)
        box.pack_start(imagen, True, True, 0)
        self.add(box)
        self.connect("button-release-event", self.on_click)

    def on_click(self,widget,event):
        print("Se ha clicado la celda de "+self.name)