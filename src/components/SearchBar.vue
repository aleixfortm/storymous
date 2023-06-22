<template>
    <form>
      <input type="text" placeholder="Search" v-model="searchQuery" @input="search">
    </form>
</template>

<script>
export default {
data() {
    return {
      searchQuery: ''
    }
},
methods: {
    search() {
    // Emit a custom event to notify the parent component of the search action
    this.$emit('search', this.searchQuery)
    }
  }
}
</script>

<style scoped>
img {
    width: 20px;
}

form {
display: block;
width: 50%;
}

input[type="text"] {
  background-color: #1d252e;
  border: none;
  border-radius: 5px;
  font-size: 14px;
  font-weight: 500;
  height: 40px;
  outline: none;
  padding: 8px 8px 8px 20px; /* add left padding */
  width: 95%;
  font: inherit;
  outline: rgb(100, 100, 100) 1px solid;
  color: whitesmoke;
  transition: all 0.1s;
}

input[type="text"]:hover {
    outline: rgb(168, 168, 168) 1px solid;
}

input[type="text"]::placeholder {
  color: #b3b3b3a1;
  font-weight: 400;
}

input[type="text"]:focus {
  outline: rgb(168, 168, 168) 1px solid;
}

</style>