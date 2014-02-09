import os, time, re
import sublime
import sublime_plugin
import glob
import os
from xml.etree import ElementTree

current_path = None

class FetchCommand(sublime_plugin.WindowCommand):
    ROOT_DIR_PREFIX = '[root: '
    ROOT_DIR_SUFFIX = ']'
    INPUT_PANEL_CAPTION = 'File name:'

    def run(self):

        if not self.find_root():
            return

        self.find_templates()
        self.show_quick_panel(self.templates, self.template_selected)



    def find_root(self):
        folders = self.window.folders()
        if len(folders) == 0:
            sublime.error_message('Could not find project root')
            return False

        self.root = folders[0]
        self.rel_path_start = len(self.root) + 1
        return True



    def find_templates(self):
        self.templates = []
        self.template_paths = []

        for root, dirnames, filenames in os.walk(sublime.packages_path()):
            for filename in filenames:
                if filename.endswith(".file-template"):
                    print(filename)
                    self.template_paths.append(os.path.join(root, filename))
                    self.templates.append(os.path.basename(root) + ": " + os.path.splitext(filename)[0])


    def template_selected(self, selected_index):
        if selected_index != -1:
            self.template_path = self.template_paths[selected_index]
            #print self.template_path
            tree = ElementTree.parse(open(self.template_path))
            self.template = tree

            cur_view = self.window.active_view()
            templ_content = self.get_content();

            if len(templ_content ) == 0:
                sublime.error_message('bad cookie')
                return
            else:
                cur_view.run_command("insert_snippet", {'contents': templ_content })

            

    def get_content(self):
        content = ''

        try:
            content = self.template.find("content").text
        except:
            pass

        try:
            path = os.path.abspath(os.path.join(os.path.dirname(self.template_path), self.template.find("file").text))
            content = open(path).read()
            print(content)
        except:
            pass

        return content




    def show_quick_panel(self, options, done):
        sublime.set_timeout(lambda: self.window.show_quick_panel(options, done), 10)


