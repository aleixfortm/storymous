<template>
    <div class="loader-container">
        <div class="spinner-border text-light mb-3" style="width: 4.5rem; height: 4.5rem;" role="status">
            <span class="visually-hidden">Loading...</span>
        </div>
        <span class="loader-text">{{ text }}</span>
    </div>
</template>

<script>
export default {
    props: ["text"]
}
</script>

<style scoped>
.loader-text {
    background-color: whitesmoke;
    color: rgb(0, 0, 0);
    padding: 3px 10px;
    border-radius: 15px;
    font-weight: bold;
}

.loader-container {
    margin: 100px 0 0 0;
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
}
</style>
