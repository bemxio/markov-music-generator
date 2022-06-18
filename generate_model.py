import encoder

from pathlib import Path
from typing import Optional
import argparse

import markovify
import mido

def main(directory: Path, state_size: int = 2, output: Optional[Path] = None):
    dataset = []
    
    for filename in directory.iterdir():
        with mido.MidiFile(filename) as file:
            messages = encoder.encode(file)

        dataset.append(messages)

        print(f"Processed {filename}")
    
    chain = markovify.Chain(dataset, state_size=state_size)

    with open(output, "w") as file:
        file.write(chain.to_json())

    print(f"Successfully generated model from {directory}! Saved to {output}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a Markov chain from a directory of MIDI files.")

    parser.add_argument(
        "directory",
        help="The path to a directory of MIDI files.",
        type=Path
    )
    parser.add_argument(
        "--state-size", "-s",
        help="The state size of the model. Defaults to 2.",
        default=2,
        type=int
    )
    parser.add_argument(
        "--output", "-o",
        help="The path to the output file. Defaults to 'model.json'",
        default=Path("model.json"),
        type=Path
    )

    main(**vars(parser.parse_args()))