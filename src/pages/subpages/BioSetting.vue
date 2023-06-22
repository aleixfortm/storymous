<template>
    <div class="stats-bio">
        <textarea
            v-textarea-autosize
            class="custom-textarea"
            v-model="textareaContent"
            @input="adjustTextareaHeight"
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
        /*
        selectItem(index) {
            // Clear selection of all items
            this.gridItems2.forEach((item) => {
                item.selected = false;
            });

            // Select the clicked item
            this.gridItems2[index].selected = true;

            //emit selected pic
            this.$emit("color-selected", this.gridItems2[index].color);
        },
        */
    },
    watch: {
        bioTextArea() {
          this.formcomment = this.formcomment.substring(0, 300);
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
    margin: 30px auto 5px auto;
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
    margin: 0 10px;
}
</style>