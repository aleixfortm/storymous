<template>
    <div class="alert alert-warning d-flex align-items-center p-1 mx-auto shadow custom-c" :class="loginErrorState ? 'show' : 'remove'" role="alert">
        <div class="material-symbols-outlined user-select-none m-2">warning</div>
        <div><strong>{{ message }}</strong></div>
    </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
    props: ["message"],
    data() {
        return {
            remove: false
        }
    },
    computed: {
    ...mapGetters('message', ['loginError']),
    loginErrorState() {
        return this.loginError
    }
  },
}
</script>

<style scoped>
.custom-c {
    position: fixed;
    transform: translateX(-50%);
    left: 50%;
    z-index: 999;
    width: 90%;
    max-width: 390px;
}

.show {
    opacity: 1;
    transition: 0.2s all;
}

.remove {
    opacity: 0;
    transition: 0.4s all;
}
</style>