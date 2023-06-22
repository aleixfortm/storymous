<template>

</template>
  
<script>

export default {
    props: ["previousBio"],
    data() {
        return {

        };
    },
    mounted() {
        
            /*
            //preselect an item (will be the one gathered from API)
            const i = this.gridItems2.findIndex((item) => item.color === this.previousColor);
            this.selectItem(i);
            */

    },
    methods: {
        /*
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
        */
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