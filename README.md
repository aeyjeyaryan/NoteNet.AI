# 🎵 NoteNet.AI 🎶

## Welcome to the Music Generation Project!

NoteNet.AI is an innovative music generation project that leverages Long Short-Term Memory (LSTM) neural networks to create captivating musical sequences. Our goal is to train a model that can generate music by predicting the next note in a sequence.

## 📋 Project Overview

The project involves the following steps:

1. **Loading and Preprocessing Data** 🗂️
   - **Load Music Sequences:** Import music note sequences from text files.
   - **Preprocess Data:** Convert notes into numerical sequences and normalize them for model training.

2. **Training the LSTM Model** 🧠
   - **Train Model:** Use an LSTM neural network to learn and capture patterns in the music sequences.

3. **Generating New Music** 🎶
   - **Generate Sequences:** Create new music sequences based on a seed sequence using the trained model.

4. **Saving Generated Data** 💾
   - **Export Data:** Save the generated music sequences into a CSV file for further analysis or use.

## 📊 About the Dataset

The dataset consists of ASCII-encoded values representing music notes. These values are used to train the LSTM model. The output of the model is a CSV file containing the note values of the generated music sequences.

## 🔧 Usage

1. **Prepare Data** 🗂️:
   - Place your music note sequences in text files as described in the dataset section.
   - Run the preprocessing script to convert and normalize the data.

2. **Train the Model** 🧠:
   - Execute the training script to build and train the LSTM model on your data.

3. **Generate Music** 🎶:
   - Use the generation script to produce new music sequences from a given seed.

4. **Export Results** 💾:
   - Save the generated sequences to a CSV file for further use.

5. **Convert CSV to Midi** 🔄
   - Convert the .csv file to .midi using mido.

6. **Convert Midi to Wav** 🎵
   - Convert the midi file to wav or use the midi file to modify on various instruments.


