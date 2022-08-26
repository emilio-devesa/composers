# -*- coding: utf-8 -*-

# Emilio Devesa
# https://emiliodevesa.wordpress.com/

import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,GdkPixbuf

class DetailWindow(Gtk.Window):

    def __init__(self,name,pixbuf,description,biography):
        super().__init__(title=name)
        self.set_default_size(320,480)
        image=Gtk.Image()
        image.set_from_pixbuf(pixbuf)

        # Label adjustments
        biography.set_line_wrap(True)
        biography.set_justify(Gtk.Justification.RIGHT)
        biography.set_max_width_chars(40)

        # Widgets
        box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box.add(image)#, False, False, 0)
        box.add(description)#, False, False, 0)
        box.add(biography)#,False,False,20)
        
        scrolled=Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scrolled.add(box)

        #vbox=Gtk.VBox(False,2)
        #vbox.pack_start(scrolled, True, True, 0)
        #box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        #box.set_homogeneous(False)
        #box.pack_start(scrolled, True, True, 0)
        #self.add(box)
        self.add(scrolled)