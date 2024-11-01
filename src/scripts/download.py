import os

from src.utils.utils import load_config, DotDict


def download_dataset(config: DotDict, dataset_name: str) -> None:
    """ 
    Download an unzip a dataset into the datasets dir specified in the config file. 
    See: https://bop.felk.cvut.cz/datasets/ for supported datasets 
    """
    dataset_dir         = os.path.join(config.data.datasets_dir, dataset_name)
    download_base_url   = os.path.join(config.data.data_url, dataset_name, dataset_name)
    temp_dir_base_path  = os.path.join(config.data.temp_dir, dataset_name)

    os.system(f"wget {download_base_url}_base.zip       -P {config.data.temp_dir}")
    os.system(f"wget {download_base_url}_models.zip     -P {config.data.temp_dir}")
    os.system(f"wget {download_base_url}_test_all.zip   -P {config.data.temp_dir}")

    os.system(f"unzip {temp_dir_base_path}_base.zip     -d {dataset_dir}")
    os.system(f"unzip {temp_dir_base_path}_models.zip   -d {dataset_dir}")
    os.system(f"unzip {temp_dir_base_path}_test_all.zip -d {dataset_dir}")


def download_datasets() -> None:
    # TODO: Argparse config name
    config = load_config("config.yaml")

    for dataset_name in config.data.datasets:
        print(f"=== Downloading dataset '{dataset_name}' ===")
        download_dataset(config, dataset_name)


if __name__ == "__main__":
    download_datasets()
