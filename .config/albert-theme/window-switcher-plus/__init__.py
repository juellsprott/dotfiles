import time
import subprocess
import os
import traceback

from collections import namedtuple
from albert import *

try:
    from pypinyin import lazy_pinyin
except:
    lazy_pinyin = lambda x: [x]

md_iid = '2.0'
md_version = "1.0"
md_name = "WindowSwitcher"
md_description = "Window switcher under Linux X-server"
md_license = "MIT"
md_url = ""
md_maintainers = "@hereisok"

Window = namedtuple("Window", ["wid", "desktop", "wm_class", "host", "wm_name"])

image_app_mapping = {
    "jetbrains-idea-ce": "idea",
    "jetbrains-pycharm-ce": "pycharm",
    "dolphin": "system-file-manager",
    "DesktopEditors": "com.onlyoffice.DesktopEditors",
    "code": "vscode",
    "clash-for-windows": "clash"
}

_sim_key_mapping = {
    "java": ["idea"],
    "min": ["tilix"]
}

_sort_maps = {}
_current_user = os.getlogin()


class Plugin(PluginInstance, TriggerQueryHandler):

    def __init__(self):
        TriggerQueryHandler.__init__(
            self,
            id=md_id,
            name=md_name,
            description=md_description,
            defaultTrigger=''
        )
        PluginInstance.__init__(self, extensions=[self])

    def handleTriggerQuery(self, query):
        start_time = time.time()
        try:
            for item in _handleQuery(query):
                query.add(item)
        except:
            error(traceback.format_exc())
        finally:
            debug(f"execute:{query.string}. cost: {round((time.time() - start_time) * 1000, 3)} ms ")


_icons = {}

for root, dirs, files in os.walk("/usr/share/icons"):
    for file_name in files:
        file_path = os.path.join(root, file_name)
        _app_name = file_name.replace(".svg", "").replace(".png", "")
        _icons.setdefault(_app_name, [])
        _icons[_app_name].append(f'file:{file_path}')

for root, dirs, files in os.walk(f"/home/{_current_user}/.local/share/icons"):
    for file_name in files:
        file_path = os.path.join(root, file_name)
        _app_name = file_name.replace(".svg", "").replace(".png", "")
        _icons.setdefault(_app_name, [])
        _icons[_app_name].append(f'file:{file_path}')

for root, dirs, files in os.walk(f"/home/{_current_user}/.local/share/JetBrains/Toolbox/apps/"):
    for file_name in files:
        file_path = os.path.join(root, file_name)
        _app_name = file_name.replace(".svg", "").replace(".png", "")
        _icons[_app_name] = [f'file:{file_path}']



def findIcons(app_name):
    if _name := image_app_mapping.get(app_name):
        app_name = _name
    return _icons.get(app_name) or []


def _match(keys, matchs):
    for key in keys:
        if any(key in match for match in matchs):
            return True
    return False

_cache_key = ""
_cache_value = None
_cache_time = None

def _fetch_wmctrl_results(stripped_key) -> list[Window]:
    global _cache_key, _cache_value, _cache_time
    if _cache_key and stripped_key.startswith(_cache_key) and (time.time() - _cache_time < 5):
        _cache_value = _cache_value
    else:
        _cache_key = stripped_key
        _cache_value = subprocess.check_output(["wmctrl", "-l", "-x"]).splitlines()
        _cache_time = time.time()

    resp = []
    for line in _cache_value:
        try:
            win_id, desktop, rest = line.decode().split(None, 2)
            win_class, rest = rest.split('  ', 1)
            host, title = rest.strip().split(None, 1)
            resp.append(Window(win_id, desktop, win_class, host, title))
        except:
            continue

    resp.sort(key=lambda x: _sort_maps.get(x.wid) or 0, reverse=True)
    return resp


def executeSelect(win_id):
    _sort_maps[win_id] = time.time()
    subprocess.check_call(["wmctrl", "-i", "-a", win_id])


def _handleQuery(query):
    stripped = query.string.strip().lower()
    if not stripped:
        return []

    target_keys = [stripped, *(_sim_key_mapping.get(stripped) or [])]

    results = []
    for win in _fetch_wmctrl_results(stripped):
        try:
            win_instance, win_class = win.wm_class.replace(" ", "-").split(".", 1)
        except:
            continue

        matches = [
            win_instance.lower(),
            win_class.lower(),
            win.wm_name.lower(),
            "".join(lazy_pinyin(win_instance)),
            "".join(lazy_pinyin(win_class)),
            "".join(lazy_pinyin(win.wm_name)),
        ]

        if not _match(target_keys, matches):
            continue
            
        iconPaths = findIcons(win_instance) or findIcons(win_class.lower())

        subtext = win_class.lower()
        if not iconPaths:
            subtext += f" ({win_instance}.image_not_found)"

        results.append(
            StandardItem(
                id=f"WindowSwitcher:{win.wm_class}",
                text=win.wm_name,
                subtext=subtext,
                iconUrls=iconPaths,
                actions=[
                    Action(
                        "SwitchWindow", "SwitchWindow", lambda x=win.wid: executeSelect(x),
                    ),
                ],
            )
        )
    return results
