import os
import yaml


class Config:
    def __init__(self) -> None:
        self.config = None
        self.load_config()

    def load_config(self) -> None:
        with open('config.yaml', 'r') as file:
            self.config = yaml.safe_load(file)
            if(os.environ.get('MODE', None)):
                print(self.config)

    def get_config(self) -> dict:
        return self.config