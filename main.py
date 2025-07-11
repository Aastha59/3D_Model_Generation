from fastapi import FastAPI, Query
from pydantic import BaseModel
import torch
import uuid
from shap_e.models.download import load_model
from shap_e.diffusion.text_to_3d import text_to_latent
from shap_e.util.notebooks import decode_latent_mesh
from fastapi.responses import FileResponse

app = FastAPI()

# Load models only once
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
text_model = load_model("text300M", device)
renderer = load_model("transmitter", device)

@app.get("/")
def root():
    return {"message": "3D Model Generator API is live."}

@app.get("/status")
def status():
    return {"model": "Shap-E", "version": "OpenAI", "device": str(device)}

@app.get("/generate3d")
def generate_3d(prompt: str = Query(..., description="Enter your 3D prompt")):
    try:
        # Generate latent from text
        latent = text_to_latent(
            model=text_model,
            tokenizer=None,
            prompt=prompt,
            guidance_scale=15.0,
            num_inference_steps=64,
            device=device,
        )

        # Decode to mesh
        mesh = decode_latent_mesh(renderer, latent)

        # Save unique .glb file
        filename = f"{uuid.uuid4().hex}.glb"
        mesh.save_glb(open(filename, "wb"))

        return FileResponse(path=filename, filename=filename, media_type="model/gltf-binary")

    except Exception as e:
        return {"error": str(e)}
