<template>
    <div class="tag-shape" :class="tag">{{ tag }}</div>
</template>

<script>
export default {
    props: ["tag"]
}
</script>

<style scoped>
.tag-shape {
    padding: 1px 5px;
    font-size: 13px;
    font-weight: bold;
    margin: 0 5px 5px 0;
    width: fit-content;
    border-radius: 100px;
}

.mystery {
    background-color: rgba(255, 145, 0, 0.274);
    color: rgb(255, 174, 0);
}
.sci-fi {
    background-color: rgba(0, 162, 255, 0.322);
    color: rgb(0, 204, 255);
}
.chill {
    background-color: rgba(0, 255, 55, 0.274);
    color: rgb(0, 255, 21);
}
.short {
    background-color: rgba(123, 132, 255, 0.274);
    color: rgb(255, 170, 234);
}

.long {
    background-color: rgba(123, 132, 255, 0.274);
    color: rgb(177, 163, 255);
}

.medieval {
    background-color: rgba(17, 0, 255, 0.274);
    color: rgb(255, 135, 135);
}

.jungle {
    background-color: rgba(60, 255, 0, 0.274);
    color: rgb(193, 255, 135);
}

.horror {
    background-color: rgba(0, 0, 0, 0.562);
    color: rgb(185, 185, 185);
}

.historical {
    background-color: rgba(88, 88, 88, 0.445);
    color: rgb(209, 77, 77);
}

.fantasy {
    background-color: rgba(0, 255, 221, 0.274);
    color: rgb(135, 251, 255);
}

.world-building {
    background-color: rgba(238, 255, 0, 0.274);
    color: rgb(255, 237, 135);
}
</style>