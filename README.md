# ASR project barebones

## Installation guide

1. `pip install -r ./requirements.txt`
2. From http://www.openslr.org/11/ download 3-gram.arpa.gz and librispeech-vocab.txt.
3. To lowercase `python hw_asr/text_encoder/fix_vocab.py` and `python hw_asr/text_encoder/lower_model.py`.
4. If you want to test my model, download it from https://drive.google.com/file/d/1QrSsx56V5YNjGHUBWy6CIRVbNbjKWUpJ/view?usp=share_link , name it `checkpoint.pth` and place to the directory `default_test_model/`.

## Train

1. `python train.py --config hw_asr/configs/config2.json`

## Test

1. `python test.py -c default_test_config.json -r default_test_model/checkpoint.pth`

## Wandb report

1. You can check my wandb report (only on Russian) and wandb project via https://wandb.ai/tgritsaev/asr_project/reports/DLA-HW-1--Vmlldzo1NzY3NjA5?accessToken=kotkj5oyzomf2d2g1f40mczdnpirwvuw1f538zx9k491g1cfh3wg9iwhsb65o054.

