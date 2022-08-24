# -*- coding: utf-8 -*-

# Emilio Devesa
# https://emiliodevesa.wordpress.com/

import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk, GLib, GdkPixbuf

class LoadWindow(Gtk.Window):
    label=Gtk.Label("Cargando elementos...")
    spinner=Gtk.Spinner()
    box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)

    def __init__(self):
        super().__init__(title="")
        self.connect("destroy", Gtk.main_quit)
        self.set_border_width(60)
        self.set_resizable(False)
        self.set_default_size(120,100)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.spinner.props.active=True

        self.box.pack_start(self.label, False, False, 0)
        self.box.pack_start(self.spinner, False, False, 0)
        self.add(self.box)

