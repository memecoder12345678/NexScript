import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QFileDialog, QAction
from PyQt5.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor
from PyQt5.QtCore import QRegExp
GLOBAL_SYMBOLS = ['NULL', 'FALSE', 'TRUE', 'MATH_PI', 'ECHO', 'INPUT_FLOAT', 'INPUT', 'INPUT_INT', 'CLEAR', 'CLS', 'IS_NUM', 'IS_STR', 'IS_LIST', 'IS_FUNC', 'APPEND', 'POP', 'EXTEND', 'LEN', 'RUN']
KEYWORDS = ['SET', 'AND', 'OR', 'NOT', 'IF', 'ELIF', 'ELSE', 'FOR', 'TO', 'STEP', 'LOOP', 'FUNC', 'THEN', 'END', 'RETURN', 'CONTINUE', 'BREAK']
class NexScriptHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.highlightingRules = []
        keywordFormat = QTextCharFormat()
        keywordFormat.setForeground(QColor('#F9CF60'))
        keywordPatterns = [f'\\b{keyword}\\b' for keyword in KEYWORDS]
        for pattern in keywordPatterns:
            rule = (QRegExp(pattern), keywordFormat)
            self.highlightingRules.append(rule)
        braceFormat = QTextCharFormat()
        braceFormat.setForeground(QColor('#FFCB6B'))
        bracePatterns = ['\\{', '\\}', '\\[', '\\]', '\\(', '\\)']
        for pattern in bracePatterns:
            rule = (QRegExp(pattern), braceFormat)
            self.highlightingRules.append(rule)
        stringFormat = QTextCharFormat()
        stringFormat.setForeground(QColor('#FF9E9E'))
        stringPattern = '"[^"]*"'
        rule = (QRegExp(stringPattern), stringFormat)
        self.highlightingRules.append(rule)
        integerFormat = QTextCharFormat()
        integerFormat.setForeground(QColor('#9E9EFF'))
        self.highlightingRules.append((QRegExp('\\b\\d+\\b'), integerFormat))
        floatFormat = QTextCharFormat()
        floatFormat.setForeground(QColor('#9E9EFF'))
        self.highlightingRules.append((QRegExp('\\b\\d*\\.\\d+\\b'), floatFormat))
        globalSymbolFormat = QTextCharFormat()
        globalSymbolFormat.setForeground(QColor('#90CFA5'))
        globalSymbolPatterns = [f'\\b{symbol}\\b' for symbol in GLOBAL_SYMBOLS]
        for pattern in globalSymbolPatterns:
            rule = (QRegExp(pattern), globalSymbolFormat)
            self.highlightingRules.append(rule)
        commentFormat = QTextCharFormat()
        commentFormat.setForeground(QColor('lightgreen'))
        self.highlightingRules.append((QRegExp('\\$(?=(?:[^"]*"[^"]*")*[^"]*$)[^\n]*'), commentFormat))
    def highlightBlock(self, text):
        for pattern, fmt in self.highlightingRules:
            expression = QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, fmt)
                index = expression.indexIn(text, index + length)
class CodeEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_file = None
        self.initUI()
    def initUI(self):
        self.setWindowTitle('NexScript Code Editor')
        self.setGeometry(100, 100, 800, 600)
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)
        self.editor.setStyleSheet("background-color: #2E2E2E; color: #D4D4D4;")
        self.highlighter = NexScriptHighlighter(self.editor.document())
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')
        open_action = QAction('Open', self)
        open_action.setShortcut('Ctrl+O')
        open_action.setStatusTip('Open a file')
        open_action.triggered.connect(self.open_file)
        create_action = QAction('New File', self)
        create_action.setShortcut('Ctrl+N')
        create_action.setStatusTip('Create a new file')
        create_action.triggered.connect(self.new_file)
        save_as_action = QAction('Save As', self)
        save_as_action.setShortcut('Ctrl+Shift+S')
        save_as_action.setStatusTip('Save the file as')
        save_as_action.triggered.connect(self.save_as_file)
        save_action = QAction('Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.setStatusTip('Save the file')
        save_action.triggered.connect(self.save_file)
        exit_action = QAction('Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit the application')
        exit_action.triggered.connect(self.close)
        file_menu.addAction(create_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addAction(save_as_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)
    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open File')
        if file_name:
            with open(file_name, 'r') as file:
                self.editor.setText(file.read())
        self.current_file = file_name
        self.update_window_title()
    def save_file(self):
        if self.current_file:
            with open(self.current_file, 'w') as file:
                file.write(self.editor.toPlainText())
        else:
            self.save_as_file()
    def save_as_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, 'Save File As')
        if file_name:
            with open(file_name, 'w') as file:
                file.write(self.editor.toPlainText())
            self.current_file = file_name
            self.update_window_title()
    def new_file(self):
        self.editor.clear()
        self.current_file = None
        self.update_window_title()
    def update_window_title(self):
        if self.current_file:
            self.setWindowTitle(f'NexScript IDE - File {self.current_file}')
        else:
            self.setWindowTitle('NexScript IDE - New File')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = CodeEditor()
    editor.show()
    sys.exit(app.exec_())
