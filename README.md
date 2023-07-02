
# storymous

<img src="https://github.com/aleixfortm/storymous/assets/95043218/0298a2af-3140-4de2-b4b3-1a0ee6262904" alt="storymous_tree" width="200" height="auto">


[Storymous](https://www.storymous.com) is a story-based social media that allows users to dynamically start and continue stories. By creating trees of multiple chapter options, amazing stories arise in which the reader is able to choose their own path through the story.

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
- [ ] Add links to user profiles dynamically to comment boxes
- [ ] Add story tags
- [ ] Add continuing story functionality
- [ ] Add functionality to write new chapters to existing stories (like a new comment form)

## Current bugs
- Trying to visit own profile when in some other user's profile will bug the data and display stats incorrectly. Needs some sort of component refresh, as the component is the same but with different data.
- Following feed appears as if user is not following anybody after log in. That, however, does not happen after refreshing page or navigating to other routes and coming back to feed.
- User profile box is not fully responsive, and screens smaller than 400px display a bit eerie. Not urgent fix.
- If JWT token expires, user will still be able to be logged in, but requests to API won't work. Solve by checking expiration status of JWT on every request and log out if expired.

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
