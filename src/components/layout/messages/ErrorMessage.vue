<template>
    <div class="alert alert-danger d-flex align-items-center p-1 mx-auto shadow custom-c" :class="remove ? 'remove' : ''" role="alert">
        <div class="material-symbols-outlined user-select-none m-2">warning</div>
        <div><strong>{{ message }}</strong></div>
    </div>
</template>

<script>

export default {
    props: ["message"],
    data() {
        return {
            remove: false
        }
    },
    mounted() {
        setTimeout(() => {
            this.remove = true;
        }, 2000);
    }
}
</script>

<style scoped>
.custom-c {
    position: fixed;
    transform: translateX(-50%);
    left: 50%;
    z-index: 999;
    width: 90%;
    max-width: 480px;
    transition: 1s ease all;
}

.remove {
    opacity: 0;
}
</style>