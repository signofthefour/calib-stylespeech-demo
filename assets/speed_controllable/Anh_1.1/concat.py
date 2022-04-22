import os
from pydub import AudioSegment

filepath = sorted([f for f in os.listdir('.') if '.wav' in f])

sound1 = AudioSegment.from_wav('ref_Anh_0.wav')
for i in range(17):
    sound1 += AudioSegment.from_wav(f'ref_Anh_{i+1}.wav')
sound1.export("abstract.wav", format="wav")
