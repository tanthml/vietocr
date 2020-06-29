import torch
from torch import nn

from vietocr.model.vgg import CNN
from vietocr.model.resnet import Resnet50

class CNN(nn.Module):
    def __init__(self, backbone, *args, **kwargs):
        if backbone == 'vgg':
            self.model = CNN(*args, **kwargs)
        elif backbone == 'resnet':
            self.model = Resnet50(*args, **kwargs)

    def forward(self, x):
        return self.model(x)
