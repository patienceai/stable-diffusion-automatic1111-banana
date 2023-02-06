import torch
import modules.safe as safe
#from modules.timer import Timer
import webui
import dill
"""
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
"""
device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

def noop(*args, **kwargs):
    pass

#def load_model():
#    modules.sd_models.load_model()
#    return shared.sd_model

def register_model():
    global model
    try:
        from modules import shared, sd_hijack
        shared.sd_model = model
        sd_hijack.model_hijack.hijack(model)
    except:
        print("Failed to hijack model.")

def init():
    global model
    import modules.sd_models
    modules.sd_models.list_models()
    modules.sd_models.list_models = noop
    model = modules.sd_models.load_model()
    modules.sd_models.load_model = noop
    register_model()
   
