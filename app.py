import torch
import modules.safe as safe

torch.load = safe.unsafe_torch_load

class Identity(torch.nn.Module):
    def forward(self, x):
        return x

def init():
    global model
    model = Identity()

