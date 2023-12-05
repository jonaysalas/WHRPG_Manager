# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.0.0-0-g0efcecf)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Warhammer RPG Manager", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer1.AddGrowableCol( 0 )
        fgSizer1.AddGrowableCol( 1 )
        fgSizer1.AddGrowableRow( 0 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.btnWHF = wx.Button( self, wx.ID_ANY, u"WHFRPG", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.btnWHF, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.btnWH40k = wx.Button( self, wx.ID_ANY, u"WH40k", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.btnWH40k, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.SetSizer( fgSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.btnWHF.Bind( wx.EVT_BUTTON, self.OpenFantasyManager )
        self.btnWH40k.Bind( wx.EVT_BUTTON, self.Open40kManager )

        #Change the background img
        self.bckgr_img = "imgs\\mainFrame_bckgr.jpg"
        self.SetBackgroundStyle(wx.BG_STYLE_ERASE)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        h,w = self.GetSize()
        self.SetSize(h+1,w+1)

    def __del__( self ):
        pass


	# Virtual event handlers, override them in your derived class
    def OpenFantasyManager( self, event ):
        '''
        Opens the window of Warhammer Fantasy RPG 2ed Manager
        '''
        event.Skip()

    def Open40kManager( self, event ):
        '''
        Opens the window of Warhammer Fantasy RPG 2ed Manager
        '''
        with wx.MessageDialog(None, "Warhammer 40k manager in development", 'DISCLAIMER') as dialog:
            dialog.ShowModal()


    # ----------------------------------------------------------------------
    def scale_bitmap(self, bitmap, width, height):
        image = wx.ImageFromBitmap(bitmap)
        image = image.Scale(width-10, height-38, wx.IMAGE_QUALITY_HIGH)
        result = wx.BitmapFromImage(image)
        return result

    def OnEraseBackground(self, evt):
        """
        Add a picture to the background
        """
        # yanked from ColourDB.py
        dc = evt.GetDC()

        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap(self.bckgr_img)

        w,h = self.GetSize()
        bmp = self.scale_bitmap(bmp, w, h)

        dc.DrawBitmap(bmp, 0, 0)
