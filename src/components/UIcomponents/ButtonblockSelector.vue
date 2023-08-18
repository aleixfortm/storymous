<template>
    <div v-if="homePage">
        <div class="block">
            <div class="rectangle">
                <select-button 
                @click="setSelectedTab1('latest-feed')" 
                :mode="selectedTab1 === 'following-feed' ? 'null' : 'flat'"
                :selected="selectedTab1 === 'latest-feed'">
                    <div>Latest</div>
                </select-button>
            </div>
            <div class="rectangle">
                <select-button @click="setSelectedTab1('following-feed')" 
                :mode="selectedTab1 === 'following-feed' ? 'flat' : 'null'"
                :selected="selectedTab1 === 'following-feed'">
                    <div>Following</div>
                </select-button>
            </div>
        </div>
    </div>
    <div v-else>
        <div class="block">
            <div class="rectangle">
                <select-button @click="setSelectedTab2('comments')" 
                :mode="selectedTab2 === 'comments' ? 'flat' : 'null'"
                :selected="selectedTab2 === 'comments'">
                    <div class="text">Comments</div>
                </select-button>
            </div>
            <div class="rectangle">
                <select-button @click="setSelectedTab2('chapters')" 
                :mode="selectedTab2 === 'chapters' ? 'flat' : 'null'"
                :selected="selectedTab2 === 'chapters'">
                    <div class="text">Chapters</div>
                </select-button>
            </div>      
        </div>
    </div>
</template>

<script>
import SelectButton from './buttons/SelectButton.vue';

export default {
    components: {
        SelectButton
    },
    props: ["homePage"],
    data() {
        return {
            selectedTab1: 'latest-feed',
            selectedTab2: 'comments'
        }
    },
    methods: {
        setSelectedTab1(tab) {
            this.selectedTab1 = tab
            this.$emit('selected-tab', tab);
        },
        setSelectedTab2(tab) {
            this.selectedTab2 = tab
            this.$emit('selected-tab', tab);
        }
    },
    mounted() {
        if (this.homePage) {
            this.$emit('selected-tab', this.selectedTab1);
        } else {
            this.$emit('selected-tab', this.selectedTab2);
        }
        
    }
}
</script>

<style scoped>
.text {
    font-size: 25px;
}

.block {
  margin: 20px 0 0 0;
  width: 100%;
  height: 50px;
  display: flex;
}

.rectangle {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: all 0.2s;
}

.null {
    color: rgba(245, 245, 245, 0.781);
}

.short {
    width: 70%;
}

@media (max-width: 520px) {

}
</style>