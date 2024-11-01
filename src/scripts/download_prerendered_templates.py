import os

from gdown import download
    
from src.utils.utils import load_config, DotDict


def download_templates(config: DotDict) -> None:
    """ Download the prerendered templates from a Google Drive and extract them to `templates_sir` specified in config """

    os.makedirs(config.data.temp_dir, exist_ok=True)
    os.makedirs(config.data.templates_dir, exist_ok=True)

    zip_path = os.path.join(config.data.temp_dir, "templates.zip")

    if os.path.exists(zip_path):
        print(f"Templates have already been downloaded at `{zip_path}`, continuing without downloading them again")
    else:
        download(config.data.prerendered_templates_url, zip_path, quiet=False, fuzzy=True) # use "pip install -U --no-cache-dir gdown --pre" in case gdown refuses because it is not public link
    
    # Remove the empty top directory of the zip file in a somewhat convoluted way
    tmp_templates_dir = os.path.join(config.data.temp_dir, "temp_unzip")
    os.system(f"unzip -q {zip_path} -d {tmp_templates_dir} && mv {os.path.join(tmp_templates_dir, '*','*')} {config.data.templates_dir} && rm -r {tmp_templates_dir}")


if __name__ == "__main__":
    # TODO: Argparse, but not really a priority
    conf = load_config(f"config.yaml")
    download_templates(conf)
