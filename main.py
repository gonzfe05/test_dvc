from omegaconf import OmegaConf
import os
import json

def main() -> None:
    cfg = OmegaConf.load("params.yaml")
    print(cfg)
    os.makedirs('dvclive', exist_ok=True)
    with open("dvclive/metrics.json", "w") as f:
        json.dump({'param': cfg["run"]["some_param"]}, f)

if __name__ == "__main__":
    main()
