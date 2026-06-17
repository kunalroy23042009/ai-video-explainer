import click
from pipeline import VideoPipeline
from config import config
import os

@click.command()
@click.option("--prompt", "-p", required=True, help="Topic or question to explain")
@click.option("--output", "-o", default=None, help="Output video file path")
@click.option("--provider", default=None, help="Video provider override (aimlapi|stub)")
def main(prompt: str, output: str, provider: str):
    """AI Video Explainer — turn any prompt into an animated educational video."""
    if provider:
        config.VIDEO_PROVIDER = provider

    os.makedirs(config.OUTPUT_DIR, exist_ok=True)
    output_path = output or os.path.join(config.OUTPUT_DIR, "explainer.mp4")

    click.echo(f"🎬 Generating explainer video for: {prompt}")
    pipeline = VideoPipeline()
    result = pipeline.run(prompt=prompt, output_path=output_path)
    click.echo(f"✅ Video saved to: {result}")

if __name__ == "__main__":
    main()
