# -*- coding: utf-8 -*-

import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk, GdkPixbuf

class AboutWindow(Gtk.Window):

    label=Gtk.Label("""
        Emilio Devesa
        http://emiliodevesa.wordpress.com/
        """)

    def __init__(self):
        super().__init__(title="Acerca De")
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_border_width(15)
        self.set_default_size(120,100)
        box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        box.pack_start(self.label, True, True, 0)
        self.add(box)
