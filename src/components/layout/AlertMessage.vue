<template>
    <div class="alert alert-warning alert-dismissible fade show mt-3" role="alert" v-if="show">
        <strong>Bug alert!</strong> Tags on posts are currently random. Working on fix.
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