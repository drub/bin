#!/Users/thedrub/anaconda3/bin/python
# hello_wx.py

import wx

app = wx.App(False)
frame = wx.Frame(parent=None, title='Hello World')
frame.Show()
app.MainLoop()


