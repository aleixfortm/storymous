<template>
    <feed-container>
        <section class="section_title">
            User settings
        </section>
        <div class="setting">
            <span class="description">Choose a new profile picture</span>
            <button class="access-button" @click="selectedSetting = 'PictureSetting'"
                :class="{ active: selectedSetting === 'PictureSetting' }">Change picture</button>
        </div>
        <div class="setting">
            <span class="description">Choose a color scheme for your profile</span>
            <button class="access-button" @click="selectedSetting = 'ColorSetting'"
                :class="{ active: selectedSetting === 'ColorSetting' }">Choose color</button>

        </div>
        <div class="setting">
            <span class="description">Change your profile's bio</span>
            <button class="access-button" @click="selectedSetting = 'BioSetting'"
                :class="{ active: selectedSetting === 'BioSetting' }">Edit bio</button>

        </div>
        <div class="save-setting nomargin">
            <button :class="{ 'save-button': true, 'disabled': isSaveButtonDisabled }" :disabled="isSaveButtonDisabled"
                @click="saveChanges">{{ saveButtonText }}</button>
        </div>
        <section class="section_title"></section>

        <component v-if="userFetchedPicture"
            :is="selectedSetting" 
            :previousImage="selectedImage" 
            :previousColor="selectedColor" 
            :previousBio="selectedBio"
            @image-selected="handleImageSelected" 
            @color-selected="handleColorSelected"
            @bio-selected="handleBioSelected">
        </component>
    </feed-container>
</template>

<script>
import axios from "axios";
import { useRouter } from 'vue-router';
import { mapGetters } from 'vuex';
import { API_BASE_URL } from '../../config';

import PictureSetting from './PictureSetting.vue';
import ColorSetting from './ColorSetting.vue';
import BioSetting from './BioSetting.vue';
import FeedContainer from '@/components/frames/FeedContainer.vue';
import store from "@/store";

export default {
    data() {
        return {
            selectedSetting: null,
            isSaveButtonDisabled: true,

            //default values
            selectedImage: null,
            selectedColor: null,
            selectedBio: null
        }
    },
    setup() {
        const router = useRouter();
        return { router: router };
    },
    components: {
        FeedContainer,
        PictureSetting,
        ColorSetting,
        BioSetting
    },
    mounted() {
        if (this.isLoggedIn === false) {
            this.router.push('/home');
        }
        axios
        .get(`${API_BASE_URL}/settings/${this.currentUser}`, { timeout: 7000 })
        .then(response => {
            const data = response.data;
            this.selectedImage = data.picture,
            this.selectedColor = data.color,
            this.selectedBio = data.bio;
        }).catch(error => {
            if (axios.isCancel(error)) {
                console.error('Request timed out:', error);
            }
        })
    },
    computed: {
        ...mapGetters('auth', ['isLoggedIn', 'currentUser', "userFetchedPicture", "colorFetched", "userFetchedBio", "nFetchedPosts", "nFetchedFollowers", "nFetchedFollowing"]),
        saveButtonText() {
            return this.isSaveButtonDisabled ? "Saved!" : "Save changes"
        }
    },
    methods: {
        handleImageSelected(image) {
            if (this.selectedImage !== image) {
                this.selectedImage = image;
                this.isSaveButtonDisabled = false;
            }
        },
        handleColorSelected(color) {
            if (this.selectedColor !== color) {
                this.selectedColor = color;
                this.isSaveButtonDisabled = false;
            }
        },
        handleBioSelected(bio) {
            if (this.selectedBio !== bio) {
                this.selectedBio = bio;
                this.isSaveButtonDisabled = false;
            }
        },
        saveChanges() {
            axios
                .post(`${API_BASE_URL}/update_settings`, {
                    username: this.currentUser,
                    selectedImage: this.selectedImage,
                    selectedColor: this.selectedColor,
                    selectedBio: this.selectedBio
                })
                .then(response => {
                    this.loading = false;
                    const data = response.data;
                    if (data.status === "Success") {
                        this.isSaveButtonDisabled = true;
                        store.commit('auth/SET_USER_DATA', data.updated_user_data);
                    }
                })
                .catch(error => {
                    console.log(error);
                    this.loading = false;
                });
        },
    }
}

</script>

<style scoped>
.setting {
    margin: 40px 10px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.section_title {
    padding-bottom: 2px;
    margin: 35px 10px 10px 10px;
    font-size: larger;
    font-weight: bold;
    color: rgb(0, 248, 174);
    border-bottom: 2px solid rgb(180, 255, 233);
}

.description {
    color: whitesmoke;
}

.access-button {
    height: fit-content;
    border: none;
    font-family: inherit;
    color: rgb(255, 255, 255);
    cursor: pointer;
    font-size: 15px;
    width: fit-content;
    margin: 0px 10px 0px 0;
    outline: solid rgb(255, 255, 255) 2px;
    background-color: #e5e3ff00;
    border-radius: 4px;
    font-weight: bold;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.322);
    padding: 5px;
}

.save-setting {
    margin: 40px 10px;
    display: flex;
    align-items: center;
    justify-content: flex-end;
}

.nomargin {
    margin: 40px 10px 0px 0;
}

.save-button {
    height: fit-content;
    font-family: inherit;
    border: 0px solid #e5e3ff;
    color: rgb(255, 255, 255);
    cursor: pointer;
    font-size: 15px;
    width: fit-content;
    margin: 0px 10px 0px 0;
    background-color: rgba(0, 255, 76, 0.726);
    border-radius: 4px;
    font-weight: bold;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.322);
    padding: 5px;
}

.disabled {
    background-color: rgba(0, 194, 58, 0.295);
    cursor: default;
}

.disabled:hover {
    background-color: rgba(0, 255, 76, 0.342);
    cursor: default;
}

.save-button:hover {
    background-color: rgba(0, 255, 76, 0.315);
}

.access-button:hover {
    outline: rgb(92, 122, 219) solid 2px;
}

.access-button:active {
    outline: rgb(92, 122, 219) solid 2px;
}

.active {
    outline: rgb(92, 122, 219) solid 2px;
    background-color: rgba(92, 94, 219, 0.603);
}</style>