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
    height: auto;
    padding: 15px 30px;
}

.postimage {
    height: 100%;
    border-radius: 500%;
    border: 4px whitesmoke solid;
    margin: auto;
    width: 100%;
}

</style>