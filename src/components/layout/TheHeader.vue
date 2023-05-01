<template>
    <header>
        <nav>
            <div>
                <router-link to="/"><img src="../../assets/img/tree2.jpeg" alt="treelogo"></router-link>
                <h1><router-link to="/">Storymous</router-link></h1>
            </div>
            <search-bar></search-bar>
            <ul v-if="loggedIn">
              <li>
                <h5><router-link to="/signup">Sign Up</router-link></h5>
              </li>
              <li>
                <h5><router-link to="/login">Log In</router-link></h5>
              </li>
                
            </ul>
            <ul v-else>
              <img src="../../assets/img/default_blue.png" alt="astronaut">
            </ul>
        </nav>
    </header>
</template>


<script>
import SearchBar from "../SearchBar.vue"

export default {
  data() {
    return {
      loggedIn: true,
    }
  },
  components: {
    SearchBar
  },
  methods: {
    performSearch(query) {
      // Perform search action here, using the query parameter
      query.indexOf(3);
    }
  }
}
</script>

<style scoped>
img {
  width: 45px;
  border-radius: 100px;
}

div {
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 20px;
}

header {
  position: fixed;
  z-index: 100;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  margin: 0;
  width: 100%;
  height: 3.5rem;
  background-color: #435055;
}

header a {
  text-decoration: none;
  color: rgb(100, 207, 0);
  display: inline-block;
  border: 1px solid transparent;
}

a:active,
a:hover,
a.router-link-active {
  text-decoration: underline;
}

h1 {
  margin: 0;
}

h1 a {
  color: rgb(100, 207, 0);
  margin: 0 0 0 5px;
}

h1 a:hover,
h1 a:active,
h1 a.router-link-active {
  border-color: transparent;
}

header nav {
  width: 100%;
  margin: auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

header ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
}

h5 {
  margin: auto 0px auto 10px;
  width: 60px;
}

li {
  margin: 0 0.5rem;
}

@media (max-width: 700px) {
  h1 {
    display: none;
  }
}

</style>