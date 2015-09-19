#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sublime
import sublime_plugin
import webbrowser


class SearchStackoverflowCommand(sublime_plugin.WindowCommand):

    def search(self, text):
        sublime.status_message("I\'ve opened web browser for this page.")
        webbrowser.open("http://stackoverflow.com/search?q="+text)
        return 0

    def run(self):
        v = self.window.active_view()
        text = v.substr(v.sel()[0]).strip()
        self.search(text)

        return 0


class SearchGoogleCommand(sublime_plugin.WindowCommand):

    def search(self, text):
        sublime.status_message("I\'ve opened web browser for this page.")
        webbrowser.open("https://www.google.tn/search?q="+text)
        return 0

    def run(self):
        v = self.window.active_view()
        text = v.substr(v.sel()[0]).strip()
        self.search(text)

        return 0
