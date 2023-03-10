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
??????????????????8K???????????????????????????????????????4K?????????????????????????????????????????????????????????GNSS??????????????????????????????????????????????????????????????????????????????????????????????????????SoccerTrack???????????????????????????????????????????????????????????????GNSS????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????ICP???????????????????????????????????????????????????ID??????????????????????????????????????????????????????14????????????????????????57?????????????????????????????????????????????????????????????????????????????????????????????????????????RMSE???GNSS??????????????????????????????????????????????????????????????????

# ???????????????
????????????????????????????????????????????????????????????GNSS??????????????????????????????????????????????????????GNSS ??????????????????????????????????????????????????????????????????????????????????????????????????????GNSS ????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????? RMSE ??????????????????????????????????????????????????????14????????????????????????57????????????????????????????????????

# ??????????????????
?????? MOT16: A benchmark for multi-object tracking by IEEE/CVF Conference on Computer Vision and Pattern Recognition June 2021????????? Soccer Video and Player Position Dataset by Peize Sun et al????????? Pose estimation and tracking in soccer videos using a graph convolutional network by Zhongdao Wang et al????????? Multi-Object Tracking with OR-CNN:Rui Zhao?????????????????????Multi-Oject Tracking with OR-CNN: A 3D Region Proposal Network for Real-Time Object Tracking??????????????????????????????????????????????????????????????????

# ????????????
- GNSS???Global Navigation Satellite System????????????????????????????????????
- LPS: ?????????????????????????????????????????????
- RMSE: ??????????????????(Root Mean Squared Error)
- ICP???Iterative Closest Point??????????????????????????????
- OSNet?????????????????????????????????????????????????????????????????????????????????
- GFootballGoogle Research Football???Google??????????????????????????????

## Images
![img-131](outputs/soccertrack/img-131.png)

![img-127](outputs/soccertrack/img-127.png)

![img-122](outputs/soccertrack/img-122.png)

![img-136](outputs/soccertrack/img-136.png)

