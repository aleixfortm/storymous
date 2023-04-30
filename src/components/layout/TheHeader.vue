<template>
    <header>
        <nav>
            <div>
                <img src="../../assets/img/tree2.jpeg" alt="treelogo">
                <h1><router-link to="/">Storymous</router-link></h1>
            </div>
            <search-bar></search-bar>
            <ul v-if="loggedIn">
                <h5><router-link to="/singup">Sign Up</router-link></h5>
                <h5><router-link to="/login">Log In</router-link></h5>
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
  background-color: #363444;
}

header a {
  text-decoration: none;
  color: #ffdf2c;
  display: inline-block;
  border: 1px solid transparent;
}

a:active,
a:hover,
a.router-link-active {
  border: 1px solid #ffdf2c;
}

h1 {
  margin: 0;
}

h1 a {
  color: rgb(150, 241, 44);
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
  margin: auto 0px auto 0px;
  width: 100px;
}

li {
  margin: 0 0.5rem;
}
</style>