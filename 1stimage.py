from diffusers import DiffusionPipeline
import PIL

# Load the pre-trained Stable Diffusion model optimized for MPS (Apple Silicon)
pipe = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5").to("mps")
pipe.enable_attention_slicing()

prompt = "a photo of an astronaut riding a horse on mars"

# Perform a warm-up pass if this is your first time running the model or if you're experiencing performance issues.
# This step is generally recommended for PyTorch on MPS to optimize subsequent inference calls.
_ = pipe(prompt, num_inference_steps=1)

# Generate the image with the desired number of inference steps. The default is used if not specified.
image = pipe(prompt).images[0]

# Saving the image
image.save("astronaut_rides_horse_on_mars.png")
