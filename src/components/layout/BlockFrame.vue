<template>
    <div class="body">
        <div class="lower-body">
            <div class="section">
                <slot></slot>
            </div>
        </div>
    </div>
</template>

<style scoped>

.lower-body {
    padding: 3.5rem 0 0 0;
}

.section {
    height: 3000px;
    max-width: 700px;
    margin: auto;
}


</style>