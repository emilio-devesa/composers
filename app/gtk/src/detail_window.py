# -*- coding: utf-8 -*-

import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,GdkPixbuf

class DetailWindow(Gtk.Window):

    def __init__(self,name,pixbuf,description,biography):
        super().__init__(title=name)
        self.set_default_size(320,320)
        self.set_border_width(15)
        self.set_position(Gtk.WindowPosition.CENTER)
        image=Gtk.Image()
        image.set_from_pixbuf(pixbuf)

        # Label adjustments
        biography.set_line_wrap(True)
        biography.set_justify(Gtk.Justification.FILL)

        # Widgets
        box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        box.set_homogeneous(False)
        box.pack_start(image, False, False, 10)
        box.pack_start(description, False, False, 5)
        box.pack_start(biography, False, False, 0)
        
        scrolled=Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scrolled.add(box)
        self.add(scrolled)