#!/usr/bin/env python

import gtk
import gtk.glade


def on_button_clicked(w, *args):
    w.set_label("you poked me!")
    w.connect("clicked", gtk.main_quit)


xml = gtk.glade.XML('hw.glade')
window = xml.get_widget('window')
window.connect("delete_event", gtk.main_quit)
button = xml.get_widget('button')
button.connect("clicked", on_button_clicked)
window.show_all()
gtk.main()
