<template>
    <div class="alert alert-primary alert-dismissible fade show m-1" role="alert" v-if="show">
        <strong>Patch notes</strong> See all new features form the latest release
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