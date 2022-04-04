import numpy as np
from matplotlib import pyplot as plt
from scipy.io.wavfile import write

SAMPLE_RATE = 44100  # Hertz
DURATION = 2  # Seconds

def generate_sine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    # 2pi because np.sin takes radians
    y = np.sin((2 * np.pi) * frequencies)
    return x, y

# Generate a 2 hertz sine wave that lasts for 5 seconds
#x, y = generate_sine_wave(10, SAMPLE_RATE, DURATION)
#plt.plot(x, y)
#plt.show()

_, nice_tone = generate_sine_wave(1, SAMPLE_RATE, DURATION)
_, noise_tone = generate_sine_wave(10000, SAMPLE_RATE, DURATION)
noise_tone = noise_tone * 0.3

mixed_tone = nice_tone + noise_tone



normalized_tone = np.int16((mixed_tone / mixed_tone.max()) * 32767)

plt.plot(normalized_tone[:1000])
plt.show()

# Remember SAMPLE_RATE = 44100 Hz is our playback rate
write("mysinewave.wav", SAMPLE_RATE, normalized_tone)