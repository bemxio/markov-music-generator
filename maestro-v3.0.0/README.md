# The MAESTRO Dataset
MAESTRO (MIDI and Audio Edited for Synchronous TRacks and Organization) is a dataset composed of about 200 hours of virtuosic piano performances captured with fine alignment (~3 ms) between note labels and audio waveforms.

**For more information, please visit [this](https://magenta.tensorflow.org/datasets/maestro) website.**

## Dataset
We partnered with organizers of the [International Piano-e-Competition](http://piano-e-competition.com/) for the raw data used in this dataset. During each installment of the competition virtuoso pianists perform on Yamaha Disklaviers which, in addition to being concert-quality acoustic grand pianos, utilize an integrated high-precision MIDI capture and playback system. Recorded MIDI data is of sufficient fidelity to allow the audition stage of the competition to be judged remotely by listening to contestant performances reproduced over the wire on another Disklavier instrument.

The dataset contains about 200 hours of paired audio and MIDI recordings from ten years of International Piano-e-Competition. The MIDI data includes key strike velocities and sustain/sostenuto/una corda pedal positions. Audio and MIDI files are aligned with ∼3 ms accuracy and sliced to individual musical pieces, which are annotated with composer, title, and year of performance. Uncompressed audio is of CD quality or higher (44.1–48 kHz 16-bit PCM stereo).

A train/validation/test split configuration is also proposed, so that the same composition, even if performed by multiple contestants, does not appear in multiple subsets. Repertoire is mostly classical, including composers from the 17th to early 20th century.

For more information about how the dataset was created and several applications of it, please see the paper where it was introduced: [Enabling Factorized Piano Music Modeling and Generation with the MAESTRO Dataset](https://goo.gl/magenta/maestro-paper).

For an example application of the dataset, see our blog post on [Wave2Midi2Wave](https://magenta.tensorflow.org/maestro-wave2midi2wave).