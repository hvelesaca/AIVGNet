"""import torch
from lib.mamba_unet import VisionMambaPVTUNet

device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = VisionMambaPVTUNet(pretrained=False).to(device)
model.eval()

dummy_input = torch.randn(1, 3, 256, 256).to(device)
torch.onnx.export(model, dummy_input, "vision_mamba.onnx", opset_version=12)
"""
import torch
from torchinfo import summary
from lib.mamba_unet import VisionMambaPVTUNet

device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = VisionMambaPVTUNet(pretrained=False).to(device)

summary(model, input_size=(1, 3, 256, 256), depth=4, col_names=["input_size", "output_size", "num_params", "kernel_size", "mult_adds"])
