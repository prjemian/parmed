"""
https://pythonspot.com/pyqt5-treeview/
"""

import sys

from PyQt5 import QtWidgets

import pyqparamwidget as qpw

sampler = {
    "tiled": {
        "server": {
            "settings_file": qpw.ParameterItemText(label="settings file", value="~/.config/settings.ini"),
            "catalog": qpw.ParameterItemText(label="catalog", value="bluesky_data"),
            "url": qpw.ParameterItemText(label="url", value="http://localhost"),
        },
    },
    "UI": {
        "plotting": {
            "autoplot": qpw.ParameterItemCheckbox(
                label="autoplot",
                value=True,
                tooltip="Plot when the run is selected.",
            ),
            "autoselect": qpw.ParameterItemCheckbox(
                label="autoselect",
                value=True,
                tooltip="Automatically select the signals to plot.",
            ),
            "colors": qpw.ParameterItemChoice(label="colors", value="", choices=["", "r", "b", "g", "k"]),
        },
    },
}
# print(sampler)


class DemoTreeWidget(QtWidgets.QTreeWidget):
    """
    Demo
    """

    def __init__(self, *args, parms={}, headings=["heading"], **kwargs):
        from PyQt5.QtWidgets import QTreeWidgetItem

        super().__init__(*args, **kwargs)
        self.setColumnCount(len(headings))
        self.setHeaderLabels(headings)
        self.setSortingEnabled(True)

        def isParmsDict(obj):
            if isinstance(obj, dict):
                for v in obj.values():
                    if not isinstance(v, qpw.ParameterItemBase):
                        return False
                return True
            return False

        def build_subtree(parent, subparms):
            if not isParmsDict(subparms):
                for k, v in subparms.items():
                    item = QTreeWidgetItem(None, [k])
                    parent.addChild(item)
                    build_subtree(item, v)

        for k, v in parms.items():
            item = QTreeWidgetItem(None, [k])
            self.addTopLevelItems([item])
            build_subtree(item, v)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = DemoTreeWidget(None, parms=sampler)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
