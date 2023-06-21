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
    data() {
        return {
            gridItems: [
                { image: astronaut_reading, selected: false },
                { image: astronaut_earth, selected: false },
                { image: astronaut_reads, selected: false },
                { image: logo, selected: false },
                { image: bookpile, selected: false },
                { image: tree1, selected: false },
                { image: tree2, selected: false },
                { image: default_blue, selected: false },
                { image: default_pink, selected: false },
                { image: default_orange, selected: false },
                { image: default_red, selected: false },
                { image: default_grey, selected: false },
                { image: default_purple, selected: false },
                { image: default_skyblue, selected: false },
            ],
        };
    },
    methods: {
        selectItem(index) {
        // Clear selection of all items
        this.gridItems.forEach((item) => {
            item.selected = false;
        });

        // Select the clicked item
        this.gridItems[index].selected = true;
        },
    },
    };
    </script>

<style>
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
    border: 1px solid #dddddd88;
    cursor: pointer;
    transition: border-color 0.2s ease;
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