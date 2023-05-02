<template>
    <form>
      <input type="text" placeholder="Search users, posts ..." v-model="searchQuery" @input="search">
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

<style>
img {
    width: 20px;
}

form {
display: block;
width: 50%;
}

input[type="text"] {
  display: block;
  background-color: #333c46;
  border: none;
  border-radius: 50px;
  font-size: 14px;
  font-weight: 500;
  height: 36px;
  outline: none;
  padding: 8px 8px 8px 20px; /* add left padding */
  width: 100%;
}



input[type="text"]::placeholder {
  color: #8d8d8da1;
  font-weight: 400;
}

input[type="text"]:focus {
  outline: none;
  color: #e2e2e2;
  background-color: #21272e;
  box-shadow: 0 0 0 2px #a1abbb;
}
</style>