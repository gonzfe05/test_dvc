from omegaconf import OmegaConf
import os
import json

def main() -> None:
    cfg = OmegaConf.load("params.yaml")
    print(cfg)
    os.makedirs('dvclive', exist_ok=True)
    with open("metrics.json") as f:
        json.dump({'param': cfg["some_param"]})

if __name__ == "__main__":
    main()
