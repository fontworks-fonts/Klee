[English](https://github.com/fontworks-fonts/Klee) /[日本語](README-JP.md) 

![KleeOne-Regular](./image_Klee-Regular.png)

![KleeOne-SemiBold](./image_Klee-SemiBold.png)

## クレー One

鉛筆やペンなどを使って書いた手書き風文字のような印象を与える楷書系硬筆体です。優しい雰囲気と、落ち着いたデザイン性から高級感を表現する書体です。楷書体や教科書体とは一味違う手書き風のイメージを持ち、本文組みに適した書体です。  
このフォントについての詳しい情報は[こちら](https://fontworks.co.jp/fontsearch/KleePro-M/)をご覧ください。


### フォントのダウンロード

以下のページより、ビルド済みのTrueTypeフォントをダウンロードできます。  

[最終リリース](https://github.com/fontworks-fonts/Klee/tree/master/fonts/ttf)


### ソースからのフォントのビルド手順

#### 要件

* [python3](https://www.python.org/)  
* [fontmake](https://github.com/googlefonts/fontmake/)
* [fonttools](https://github.com/fonttools/fonttools/)
* [ttfautohint](https://www.freetype.org/ttfautohint/doc/ttfautohint.html)  


#### フォントのビルド

ワーキングディレクトリ(カレントディレクトリ)を「Klee」フォルダへ変更し、**build.py**を実行します。

    $ python build.py

**--autohinting**コマンドラインオプションを指定すると、ttfautohintを使用してヒントを付与します。

    $ python build.py --autohinting

### ライセンス

* 個人利用・商用利用にかかわらずどなたでも無料でお使いいただけます。
* ゲームやアプリなどへの組み込みやwebフォントとしての利用も可能です。
* このフォントを使用し、派生フォントを作ることもできます。ただし、配布の際はSIL Open Font Licenseに基づいてリリースする必要があります。
* SILライセンスについて詳しくは[SIL Open Font License 1.1 日本語訳](https://licenses.opensource.jp/OFL-1.1/OFL-1.1.html)または同梱の「OFL.txt」(英語)をご確認ください。


### 収録文字

* [Adobe-Japan1-4](https://github.com/adobe-type-tools/Adobe-Japan1)の全グリフ  
* [GF Latin Core](https://github.com/googlefonts/gftools/tree/master/Lib/gftools/encodings/GF%20Glyph%20Sets#gf-latin-core)  


### 禁止行為

* 「SIL Open Font License Version 1.1」以外のライセンスで再配布すること。
* フォントファイル自体を単体で販売すること。
