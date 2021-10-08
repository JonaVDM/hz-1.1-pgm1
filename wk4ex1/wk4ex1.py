# Programmeren I, Practicum 4
# Bestandsnaam: wk4ex1.py
# Naam:
# Probleemomschrijving: Geluidsbewerking

import time
import random
import math
from audio import *


# een functie zodat we kunnen beginnen met een opfrisser
# over list comprehensions...
def three_ize(L):
    """three_ize is a function that accepts a list and
       returns a list of elements each three times as large.
    """
    # dit is een voorbeeld van een list comprehension
    lc = [3 * x for x in L]
    return lc


# Te schrijven functie #1: scale
def scale(l: list, scale_factor: float) -> list:
    return [x * scale_factor for x in l]


# hier is een voorbeeld van hoe je op een andere
# manier de functie three_ize kan schrijven:
def three_ize_by_index(L):
    """three_ize_by_index has the same behavior as three_ize
       but it uses the INDEX of each element, instead of
       using the elements themselves -- this is much more flexible!
    """
    # nog een voorbeeld van een list comprehension
    n = len(L)
    lc = [3 * L[i] for i in range(n)]
    return lc


# Te schrijven functie #2: add_2
def add_2(l: list, m: list) -> list:
    """ Combines the two list together in one
        beautiful list using +
    """
    return [l[i] + m[i] for i in range(min(len(l), len(m)))]


# Te schrijven functie #3: add_3
def add_3(l: list, m: list, p: list) -> list:
    """ Basically the same as add_2, but than
        with three instead of two
    """
    return [l[i] + m[i] + p[i] for i in range(min(len(l), len(m), len(p)))]


# Te schrijven functie #4: add_scale_2
def add_scale_2(l: list, m: list, l_scale: float, m_scale: float) -> list:
    """ Add the two lists together whilst also scaling it
    """
    return [l[i] * l_scale + m[i] * m_scale for i in range(min(len(l), len(m)))]


def add_scale_3(l: list, m: list, p: list, l_scale: float, m_scale: float, p_scale: float) -> list:
    """ Add the three lists together whilst also scaling it
    """
    return [l[i] * l_scale + m[i] * m_scale + p[i] * p_scale for i in range(min(len(l), len(m), len(p)))]


# Hulpfunctie: randomize
def randomize(x, chance_of_replacing):
    """randomize accepts an original value, x
       and a fraction named chance_of_replacing.

       With the "chance_of_replacing" chance, it
       should return a random float from -32767 to 32767.

       Otherwise, it should return x (not replacing it).
    """
    r = random.uniform(0, 1)
    if r < chance_of_replacing:
        return random.uniform(-32768, 32767)
    else:
        return x


# Te schrijven functie #5: replace_some
def replace_some(l: list, change_of_replacing: float):
    return [randomize(x, change_of_replacing) for x in l]

#
# de functies hieronder betreffen geluidsbewerking...
#

# een functie om te zorgen dat alles werkt


def test():
    """A test function that plays swfaith.wav
       You'll need swfaith.wav in this folder.
    """
    play('swfaith.wav')


# De voorbeeldfunctie change_speed
def change_speed(filename, newsr):
    """change_speed allows the user to change an audio file's speed.
       Arguments: filename, the name of the original file
                  newsr, the new sampling rate in samples per second
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """
    print("Het originele geluid afspelen...")
    play(filename)

    sound_data = [0, 0]             # een "lege" lijst
    read_wav(filename, sound_data)  # laad gegevens IN sound_data

    samps = sound_data[0]           # de samples van de ruwe geluidsgolven

    print("De eerste 10 geluidsdruksamples zijn\n", samps[:10])
    sr = sound_data[1]              # de sampling rate, sr

    print("Het aantal samples per seconde is", sr)

    # deze regel is niet echt nodig, maar staat hier voor de consistentie...
    newsamps = samps                      # dezelfde samples als eerder
    new_sound_data = [newsamps, newsr]    # nieuwe geluidsgegevens
    write_wav(new_sound_data, "out.wav")  # sla de gegevens op naar out.wav
    print("\nNieuw geluid afspelen...")
    play('out.wav')   # speel het nieuwe bestand 'out.wav' af


def flipflop(filename):
    """flipflop swaps the halves of an audio file
       Argument: filename, the name of the original file
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """
    print("Het originele geluid afspelen...")
    play(filename)

    print("Geluidsgegevens inlezen...")
    sound_data = [0, 0]
    read_wav(filename, sound_data)
    samps = sound_data[0]
    sr = sound_data[1]

    print("Nieuw geluid berekenen...")
    # dit bepaalt het middelpunt en noemt dat x
    x = len(samps)//2
    newsamps = samps[x:] + samps[:x]
    newsr = sr
    new_sound_data = [newsamps, newsr]

    print("De nieuwe geluidsgegevens opslaan...")
    write_wav(new_sound_data, "out.wav")  # schrijf gegevens naar out.wav

    print("Nieuw geluid afspelen...")
    play('out.wav')


# Te schrijven geluidsfunctie #1: reverse
def reverse(filename: str) -> None:
    """ reverse the audio!
    """
    print("Het originele geluid afspelen...")
    play(filename)

    print("Geluidsgegevens inlezen...")
    sound_data = [0, 0]
    read_wav(filename, sound_data)
    samps = sound_data[0]
    sr = sound_data[1]

    print("Nieuw geluid berekenen...")
    new_sound_data = [samps[::-1], sr]

    print("De nieuwe geluidsgegevens opslaan...")
    write_wav(new_sound_data, "out.wav")

    print("Nieuw geluid afspelen...")
    play('out.wav')


# Te schrijven geluidsfunctie #2: volume
def volume(filename: str, scale_factor: float) -> None:
    """ Change the volume level on the scale_factor
    """
    print("Het originele geluid afspelen...")
    play(filename)

    print("Geluidsgegevens inlezen...")
    sound_data = [0, 0]
    read_wav(filename, sound_data)
    samps = sound_data[0]
    sr = sound_data[1]

    print("Nieuw geluid berekenen...")
    new_sound_data = [scale(samps, scale_factor), sr]

    print("De nieuwe geluidsgegevens opslaan...")
    write_wav(new_sound_data, "out.wav")

    print("Nieuw geluid afspelen...")
    play('out.wav')


# Te schrijven geluidsfunctie #3: static
def static(filename: str, probability_of_static) -> None:
    """ add random noise in the audio
    """
    print("Het originele geluid afspelen...")
    play(filename)

    print("Geluidsgegevens inlezen...")
    sound_data = [0, 0]
    read_wav(filename, sound_data)
    samps = sound_data[0]
    sr = sound_data[1]

    print("Nieuw geluid berekenen...")
    new_sound_data = [replace_some(samps, probability_of_static), sr]

    print("De nieuwe geluidsgegevens opslaan...")
    write_wav(new_sound_data, "out.wav")

    print("Nieuw geluid afspelen...")
    play('out.wav')

# Te schrijven geluidsfunctie #4: overlay


def overlay(filename1: str, filename2: str) -> None:
    """ combine two audio files
    """
    print("Het originele eerste geluid afspelen...")
    play(filename1)

    print("Het originele tweede geluid afspelen...")
    play(filename2)

    sound_data1 = [0, 0]
    sound_data2 = [0, 0]
    read_wav(filename1, sound_data1)
    read_wav(filename1, sound_data2)

    print("Nieuw geluid berekenen...")
    sr = sound_data1[1]
    new_sound_data = [add_scale_2(
        sound_data1[0], sound_data2[0], 0.5, 0.5), sr]

    print("De nieuwe geluidsgegevens opslaan...")
    write_wav(new_sound_data, "out.wav")

    print("Nieuw geluid afspelen...")
    play('out.wav')


# Te schrijven geluidsfunctie #5: echo
def echo(filename: str, time_delay: float) -> None:
    """ Play some sounds with a cool echo
    """
    print("Het originele geluid afspelen...")
    play(filename)

    sound_data = [0, 0]
    read_wav(filename, sound_data)

    print('Nieuw geluid...')
    wt = sound_data[1] / time_delay
    new_data = [add_2(sound_data[0], [0] * int(wt) +
                      sound_data[0]), sound_data[1]]

    print("De nieuwe geluidsgegevens opslaan...")
    write_wav(new_data, "out.wav")

    print("Nieuw geluid afspelen...")
    play('out.wav')


# Hulpfunctie om pure tonen te genereren
def gen_pure_tone(freq, seconds, sound_data):
    """pure_tone returns the y-values of a cosine wave
       whose frequency is freq Hertz.
       It returns nsamples values, taken once every 1/44100 of a second.
       Thus, the sampling rate is 44100 hertz.
       0.5 second (22050 samples) is probably enough.
    """
    if sound_data != [0, 0]:
        print("De waarde van sound_data moet [0, 0] zijn.")
        return
    sampling_rate = 22050
    # hoeveel samples we moeten genereren
    nsamples = int(seconds*sampling_rate)  # naar beneden afgerond
    # de factor f om de frequentie te schalen
    f = 2*math.pi/sampling_rate   # omrekenen van samples naar Hz
    # de factor a om de amplitude te schalen
    a = 32767.0
    sound_data[0] = [a * math.sin(f*n*freq) for n in range(nsamples)]
    sound_data[1] = sampling_rate
    return sound_data


def pure_tone(freq, time_in_seconds):
    """Generates and plays a pure tone of the given frequence."""
    print("Toon genereren...")
    sound_data = [0, 0]
    new_sound_data = gen_pure_tone(freq, time_in_seconds, sound_data)

    print("De nieuwe geluidsgegevens opslaan...")
    write_wav(new_sound_data, "out.wav")  # schrijf gegevens naar out.wav

    print("Nieuw geluid afspelen...")
    play('out.wav')


# Te schrijven geluidsfunctie #6: chord
def chord(f1: float, f2: float, f3: float, time_in_seconds: float):
    """ Play a nice chord!
    """
    samps1, sr1 = gen_pure_tone(f1, time_in_seconds, [0, 0])
    samps2, sr2 = gen_pure_tone(f2, time_in_seconds, [0, 0])
    samps3, sr3 = gen_pure_tone(f3, time_in_seconds, [0, 0])

    sound_data = [add_scale_3(samps1, samps2, samps3, 1/3, 1/3, 1/3), sr1]

    print("De nieuwe geluidsgegevens opslaan...")

    write_wav(sound_data, "out.wav")  # schrijf gegevens naar out.wav

    print("Nieuw geluid afspelen...")
    play("out.wav")
