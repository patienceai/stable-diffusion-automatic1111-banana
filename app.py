import torch
import modules.safe as safe
import modules.shared as shared
import modules.sd_models

from modules.timer import Timer
import dill

original_save = torch.save
original_load = safe.unsafe_torch_load

def save(*args, **kwargs):
    kwargs['pickle_module'] = dill
    return original_save(*args, **kwargs)

def load(*args, **kwargs):
    kwargs['pickle_module'] = dill
    return original_load(*args, **kwargs)

torch.save = save
torch.load = load

device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

def noop(*args, **kwargs):
    pass

def load_model():
    modules.sd_models.load_model()
    return shared.sd_model

def init():
    from modules import sd_hijack
    global model
    shared.cmd_opts.no_hashing = True
    modules.sd_models.list_models()
    modules.sd_models.list_models = noop
    model = load_model()
    modules.sd_models.load_model = noop
    sd_hijack.model_hijack.hijack(model)
    shared.sd_model = model
