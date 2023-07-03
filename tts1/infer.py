import soundfile as sf

from espnet2.bin.tts_inference import Text2Speech


model_path = "exp/tts_train_raw_char/train.loss.ave_5best.pth"
vocoder_path = "checkpoint-400000steps.pkl"

tts = Text2Speech.from_pretrained(
    model_file=model_path,
    vocoder_file=vocoder_path,
    device = "cpu",
    threshold=0.5,
    minlenratio=0.0,
    maxlenratio=10.0,
    use_att_constraint=False,
    backward_window=1,
    forward_window=3,
    prefer_normalized_feats=True,
)

wav = tts("Менің атым Қожа болады. Ал сіздің атыңыз қалай?")["wav"]
sf.write("test1.wav", wav.numpy(), tts.fs, "PCM_16")
