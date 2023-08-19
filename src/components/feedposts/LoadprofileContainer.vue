<template>
    <div class="outline">
        <div class="picture"></div>
    </div>
</template>

<script>

export default {
    name: "LoadprofileContainer"
}
</script>

<style scoped>
.picture {
    height: 300px;
    width: 300px;
    border-radius: 500%;
    background-color: #ffffff09;
}

.outline {
    margin-top: 12px;
    padding: 20px;
    height: fit-content;
    width: 100%;
    border-radius: 1px;
    border: 0px rgba(255, 255, 255, 0.247) solid;
    background-color: rgba(61, 61, 65, 0.671);
    transition: 0.2s all;
    display: flex;
    justify-content: center;
    align-items: center;
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