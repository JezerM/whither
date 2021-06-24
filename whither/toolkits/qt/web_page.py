from PyQt5.QtWebEngineWidgets import QWebEnginePage

class WebPage(QWebEnginePage):

    def javaScriptConsoleMessage(self, level: QWebEnginePage.JavaScriptConsoleMessageLevel, message: str, lineNumber: int, sourceID: str):
        if sourceID == "":
            sourceID = "console"

        typeLog = ""
        if level == QWebEnginePage.JavaScriptConsoleMessageLevel.ErrorMessageLevel:
            typeLog = "[ERROR]"
        elif level == QWebEnginePage.JavaScriptConsoleMessageLevel.WarningMessageLevel:
            typeLog = "[WARNING]"
        elif level == QWebEnginePage.JavaScriptConsoleMessageLevel.InfoMessageLevel:
            return
        else:
            return

        print("{typ} {source} {line}: {msg}".format(typ = typeLog, msg = message, source = sourceID, line = lineNumber))
