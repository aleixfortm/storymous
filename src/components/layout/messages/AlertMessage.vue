<template>
    <div class="alert alert-primary d-flex align-items-center alert-dismissible fade show m-1" role="alert" v-if="show">
        <div class="material-symbols-outlined ml-2">info</div>
        <div><strong class="mr-1">Update</strong> Resolved bug that prevented posting new stories</div>
        <button type="button" class="btn-close" @click="dismiss" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>
</template>

<script>
export default {
    data() {
        return {
            show: true
        }
    },
    methods: {
        dismiss() {
            this.show = false;
        }
    }
}
</script>

<style scoped>
.align {
    display: flex;
    align-items: center;
}
</style>