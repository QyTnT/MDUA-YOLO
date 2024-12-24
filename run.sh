#python train.py --cfg models/yolov5s_SENet_kmeans.yaml --name yolov5s_Giou_SENet_kmeans
#python train.py --cfg models/yolov5s_CBAM_kmeans.yaml --name yolov5s_Giou_CBAM_kmeans

#python train.py --cfg models/yolov5s_llxw.yaml --name yolov5s_llxw.yaml
#python train.py --cfg models/hub/yolov5-fpn.yaml --name yolov5s-fpn
#python train.py --cfg models/hub/yolov5-bifpn.yaml --name yolov5s-bifpn

#python train.py --cfg models/yolov5s_llxw_kmeans.yaml --name yolov5s_llxw_kmeans
python train.py --cfg models/test.yaml --name 0418_  --batch-size 8 --rect False
#python train.py --cfg models/yolov5l_llxw_kmeans_CBAM.yaml --name yolov5l_llxw_k_CBAM --batch-size 8
#python train.py --cfg models/yolov5s.yaml --name ccpd --batch-size 8 --data ccpd.yaml --epochs 50