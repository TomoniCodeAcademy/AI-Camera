# AIカメラとは？どうやって使うのか？
## AIカメラ(HuskyLens)でできること
- 顔認識 (Face Recognition)
  - 機能：カメラに映る人が誰であるかを判断する
  - 学習：認識したい人の顔を学習させる。複数の人を学習可能
  - 位置情報：未確認
- 物の追跡 (Object Tracking)
  - 機能：学習した物が画面内のどこに存在するかを探し出し、位置を返す
  - 学習：追跡させたい対象を学習させる
  - 位置情報：取得可能
  - 制約：学習、追跡できる物は一つに限られる
  - 補足：ジェスチャーでLEGOを制御する場合、Object Trackingを使えば良いのか？
- 物の認識 (Object Recognition)
  - 機能：画面の中にどのような物（動物、家具、自転車等）があるかを特定する
  - 20種類の物が学習済み（プレ学習）
     - aeroplane, bicycle, bird, boat, bottle, bus, car, cat, chair, cow, dining table, dog, horse, motorbike, person, potted plant, sheep, sofa, train, TV   
  - 学習：物を認識させるには学習必要(学習させないと 対象物を認識してもblockのIDが0で返却される)
  - 位置情報：取得可能
  - 制約：あらかじめ学習した物（プレ学習）以外の別の種類は学習できない（鉛筆、ボール、カップ等は学習できない）
- 物の分類 (Object Classification)
  - 機能：カメラに映る物（形状、モノ）がどの分類に属するかを判断する
  - 学習：認識したい対象物を学習させる。複数学習可能
  - 位置情報：未確認
  - 補足：何もない状態を一つの対象物として学習させることで、どれにも当てはまらない場合にも正しい回答が得られる。テニスボール、サッカーボールの識別も可能(少しの違いでも識別できる)
- 色の認識(Color Recogniton)
  - 機能：あらかじめ学習させた色を画面の中から見つけ出す
  - 学習：認識させたい色を学習させる。複数の色を学習させることが可能
  - 位置情報：取得可能
  - 補足：色を目標物として利用することが可能（オレンジ色のボールを追いかける等の用途に使える）
- ライントレース(Line Tracking)
  - 機能：明るい背景の中の黒い線を見つけ出して、矢印（ベクトル？）で返却する
  - 位置情報：取得可能（ベクトルで返却）
  - 学習：可能だが何を学習する？(線の色を学習する？)
  - 補足：縦線は検知できるが横線は検知できない。だから、停止線は検知できない
- タグ認識(Tag Recogniton)
  - 機能：QRコードのようなタグ(AprilTag)を認識してIDを返却する
  - 学習：認識させたいタグを学習させる。複数学習可能
  - 位置情報：取得可能
  - 制約：学習できるタグはAprilTagに限られるようである。
  - 補足：目標物にタグを貼り付けることで、追いかける対象、運搬先、ゴール等を、LEGOカーに伝えることが可能になる

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
