import torch
import modules.safe as safe
import modules.shared as shared
import modules.sd_models
from modules.timer import Timer

torch.load = safe.unsafe_torch_load
device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

def noop(*args, **kwargs):
    pass

def get_checkpoint_info():
    return list(modules.sd_models.checkpoints_list.values())[0]

def load_weights():
    checkpoint = get_checkpoint_info()
    return modules.sd_models.get_checkpoint_state_dict(checkpoint, Timer())

def init():
    global model
    modules.sd_models.list_models()
    modules.sd_models.list_models = noop
    model = load_weights()

def apply_weights():
    global model
    checkpoint = get_checkpoint_info()
    modules.sd_models.checkpoints_loaded[checkpoint] = model
