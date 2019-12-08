from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
import webbrowser
import re


class OpenInBrowser(Extension):

    def __init__(self):
        super(OpenInBrowser, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        data = event.get_argument()
        items = [
            ExtensionResultItem(
                icon='images/icon.png',
                name=event.get_argument(),
                description='Open "%s" in the browser' % event.get_argument(),
                on_enter=ExtensionCustomAction(data, keep_app_open=True)
            )
        ]

        return RenderResultListAction(items)

class ItemEnterEventListener(EventListener):

    def on_event(self, event, extension):
        data = event.get_data()
        if not re.match(r'^https?://', data):
            data = ''+ data
        
        webbrowser.open_new_tab(data)

        return RenderResultListAction([])

if __name__ == '__main__':
    OpenInBrowser().run()
