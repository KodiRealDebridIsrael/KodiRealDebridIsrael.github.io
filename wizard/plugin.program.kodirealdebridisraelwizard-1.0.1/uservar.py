import os, xbmc, xbmcaddon

#########################################################
#         Global Variables - DON'T EDIT!!!              #
#########################################################
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
PATH           = xbmcaddon.Addon().getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')
#########################################################

#########################################################
#        User Edit Variables                            #
#########################################################
ADDONTITLE     = '[COLOR lightblue]Kodi + Real Debrid Israel Mini Build Wizard[/COLOR]'
BUILDERNAME    = '[COLOR lightblue]Kodi + Real Debrid Israel[/COLOR]'
EXCLUDES       = [ADDON_ID, 'script.module.kodi-six', 'script.module.six']
# Enable/Disable the text file caching with 'Yes' or 'No' and age being how often it rechecks in minutes
CACHETEXT      = 'No'
CACHEAGE       = 1
# Text File with build info in it.
BUILDFILE = 'https://kodirealdebridisrael.github.io/wizard/assets/build.txt'
# How often you would like it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK    = 0
# Text File with apk info in it.  Leave as 'https://' to ignore
APKFILE        = 'https://'
# Text File with Youtube Videos urls.  Leave as 'https://' to ignore
YOUTUBETITLE   = ''
YOUTUBEFILE    = 'https://'
# Text File for addon installer.  Leave as 'https://' to ignore
ADDONFILE      = 'https://'
# Text File for advanced settings.  Leave as 'https://' to ignore
ADVANCEDFILE   = 'https://'
#########################################################

#########################################################
#        Theming Menu Items                             #
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'https://aftermathwizard.net/repo/wizard/settings.png'
# Leave as https:// for default icon
ICONBUILDS     = os.path.join(ART, 'builds.png')
ICONMAINT      = os.path.join(ART, 'maintenance.png')
ICONSPEED      = os.path.join(ART, 'speed.png')
ICONAPK        = os.path.join(ART, 'apkinstaller.png')
ICONADDONS     = os.path.join(ART, 'addoninstaller.png')
ICONYOUTUBE    = os.path.join(ART, 'youtube.png')
ICONSAVE       = os.path.join(ART, 'savedata.png')
ICONTRAKT      = os.path.join(ART, 'keeptrakt.png')
ICONREAL       = os.path.join(ART, 'keepdebrid.png')
ICONLOGIN      = os.path.join(ART, 'keeplogin.png')
ICONCONTACT    = os.path.join(ART, 'information.png')
ICONSETTINGS   = os.path.join(ART, 'settings.png')
# Hide the section seperators 'Yes' or 'No'
HIDESPACERS    = 'No'
# Character used in seperator
SPACER         = '='

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'lightblue'
COLOR2         = 'yellow'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR1+'](Kodi + Real Debrid Israel)[/COLOR]  [COLOR '+COLOR2+']%s[/COLOR]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR1+']מיני בילד נוכחי:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR1+']Current Theme:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'Yes'
# You can add \n to do line breaks
CONTACT        = 'Thank you for choosing OpenWizard'
#Images used for the contact window.  https:// for default icon and fanart
CONTACTICON    = 'https://'
CONTACTFANART  = 'https://'
#########################################################

#########################################################
#        Auto Update For Those With No Repo             #
#########################################################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'No'
# Url to wizard version
WIZARDFILE     = BUILDFILE
#########################################################

#########################################################
#        Auto Install Repo If Not Installed             #
#########################################################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'No'
# Addon ID for the repository
REPOID         = 'spaceholder'
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = 'https://'
# Url to folder zip is located in
REPOZIPURL     = 'https://'
#########################################################

#########################################################
#        Notification Window                            #
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'Yes'
# Url to notification file
NOTIFICATION   = 'https://kodirealdebridisrael.github.io/wizard/assets/notify.txt'
# Use either 'Text' or 'Image'
HEADERTYPE     = 'Text'
# Font size of header
FONTHEADER     = 'Font30'
HEADERMESSAGE  = '[COLOR lightblue]Kodi + Real Debrid Israel[/COLOR]'
# url to image if using Image 424x180
HEADERIMAGE    = 'https://'
# Font for Notification Window
FONTSETTINGS   = 'Font13'
# Background for Notification Window
BACKGROUND     = 'https://'
#########################################################