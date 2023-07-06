<p align="center">
  <img src="https://github.com/aleixfortm/storymous/assets/95043218/97013ee7-c787-4587-adfe-6650a9c29f3b" alt="storymous_tree" width="900" height="auto">
</p>
<!--![storymous-forest-min](https://github.com/aleixfortm/storymous/assets/95043218/97013ee7-c787-4587-adfe-6650a9c29f3b)-->

### **<p align="center">[Storymous](https://www.storymous.com)</p>**

<p align="center"><strong>Unique social media platform centered around storytelling where users are empowered to collaborate and continue existing stories dynamically through a chapter-based system. With the creation of branching storylines, captivating narratives unfold, offering readers the ability to shape their own journey.</strong></p>


## Roadmap
- [x] Add story feed
- [x] Add user profiles
- [x] Add user posts section on user profile page
- [x] Add user settings option
- [x] Add logout option
- [x] Save data on session storage to keep user logged in
- [x] Create storymous art for homepage, profile pictures, and more
- [x] Style posts with colors and page style
- [x] Add latest/following sections on homepage
- [x] Add logged in/out homepage
- [x] Add starting stories functionality
- [x] Add commenting on posts functionlity
- [x] Display comments on post page
- [x] Allow visiting user profiles
- [x] Add different user settings options (Color scheme, picture and bio)
- [ ] Add general stats, either on home page or a create a dedicated route for it
- [ ] Add option to select color scheme for new story
- [ ] Make search bar functional and responsive to input
- [ ] Show users following/followers when hover/click on profile stats
- [x] Add links to user profiles dynamically to comment boxes
- [x] Add story tags
- [ ] Add continuing story functionality
- [x] Add functionality to write new chapters to existing stories (like a new comment form)

## Current bugs
- [ ] Feed stories display only a section of the content (substring of the whole text). However, when inside the story page, it should display the whole text, and still displays de substring.
- [x] <code>Solved!</code> Trying to visit own profile when in some other user's profile will bug the data and display stats incorrectly. Needs some sort of component refresh, as the component is the same but with different data. 
- [x] <code>Solved!</code> Following feed appears as if user is not following anybody after log in. That, however, does not happen after refreshing page or navigating to other routes and coming back to feed.
- [ ] User profile box is not fully responsive, and screens smaller than 400px display a bit eerie. Not urgent fix.
- [ ] If JWT token expires, user will still be able to be logged in, but requests to API won't work. Solve by checking expiration status of JWT on every request and log out if expired.

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
