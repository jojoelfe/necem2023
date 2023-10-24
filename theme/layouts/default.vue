<script setup lang="ts">
const props = defineProps({
  class: {
    type: String,
    default: '',
  },
});
</script>

<template>
  <div class="slidev-layout default col-grid">
    <LayoutHeader class="absolute bottom-0 right-0 transform rotate-y-180" />
    <div
      class="top"
      :class="props.class"
    >
    <slot />
    
    </div>
    <div class="middle" :class="props.class">
      <slot name="middle" />
    </div>
    <div
      class="left"
      :class="props.class"
    >
      <slot name="left" />
    </div>
    <div
      class="right"
      :class="props.class"
    >
      <slot name="right" />
    </div>
    <div
      class="bottom"
      :class="props.class"
    >
      <slot name="bottom" />
    </div>
    <LayoutFooter />
  </div>
</template>

<style>
.col-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: min-content auto min-content;
  grid-column-gap: 3rem;
  grid-row-gap: 0;
  height: 100%;
}

.top {
  grid-area: 1 / 1 / 2 / 3;
}

.left {
  grid-area: 2 / 1 / 3 / 2;
  display: flex;
  align-items: center;
}

.right {
  grid-area: 2 / 2 / 3 / 3;
  display: flex;
  align-items: center;
}

.middle {
  grid-area: 2 / 1 / 3 / 3;
  display: flex;
  align-items: center;
}

.bottom {
  grid-area: 3 / 1 / 4 / 3;
}
</style>
