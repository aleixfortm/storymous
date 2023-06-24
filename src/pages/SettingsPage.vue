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

        <component 
            :is="selectedSetting" 
            :previousImage="selectedImage" 
            :previousColor="selectedColor" 
            :previous-bio="selectedBio"
            @image-selected="handleImageSelected" 
            @color-selected="handleColorSelected"
            @bio-selected="handleBioSelected">
        </component>
    </feed-container>
</template>

<script>
import { useRouter } from 'vue-router';
import { mapGetters } from 'vuex';

import PictureSetting from '../pages/subpages/PictureSetting.vue';
import ColorSetting from './subpages/ColorSetting.vue';
import BioSetting from './subpages/BioSetting.vue';

import FeedContainer from '@/components/layout/FeedContainer.vue';

export default {
    data() {
        return {
            selectedSetting: null,
            isSaveButtonDisabled: true,

            //default values
            selectedImage: "astronaut_reading.jpeg",
            selectedColor: 'blue',
            selectedBio: "yo! My name's asdf and I love Storymous! Follow me to be up to date with my content :) Let us go lololo lolol lololololo! Yeah boom bam paaam!!! PAPAPPAPA BOOM, pipip pipi fiuuuum...",
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
            this.router.push('/storymous/home');
        }
    },
    computed: {
        ...mapGetters('auth', ['isLoggedIn', 'currentUser']),
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
            this.isSaveButtonDisabled = true;
            
            // Handle saving sequence (API request in the future)
            console.log(this.selectedImage);
            console.log(this.selectedColor);
            console.log(this.selectedBio);
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