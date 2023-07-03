import csv
import os
import soundfile as sf
from espnet2.bin.tts_inference import Text2Speech

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0,1"  # Specify the GPU device ID

model_path = "exp/tts_train_raw_char/train.loss.ave_5best.pth"
vocoder_path = "checkpoint-400000steps.pkl"

tts = Text2Speech.from_pretrained(
    model_file=model_path,
    vocoder_file=vocoder_path,
    device = "cuda",
    threshold=0.5,
    minlenratio=0.0,
    maxlenratio=10.0,
    use_att_constraint=False,
    backward_window=1,
    forward_window=3,
    prefer_normalized_feats=True,
)


csv_file = "testsentences.csv"
output_folder = "audios2"
# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

with open(csv_file, "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row if exists
    counter = 1  # Counter variable for naming the audio files
    for row in reader:
        if len(row) > 0:  # Check if the row has at least one element
            text = row[0]  # Assuming the text is in the first column of the CSV
            # Generate audio from the text using the TTS model
            wav = tts(text)["wav"]
            # Construct the output file path with a number as the name
            output_file = os.path.join(output_folder, f"{counter}.wav")
            # Save the generated audio to the output file
            sf.write(output_file, wav.cpu().numpy(), tts.fs, "PCM_16")

            if counter % 100 == 0:
                print(f"Processed {counter} files")
            counter += 1  # Increment the counter for the next file
if counter % 1000 != 0:
        print(f"Processed {counter-1} files")
