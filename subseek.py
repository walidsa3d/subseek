#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sublime
import sublime_plugin
import webbrowser

sites = {
    "google": "https://www.google.tn/search?q=%s",
    "stackoverflow": "http://stackoverflow.com/search?q=%s",
    "serverfault": "http://serverfault.com/search?q=%s",
    "semanticoverflow": "https://github.com/search?q=%s&type=Code",
    "github": "http://answers.semanticweb.com/search/?q=%s"
}


class SearchCommand(sublime_plugin.WindowCommand):

    def search(self, text, site):
        url = sites.get(site) %text
        sublime.status_message("Opening browser.")
        webbrowser.open(url)
        return 0

    def run(self, site=None):
        v = self.window.active_view()
        text = v.substr(v.sel()[0]).strip()
        self.search(text, site)

        return 0
