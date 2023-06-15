<template>
    <feed-container>
    <div>
      <form @submit.prevent="submitForm">
        <div>
          <label for="title">Title:</label>
          <input id="title" v-model="form.title" type="text" required>
        </div>
        <div>
          <label for="comment">Comment:</label>
          <textarea id="comment" v-model="form.comment" required></textarea>
        </div>
        <div>
          <label for="body">Body:</label>
          <textarea id="body" v-model="form.body" required></textarea>
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
</feed-container>
  </template>
  
  <script>
  export default {
    name: "NewPost",
    data() {
      return {
        form: {
          title: '',
          comment: '',
          body: ''
        }
      };
    },
    methods: {
      submitForm() {
        // Here you can perform the desired actions with the form data
        console.log(this.form);
      }
    }
  };
  </script>