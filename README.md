
# 🎶 Making a Pop Hit 🎤

This project explores how to maximise the chances of creating the next big hit song. The approach combines data analysis, machine learning, and chord progression generation to identify the key features of popular songs and leverage them in generating new music.

## 📚 Modules

### 01: Analysis 📊
An exploratory analysis aimed at maximising the likelihood of making a hit song. This module involves examining a Spotify dataset to identify key features that could contribute to creating popular tracks.

- **Dataset (removed)**: [Spotify Dataset (1921-2020, 160k tracks)](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks)

### 02: Data Scraping 🧑‍💻
Scrapes the most popular guitar chords from a user-specified number of tracks, parsing them for use in training a machine learning model.

- **Source**: [Ultimate Guitar - Popular Chords](https://www.ultimate-guitar.com/explore?order=hitstotal_desc&page=1&type[]=Chords)

### 03: Chord Progression Generator 🎸
Builds, trains, and tests a machine learning model to generate chord progressions with a high likelihood of popularity.

### 04: Results 🎬
Want to skip ahead to the results? Watch it in action or give it a try! 🚀

---

## 🚀 Getting Started

### Clone the Repository
To get started, clone the repository:
```bash
git clone https://github.com/chardrew/make-a-pop-hit.git
```

### Navigate to the Project Directory
Change into the project directory:
```bash
cd make-a-pop-hit
```

### Build the Docker Image 🐳
Create the Docker image with the following command:
```bash
docker build -t chardrew/chord_progression_generator:1.0 .
```

### Create a Container from the Image 🖥️
Run the container interactively:
```bash
docker run -it chardrew/chord_progression_generator:1.0
```

### Navigate to the Script 📂
Go to the script directory:
```bash
cd src
```

### Start Generating Chord Sequences 🎶
Generate chord progressions with:
```bash
python chord_progression_generator.py
```

---

Feel free to explore and have fun jamming! 🌟
