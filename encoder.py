from typing import Optional, List
from pathlib import Path
import argparse

import mido

def encode(file: mido.MidiFile) -> List[str]:
    notes = []

    for message in mido.merge_tracks(file.tracks):
        if message.type != "note_on":
            continue

        notes.append(str(message))

    return notes

def main(file_path: Path, output: Optional[Path]):
    output = output or file_path.with_suffix(".txt")

    with mido.MidiFile(file_path) as midi:
        notes = encode(midi)
    
    with open(output, "w") as file:
        file.write("\n".join(notes))

    print(f"Successfully encoded {file_path} to {output}!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Encode a MIDI file to a text format.")

    parser.add_argument(
        "file_path",
        help="The path to a MIDI file.",
        type=Path
    )
    parser.add_argument(
        "--output", "-o",
        help="The path to the output file. Defaults to the same path as the input file, with a `.txt` file extension.",
        default=None,
        type=Path
    )

    main(**vars(parser.parse_args()))