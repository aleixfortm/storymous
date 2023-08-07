<template>
    <div class="alert alert-warning d-flex align-items-center alert-dismissible fade show m-1 mt-3 custom-c" :class="opa ? '' : 'null-op'" role="alert" v-if="show">
        <div><strong class="mr-1">Update</strong> Story tags are not functioning properly, working on fix </div>
        <button type="button" class="btn-close" @click="dismiss" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>
</template>

<script>
export default {
    data() {
        return {
            show: true,
            opa: true
        }
    },
    methods: {
        dismiss() {
            this.opa = false
            setTimeout(() => {
                this.show = false
            }, 500)
        }
    }
}
</script>

<style scoped>
.custom-c {
    transition: all 0.5s;
}

.null-op {
    opacity: 0;
}
</style>