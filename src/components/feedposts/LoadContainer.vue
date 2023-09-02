<template>
    <div>
        <div class="outline">
            <div class="origin"></div>
            <div class="user-container">
                <div class="picture"></div>
                <div class="user-data-container">
                    <div class="comment"></div>
                    <div class="username-date"></div>
                </div>
            </div>
            <div class="title-container">
                <div class="chapter"></div>
                <div class="title"></div>
            </div>
            <div v-for="i in 12" :key="i" class="line"></div>
        </div>
    </div>
</template>

<script>

export default {
    name: "LoadContainer"
}
</script>

<style scoped>
.line {
    width: 100%;
    height: 12px;
    background-color: #ffffff09;
    margin-right: 10px;
    border-radius: 4px;
    margin-top: 5px;
}
.chapter {
    width: 10%;
    height: 15px;
    background-color: #ffffff09;
    margin-right: 10px;
    border-radius: 4px;
}
.title-container {
    display: flex;
    justify-content: flex-start;
    margin-top: 8px;
    margin-bottom: 10px;
}
.title {
    width: 60%;
    height: 15px;
    background-color: #ffffff09;
    border-radius: 4px;
}
.username-date {
    width: 100%;
    height: 15px;
    background-color: #ffffff09;
    margin-top: 8px;
    border-radius: 4px;
}
.comment {
    width: 100%;
    height: 25px;
    background-color: #ffffff09;
    border-radius: 4px;
}
.user-data-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    margin: 0 0 0 5px;
    width: 100%;
}
.picture {
    height: 45px;
    width: 45px;
    border-radius: 500%;
    background-color: #ffffff09;
}
.user-container {
    display: flex;
    justify-content: flex-start;
    align-items: center;
    margin: 5px 0;
}
.origin {
    height: 15px;
    width: 55%;
    background-color: #ffffff09;
    border-radius: 4px;
}
.outline {
    margin-top: 12px;
    padding: 10px;
    height: fit-content;
    width: 100%;
    border-radius: 5px;
    border: 1px rgba(255, 255, 255, 0.247) solid;
    background-color: rgba(39, 39, 39, 0.788);
    transition: 0.2s all;
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

.origin, .picture, .comment, .username-date, .title, .chapter, .line {
    animation: breathing 2s infinite;
}
</style>