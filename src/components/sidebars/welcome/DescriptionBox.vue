<template>
    <div class="entirebox">
        <img :src="imgSrc" class="tree-image">
        <div class="box">
            
            <div class="explanation">
                <div class="data-section">
                    <div class="title">Species</div>
                    <div class="data">Storymous aarborea</div>
                </div>
                <div class="data-section">
                    <div class="title">Common name</div>
                    <div class="data">Storymous</div>
                </div>
                <div class="data-section">
                    <div class="title">Location</div>
                    <div class="data">Exoplanet Epstein-312b, <br> Epstein-312, <br> Andromeda</div>
                </div>
                <!--
                <div class="data-section">
                    <div class="title">Destinctive traits</div>
                    <div class="data">
                        <div class="marginated">Singular instances have been identified within the observable universe</div> 
                        <div class="marginated">It exhibits the extraordinary capacity to grow books from its branches</div>
                        <div class="marginated">The quantity of leaves appears to correlate with the narrative maturity</div>
                    </div>
                </div>
                -->
                <!--
                <div class="extra">Storymous is a unique tree species found throughout the observable universe that possesses the exceptional ability to cultivate stories</div>
                -->
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "DescriptionBox",
    computed: {
        imgSrc() {
            return require("@/assets/img/storymous-forest-min.png")
        }
    }
}
</script>

<style scoped>
.extra {
    padding: 2px 6px;
    font-size: 12px;
}

.entirebox {
    margin-top: 10px;
}

.marginated {
    margin-top: 5px;
    line-height: 1.05 !important;
}

.box {
    color: black;
    height: fit-content;
    width: 100%;
    text-align: left;
    padding: 4px 8px 8px 4px;
    border-radius: 0 0 5px 5px;
    border: 1px rgba(255, 255, 255, 0.247) solid;
    border-top: none;
    background-color: rgba(39, 39, 39, 0.788);
    transition: 0.2s all;
}

.title {
    font-weight: bold;
    font-size: 14px;
    margin-left: -2px;
    background-color: rgb(238, 238, 238);
    width: fit-content;
    padding: 1px 5px;
    border-radius: 8px;
}

.data-section {
    margin-top: 5px;
    padding: 2px 6px;
    border-radius: 5px;
}

.data {
    font-size: 14px;
    line-height: 1.05 !important;
    margin-top: 3px;
    color: rgb(214, 214, 214);
}

.tree-image {
    width: 100%;
    border-radius: 5px 5px 0 0;
    border: 1px rgba(255, 255, 255, 0.247) solid;
    border-bottom: none;
}
</style>
