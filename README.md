## Install and How to run
    pip install -r pip.txt
    python -b <bin_size> -n <number_of_item> -d <distribution_id> 

## ファイル構成
- main.py
    + 実行用ファイルです。実際の実行の部分を制御しており、実行時間の測定を行っています。
- problem.py
    + ビンパッキング問題とその双対問題を解くための関数が定義されています。
- distribution.py
    + アイテムの分布を決める関数が定義されています。

## 実行時
- サイズ bin_size のビンに 1〜bin_size までのアイテムを numver_of_item 個を詰めることを考えるビンパッキング問題を解きます。
- アイテムサイズを増やしながら実行したい場合、main.sh や main.fish を利用すると便利です。
    - seq コマンドの引数やリダイレクト先を調整して実行してください。

## omake
- scripts に格納されているファイルは手計算で列生成法を解いた際の補助ツール群です。
    - binpacking.py: TEMP-n として扱われる部分問題を解く際に使用します。
    - knapsack.py: ループの終了条件を満たすかどうかを判別する 0-1 ナップザック問題を解く際に使用します。
    - binpacking_min.py: ループが終了した際に、最後に最適解を求める際に使用します。