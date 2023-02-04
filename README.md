
# 🍌 Stable Diffusion WebUI for banana (Stable Diffusion 1.5)

Run the API for AUTOMATIC1111's [Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) on banana.dev with **Stable Diffusion 1.5** included.

Supports features not available in other Stable Diffusion templates, such as:

* [Prompt emphasis](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Features#attentionemphasis)
* [Unlimited prompt length](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Features#infinite-prompt-length)

Please note that this deployment provides an API only and does not include the WebUI's user interface.

## Instant Deploy

[See how to deploy in seconds](https://app.banana.dev/templates/patienceai/stable-diffusion-1.5-automatic1111).

## Model Inputs

### txt2img example

```
{
  "endpoint": "txt2img",
  "params": {
    "prompt": "an astronaut riding a (horse:motorcycle:0.5) on the moon",
    "cfg_scale": 7.5,
    "steps": 25
  }
}
```

Output:

```
{
  "images": [
    "<base64 image>"
  ]
}
```

### img2img example

```
{
  "endpoint": "img2img",
  "params": {
    "prompt": "an astronaut riding a horse on the moon in anime style",
    "cfg_scale": 7.5,
    "steps": 25,
    "init_images": [
        "<base64 image>"
    ]
  }
}
```

Output:

```
{
  "images": [
    "<base64 image>"
  ]
}
```

### Interrogation example

```
{
  "endpoint": "interrogate",
  "params": {
    "image": "<base64 image>"
  }
}
```

Output:

```
{
  "caption": "<interrogate result>"
}
```

### Other endpoints

For full documentation of available endpoints and their parameters, run a local copy of the Stable Diffusion WebUI and visit http://localhost:7860/docs. Not all endpoints have been tested with this banana deployment. Please report any issues you encounter.

Model inputs should be in the following format:

```
{
  "endpoint": "<endpoint>",
  "params": {
    ...
  }
}
```