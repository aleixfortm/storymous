<template>
    <div v-if="!clickable" class="tag-shape user-select-none" :class="tag">{{ tag }}</div>
    <div v-else @click="selectTag" class="clickable tag-shape user-select-none" :class="[tag, selected ? 'tag-selected' : '']">
        <span class="material-symbols-outlined neutral-class" v-if="selected">done</span>
        {{ tag }}
    </div>
</template>

<script>
export default {
    props: ["tag", "clickable"],
    data() {
        return {
            selected: false,
        };
    },
    methods: {
        selectTag() {
            this.selected = !this.selected;
            this.$emit("selected", this.tag, this.selected);
        }
    },
}
</script>

<style scoped>
.material-symbols-outlined {
  font-variation-settings:
  'FILL' 0,
  'wght' 100,
  'GRAD' 0,
  'opsz' 0
}

.neutral-class {
  color: white;
}

.clickable {
    cursor: pointer;
    outline: 1px rgba(255, 255, 255, 0) solid;
    height: 30px;
    transition: 0.2s all;
}

.clickable:hover {
  outline: 1px rgba(245, 245, 245, 0.877) solid;
}

.tag-shape {
    display: flex;
    padding: 1px 5px;
    font-size: 13px;
    font-weight: bold;
    margin: 0 5px 5px 0;
    width: fit-content;
    border-radius: 100px;
    align-items: center;
}

.tag-selected {
    outline: 1px rgba(255, 255, 255, 0.568) solid;
    padding-right: 10px;

}

.mystery {
    background-color: rgba(255, 145, 0, 0.274);
    color: rgb(255, 174, 0);
}
.sci-fi {
    background-color: rgba(0, 162, 255, 0.322);
    color: rgb(0, 204, 255);
}
.chill {
    background-color: rgba(0, 255, 55, 0.274);
    color: rgb(0, 255, 21);
}
.short {
    background-color: rgba(123, 132, 255, 0.274);
    color: rgb(255, 170, 234);
}

.long {
    background-color: rgba(123, 132, 255, 0.274);
    color: rgb(177, 163, 255);
}

.medieval {
    background-color: rgba(17, 0, 255, 0.274);
    color: rgb(255, 135, 135);
}

.jungle {
    background-color: rgba(60, 255, 0, 0.274);
    color: rgb(193, 255, 135);
}

.horror {
    background-color: rgba(0, 0, 0, 0.562);
    color: rgb(185, 185, 185);
}

.historical {
    background-color: rgba(88, 88, 88, 0.445);
    color: rgb(209, 77, 77);
}

.fantasy {
    background-color: rgba(0, 255, 221, 0.274);
    color: rgb(135, 251, 255);
}

.world-building {
    background-color: rgba(238, 255, 0, 0.274);
    color: rgb(255, 237, 135);
}

.romance {
  background-color: rgba(255, 145, 0, 0.274);
  color: rgb(255, 174, 0);
}

.thriller {
  background-color: rgba(0, 162, 255, 0.322);
  color: rgb(0, 204, 255);
}

.young-adults {
  background-color: rgba(0, 255, 55, 0.274);
  color: rgb(0, 255, 21);
}

.humor {
  background-color: rgba(255, 0, 0, 0.274);
  color: rgb(255, 100, 0);
}

.self-help {
  background-color: rgba(255, 0, 255, 0.274);
  color: rgb(255, 100, 255);
}

.action {
  background-color: rgba(0, 162, 255, 0.274);
  color: rgb(255, 0, 0);
}

.suspense {
  background-color: rgba(0, 0, 255, 0.274);
  color: rgb(104, 104, 182);
}

.fairy {
  background-color: rgba(255, 0, 255, 0.274);
  color: rgb(255, 0, 100);
}

.pirate {
  background-color: rgba(0, 255, 255, 0.274);
  color: rgb(100, 255, 255);
}

.space {
  background-color: rgba(0, 100, 255, 0.274);
  color: rgb(0, 200, 255);
}

.science {
  background-color: rgba(200, 0, 255, 0.274);
  color: rgb(172, 117, 255);
}

.contemporary {
  background-color: rgba(100, 255, 0, 0.274);
  color: rgb(200, 255, 0);
}

.spirituality {
  background-color: rgba(255, 200, 0, 0.274);
  color: rgb(255, 150, 0);
}

.politics {
  background-color: rgba(0, 255, 200, 0.274);
  color: rgb(34, 34, 189);
}

.paranormal {
  background-color: rgba(255, 255, 0, 0.274);
  color: rgb(0, 0, 0);
}

.crime {
  background-color: rgba(135, 206, 235, 0.274);
  color: rgb(30, 144, 255);
}

.speculation {
  background-color: rgba(255, 192, 203, 0.274);
  color: rgb(255, 57, 163);
}

.literature {
  background-color: rgba(255, 250, 205, 0.274);
  color: rgb(255, 215, 0);
}

.travel {
  background-color: rgba(240, 230, 140, 0.274);
  color: rgb(223, 96, 255);
}

.development {
  background-color: rgba(127, 255, 212, 0.274);
  color: rgb(64, 224, 208);
}

.adventure {
  background-color: rgba(0, 128, 128, 0.274);
  color: rgb(0, 255, 255);
}

.classic {
  background-color: rgba(0, 0, 128, 0.274);
  color: rgb(255, 215, 0);
}

.detective {
  background-color: rgba(138, 43, 226, 0.274);
  color: rgb(238, 130, 238);
}

.memoir {
  background-color: rgba(139, 0, 139, 0.274);
  color: rgb(255, 192, 203);
}

</style>