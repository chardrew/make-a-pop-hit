# Making a pop hit

## Modules
### 01 Analysis
An exploratory analysis on maximising my chances of making the next hit song.  
Explore the Spotify dataset for features that may give me the edge on writing a popular song.  

Dataset: https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks

### 02 Data scraping
Scraping a user-specified number of the most popular guitar chords and parsing them to be used in machine learning model

Site: https://www.ultimate-guitar.com/explore?order=hitstotal_desc&page=1&type[]=Chords

### 03 Chord progression generator
Build, train and test a machine learning model to generate chord progression with high popularity

### 04 Results
Want to skip to the results? Watch it in action or...

# Try it for yourself!
### Clone repo
`git clone https://github.com/chardrew/make-a-pop-hit.git`
### Change directory
`cd make-a-pop-hit`
### Build docker image
`docker build -t chardrew/chord_progression_generator:1.0 .`
### Create a container using the image
`docker run -it chardrew/chord_progression_generator:1.0`
### Navigate to script
`cd src`
### Start generating sequences
`python chord_progression_generator.py`
