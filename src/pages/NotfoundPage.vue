<template>
    <div class="imagecontainer">
        <div class="onomatopoeia">crick crick</div>
        <img class="astronaut-image" src="../assets/img/astronaut_reading_space_nostars.png" alt="astronaut floating">
        <div class="loader-text">There are up to 400 billion stars in our galaxy. Perhaps there is an inhabitable planet out here where this URL exists. Who knows?</div>
    </div>
</template>

<script>
export default {
    data() {
        return{
            
        }
    }
}

</script>

<style scoped>

.onomatopoeia {
    color: whitesmoke;
    font-weight: bold;
    font-size: 14px;
    margin-bottom: -10px;
}

@keyframes floatAnimation {
  0% {
    transform: translateY(-5px);
  }
  50% {
    transform: translateY(5px);
  }
  100% {
    transform: translateY(-5px);
  }
}

.astronaut-image {
    width: 175px;
    height: auto;
    animation: floatAnimation 4s ease-in-out infinite;
}

.imagecontainer {
    margin: 50px auto;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: fit-content;
}

.loader-text {
    background-color: whitesmoke;
    text-align: center;
    color: rgb(0, 0, 0);
    padding: 5px 10px;
    border-radius: 15px;
    font-weight: bold;
    margin: 0 10px;
}
</style>