<template>
    <div class="imagecontainer" v-if="!flipped">
        <div v-if="onomatopoeia" class="onomatopoeia">{{ onomatopoeia }}</div>
        <img class="astronaut-image" src="@/assets/img/astronaut_reading_space_nostars.png" alt="astronaut floating">
        <div v-if="text" class="loader-text-below">{{ text }}</div>
        <div v-else class="loader-text-below">{{ text }}</div>
    </div>
    <div class="imagecontainer" v-else>
      <div v-if="onomatopoeia" class="onomatopoeia">{{ onomatopoeia }}</div>
        <div v-if="text" class="loader-text-above">"{{ text }}"</div>
        <div v-else class="loader-text-above">"{{ text }}"</div>
        <img class="astronaut-image" src="@/assets/img/astronaut_reading_space_nostars.png" alt="astronaut floating">
    </div>
</template>

<script>

export default {
    props: ["onomatopoeia", "text", "flipped"]
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

.loader-text-below {
  position: relative;
  text-align: center;
  margin: 15px 5px 5px 5px;
  padding: 5px 10px;
  background-color: rgba(255, 255, 255, 0.88);
  color: rgb(0, 0, 0);
  padding: 5px 10px;
  border-radius: 15px;
  font-weight: bold;
  font-size: 15px;
}

.loader-text-below::before {
  content: '';
  position: absolute;
  left: 50%;
  bottom: 100%; /* Change 'top' to 'bottom' */
  margin-left: -10px;
  border-left: 10px solid transparent;
  border-right: 10px solid transparent;
  border-bottom: 10px solid rgba(255, 255, 255, 0.88);
}

.loader-text-above {
  position: relative;
  text-align: center;
  margin: 5px 5px;
  padding: 5px 10px;
  background-color: rgba(255, 255, 255, 0.88);
  color: rgb(0, 0, 0);
  padding: 5px 10px;
  border-radius: 15px;
  font-weight: bold;
  font-size: 15px;
}

.loader-text-above::after {
  content: '';
  position: absolute;
  left: 50%;
  top: 100%;
  margin-left: -10px;
  border-left: 10px solid transparent;
  border-right: 10px solid transparent;
  border-top: 10px solid rgba(255, 255, 255, 0.88);
}
</style>