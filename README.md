# detect_human_chime
  
## 概要  
  
ロボットシステム学の課題2で作成したROSを用いた人感チャイムです。  
USBカメラとOpenCVを用いて人を検出し、コンビニやレストランの入口のチャイムのような音を鳴らします。
  
---  
  
## 動作環境
  
以下の環境で動作を確認しています。  
- ROS Melodic  
　- OS: Ubuntu 18.04.5 LTS  
　- ROS Distribution: Melodic Morenia 1.14.3  
- [usb-cam](http://wiki.ros.org/usb_cam)  
- [OpenCV (version 3.4.3)](https://opencv.org/)  
- python 2.7.17  
  
また、USBカメラは[logicool c270n](https://www.logicool.co.jp/ja-jp/product/hd-webcam-c270n)を用いて動作を確認しています。  
  
---
  
## 環境構築  
  
1. 本パッケージをインストールします。  
  
```sh
cd ~/catkin_ws/src  
git clone https://github.com/Dansato1203/detect_human_chime.git  
cd ~/catkin_ws
catkin_make
```  
  
2. pythonでサウンドを扱うため、playsoundをインストールします。  
```sh
pip install playsound
```
3. usb-camをインストールします。  
```sh
sudo apt-get update
sudo apt-get install ros-melodic-usb-cam
```
  
---
  
## 実行方法  
  
1. USBカメラのデバイス番号を確認します。
```sh
ls dev/video*
```

2. usb-camを立ち上げます。  
```sh
roslaunch detect_human_chime usb_cam.launch  
```
  
3. 本パッケージのチャイムを鳴らすサンプルコードを実行します。  
チャイム音が違う３つのコードを準備しています。どれか一つを実行してください。  
```sh
rosrun detect_human_chime 01_chime.py
```
  
4. 本パッケージの人を検知するサンプルコードを実行します。  
```sh
rosrun detect_human_chime detect_human.py
```
  
---
  
### 注意点
  
実行する場合、各サンプルコード内の下記部分のファイルまでのパスを自分の環境に合わせ変更してください。  
  
- 01_chime.py (02,03も同様)  
`playsound("/home/dan/catkin_ws/src/detect_human_chime/scripts/konnbini.mp3")`  
  
- detect_human.py  
`faceCascade = cv2.CascadeClassifier('/home/dan/catkin_ws/src/detect_human_chime/scripts/haarcascade_frontalface_alt2.xml')`  
  
---
  
## LICENSE
This repository is licensed under The BSD 3-Clause License, see [LICENSE](https://github.com/Dansato1203/detect_human_chime/blob/master/LICENSE).  
  
The sample chime in this repository is from [OtoLogic](https://otologic.jp/).  See [here](https://otologic.jp/free/license.html) for details.
