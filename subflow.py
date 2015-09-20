#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sublime
import sublime_plugin
import webbrowser


class SearchStackoverflowCommand(sublime_plugin.WindowCommand):

    def search(self, text):
        sublime.status_message("Opening browser.")
        webbrowser.open("http://stackoverflow.com/search?q=%s" % text)
        return 0

    def run(self):
        v = self.window.active_view()
        text = v.substr(v.sel()[0]).strip()
        self.search(text)

        return 0


class SearchGoogleCommand(sublime_plugin.WindowCommand):

    def search(self, text):
        sublime.status_message("Opening browser.")
        webbrowser.open("https://www.google.tn/search?q=%s" % text)
        return 0

    def run(self):
        v = self.window.active_view()
        text = v.substr(v.sel()[0]).strip()
        self.search(text)

        return 0


class SearchGithubCommand(sublime_plugin.WindowCommand):

    def search(self, text):
        sublime.status_message("Opening browser.")
        webbrowser.open("https://github.com/search?q=%s&type=Code" % text)
        return 0

    def run(self):
        v = self.window.active_view()
        text = v.substr(v.sel()[0]).strip()
        self.search(text)

        return 0


class SearchSemanticwebCommand(sublime_plugin.WindowCommand):

    def search(self, text):
        sublime.status_message("Opening browser.")
        webbrowser.open("http://answers.semanticweb.com/search/?q=%s" % text)
        return 0

    def run(self):
        v = self.window.active_view()
        text = v.substr(v.sel()[0]).strip()
        self.search(text)

        return 0


class SearchServerfaultCommand(sublime_plugin.WindowCommand):

    def search(self, text):
        sublime.status_message("Opening browser.")
        webbrowser.open("http://serverfault.com/search?q=%s" % text)
        return 0

    def run(self):
        v = self.window.active_view()
        text = v.substr(v.sel()[0]).strip()
        self.search(text)

        return 0
