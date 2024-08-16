import csv
from mido import Message, MidiFile, MidiTrack

def csv_to_midi(csv_filename, midi_filename):
    # Create a new MIDI file and track
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    # Start time
    current_time = 0

    # Read the CSV file
    with open(csv_filename, mode='r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            value = int(row['Values'])

            if value > 0:  # If it's a valid note value
                # Add a note on message
                track.append(Message('note_on', note=value, velocity=64, time=current_time))
                # Add a note off message after a fixed duration
                track.append(Message('note_off', note=value, velocity=64, time=480))  # Duration of the note
                current_time = 0  # Reset time for the next note

            elif value == 0:  # If it's a rest
                current_time += 480  # Add rest time to the next event

            # If the value is negative, we'll just treat it as a rest
            # You can customize this part if you have a specific interpretation of these values.

    # Save the MIDI file
    mid.save(midi_filename)

# Example usage
csv_to_midi('output_data.csv', 'output.mid')
