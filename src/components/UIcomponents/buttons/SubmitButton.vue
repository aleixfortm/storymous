<template>
    <button v-if="!buttonLoading" class="button d-flex align-items-center" :class="{ 'custom-margin': margin }" type="submit">
        <slot></slot>
        {{ text }}
    </button>
    <button v-else class="button d-flex align-items-center" :class="{ 'disabled': buttonLoading, 'custom-margin': margin }" :disabled="buttonLoading" type="submit">
        <div class="spinner-border spinner-border-sm" role="status">
            <span class="visually-hidden">Loading...</span>
        </div>
    </button>
</template>

<script>

export default {
    props: ["buttonLoading", "color", "text", "margin", "buttonType"],
}
</script>

<style scoped>
.button {
    font-family: inherit;
    border: 0px solid #e5e3ff;
    color: rgb(255, 255, 255);
    font-size: 15px;
    min-width: 80px;
    border-radius: 4px;
    padding: 0px 5px;
    font-weight: bold;
    text-shadow: 0px 0px 1px rgba(0, 0, 0, 0.3);
    background-color: rgb(0, 172, 77);
    justify-content: center;
    min-height: 25px;
    height: fit-content;
    cursor: pointer;
    transition: 0.2s all;
}

.button:hover {
    background-color: rgba(0, 143, 64, 0.685);
}

.custom-margin {
    margin: 10px;
}

.disabled {
    font-family: inherit;
    border: 0px solid #e5e3ff;
    color: rgb(255, 255, 255);
    cursor: default;
    margin: 10px 10px 10px 0;
    background-color: rgba(0, 143, 64, 0.685);
}

.submit {
    background-color: rgb(172, 0, 0);
}
</style>