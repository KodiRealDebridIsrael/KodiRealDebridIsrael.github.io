import sys
import os
import xbmcaddon
import xbmcgui
import xbmcplugin
import urllib.request
import ssl

if len(sys.argv) > 1:
    HANDLE = int(sys.argv[1])
else:
    HANDLE = -1

# Create an SSL context that allows SSL verification to be skipped
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# Addon Variables
ADDON = xbmcaddon.Addon()
ADDON_PATH = ADDON.getAddonInfo('path')

# Themes
THEME_TITLE = u'[COLOR {color2}]{{}}[/COLOR]'.format(color2='blue')
THEME_TEXT = u'[COLOR {color2}]{{}}[/COLOR]'.format(color2='limegreen')

url_title_map = {
    "מדריך 1 בילד": "https://kodirealdebridisrael.github.io/wizard/assets/build.txt",
    "notify מדריך 2": "https://kodirealdebridisrael.github.io/wizard/assets/notify.txt",
    "מדריך 3 לא זמין": "https://example.com/guide3"
}

# Exit Actions
ACTION_PREVIOUS_MENU = 10  # ESC action
ACTION_NAV_BACK = 92  # Backspace action
ACTION_MOVE_LEFT = 1  # Left arrow key
ACTION_MOVE_RIGHT = 2  # Right arrow key
ACTION_MOVE_UP = 3  # Up arrow key
ACTION_MOVE_DOWN = 4  # Down arrow key
ACTION_MOUSE_WHEEL_UP = 104	 # Mouse wheel up
ACTION_MOUSE_WHEEL_DOWN = 105  # Mouse wheel down
ACTION_MOVE_MOUSE = 107  # Down arrow key
ACTION_SELECT_ITEM = 7  # Number Pad Enter
ACTION_BACKSPACE = 110  # ?
ACTION_MOUSE_LEFT_CLICK = 100
ACTION_MOUSE_LONG_CLICK = 108
BACK_ACTIONS = [ACTION_PREVIOUS_MENU, ACTION_NAV_BACK, ACTION_BACKSPACE]


def show_guide(title, url):
    class ShowGuide(xbmcgui.WindowXMLDialog):

        def __init__(self, *args, **kwargs):
            try:
                with urllib.request.urlopen(url, context=context) as response:
                    self.guide_text = response.read().decode()
            except Exception as e:
                self.menu_item_text = "הייתה בעיה בטעינת הטקסט. אם אתה רואה את ההודעה הזאת, נא דווח על כך בקבוצת הטלגרם בצירוף השם מהתפריט שניסית לפתוח.\n\nhttp://bit.ly/kodi7rd"
            
            self.title = THEME_TITLE.format(title)
            self.guide_text = THEME_TEXT.format(self.guide_text)

        def onInit(self):
            self.titlebox = 102
            self.textbox = 103
            self.close_button = 202
            self.show_dialog()

        def show_dialog(self):
            self.getControl(self.titlebox).setLabel(self.title)
            self.getControl(self.textbox).setText(self.guide_text)
            
        def onAction(self, action):
            if action.getId() in BACK_ACTIONS:
                self.close()

        def onClick(self, controlid):
            if controlid == self.close_button:
                self.close()

    guide = ShowGuide("guide.xml", ADDON_PATH, 'Default')
    guide.doModal()
    del guide

def show_main_menu(title, url_title_map):
    class ShowMainMenu(xbmcgui.WindowXMLDialog):

        def __init__(self, *args, **kwargs):
            self.title = THEME_TITLE.format(title)
            self.url_title_map = url_title_map
            self.menu_item_text = '\n'.join([THEME_TEXT.format(k) for k in self.url_title_map])

        def onInit(self):
            self.title = 101
            self.textbox = 9000
            self.close_button = 201
            self.show_dialog()
            
            self.controllist = [self.menu1, self.menu2]
            
            for item in self.controllist:
                if CONFIG.get_setting(self.controlsettings[self.controllist.index(item)]) == 'true':
                    self.getControl(item).setSelected(True)


        def show_dialog(self):
            self.getControl(self.titlebox).setLabel(self.title)
            self.getControl(self.textbox).setText(self.menu_item_text)

        def onClick(self, controlid):
            if controlid == self.close_button:
                 self.close()
                for item in self.controllist:
                        at = self.controllist.index(item)
                    if self.getControl(item).isSelected():
                    else:

                if self.getControl(self.whitelist).isSelected() and not self.whitelistcurrent == 'true':
                    from resources.libs import whitelist
                    whitelist.whitelist('edit')
                
                self.close()


        #def onClick(self, control_id):
        #    if control_id == self.close_button:
        #        self.close()
        #    else:
        #        selected_item = self.getControl(self.textbox).getSelectedItem()
        #        title = selected_item.getLabel()
        #        url = self.url_title_map[title]
        #       show_guide(title, url)
        #        self.close()

    show_main_menu_dialog  = ShowMainMenu("main_menu_dialog.xml", ADDON_PATH, 'Default')
    show_main_menu_dialog.doModal()

def main():
    show_main_menu("test", url_title_map)

if __name__ == "__main__":
    main()
    if HANDLE > -1:
        xbmcplugin.endOfDirectory(HANDLE)
