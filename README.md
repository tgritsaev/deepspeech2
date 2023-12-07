# Automatic speech recognition with DeepSpeech2

Implementation is based on the [Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](https://arxiv.org/pdf/1512.02595.pdf) article.

The model recognizes speech in audio.

You can read the original [statement](https://github.com/XuMuK1/dla2023/tree/2023/hw1_asr).

## Installation guide

1. Install libraries
```shell
pip3 install -r ./requirements.txt
```
2. Download from http://www.openslr.org/11/ `3-gram.arpa.gz` and `librispeech-vocab.txt`
3. Prepare vocab and model for using
```shell
python3 hw_asr/text_encoder/fix_vocab.py
python3 hw_asr/text_encoder/lower_model.py
```
4. In order to check solution quality, you can download my final checkpoint from the [google disc](https://drive.google.com/file/d/1QrSsx56V5YNjGHUBWy6CIRVbNbjKWUpJ/view?usp=share_link).

## Train
```shell
python train.py --config hw_asr/configs/config2.json
```

## Test
```shell
python test.py -c default_test_config.json -r default_test_model/checkpoint.pth
```

## Wandb report
You can read my wandb [report](https://wandb.ai/tgritsaev/asr_project/reports/DLA-HW-1--Vmlldzo1NzY3NjA5?accessToken=kotkj5oyzomf2d2g1f40mczdnpirwvuw1f538zx9k491g1cfh3wg9iwhsb65o054) (Russian only).
