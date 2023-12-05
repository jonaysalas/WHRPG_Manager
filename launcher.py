from GUI.MainFrame import MainFrame
import wx

if __name__ == "__main__":
    app = wx.App(False)
    mf = MainFrame(None)
    mf.Show()
    app.MainLoop()