<template>
    <div class="stats-bio">
        
    </div>
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

<style scoped>
.stats-bio {
    background-color: rgb(255, 255, 255);
    border-radius: 10px 10px 10px 10px;
    padding: 10px;
    margin: 30px 10px 5px 10px;
    color: rgb(0, 0, 0);
}
</style>