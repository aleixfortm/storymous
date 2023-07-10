<p align="center">
  <img src="https://github.com/aleixfortm/storymous/assets/95043218/97013ee7-c787-4587-adfe-6650a9c29f3b" alt="storymous_tree" width="800" height="auto">
</p>
<!--![storymous-forest-min](https://github.com/aleixfortm/storymous/assets/95043218/97013ee7-c787-4587-adfe-6650a9c29f3b)-->





###  **<p align="center">Storymous</p>**
<p align="center"><strong>Unique social media platform centered around storytelling where users are empowered to start or continue existing stories dynamically through a chapter-based system. </strong><br><br> With the creation of branching storylines, captivating narratives unfold, offering readers the ability to shape their own journey.</p>

###  **<p align="center">[![Shields](https://img.shields.io/badge/Website-Online-brightgreen)](https://www.storymous.com)  ![Shields](https://img.shields.io/badge/Version-1.0-blue)</p>**

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=vue,js,mongodb,python,flask" />
  </a>
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
- [ ] User profiles
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
  - [ ] Responsive user profile box
  - [ ] Specific data visualization upon stat hover (e.g. show name of followers)
- [ ] Story page
  - [x] Includes prologue
  - [x] Option to mount chapters on current storyline
  - [x] Option to write new chapter on current storyline
  - [x] Option to write comment on story post
  - [x] Comments and continued chapters feed
  - [ ] Option for filtering comments / continued stories
  



## Known bugs 
- [x] <code>Solved!</code> Routing client to the same component (same URL) but with different URL param will not reload data and page will not update. Solved by passing <code>:key="router.params.id"</code> prop to router-view on App.vue
- [x] <code>Solved!</code> Feed stories display only a section of the content (substring of the whole text). However, when inside the story page, it should display the whole text, and still displays de substring.
- [x] <code>Solved!</code> Trying to visit own profile when in some other user's profile will bug the data and display stats incorrectly. Needs some sort of component refresh, as the component is the same but with different data.
- [x] <code>Solved!</code> Switching to "following" feed before "latest" feed finishes loading causes a bug in which all retrieved data is lost. Needs page refresh to solve and reload posts. 
- [x] <code>Solved!</code> Following feed appears as if user is not following anybody after log in. That, however, does not happen after refreshing page or navigating to other routes and coming back to feed.
- [ ] Posting comments broken when at least one chapter has been mounted to the story.
- [ ] User profile box is not fully responsive, and screens smaller than 400px display a bit eerie. Not urgent fix.
- [ ] If JWT token expires, user will still be able to be logged in, but requests to API won't work. Solve by checking expiration status of JWT on every request and log out if expired.

## Preview 

### Homepage
![image](https://github.com/aleixfortm/storymous/assets/95043218/5c57db4c-41d9-4a21-9453-44f4513b472b)

### Post page, including comments and continued chapters
![image](https://github.com/aleixfortm/storymous/assets/95043218/01a04a84-b495-4c31-b6c6-07ffa2e9b766)



### Own profile
![image](https://github.com/aleixfortm/storymous/assets/95043218/91976897-b320-4e47-bac8-7c03492031c1)

### Others' user profiles
![image](https://github.com/aleixfortm/storymous/assets/95043218/c9e0f2ea-3921-413c-9c47-f1e2cec929bd)


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
