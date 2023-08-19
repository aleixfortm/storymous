<template>
    <div class="entirebox">
        <div class="box">
            <div class="explanation">
                <div class="title"></div>
                <div class="content"></div>
                <div class="content"></div>
                <div class="content"></div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    computed: {
        imgSrc() {
            return require("@/assets/img/storymous-forest-min.png")
        }
    }
}
</script>

<style scoped>
.entirebox {
    margin-top: 10px;
}

.box {
    height: fit-content;
    width: 100%;
    text-align: left;
    padding: 8px;
    border-radius: 4px;
    border: 1px rgba(255, 255, 255, 0.247) solid;
    background-color: rgba(43, 43, 46, 0.671);
    transition: 0.2s all;
}

.title {
    height: 20px;
    width: 100%;
    background-color: #ffffff09;
    border-radius: 4px;
}

.content {
    height: 50px;
    width: 100%;
    background-color: #ffffff09;
    margin-top: 8px;
    border-radius: 4px;
}

@keyframes breathing {
    0%, 100% {
        transform: scale(0.98);
        background-color: #ffffff09;
    }
    50% {
        transform: scale(1);
        background-color: #ffffff18; /* Slightly darker background color */
    }
}

.title, .content {
    animation: breathing 2s infinite;
}

</style>
