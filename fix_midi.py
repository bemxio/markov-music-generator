from pathlib import Path
from typing import Optional
import argparse

import mido

def main(input_file: Path, output: Path = None, max_ticks: int = 100):
    output = output or input_file.with_stem(input_file.stem + "_fixed")
    
    midi = mido.MidiFile(input_file)
    messages = mido.MidiTrack()

    time = 0
    pending = {}

    for message in mido.merge_tracks(midi.tracks):
        time += message.time

        messages.append(message)

        if message.type not in ("note_on", "note_off"):
            continue
        
        if message.velocity >= 1: # note turned on
            pending[message.note] = time
        elif message.type == "note_off" or message.velocity == 0: # note turned off
            pending.pop(message.note, None)
        
        for note, timestamp in pending.copy().items():
            if time - timestamp < max_ticks:
                continue
            
            messages.append(mido.Message(
                "note_on", 
                note=note,
                velocity=0,
                time=time - timestamp
            ))
            pending.pop(note)
            
    midi.tracks = [messages]
    midi.save(output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fix a MIDI file by adding note_off messages after each note_on message.")

    parser.add_argument(
        "input_file",
        help="The path to a MIDI file.",
        type=Path
    )
    parser.add_argument(
        "--max_ticks", "-m",
        help="The maximum length of a note in ticks. Defaults to 100.",
        default=100,
        type=int
    )
    parser.add_argument(
        "--output", "-o",
        help="The path to the output file.",
        default=None,
        type=Path
    )

    main(**vars(parser.parse_args()))