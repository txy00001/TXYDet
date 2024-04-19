
# 基础环境
Ubuntu20.04<br>
PyTorch 1.13<br>
Python 3.8<br>

## 支持
backbone 支持 mobilenetv3、shufflenetv2、ghostnet、efficientnet，vovnet
neck 支持 FPN,PAN、FPN_Slim，PAN_Slim、BiFPN
head 支持 gfl、gfl v2(改进版)

# txydet可选组式
如：
EfficientNet + BiFPN + GFL
GhostNet + PAN + GFL
GhostNet + BiFPN + GFL
MobileNetV3 + PAN/PAN_Slim + GFLv2
ShuffleNetV2 + PAN/PAN_Slim + GFL

可以随意组合
还在持续更新...


关于EfficientDet优化版

EfficientNet + BiFPN + GFLv2

## 支持mosaic数据增强
4张图片大小相同，采用固定的中心点即4张图片，均分大小
load_mosaic：是否启动数据增强
mosaic_probability：有多少比例的数据采用mosaic数据增强
mosaic_area：GT bbox<该阈值则过滤掉

## gfl v2版本
能涨点0.2个百分点
可以从class txydetHead(GFLHead): # 在head里进行替换


# GhostNet分为完整版和精简版
配置文件 
ghostnet_full.yml 原始版
ghostnet_slim.yml 轻量版



### 单卡GPU训练命令
```
python tools/train.py config/txydet.yml
```

### 多卡GPU训练命令
```
python -m torch.distributed.launch --nproc_per_node=2 --master_port 30001 tools/train.py config/txydet.yml
```
## Inference video
可用于演示<br>
```
python ./demo/demo.py  'video' --path /media/ubuntu/data/1.mp4 --config config/efficientdet.yml --model ./workspace/efficientdet/model_best/model_best.pth
```


如果是分布式训练，可以在norm_cfg中
dict(type='BN', momentum=0.01,eps=1e-3, requires_grad=True)
type='BN'更改为 type='SyncBN'

## 说明
此项目框架借鉴了https://github.com/CycloneBoy/PPDetectionPytorch/tree/master/ppdettorch
https://github.com/RangiLyu/nanodet/tree/main/nanodet
https://github.com/ultralytics/yolov5


后续还会更新。。。

