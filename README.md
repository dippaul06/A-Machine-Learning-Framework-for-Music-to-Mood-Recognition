# Music

##Motivation

As music lovers, we’ve always felt that music players should do far more things than just playing songs
and allowing users to create play-lists. A music player should be intelligent and act according to user’s
preferences. A music player should help users organize and play the songs automatically without
putting much effort into selection and re-organization of songs. The Emotion-Based Music Player
provides a better platform to all the music listeners and ensures automation of song selection and
periodic updating of play-lists. This helps users organize and play songs based on their moods. But
currently the recommendation systems that are in use commercially mostly organize songs based on
collaborative filtering, content-based filtering or a hybrid of both. Emotion or mood is not always taken
into consideration. So, we wanted to create a recommendation system that takes into account not only
collaborative filtering and content-based filtering but also emotion or mood-based filtering and creates a
hybrid model. First part in recognizing this goal is to create a music mood recognition framework that
we have implemented in this project.

##Objective
The aim of this project was to develop a music mood classifier. There are many categories of mood into
which songs may be classified, e.g. happy, sad, angry, brooding, calm, uplifting, etc. People listen to
different kinds of music depending on their mood. The development of a framework for estimation of
musical mood, robust to the tremendous variability of musical content across genres, artists, world
regions and time periods, is an interesting and challenging problem with wide applications in the music
industry. In order to keep the problem simple, we are considering two song moods: Happy and Sad.

##Organization
In this proposed work, we develop a music mood classifier. First, we extract the features of music such
as Tempo, Zero Crossing Rate, Mel-frequency cepstral coefficients (MFCCs), Chroma Energy Normalized (CENS), Spectral Centroid, Spectral Contrast and Spectral Roll off. Then we stored all
these features into a .csv file and prepared our dataset. Afterwards, we used a multilayer Artificial
Neural Network (ANN) classifier on our dataset and trained our model.
