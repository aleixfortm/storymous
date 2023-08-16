<template>
    <div class="box">
        <div class="main-title-container">
          <h2 class="main-title">{{ data.title.toUpperCase() }}</h2>
        </div>
        <div class="tag-section">
            <post-tag v-for="tag in data.tags" :key="tag" :clickable="false" :tag="tag"></post-tag>
        </div> 
        <div class="story-stats user-select-none">
            <div class="story-stats-section" 
                  :class="[data.leaves.includes(currentUser) ? 'includes-leaf-icon' : '']" 
                  @mouseover="showLeavesTooltip = true" 
                  @mouseout="showLeavesTooltip = false">
              <span class="material-symbols-outlined margin1 leaf-icon" :class="[data.leaves.includes(currentUser) ? 'includes-leaf-icon' : '']">nest_eco_leaf</span>
              <span>{{ data.leaves.length }}</span>
              <small-tooltip :condition="showLeavesTooltip" :text="'Storyline leaves'" :top="'35px'"></small-tooltip>
            </div>
            <div class="story-stats-section" @mouseover="showViewsTooltip = true" @mouseout="showViewsTooltip = false">
              <span class="material-symbols-outlined margin1">bar_chart</span>
              <span>{{ data.views }}</span>
              <small-tooltip :condition="showViewsTooltip" :text="'Highest views'" :top="'35px'"></small-tooltip>
            </div>
            <div class="story-stats-section" @mouseover="showChaptersTooltip = true" @mouseout="showChaptersTooltip = false">
              <span class="material-symbols-outlined margin1">call_split</span>
              <span>0</span>
              <small-tooltip :condition="showChaptersTooltip" :text="'Mounted chapters'" :top="'35px'"></small-tooltip>
            </div>
            <div class="story-stats-section" @mouseover="showCommentsTooltip = true" @mouseout="showCommentsTooltip = false">
              <span class="material-symbols-outlined margin1">chat</span>
              <span>{{ data.user_comments.length }}</span>
              <small-tooltip :condition="showCommentsTooltip" :text="'Comments'" :top="'35px'"></small-tooltip>
            </div>
        </div>
      </div>
</template>

<script>
import SmallTooltip from '@/components/UIcomponents/SmallTooltip.vue';
import PostTag from '@/components/UIcomponents/PostTag.vue';

export default {
    props: ["data"],
    components: {
        SmallTooltip,
        PostTag
    },
    data() {
        return {
            showLeavesTooltip: false,
            showViewsTooltip: false,
            showChaptersTooltip: false,
            showCommentsTooltip: false,
        }
    }

    
}
</script>

<style scoped>
.box {
    outline: rgba(255, 255, 255, 0.103) 1px solid;
    background-color: rgb(43, 43, 46);
    padding-bottom: 5px;
    margin: auto 1px;
}
.story-container {
  border: hsla(0,0%,51%,.322) 1px solid;
  border-radius: 2px 2px 0 0;
  background-color: rgb(43, 43, 46);
}
.main-title-container {
    display: flex;
    margin: 5px 0 5px 0;
    justify-content: center;
    align-items: center;
    text-align: center;
}
.main-title {
    color: bisque;
    font-size: 25px;
    margin: 10px 0px 10px 0px;
}
.tag-section {
    display: flex;
    justify-content: center;
    margin: -8px 7px 0px 7px;
    flex-wrap: wrap;
}
.story-stats {
    display: flex;
    color: whitesmoke;
    margin: 5px;
    justify-content: center;
}
.story-stats-section {
    position: relative;
    display: flex;
    align-items: center;
    margin: 0 12px;
    padding: 1px 6px 1px 1px;
    cursor: pointer;
}
.story-stats-section:hover {
    background-color: rgba(194, 194, 194, 0.137);
    border-radius: 10px;
}
.material-symbols-outlined {
  font-variation-settings:
  'FILL' 1,
  'wght' 400,
  'GRAD' 200,
  'opsz' 48
}
.leaf {
    color: white;
    transition: all 0.1s;
}
.leaf-icon {
    color: rgb(0, 255, 106);
}
.leaf:hover .leaf-icon{
    color: rgb(0, 255, 106);
}
.includes-leaf {
    color: rgb(0, 255, 106);
}
.includes-leaf-icon {
    color: rgb(0, 255, 106);
}
</style>