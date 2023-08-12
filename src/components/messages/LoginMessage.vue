<template>
    <div class="boxy" role="alert">
        <strong>Log In </strong> 
        <span class="text">{{ text }}</span>
    </div>
</template>

<script>
export default {
    props: ["text"]
}
</script>

<style scoped>
.boxy {
    background-color: #fcf0cf;
    border-left: #ffc400 6px solid;
    color: #604005;
    border-radius: 3px;
    opacity: 0.9;
    padding: 5px;
    margin: 5px 0;
}

.margin1 {
    margin-right: 12px;
}
</style>