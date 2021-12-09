# Unit 4 Project
#### By Matthew Laude

## Description
This project is a music app that allows user to add songs to their own personal library. The app has full CRUD functionality, allowing users to add, edit, and delete songs. Additional song details include the album cover, genre, and track length. 

## User Stories
As a user, I can see a list of all my songs on the home page. \
As a user, I can click on a song, and all the details of the song will pop up \
As a user, I can add a song on the home page immediately \
As a user, I can delete songs from my library \
As a user, I can edit and update my currently existing songs

## Components
- Header
- Index
- Song
- Carousel

## Dependencies
- cors
- dotenv
- gunicorn
- psycopg2

## Technologies
Masonite, React, react-router-dom, react-icons, sass

## Models
Song:
- title: string
- artist: string
- album: string
- albumCover: string
- genre: string
- trackLength: integer

## Backend Route Table 
| url | method | action |
|-----|--------|--------|
| /songs | get | getting all the songs (index)||
| /songs | post | posting a new song (create) |
| /songs/:id | put | updating a song (update) |
| /songs/:id | delete | delete a song (destroy) |

## React Router Route Table
| URL | Component | Method | Action |
|-----|-----------|--------|--------|
| / | Index | get | getting all songs (index)||
| / | Index | post | posting a new song (create) |
| /songs/:id | Show | put | updating a song (update) |
| /songs/:id | Show | delete | delete a song (destroy) |

## React Component Architecture
```
-> App
  -> Header
  -> Main |state: songs|
    -> Routes
      -> Route |path: "/"|
        -> Index |Props: songs|
      -> Route |path="/songs/:id|
        -> Show |Props: songs, updateSong, deleteSong|
```

## Bonus Features
**Carousel** \
A functional carousel is displayed at the top of the Index page.

## Challenges
**TBD**
