import copy
from .ghostnet import GhostNet_slim, GhostNet_full
from .shufflenetv2 import ShuffleNetV2
from .mobilenetv2 import MobileNetV2
from .mobilenetv3 import MobileNetV3_Small
from .efficientnet import EfficientNet
from .vovnet import VoVNet

def build_backbone(cfg):
    backbone_cfg = copy.deepcopy(cfg)
    name = backbone_cfg.pop('name')
    if name == 'MicroNet':
        pass
    elif name == 'VovNet':
        pass
    elif name == 'ShuffleNetV2':
        return ShuffleNetV2(**backbone_cfg)
    elif name == 'GhostNet_slim':
        return GhostNet_slim(**backbone_cfg)
    elif name == 'GhostNet_full':
            return GhostNet_full(**backbone_cfg)

    elif name == 'MobileNetV2':
        return MobileNetV2(**backbone_cfg)
    elif name == 'MobileNetV3_Small':
        return MobileNetV3_Small(**backbone_cfg)
    elif name == 'EfficientNet':
            return EfficientNet(**backbone_cfg)

    else:
        raise NotImplementedError

