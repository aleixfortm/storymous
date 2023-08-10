<template>
    <div v-if="homePage">
        <div class="block">
            <div class="rectangle">
                <select-button @click="setSelectedTab('latest-feed')" :mode="selectedTab === 'following-feed' ? 'null' : 'flat'">
                    <div>Latest</div>
                </select-button>
            </div>
            <div class="rectangle">
                <select-button @click="setSelectedTab('following-feed')" :mode="selectedTab === 'following-feed' ? 'flat' : 'null'">
                    <div>Following</div>
                </select-button>
            </div>
        </div>
    </div>
    <div v-else>
        
    </div>
</template>

<script>
import SelectButton from '../SelectButton.vue';

export default {
    components: {
        SelectButton
    }
}
</script>

<style scoped>
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
  transition: all 0.1s;
}
</style>