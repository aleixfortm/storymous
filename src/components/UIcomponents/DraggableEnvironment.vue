<template>
    <div
    id="gesture-area"
    @touchmove.prevent
    ref="gestureArea"
    class="draggable-container"
    >
        <div
        class="draggable-element"
        :class="{ reset: isReset }"
        ref="scaleElement"
        >
            <slot></slot>
        </div>
    </div>
</template>
  
<script>
import interact from 'interactjs';

export default {
  data() {
    return {
      angleScale: {
        angle: 0,
        scale: 1,
      },
      isReset: false,
      resetTimeout: null,
    };
  },
  mounted() {
    interact(this.$refs.gestureArea)
      .gesturable({
        listeners: {
          start: this.handleGestureStart,
          move: this.handleGestureMove,
          end: this.handleGestureEnd,
        },
      })
      .draggable({
        listeners: { move: this.dragMoveListener },
      });
  },
  methods: {
    handleGestureMove(event) {
      const currentAngle = event.angle + this.angleScale.angle;
      const currentScale = event.scale * this.angleScale.scale;

      this.$refs.scaleElement.style.transform =
        'rotate(' + currentAngle + 'deg)' + 'scale(' + currentScale + ')';

      // Zoom in/out using pinch-to-zoom
      this.$refs.scaleElement.style.transform += ` scale(${event.ds})`;

      this.dragMoveListener(event);
    },
    handleGestureStart(event) {
      this.angleScale.angle -= event.angle;

      clearTimeout(this.resetTimeout);
      this.isReset = false;
    },
    handleGestureEnd(event) {
      this.angleScale.angle = this.angleScale.angle + event.angle;
      this.angleScale.scale = this.angleScale.scale * event.scale;

      this.resetTimeout = setTimeout(this.reset, 1000);
      this.isReset = true;
    },
    dragMoveListener(event) {
      const target = this.$refs.scaleElement;
      const x = (parseFloat(target.getAttribute('data-x')) || 0) + event.dx;
      const y = (parseFloat(target.getAttribute('data-y')) || 0) + event.dy;

      target.style.transform = `translate(${x}px, ${y}px)`;

      target.setAttribute('data-x', x);
      target.setAttribute('data-y', y);
    },
    reset() {
      this.$refs.scaleElement.style.transform = 'scale(1)';

      this.angleScale.angle = 0;
      this.angleScale.scale = 1;
    },
  },
};
</script>
  
<style>
.draggable-container {
    width: 100%;
    height: 400px;
    overflow: hidden;
    position: relative;
    border: 1px solid white;
    background-color: rgb(29, 29, 29);
}
</style>