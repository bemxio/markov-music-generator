from typing import Optional, List
from pathlib import Path
import argparse

from mido import MidiFile, MidiTrack
from mido import Message, MetaMessage

def decode_meta_message(line: str) -> MetaMessage:
    args = line[12:-1].split(", ")
    message_type = args.pop(0)[1:-1]

    #args = [argument.split("=") for argument in args]
    kwargs = {}

    for argument in args:
        key, value = argument.split("=")
        
        if value.startswith("'") and value.endswith("'"): # string, we gotta remove the quotes
            value = value[1:-1]
        elif value.isnumeric():
            value = int(value)

        kwargs[key] = value
    
    #print(f"Decoded meta message: {message_type} {kwargs}")
    return MetaMessage(message_type, **kwargs)

def decode(text: List[str]) -> MidiFile:
    track = MidiTrack()

    for line in text:
        if line.startswith("MetaMessage"):
            track.append(decode_meta_message(line))
            continue

        try:
            track.append(Message.from_str(line))
        except:
            print(f"Failed to decode message: {line}")
    
    return MidiFile(tracks=[track])

def main(file_path: Path, output: Optional[Path] = None):
    output = output or file_path.with_suffix(".mid")
    
    with open(file_path, "r") as file:
        text = file.read()
    
    midi = decode(text.splitlines())
    midi.save(output)

    print(f"MIDI file successfully decoded from {file_path}! Saved to {output}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Decode a MIDI in a text format back to a MIDI file.")

    parser.add_argument(
        "file_path",
        help="The path to tthe text file.",
        type=Path
    )
    parser.add_argument(
        "--output", "-o",
        help="The path to the output file. Defaults to the same path as the input file, with a `.mid` file extension.",
        default=None,
        type=Path
    )

    main(**vars(parser.parse_args()))