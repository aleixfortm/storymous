<template>
    <div class="grid-container">
      <div
        v-for="(item, index) in gridItems"
        :key="index"
        class="grid-item"
        :class="{ selected: item.selected }"
        @click="selectItem(index)">
        <img :src="item.color" alt="Color" class="color" />
        <div class="selector"></div>
      </div>
    </div>

</template>
  
  <script>

export default {
    components: {
    },
    data() {
        return {
            gridItems: [
            { color: '#ff0000', selected: false }, // Red color
            { color: '#00ff00', selected: false }, // Green color
            { color: '#0000ff', selected: false }, // Blue color
            { color: '#ffff00', selected: false }, // Yellow color
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
                extendedLength: false,
                imgName: "astronaut_reading.jpeg",
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

            //emit selected pic
            //this.$emit("image-selected", this.gridItems[index].color);
        },
    },
    };
    </script>