<template>
    <div class="imageblock">
        <img class="postimage" :src="imgSource" alt="profilepic">
    </div>
</template>

<script>
export default {
    props: ["picture"],
    computed: {
        imgSource() {
            console.log(this.picture)
            return require("../../assets/img/" + this.picture);
        }
    }
}
</script>

<style scoped>
.imageblock {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: stretch;
    width: 340px;
}

.postimage {
    height: 100%;
    border-radius: 500%;
    border: 6px whitesmoke solid;
    margin: 35px;
}

</style>