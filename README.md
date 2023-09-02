<p align="center">
  <img src="https://github.com/aleixfortm/storymous/assets/95043218/97013ee7-c787-4587-adfe-6650a9c29f3b" alt="storymous_tree" width="800" height="auto">
</p>

###  **<p align="center">Storymous</p>**
<p align="center"><strong>Unique social media platform centered around storytelling where users are empowered to start and continue existing stories dynamically through a chapter-based system. </strong><br><br> With the creation of branching storylines, captivating narratives unfold, offering readers the ability to shape their own journey.</p>

###  **<p align="center">[![Shields](https://img.shields.io/badge/Website-Online-brightgreen)](https://www.storymous.com)  ![Shields](https://img.shields.io/badge/Version-1.0-blue)</p>**

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=vue,js,mongodb,python,flask" />
  </a>
</p>
<br>
<br>


<div align="center">
  <a href="https://ko-fi.com/G2G7NPEM9" target="_blank">
    <img src="https://ko-fi.com/img/githubbutton_sm.svg" alt="ko-fi" />
  </a>
</div>

<p align="center"><strong>Time for a coffee? Help me maintain the infrastructure cost of this project!</strong></p>

## Preview 

###  **<p align="center">Explore stories form the community</p>**
<p align="center">
  <img src="https://github.com/aleixfortm/storymous/assets/95043218/d441cf3e-439f-4f36-ba2b-e28898ff3b86" alt="storymous_tree" width="600" height="auto">
</p>

###  **<p align="center">Log in and start contributing</p>**
<p align="center">
  <img src="https://github.com/aleixfortm/storymous/assets/95043218/3038c64c-6fe9-4a9f-af7b-00cd76300acc" alt="storymous_tree" width="600" height="auto">
</p>

###  **<p align="center">Check out user profiles</p>**
<p align="center">
  <img src="https://github.com/aleixfortm/storymous/assets/95043218/f918dc52-d4dd-42bb-99ea-92cbd6a52761" alt="storymous_tree" width="600" height="auto">
</p>

###  **<p align="center">Start a new story yourself</p>**
<p align="center">
  <img src="https://github.com/aleixfortm/storymous/assets/95043218/309d5406-f33e-4f4c-825d-2131d1f4d362" alt="storymous_tree" width="600" height="auto">
</p>

###  **<p align="center">Mount and unmount chapters to shape a storyline</p>**
<p align="center">
  <img src="https://github.com/aleixfortm/storymous/assets/95043218/8c955ed8-d1bc-49e9-be58-32926fdbd91b" alt="storymous_tree" width="600" height="auto">
</p>



## Features 
- 🌍 Browse stories from the community
- 🌟 Start new stories
- 📚 Continue stories via a chapter-based system
- 📈 Comment on stories and express your thoughts
- 🙌 Check out user profiles
- 🎈 Customize your profile with color schemes, pictures and more
- 🧩 Beautifully themed on sci-fi pixel art
- 📱 Fully responsive design that gently adapts to any screen
- 🔥 More to come!

## Roadmap 
- [x] Welcome page (logged out)
  - [x] Explore feed
  - [x] Welcome message  
- [ ] Home page
  - [x] Latest / Following feed selector
  - [ ] Top section
    - [x] Top image
    - [ ] General stats section
      - [ ] Most active authors
      - [ ] Most visited / liked stories
      - [ ] Longest storyline
  - [x] Start new story option
- [x] Theme
  - [x] Huge amount of cool astronauts
  - [x] Story tree as storymous logo 
  - [x] Pixel art themed site
  - [x] Following color patterns across components
- [x] User profiles
  - [x] Visiting user profiles
  - [x] Check profile stats (Following, Followers, Posts)
  - [x] User bio
  - [x] Following and unfollowing user
  - [x] Profile color scheme (border of user profile box)
  - [x] User settings if user owner
    - [x] Changing profile picture
    - [x] Changing bio
    - [x] Changing profile color scheme
  - [x] User posts feed
  - [x] Responsive user profile box
  - [x] Specific data visualization upon stat hover (e.g. show name of followers)
- [ ] Story page
  - [x] Includes prologue
  - [x] Option to mount chapters on current storyline
  - [x] Option to write new chapter on current storyline
  - [x] Option to write comment on story post
  - [x] Comments and continued chapters feed
  - [x] Option for filtering comments / continued stories
  
## Database structure
<p align="center">
  <img src="https://github.com/aleixfortm/storymous/assets/95043218/e68b8a81-e2aa-419a-8f48-18f271c51a59" alt="database" width="600" height="auto">
</p>


## Known bugs 
- [x] <code>Solved!</code> Routing client to the same component (same URL) but with different URL param will not reload data and page will not update. Solved by passing <code>:key="router.params.id"</code> prop to router-view on App.vue
- [x] <code>Solved!</code> Feed stories display only a section of the content (substring of the whole text). However, when inside the story page, it should display the whole text, and still displays de substring.
- [x] <code>Solved!</code> Trying to visit own profile when in some other user's profile will bug the data and display stats incorrectly. Needs some sort of component refresh, as the component is the same but with different data.
- [x] <code>Solved!</code> Switching to "following" feed before "latest" feed finishes loading causes a bug in which all retrieved data is lost. Needs page refresh to solve and reload posts. 
- [x] <code>Solved!</code> Following feed appears as if user is not following anybody after log in. That, however, does not happen after refreshing page or navigating to other routes and coming back to feed.
- [x] <code>Solved!</code> Posting comments broken when at least one chapter has been mounted to the story.
- [x] <code>Solved!</code> If JWT token expires, user will still be able to be logged in, but requests to API won't work. Solve by checking expiration status of JWT on every request and log out if expired.
- [x] <code>Solved!</code> User profile box is not fully responsive, and screens smaller than 400px display a bit eerie. Not urgent fix.






## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

## License
This project is licensed under the Apache License - read the [LICENSE](https://www.apache.org/licenses/LICENSE-2.0) file for details.
