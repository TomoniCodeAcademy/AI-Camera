# AIカメラとは？どうやって使うのか？
## AIカメラでできること
- 顔認識 (Face Recognition)
機能：特定の人の顔を学習して、相手が誰か？を判断する
学習：複数の人を学習可能
位置情報：不明
- 物の追跡 (Object Tracking)
機能：学習した物が画面内のどこに存在するかを探し出し、位置を返す
学習：追跡させたい対象を学習させる
位置情報：可能
制約：学習できる物、追跡できる物は一つに限られる
補足：ジェスチャーでLEGOを制御する場合、Object Trackingを使えば良いのだろうか？
- 対象物の認識 (Object Recognition)
機能：画面の中にどのような物（動物、家具、自転車等）があるかを特定する
20種類のObjectが学習済み
学習：不可
位置情報：不明
制約：新しい対象物を学習させることはできない
- 対象物の分類 (Object Classification)
機能：画面内の対象物（形状、モノ）がどの分類に属するかを判断する
学習：新しい対象物を学習させる。複数学習可能
位置情報：不明
補足：何もない状態を一つの対象物として学習させることで、どれにも当てはまらない場合にも正しい回答が得られる。テニスボール、サッカーボールの識別も可能(少しの違いでも識別できる)
- 色の識別(Color Recogniton)
機能：あらかじめ学習させた色を見つけ出す
学習：認識させたい色を学習させる。複数の色を学習させることが可能
位置情報：可能
補足：色をタグや目標物として利用することが可能
- ライントレース(Line Tracking)
機能：明るい背景の中の黒い線を見つけ出して、矢印（ベクトル？）で返却する
- 位置情報：可能（ベクトルで返却）
学習：可能だが何を学習する？(線の色を学習する？)
補足：縦線は検知できるが横線は検知できない
- タグ認識(Tag Recogniton)
機能：QRコードのようなタグ(AprilTag)を認識してIDを返却する
学習：認識させたいタグを学習させる。複数学習可能
位置情報：可能
制約：学習できるタグはAprilTagに限られるようである。
補足：目標物にタグを貼り付けることで、追いかける対象、運搬先、ゴール等を、LEGOカーに伝えることが可能になる

## プログラミング方法
Data's correspondent algorithm:

Data	Algorithm
```
0x00 0x00	ALGORITHM_FACE_RECOGNITION
0x01 0x00	ALGORITHM_OBJECT_TRACKING
0x02 0x00	ALGORITHM_OBJECT_RECOGNITION
0x03 0x00	ALGORITHM_LINE_TRACKING
0x04 0x00	ALGORITHM_COLOR_RECOGNITION
0x05 0x00	ALGORITHM_TAG_RECOGNITION
0x06 0x00	ALGORITHM_OBJECT_CLASSIFICATION
```

## 参考資料
開発元の資料、サンプルプロジェクト
- https://www.dfrobot.com/product-1922.html
- Huskylens Project
- https://learn.dfrobot.com/tag-489-1.html
- https://www.dfrobot.com/blog-tag-huskylens.html
- Huskylensの概要説明、使い方(Youtube)
- Huskylens概要説明
- Huskylens使い方説明
- Huskylensを制御するコマンド仕様書(GitHub)
- https://github.com/HuskyLens/HUSKYLENSArduino/blob/master/HUSKYLENS%20Protocol.md
- https://github.com/HuskyLens
