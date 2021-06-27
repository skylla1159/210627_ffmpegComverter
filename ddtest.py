# -*- coding: utf-8 -*-

import wx
import os

class MyFileDropTarget(wx.FileDropTarget):
    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        self.window = window

    def OnDropFiles(self, x, y, filenames):
        for filename in filenames:
            self.window.filelistbox.Append(os.path.basename(filename), filename)
        return True


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Drop Target", size=(500, 200))
        p = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        OutputLabel = wx.StaticText(p, wx.ID_ANY, "Output directory")
        OutputText = wx.TextCtrl(p, wx.ID_ANY, "/tmp")
        filelistLabel = wx.StaticText(p, wx.ID_ANY, "File list")

        self.filelist = []
        self.filelistbox = wx.ListBox(p, wx.ID_ANY, style=wx.LB_ALWAYS_SB)
        sizer.Add(OutputLabel, 0, wx.ALL, 5)
        sizer.Add(OutputText, 0, wx.ALL, 5)
        sizer.Add(filelistLabel, 0, wx.ALL, 5)
        sizer.Add(self.filelistbox, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)
        p.SetSizer(sizer)


        dt = MyFileDropTarget(self)
        self.SetDropTarget(dt)
        self.Show()

class Encode(self):
    def main(self):
        pass
if __name__ == '__main__':
    app = wx.App()
    MyFrame()
    app.MainLoop()