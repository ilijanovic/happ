<script setup lang="ts">
import buttonVue from "./components/button.vue";

function turnOff() {
  fetch("10.0.0.248/app/off");
}

function turnOn() {
  fetch("10.0.0.248/app/on");
}
</script>

<template>
  <div class="border flex flex-col gap-4 p-4 shadow-md">
    <h1>Premium App</h1>
    <div class="flex gap-4 justify-between">
      <buttonVue @click.native="turnOn">An</buttonVue>
      <buttonVue @click.native="turnOff">Aus</buttonVue>
    </div>
  </div>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
