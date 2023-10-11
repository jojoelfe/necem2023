<script setup lang="ts">
import { computed } from 'vue'
import { handleBackground } from './layoutHelper'

const props = defineProps({
  background: {
    default: '',
  },
})

const style = computed(() => handleBackground(props.background, true))
</script>

<template>
  <div class="slidev-layout cover text-center" :style="style">
    <LayoutHeader class="absolute bottom-0 right-0 transform rotate-y-180" />
    <div class="my-auto">
      <slot />
    </div>
    <LayoutFooter />
  </div>
</template>
