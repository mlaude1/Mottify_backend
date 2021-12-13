# Unit 4 Project
#### By Matthew Laude

## Dependencies
- cors
- dotenv
- gunicorn
- psycopg2

## Models
Song:
- title: string
- artist: string
- album: string
- albumCover: string
- genre: string
- favorite: boolean

## Backend Route Table 
| url | method | action |
|-----|--------|--------|
| /songs | get | getting all the songs (index)||
| /songs | post | posting a new song (create) |
| /songs/:id | put | updating a song (update) |
| /songs/:id | delete | delete a song (destroy) |
