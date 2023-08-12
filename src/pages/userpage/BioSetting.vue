<template>
    
    <div class="stats-bio">
        Bio
        <textarea
            class="custom-textarea"
            v-model="textareaContent"
            @input="handleTextareaInput"
        ></textarea>
    </div>
</template>
  
<script>
export default {
    props: ["previousBio"],
    data() {
        return {
            textareaContent: '',
        };
    },
    mounted() {
        this.textareaContent = this.previousBio;
    },
    methods: {
        adjustTextareaHeight() {
          const textarea = this.$el.querySelector('.custom-textarea');
          textarea.style.height = 'auto';
          textarea.style.height = textarea.scrollHeight + 'px';
          this.textareaHeight = textarea.style.height;
        },
        handleTextareaInput() {
            this.adjustTextareaHeight();
            this.$emit("bio-selected", this.textareaContent);
        },
    },
    watch: {
        textareaContent() {
          this.textareaContent = this.textareaContent.substring(0, 200);
          this.adjustTextareaHeight();
        },
    }
}
</script>

<style scoped>
.custom-textarea {
    background-color: rgb(255, 255, 255);
    font-size: 16px;
    min-height: 100px;
    width: 100%;
    border: none;
    outline: none;
    border-radius: 10px 10px 10px 10px;
    padding: 10px;
    margin: 10px auto 5px auto;
    color: rgb(0, 0, 0);
    overflow: auto;
    resize: none;
    box-sizing: border-box;
}

@media (max-width: 500px) {
    .custom-textarea {
        min-height: 150px;
}
}

.stats-bio {
    margin: 20px 10px;
    color: whitesmoke;
    font-weight: bold;

}
</style>