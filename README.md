# FileManager

英語はDeepLで翻訳

## 環境

https://img.shields.io/badge/python-3.10.5-33CCFF

### pip

- customtkinter
- CTkListBox
  - https://github.com/Akascape/CTkListbox

## 目的(Purpose)

dataという名前のディレクトリ内部に存在するファイルにラベルをつけて管理する機能

Ability to label and manage files that reside inside a directory named data

## デザイン(Design)

詳細は決めていないが，上側にツールバー，左サイドにdataディレクトの中にある全ファイルを表示(サブディレクトリの内も), メイン画面にはラベル付きのファイル一覧やファイルの中身を確認できるものを作成
vscodeのようなよく親しんだエディタに近いUIになるかと思う

The details have not been decided yet, but I'd like to have a toolbar on the top, all files in the data directory on the left side (including those in subdirectories), and a main screen with a list of files with labels and a view of the contents of the files.
The UI will be similar to a familiar editor like vscode.

## 機能(Function)

- ツールバー
  - 未計画
- サイドメニュー
  - ディレクトリを選択したら, サブディレクトリの中身を表示
  - ファイルを選択したら，メイン画面にファイルの中身を表示
- メイン画面
  - ファイル一覧の表示(サイドメニューと同じ機能)
  - ラベルによるファイルのソート
  - 開いているファイル(ファイルの中身見るための)タブの消去

- Toolbar
  - Not planned yet
- Side menu
  - When a directory is selected, the contents of its subdirectories are displayed
  - When a file is selected, the contents of the file are displayed on the main screen
- Main Screen
  - Display of file list (same function as side menu)
  - Sort files by label
  - Clear tabs for open files (to see contents of files)
 
## 参考文献(Reference)

- https://nazmul-ahsan.medium.com/how-to-organize-multi-frame-tkinter-application-with-mvc-pattern-79247efbb02b
- https://www.pythontutorial.net/tkinter/tkinter-mvc/
- https://github.com/TomSchimansky/CustomTkinter



