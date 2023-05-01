<template>
    <v-dialog v-model="dialog" max-width="500px">

    </v-dialog>
  </template>
  
  <script>
  export default {
    data: () => ({
      dialog: false,
      dialogTitle: "Sign in"
    })
  };
  </script>