<template>
    <div class="grid-container2">
      <div
        v-for="(item, index) in gridItems2"
        :key="index"
        class="grid-item2"
        :class="{ selected: item.selected }"
        @click="selectItem(index)"
      >
        <div class="color" :style="{ backgroundColor: item.color_code }"></div>
        <div class="selector"></div>
      </div>
    </div>
  </template>
  
  <script>

export default {
    props: ["previousColor"],
    data() {
        return {
            gridItems2: [
            { color_code: 'rgb(255, 109, 93)', color:"salmon", selected: false }, // Red color
            { color_code: 'rgb(255, 25, 0)', color:"red", selected: false }, // Green color
            { color_code: 'rgb(0, 153, 255)', color:"blue", selected: false }, // Blue color
            { color_code: 'rgb(55, 182, 97)', color:"green", selected: false }, // Yellow color
            { color_code: 'rgb(255, 217, 0)', color:"yellow", selected: false }, // Red color
            { color_code: 'rgb(255, 255, 255)', color:"white", selected: false }, // Green color
            { color_code: 'rgb(183, 0, 255)', color:"purple", selected: false }, // Blue color
            { color_code: 'rgb(255, 0, 179)', color:"pink", selected: false }, // Yellow color
            { color_code: 'rgb(255, 145, 0)', color:"orange", selected: false }, // Red color
            ],
        };
    },
    mounted() {
        this.post = {
                _id: "test",
                title: "This is an example title!",
                content: "This shows how amazing your incredible story will look! Let us begin writing! Oh, and here is extra filler to make it look bigger, since a story is much longer than that hahaha, but never mind this!",
                username: "your username",
                postComment: "Looks awesome! Good color choice!",
                date: "Now",
                picture: "astronaut_reading.jpeg",
                color: "red"
            };

            //preselect an item (will be the one gathered from API)
            const i = this.gridItems2.findIndex((item) => item.color === this.previousColor);
            this.selectItem(i);
    },
    methods: {
        selectItem(index) {
            // Clear selection of all items
            this.gridItems2.forEach((item) => {
                item.selected = false;
            });

            // Select the clicked item
            this.gridItems2[index].selected = true;

            //emit selected pic
            this.$emit("color-selected", this.gridItems2[index].color);
        },
    },
    };
    </script>

<style>
.grid-container2 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(80px, 1fr)); /* Adjust the grid item size here */
  grid-gap: 10px;
}

.grid-item2 {
  position: relative;
  width: 100%;
  padding-bottom: 0;
  cursor: pointer;
  transition: all 0.2s ease;
  overflow: hidden;
}

.grid-item2:hover {
  background-color: rgba(107, 107, 107, 0.281);
}

.grid-item2.selected {
  background-color: rgba(143, 143, 143, 0.192);
  border: 2px solid #ddddddc9;
}

.color {
  width: 100%;
  height: 0;
  padding-bottom: 100%; /* Maintain aspect ratio for circles */
  border-radius: 50%;
  overflow: hidden;
}

.color:before {
  content: "";
  display: block;
  width: 100%;
  height: 100%;
}

.selector {
  position: absolute;
  top: 3px;
  right: 3px;
  width: 10px;
  height: 10px;
  background-color: rgb(255, 255, 255);
  border-radius: 50%;
  opacity: 0.1;
  transition: opacity 0.2s ease;
}

.grid-item2.selected .selector {
  opacity: 1;
}
</style>