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
    border-radius: 500%;
    border: 2px rgba(245, 245, 245, 0.637) solid;
    margin: auto;
    width: 100%;
}

</style>