import os
from pydub import AudioSegment
import numpy as np
from scipy.io.wavfile import read, write

def convert_to_432hz(input_file, output_file):
    # Load the MP3 file
    audio = AudioSegment.from_mp3(input_file)

    # Export the audio to WAV format
    audio.export("temp.wav", format="wav")

    # Read the WAV file
    rate, data = read("temp.wav")

    # Calculate the frequency conversion factor
    factor = 432 / 440

    # Resample the audio data
    resampled_data = np.round(np.interp(np.arange(0, len(data), factor), np.arange(0, len(data)), data)).astype(data.dtype)

    # Write the resampled audio data to a new WAV file
    write(output_file, rate, resampled_data)

    # Remove the temporary WAV file
    os.remove("temp.wav")

# Example usage
input_file = "input.mp3"
output_file = "output_432hz.mp3"

convert_to_432hz(input_file, output_file)
