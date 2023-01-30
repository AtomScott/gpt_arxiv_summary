## Summary

# Summary: 
This paper introduces SoccerTrack, a dataset consisting of GNSS and bounding box tracking data annotated on video captured with a 8K-resolution fish-eye camera and a 4K-resolution drone camera. The dataset was used to evaluate the tracking accuracy between the GNSS, fish-eye camera and drone camera data. The data was collected using a fish-eye lens and drone camera, and then transformed into pitch coordinates. Furthermore, an object detector was trained for ball detection, and the IDs of each bounding box were estimated by performing ICP between the detections in fish-eye videos and annotated drone videos. The average tracking performance in fish-eye video resulted in a 14, and the drone video resulted in a 57. The paper suggests that the bias-corrected RMSE of location data in the fish-eye camera was more accurate than that in the GNSS.

# Experiments:
The data collected from the fish-eye and drone cameras were evaluated for tracking accuracy compared to GNSS data. The GNSS data was upsampled to the same frequency as the drone and fish-eye data, and the bias-corrected RMSE was calculated using the euclidean distance between the GNSS and drone data and that between the fish-eye and drone data. The average tracking performance in fish-eye video resulted in a 14, and the drone video resulted in a 57.

# Further reading:
The paper MOT16: A benchmark for multi-object tracking by IEEE/CVF Conference on Computer Vision and Pattern Recognition June 2021, the paper Soccer Video and Player Position Dataset by Peize Sun et al., the paper Pose estimation and tracking in soccer videos using a graph convolutional network by Zhongdao Wang et al., and the paper Multi-Object Tracking with OR-CNN: A 3D Region Proposal Network for Real-Time Object Tracking by Rui Zhao et al. are suggested for further reading.

# Glossary:
- GNSS: Global Navigation Satellite System
- LPS: Local Positioning System
- RMSE: Root Mean Squared Error
- ICP: Iterative Closest Point
- OSNet: Open-Set Network
- GFootball: Google Research Football

## Summary (Japanese)

# Summary
本論文では、8K解像度の魚眼レンズカメラと4K解像度のドローンカメラで撮影した映像にGNSSとバウンディングボックスのトラッキングデータを注釈したデータセット「SoccerTrack」を紹介します。このデータセットを用いて、GNSS、魚眼レンズカメラ、ドローンカメラのデータ間のトラッキング精度を評価しました。魚眼レンズとドローンカメラで収集したデータを、ピッチ座標に変換した。さらに、ボール検出のために物体検出器を学習させ、魚眼映像の検出値と注釈付きドローン映像の検出値との間でICPを行い、各バウンディングボックスのIDを推定した。魚眼映像の平均追跡性能は14、ドローン映像は57という結果になった。この論文では、魚眼レンズの位置データのバイアス補正RMSEがGNSSのそれよりも正確であったことを示唆している。

# 実験の様子
魚眼カメラとドローンから収集したデータをGNSSデータと比較し、追跡精度を評価した。GNSS データはドローンおよび魚眼データと同じ周波数にアップサンプリングし、GNSS とドローンのデータ間のユークリッド距離と魚眼とドローンのデータ間の距離を用いてバイアス補正した RMSE を算出した。魚眼映像の平均追尾性能は14、ドローン映像は57という結果になりました。

# さらに読む。
論文 MOT16: A benchmark for multi-object tracking by IEEE/CVF Conference on Computer Vision and Pattern Recognition June 2021、論文 Soccer Video and Player Position Dataset by Peize Sun et al、論文 Pose estimation and tracking in soccer videos using a graph convolutional network by Zhongdao Wang et al、論文 Multi-Object Tracking with OR-CNN:Rui Zhaoらによる論文「Multi-Oject Tracking with OR-CNN: A 3D Region Proposal Network for Real-Time Object Tracking」は、さらに詳しい情報を得ることができます。

# 用語解説
- GNSS：Global Navigation Satellite System（全地球衛星測位システム
- LPS: ローカルポジショニングシステム
- RMSE: 平均二乗誤差(Root Mean Squared Error)
- ICP：Iterative Closest Point（反復的最接近点）。
- OSNet：オープンセットネットワークオープンセットネットワーク
- GFootballGoogle Research Football：Googleリサーチフットボール

## Images
![img-131](outputs/soccertrack/img-131.png)

![img-127](outputs/soccertrack/img-127.png)

![img-122](outputs/soccertrack/img-122.png)

![img-136](outputs/soccertrack/img-136.png)

