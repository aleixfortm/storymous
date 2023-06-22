<template>
    <div class="grid-container">
      <div
        v-for="(item, index) in gridItems"
        :key="index"
        class="grid-item"
        :class="{ selected: item.selected }"
        @click="selectItem(index)">
        <img :src="item.image" alt="Picture" class="picture" />
        <div class="selector"></div>
      </div>
    </div>
  </template>
  
  <script>
import astronaut_reading from "@/assets/img/astronaut_reading.jpeg";
import astronaut_earth from "@/assets/img/astronaut_earth.jpeg";
import astronaut_reads from "@/assets/img/astronaut_reads.jpeg";
import logo from "@/assets/img/logo.png";
import bookpile from "@/assets/img/bookpile.jpeg";
import tree1 from "@/assets/img/tree1.jpeg";
import tree2 from "@/assets/img/tree2.jpeg";
import default_blue from "@/assets/img/default_blue.png";
import default_pink from "@/assets/img/default_pink.png";
import default_orange from "@/assets/img/default_orange.png";
import default_red from "@/assets/img/default_red.png";
import default_grey from "@/assets/img/default_grey.png";
import default_purple from "@/assets/img/default_purple.png";
import default_skyblue from "@/assets/img/default_skyblue.png";

export default {
    props: ["previousImage"],
    data() {
        return {
            gridItems: [
                { image: astronaut_reading, name: "astronaut_reading.jpeg", selected: false },
                { image: astronaut_earth, name: "astronaut_earth.jpeg", selected: false },
                { image: astronaut_reads, name: "astronaut_reads.jpeg", selected: false },
                { image: logo, name: "logo.png", selected: false },
                { image: bookpile, name: "bookpile.jpeg", selected: false },
                { image: tree1, name: "tree1.jpeg", selected: false },
                { image: tree2, name: "tree2.jpeg", selected: false },
                { image: default_blue, name: "default_blue.png", selected: false },
                { image: default_pink, name: "default_pink.png", selected: false },
                { image: default_orange, name: "default_orange.png", selected: false },
                { image: default_red, name: "default_red.png", selected: false },
                { image: default_grey, name: "default_grey.png", selected: false },
                { image: default_purple, name: "default_purple.png", selected: false },
                { image: default_skyblue, name: "default_skyblue.png", selected: false },
            ],
        };
    },
    mounted() {
            //preselect an item (will be the one gathered from API)
            const i = this.gridItems.findIndex((item) => item.name === this.previousImage);
            this.selectItem(i);
    },
    methods: {
        selectItem(index) {
            // Clear selection of all items
            this.gridItems.forEach((item) => {
                item.selected = false;
            });

            // Select the clicked item
            this.gridItems[index].selected = true;

            //emit selected pic
            this.$emit("image-selected", this.gridItems[index].name);
        },
    },
    };
    </script>

<style scoped>
    .grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    grid-gap: 10px;
    }

    /* Adjust the size of the picture based on the grid item size */
    .picture {
        width: 100%;
        height: auto;
        border-radius: 500%;
    }

    .grid-item {
    position: relative;
    border: 2px solid #dddddd3b;
    cursor: pointer;
    transition: all 0.2s ease;
    }

    .grid-item:hover {
    background-color: rgba(107, 107, 107, 0.281);
    }

    .grid-item.selected {
    border-color: rgb(255, 255, 255);
    }

    .selector {
    position: absolute;
    top: 10px;
    right: 10px;
    width: 20px;
    height: 20px;
    background-color: rgb(255, 255, 255);
    border-radius: 50%;
    opacity: 0.1;
    transition: opacity 0.2s ease;
    }

    .grid-item.selected .selector {
    opacity: 1;
    }
</style>