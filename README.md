# markov-music-generator
A set of Python scripts, for generating a MIDI file from an another dataset of MIDI files, using Markov chains.

## Usage
Just before you do anything, make sure you are running Python 3.8+, so that you can run the script without any issues.
You can either collect your own dataset of MIDI files, or use The MAESTRO Dataset, bundled in the repository.

All scripts have help messages, that will show the usage of a script, but the steps usually go as follows:
1. Put all of your MIDI files in a directory.
2. Run the `generate_model.py` script, specifying the directory where the MIDI files are, ex. `python3 generate_model.py maestro-v3.0.0/2008`.
3. After generating the model, run the `generate_song.py` script, specyfing the path to the model file, ex. `python3 generate_song.py model.json`.
4. Clean up the MIDI file by using the `fix_midi.py` script, ex. `python3 fix_midi.py generated_song.mid`.

Cleaning up the MIDI file is often needed, since the Markov chain likes to not end the notes and instead leave them open.
The script mentioned above will make them not surpass the maximum length limit.

## Resources used
- [`mido`](https://github.com/mido/mido), for reading and writing MIDI files.
- [`markovify`](https://github.com/jsvine/markovify), for creating and saving Markov chains.
- [The MAESTRO Dataset](https://magenta.tensorflow.org/datasets/maestro), for the dataset used in this project.