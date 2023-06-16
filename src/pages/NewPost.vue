<template>
    <feed-container>
      <section class="section_title">
        Write new story
      </section>
        <div class="pollancre">
            <form @submit.prevent="submitForm">
                <div class="newstory_comment">
                    <div class="image_box">
                        <img class="postimage" src="../assets/img/default_blue.png" alt="profilepic">
                    </div>
                    <textarea id="comment" v-model="formcomment" placeholder="Author comment" rows="1" :style="{ height: textareaHeight }" required></textarea>
                    
                </div>
                <div class="newstory_title">
                    <input id="title" v-model="formtitle" type="text" placeholder="Story title" required>
                    
                </div>
                <div class="newstory_title">
                    <textarea id="body" v-model="formbody" placeholder="Story content" required></textarea>
                </div>
                <div class="buttonbox">
                  <button class="postbutton" type="submit">Submit</button>
                </div>
                    
            </form>
        </div>
    </feed-container>
  </template>
  
  <script>
  import axios from 'axios';

  export default {
    name: "NewPost",
    data() {
      return {
        formtitle: "",
        formcomment: "",
        formbody: "",
      };
    },
    methods: {
      submitForm() {
        // Here you can perform the desired actions with the form data
        axios.post('http://192.168.1.44:5000/newpost', this.formtitle)
      },
      adjustTextareaHeight() {
          const textarea = this.$el.querySelector('#comment');
          textarea.style.height = 'auto';
          textarea.style.height = textarea.scrollHeight + 'px';
          this.textareaHeight = textarea.style.height;
        },
        adjustTextareaHeight1() {
          const textarea1 = this.$el.querySelector('#body');
          textarea1.style.height = 'auto';
          textarea1.style.height = textarea1.scrollHeight + 'px';
          this.textareaHeight1 = textarea1.style.height;
        }
    },
    watch: {
        formcomment() {
          this.formcomment = this.formcomment.substring(0, 300);
          this.adjustTextareaHeight();
        },
        formbody() {
          this.formbody = this.formbody.substring(0, 5000);
          this.adjustTextareaHeight1();
        },
        formtitle() {
          this.formtitle = this.formtitle.substring(0, 66);
        }
      },
    mounted() {
      this.adjustTextareaHeight();
    },
  };
  </script>

<style scoped>
.section_title {
  padding-bottom: 2px;
  margin: 30px 10px 20px 10px;
  border-bottom: 2px solid rgb(180, 255, 233);
}

.pollancre {
  padding: 1px 0 0 0;
  background-color: rgb(119 119 119 / 19%);
  border-radius: 10px;
}
section {
  margin: 35px 0 20px 10px;
  font-size: larger;
  font-weight: bold;
  color: rgb(0, 248, 174);
}

.image_box {
    height: max-content;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-self: end;
}

.newstory_comment {
    display: flex;
    flex-direction: row;
    width: 100%;
    height: 100%;
    margin: 20px 0 10px 0;
    display: flex;
    justify-content: left;
    border-radius: 10px;
}

.postimage {
    height: 50px;
    border-radius: 100%;
    margin: 10px 8px 0 10px;
    border: 2px whitesmoke solid;
}

textarea {
    background-color: #1d252e;
    border: none;
    border-radius: 5px;
    font-size: 14px;
    font-weight: 500;
    outline: none;
    padding: 8px 8px 8px 20px; /* add left padding */
    width: 95%;
    font: inherit;
    outline: rgb(100, 100, 100) 1px solid;
    color: whitesmoke;
    resize: none;
    overflow: auto;
    box-sizing: border-box;
    margin: 0 10px 0 0;
  }

#comment {
  background-color: #ffffff;
    border: none;
    border-radius: 10px 10px 10px 0;
    font-size: 14px;
    font-weight: 500;
    outline: none;
    padding: 8px 8px 8px 20px; /* add left padding */
    width: 95%;
    font: inherit;
    color: rgb(0, 0, 0);
    resize: none;
    overflow: auto;
    box-sizing: border-box;
    margin: 0 10px 20px 0;
}

#comment:hover {
  background-color: rgb(224, 224, 224);
}

#body {
  background-color: #1d252e;
    border: none;
    border-radius: 5px;
    font-size: 14px;
    font-weight: 500;
    outline: none;
    padding: 8px 8px 8px 20px; /* add left padding */
    width: 100%;
    font: inherit;
    color: rgb(255, 255, 255);
    resize: none;
    overflow: auto;
    box-sizing: border-box;
    margin: 10px 10px 0px 10px;
}

#body:hover {
  background-color: #161d24;
}

.newstory_title {
  display: flex;
  width: 100%;
}

input[type="text"] {
    background-color: bisque;
    border: none;
    border-radius: 5px;
    font-size: 14px;
    font-weight: 500;
    height: 35px;
    outline: none;
    padding: 8px 8px 8px 20px; /* add left padding */
    width: 100%;
    font: inherit;
    color: rgb(0, 0, 0);
    box-sizing: border-box;
    margin: 0 10px 0 10px;
  }
  
  input[type="text"]:hover {
      background-color: rgb(214, 193, 167);
  }
  
  input[type="text"]::placeholder {
    color: #000000a1;
    font-weight: 400;
  }

  textarea::-webkit-scrollbar {
      width: 0.5em;
    }

    textarea::-webkit-scrollbar-track {
      background: transparent;
    }

    textarea::-webkit-scrollbar-thumb {
      background-color: transparent;
    }
  
    .postbutton {
    height: 30px;
    font-family: inherit;
    border: 0px solid #e5e3ff;
    color: rgb(0, 255, 98);
    cursor: pointer;
    font-size: 15px;
    width: 80px;
    margin: 10px 10px 10px 0;
    background-color: #ffffff1e;
    border-radius: 4px;
    }

    .postbutton:hover {
      background-color: #94949425;
    }

    .buttonbox {
      display: flex;
      justify-content: flex-end;
      flex-direction: row;
    }

</style>