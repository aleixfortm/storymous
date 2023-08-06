<template>
    <div class="alert alert-success d-flex align-items-center m-1 mt-2 mb-2 p-1" role="alert">
        <div class="material-symbols-outlined ml-2">done</div>
        <div class="mr-2"><strong>Logged in successfully</strong> at {{ currentTime.toLocaleTimeString() }}</div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                currentTime: new Date(),
            }
        }
    }
</script>

<style scoped>
.abs {
    position: relative;
}
</style>